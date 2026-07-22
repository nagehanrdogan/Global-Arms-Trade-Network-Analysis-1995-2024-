"""
05_figures.py

Figures 1a-1e: network visualization for each cross-section. Node size
and color reflect out-degree centrality (larger/darker = more central
supplier).

Input:  data/processed/edges_cross_sections.csv
Output: output/figures/figure_1a_2005.png ... figure_1e_2025.png
"""

import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pathlib import Path

try:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
except NameError:
    # __file__ isn't defined when this code is pasted directly into a Jupyter cell.
    # In that case, use the current working directory (go up one level if we're in src/).
    PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == 'src' else Path.cwd()
EDGES_PATH = PROJECT_ROOT / "data/processed/edges_cross_sections.csv"
FIGURES_DIR = PROJECT_ROOT / "output/figures"
YEARS = [2005, 2010, 2015, 2020, 2025]
LABELS = {2005: "1a", 2010: "1b", 2015: "1c", 2020: "1d", 2025: "1e"}


def plot_year(edges_year: pd.DataFrame, year: int):
    G = nx.DiGraph()
    for _, row in edges_year.iterrows():
        G.add_edge(row["supplier"], row["recipient"], weight=row["tiv"])

    g = G.number_of_nodes()
    outdeg_norm = {n: v / (g - 1) for n, v in dict(G.out_degree()).items()}

    node_sizes = [300 + 4000 * outdeg_norm[n] for n in G.nodes()]
    node_colors = [outdeg_norm[n] for n in G.nodes()]

    fig, ax = plt.subplots(figsize=(9, 7.5))
    pos = nx.spring_layout(G, seed=42, k=0.3)
    nx.draw_networkx_edges(G, pos, alpha=0.15, arrows=False, ax=ax)
    nodes = nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors,
        cmap=plt.cm.viridis, ax=ax,
    )
    # Label only the 10 most central nodes (to avoid visual clutter)
    top10 = sorted(outdeg_norm.items(), key=lambda x: -x[1])[:10]
    labels = {n: n for n, _ in top10}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, ax=ax)

    ax.set_title(f"Figure {LABELS[year]}: Arms Trade Network, {year}")
    ax.axis("off")
    plt.colorbar(nodes, ax=ax, label="Out-degree centrality", shrink=0.7)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"figure_{LABELS[year]}_{year}.png", dpi=150)
    plt.close()


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    edges = pd.read_csv(EDGES_PATH)
    for year in YEARS:
        plot_year(edges[edges["year"] == year], year)
        print(f"figure_{LABELS[year]}_{year}.png saved")


if __name__ == "__main__":
    main()
