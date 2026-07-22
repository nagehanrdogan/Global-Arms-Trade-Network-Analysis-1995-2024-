# Kinsella Revisited: A Longitudinal Replication

A replication and extension of David Kinsella's (2003) social network
analysis of the international arms trade, using SIPRI Arms Transfers
Database data through 2025. Working paper / draft — comments welcome.

## Research question

Kinsella (2003) argued that the arms trade is shaped by an interaction
between commercial and political logics, and expected that the end of
Cold War bipolarity would produce a more dispersed, less centralized
supplier structure over time. This project asks: two decades on, has
that marketization continued — or has supplier concentration persisted
or deepened?

## Key findings

- Network centralization rose from **0.36 (2005) to 0.54 (2025)**, and
  the Herfindahl-Hirschman Index (HHI) rose from **0.18 to 0.21** over
  the same period — the arms trade has become *more* concentrated, not
  less, contrary to Kinsella's expectation.
- The leading supplier's share of global transfer value rose from
  **31% to 42%**.
- This aggregate trend conceals a dual dynamic: **consolidation at the
  top** (Russia's out-degree centrality collapsed from 0.29 in 2010 to
  0.09 in 2025, falling out of the top ten suppliers) alongside
  **diversification below it** (Türkiye and South Korea enter the top
  ten for the first time by 2025).
- Robustness check: excluding component-level transfers (engines,
  sensors, naval weapons) entirely, centralization still rises from
  0.31 to 0.47 across the same period — the trend is not an artifact
  of how SIPRI records sub-system transfers.

Full discussion, citations, and methodological caveats are in
[`paper/research_note.md`](paper/research_note.md).

## Data

Source: [SIPRI Arms Transfers Database](https://www.sipri.org/databases/armstransfers),
Trade Register export, deliveries 1995–2025, filtered to 2004–2025 for
this analysis. Delivery-year records with SIPRI TIV (trend-indicator
value) as the transfer weight.

**Raw data is not redistributed in this repository** — SIPRI's terms
require users to query the database directly. To reproduce:

1. Go to the [SIPRI Trade Register](https://www.sipri.org/databases/armstransfers) query page
2. Set supplier/recipient to "All countries", delivery years 1995–2025
3. Export as CSV and place it at `data/raw/1995-2025.csv`

## Method summary

- Five annual cross-sections (2005, 2010, 2015, 2020, 2025), following
  Kinsella's approach of examining the network at multiple points in
  time rather than aggregating over periods.
- Directed, weighted edges: supplier → recipient, weight = summed TIV
  of deliveries in that year.
- Out-degree centrality (Freeman-normalized), group centralization,
  and HHI computed per cross-section.
- Component-level vs. platform-level transfers classified via SIPRI's
  Armament category field, as a robustness check on whether SIPRI's
  sub-system reporting conventions drive the centralization trend.

Full formula details are documented as comments in `src/`.

## Repository structure

```
├── data/
│   ├── raw/            # SIPRI export (not redistributed — see above)
│   └── processed/       # cleaned deliveries + cross-section edge lists
├── src/
│   ├── 01_clean_data.py          # load, clean, build cross-section edges
│   ├── 02_network_metrics.py     # Tables 1-4 (density, centralization, HHI)
│   ├── 03_robustness_check.py    # component/platform split, %10 share check
│   ├── 04_discussion_checks.py   # Russia in/out-degree balance
│   └── 05_figures.py             # Figures 1a-1e (network visualizations)
├── notebooks/
│   └── pipeline.ipynb    # runs the full pipeline, Colab-ready
├── output/
│   ├── tables/          # all output tables as CSV
│   └── figures/          # Figures 1a-1e as PNG
├── paper/
│   └── research_note.md  # full text of the research note
└── requirements.txt
```

## Reproducing the analysis

### Option A: notebook (recommended for inspecting the data)

Open [`notebooks/pipeline.ipynb`](notebooks/pipeline.ipynb) — either
locally in Jupyter, or on Google Colab via the "Open in Colab" badge at
the top of the notebook. It runs every step in order and displays each
resulting table and figure inline, so you can check the data at every
stage rather than just running scripts blindly. Steps 2-5 work
out of the box against the processed data already committed to this
repo; Step 1 (raw-data cleaning) only runs if you've supplied your own
SIPRI export (see [Data](#data) above).

### Option B: command line

```bash
pip install -r requirements.txt
cd src
python 01_clean_data.py
python 02_network_metrics.py
python 03_robustness_check.py
python 04_discussion_checks.py
python 05_figures.py
```

Each script reads the previous script's output from `data/processed/`
or `output/`, so they must be run in order on a first pass.

## Future work

- **Network resilience:** simulating the effect of removing top
  suppliers on overall connectivity and density, to assess whether the
  arms trade's current concentration is fragile or robust to a shock
  affecting a dominant supplier.
- **Testing Kinsella's bloc-dispersion mechanism directly:** coding
  states into Cold War-era alliance blocs and measuring intra- versus
  inter-bloc transfer shares over time, extending the analysis
  backward to pre-2005 cross-sections where data permits. The present
  analysis tests Kinsella's thesis only at the level of aggregate
  outcomes, not this specific proposed mechanism.

## Citation

Kinsella, D. (2003). *Changing structure of the arms trade: A social
network analysis.*
https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1018&context=polisci_fac

SIPRI. (n.d.). *Sources and methods: SIPRI Arms Transfers Database.*
https://www.sipri.org/databases/armstransfers/sources-and-methods

## License

Code: MIT. Data: subject to SIPRI's terms of use (not redistributed here).
