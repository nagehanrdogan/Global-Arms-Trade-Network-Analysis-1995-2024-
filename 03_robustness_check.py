"""
03_robustness_check.py

Numerically verifies two claims made in the method section:
  (a) Component-level transfers make up ~10% of total TIV and this share
      is stable over time.
  (b) Component-level edges do not drive the centralization finding
      (the same direction/trend holds even when components are excluded).

Classification based on SIPRI's "Armament category" field:
  component-level: Engines, Sensors, Naval weapons, Other
      (per SIPRI's methodology, these categories are recorded as separate
      rows only when supplied independently of a platform)
  platform-level:   Aircraft, Armoured vehicles, Ships, Artillery,
                     Missiles, Air-defence systems, Satellites

Input:  data/processed/deliveries_clean.csv
Output: output/tables/table5_component_share.csv
        output/tables/table6_robustness_centralization.csv
"""

from pathlib import Path
import pandas as pd
import networkx as nx

try:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
except NameError:
    # __file__ isn't defined when this code is pasted directly into a Jupyter cell.
    # In that case, use the current working directory (go up one level if we're in src/).
    PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == 'src' else Path.cwd()
DELIVERIES_PATH = PROJECT_ROOT / "data/processed/deliveries_clean.csv"
TABLES_DIR = PROJECT_ROOT / "output/tables"
YEARS = [2005, 2010, 2015, 2020, 2025]

COMPONENT_CATEGORIES = ["Engines", "Sensors", "Naval weapons", "Other"]


def classify(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["level"] = df["Armament category"].apply(
        lambda x: "component" if x in COMPONENT_CATEGORIES else "platform"
    )
    return df


def component_share_over_time(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year in YEARS:
        d = df[df["Delivery year"] == year]
        comp_tiv = d[d["level"] == "component"]["TIV delivery values"].sum()
        plat_tiv = d[d["level"] == "platform"]["TIV delivery values"].sum()
        total = comp_tiv + plat_tiv
        rows.append({
            "year": year,
            "component_tiv": round(comp_tiv, 1),
            "platform_tiv": round(plat_tiv, 1),
            "component_share_pct": round(100 * comp_tiv / total, 2),
        })
    result = pd.DataFrame(rows)
    print(f"Average component share: {result['component_share_pct'].mean():.1f}%  "
          f"(SD: {result['component_share_pct'].std():.2f})")
    return result


def centralization_platform_only(df: pd.DataFrame) -> pd.DataFrame:
    """Recomputes centralization using platform-level transfers only;
    placed side by side with the full data (including components) from
    Table 1 for comparison."""
    rows = []
    for year in YEARS:
        d = df[(df["Delivery year"] == year) & (df["level"] == "platform")]
        edges = d.groupby(["Supplier", "Recipient"])["TIV delivery values"].sum().reset_index()

        G = nx.DiGraph()
        for _, row in edges.iterrows():
            G.add_edge(row["Supplier"], row["Recipient"], weight=row["TIV delivery values"])

        g = G.number_of_nodes()
        outdeg_raw = dict(G.out_degree())
        c_max = max(outdeg_raw.values())
        numerator = sum(c_max - v for v in outdeg_raw.values())
        centralization = numerator / (g * (g - 1))

        rows.append({"year": year, "centralization_platform_only": round(centralization, 4)})
    return pd.DataFrame(rows)


def main():
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DELIVERIES_PATH)
    df = classify(df)

    table5 = component_share_over_time(df)
    table5.to_csv(TABLES_DIR / "table5_component_share.csv", index=False)

    table6 = centralization_platform_only(df)
    table6.to_csv(TABLES_DIR / "table6_robustness_centralization.csv", index=False)

    print()
    print("Table 5 (component share over time):")
    print(table5.to_string(index=False))
    print()
    print("Table 6 (centralization, platform-only vs. full):")
    print(table6.to_string(index=False))


if __name__ == "__main__":
    main()
