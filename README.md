# Global Arms Trade Network Analysis (1995–2024)
## A Replication and Longitudinal Extension of Kinsella (2003)

**Nagehan Reyhan Doğan** | PhD Candidate, Istanbul University | 2026

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Data](https://img.shields.io/badge/data-SIPRI-green.svg)
![Field](https://img.shields.io/badge/field-SNA%20%7C%20IR-red.svg)

---

## Research Question
How has the structure of the global arms trade network evolved 
between 1995 and 2024? This project replicates the foundational 
SNA methodology of Kinsella (2003) and extends it to the present, 
examining shifts in network density, structural equivalence, and 
the emergence of new supplier clusters.

---

## Data
This project uses the **SIPRI Arms Transfers Database**.  
Data is **not included** in this repository due to licensing restrictions.

**To download the data:**
1. Go to: https://armstransfers.sipri.org/ArmsTransfer/TransferRegister
2. Settings: Year 1995–2025 | Order by Buyer
3. Check: ✓ Register with deliveries broken down by year
4. Click **Download as CSV**
5. Save as `trade-register.csv` in the same folder as the notebook

---

## Methodology
Binary Adjacency Matrices (N × N) where:
- **Nodes:** Participating states
- **Edges:** x_ij = 1 if a transfer exists from supplier i to recipient j
- **Density:** D = L / g(g-1)
- **Structural equivalence** via Multidimensional Scaling (MDS)

---

## Key Findings

| Metric | 2000 (Kinsella Baseline) | 2024 (Extension) |
|--------|--------------------------|------------------|
| Countries (g) | 119 | 119 |
| Connections (L) | 317 | 383 |
| Density (D) | 0.0225 | 0.0272 |

Global network density remains low and stable (~0.025), confirming 
that arms trade operates as an embedded social network based on 
strategic trust rather than a free market.

**Turkiye case:** Supplier diversity dropped from 9 (2012) to 4 (2024) 
while export reach rose from 2 to 25 destinations — consistent with 
import substitution and the "Manufacturer Effect."

---

## Requirements
pip install pandas numpy networkx matplotlib scipy

## Usage
Open the notebook and run cells in order.  
Outputs are saved to the `outputs/` folder.

---

## Reference
Kinsella, D. (2003). Changing structure of the arms trade: 
A social network analysis. *Annual Meeting of the American 
Political Science Association*, Philadelphia.

## Citation
Doğan, N. R. (2026). *Global Arms Trade Network Analysis 
(1995–2024)*. Unpublished working paper, Istanbul University.  
https://github.com/nagehanrdogan/Global-Arms-Trade-Network-Analysis-1995-2024-
