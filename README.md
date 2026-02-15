# Evolution of the Global Arms Trade Network (1995-2024)
## A Replication and Longitudinal Extension of David Kinsella's (2003) SNA Study

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Data](https://img.shields.io/badge/data-SIPRI-green.svg)
![Field](https://img.shields.io/badge/field-SNA%20|%20IR-red.svg)

## 📌 Project Overview
This project performs a **Social Network Analysis (SNA)** of the global arms trade, replicating the foundational methodology of **David Kinsella (2003)**. While the original study analyzed the period of 1950-2000, this extension bridges the gap to **2024**, analyzing modern shifts like the "Manufacturer Effect" and geopolitical re-polarization.

---

## 🛠 Methodology
The analysis is based on **Binary Adjacency Matrices** ($N \times N$) where:
* **Nodes ($g$):** Participating states in the arms trade.
* **Edges ($L$):** $x_{ij} = 1$ if a major conventional weapon transfer exists from supplier $i$ to recipient $j$, and $0$ otherwise.
* **Density Formula:** $D = \frac{L}{g(g-1)}$.

### Data Source
* **Database:** SIPRI Arms Transfers Database (Trade Registers).
* **Scope:** Major Conventional Weapons (TIV values > 0).

---

## 📊 Key Findings

### 1. Global Network Density
The analysis shows that global network density remains low and stable (approx. **0.025**), confirming that arms trade is not a free market but an **embedded social network** based on strategic trust.

| Metric | 2000 (Kinsella Baseline) | 2024 (Extension) |
| :--- | :--- | :--- |
| **Countries ($g$)** | 119 | 119 |
| **Connections ($L$)** | 317 | 383 |
| **Density ($D$)** | 0.0225 | 0.0272 |

### 2. The Turkiye Case: Strategic Decoupling & Autonomy
A deep dive into Turkiye's structural position reveals a historic transformation:
* **Supplier Diversity (Indegree):** Dropped from **9** unique suppliers in 2012 to **4** in 2024.
* **Export Reach (Outdegree):** Rose from **2** destinations (2000) to **25** destinations (2024).
* **Manufacturer Effect:** The decline in supplier diversity is a direct result of **Import Substitution**, as Turkiye transitioned from a dependent recipient to a strategic supplier.

---

## 🗺 Structural Equivalence (MDS Analysis)
We analyzed structural positions using **Multidimensional Scaling (MDS)** across four panels: **2000, 2008, 2016, and 2024**. 

* **2000:** Tight Western cluster (USA, Germany, France).
* **2024:** Fragmentation and the emergence of independent clusters, with Turkiye moving away from the traditional NATO-dependent node toward its own niche network.

