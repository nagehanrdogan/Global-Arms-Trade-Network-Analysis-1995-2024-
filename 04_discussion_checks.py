"""
04_discussion_checks.py

Produces two checks for the Russia paragraph in the Discussion section:
  (a) How Russia's in-degree/out-degree and in-TIV/out-TIV change across
      the 5 cross-sections.
  (b) Who supplies Russia (and with what TIV) in the 2025 cross-section.

Input:  data/processed/edges_cross_sections.csv
Output: output/tables/table7_russia_balance.csv
        output/tables/table8_russia_2025_suppliers.csv
"""

from pathlib import Path
import pandas as pd

try:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
except NameError:
    # __file__ isn't defined when this code is pasted directly into a Jupyter cell.
    # In that case, use the current working directory (go up one level if we're in src/).
    PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == 'src' else Path.cwd()
EDGES_PATH = PROJECT_ROOT / "data/processed/edges_cross_sections.csv"
TABLES_DIR = PROJECT_ROOT / "output/tables"
YEARS = [2005, 2010, 2015, 2020, 2025]
TARGET = "Russia"


def russia_balance_over_time(edges: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year in YEARS:
        e = edges[edges["year"] == year]
        as_recipient = e[e["recipient"] == TARGET]
        as_supplier = e[e["supplier"] == TARGET]
        rows.append({
            "year": year,
            "in_degree": len(as_recipient),
            "in_tiv": round(as_recipient["tiv"].sum(), 1),
            "out_degree": len(as_supplier),
            "out_tiv": round(as_supplier["tiv"].sum(), 1),
        })
    return pd.DataFrame(rows)


def russia_2025_suppliers(edges: pd.DataFrame) -> pd.DataFrame:
    e = edges[(edges["year"] == 2025) & (edges["recipient"] == TARGET)]
    return e[["supplier", "tiv"]].sort_values("tiv", ascending=False).reset_index(drop=True)


def main():
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    edges = pd.read_csv(EDGES_PATH)

    table7 = russia_balance_over_time(edges)
    table7.to_csv(TABLES_DIR / "table7_russia_balance.csv", index=False)

    table8 = russia_2025_suppliers(edges)
    table8.to_csv(TABLES_DIR / "table8_russia_2025_suppliers.csv", index=False)

    print("Table 7 (Russia in/out balance over time):")
    print(table7.to_string(index=False))
    print()
    print("Table 8 (Russia's 2025 suppliers):")
    print(table8.to_string(index=False))


if __name__ == "__main__":
    main()
