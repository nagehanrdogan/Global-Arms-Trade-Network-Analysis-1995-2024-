**Revision Kinsella's (2003) Social Network Analysis on 1950-2003**

**Introduction**

Kinsella (2003) argued that the decision to become a supplier or
recipient in the arms trade is shaped not by governments alone, nor by
private actors alone, but by an interaction between the two. He gives
the example of the United States, where the government established
control over arms transactions during World War II, after which arms
transfers became both a profit-making activity for private traders and a
policy instrument for governments --- the commercial dimension did not
disappear, but a political dimension was added on top of it.

Kinsella framed this as a question of network structure: if arms
transfers are relational ties between states, then changes in the
commercial and political logic of the arms trade should be visible as
changes in the structure of the network itself --- its density, and the
concentration of supplier positions within it.

This article takes up the question Kinsella left open in his concluding
remarks --- "how far will marketization proceed?" This research aims to
answer this question with updated SIPRI data, disaggregating
subsystem-level transfers --- engines, sensors, and the like --- from
platform-level transfers, to test whether component-level ties, which
may not reflect a genuine bilateral supplier--recipient relationship,
distort the network's apparent structure. The purpose of this study,
then, is to extend Kinsella's analysis into the present: using
arms-transfer data through 2025, it re-examines whether the arms trade
network has continued to marketize --- becoming more dispersed and less
centralized --- or whether supplier concentration has instead persisted
or deepened.

**Method**

Kinsella (2003) chose the arms-transfer relationship connecting two
states as his unit of analysis. He describes states are actors, with
existence of a relational tie indicated a connection between them. A tie
is a directed that it represents the flow of military resources from one
actor to another. Kinsella creates a socio-matrix in which there is both
a row and a column for each actor in the network. Kinsella's tie is
binary -- it records only the presence or absence of a transfer in a
given year. This study instead uses a weighted tie, where the weight is
the total SIPRI TIV value of deliveries between a supplier and a
recipient. This allows the analysis to capture not only whether a
transfer relationship exists, but also its relative magnitude. However,
the arms transfer data for this study come from same sources as
Kinsella's -- the SIPRI Arms Transfers Database. I used SIPRI Arms
Transfer Database, restricted to the 2004- 2025 period, to revisit
Kinsella's argument under more recent data.

I filtered the data, using the "delivery year" rather than the "order
date," because some orders are placed but never delivered. This was
intended to capture the actual realization of a transfer relationship,
rather than a mere agreement to transfer. Following Kinsella's approach
of examining the network at several points in time, this study uses five
annual cross-sections: 2005, 2010, 2015, 2020, and 2025. Kinsella's
argument concerns a dynamic process --- change over time --- so a single
snapshot would not be sufficient to capture the trend. A directed graph
was constructed in which each supplier--recipient pair constitutes a
single edge. For each edge, the cumulative SIPRI TIV of deliveries in
that year was recorded as an edge attribute. Degree-based network
measures were then calculated from the existence of ties, while transfer
magnitude was analysed separately using the HHI.

Following Kinsella's (2003, 18) formulation, a state's out-degrees is
defined as the number of other states it supplies with arms in a given
year, while its in-degree is the number of states from which it receives
arms. Network density is then calculated as the sum of all out-degrees
and in-degrees, expressed as a proportion of the maximum number of
possible directed ties. Kinsella's network analysis does not report the
total number of states (g), and this number changes across periods. The
networks used in this study likewise vary in size across sub-periods,
ranging from 165 to 177 states. Therefore, due to these differences --
both between this study and Kinsella's, and across the sub-periods
within this study -- raw values cannot be meaningfully compared;
instead, only the direction of the trend can be compared.

In Kinsella's formulas do not include the volume dimension of
arms-transfer relations: his measure are based solely on the number of
trading partners (degree). However, degree and volume can diverge -- a
state may supply many countries with small amounts, or few countries
with large amounts, and these two patterns reflect different kinds of
supplier positions. To measure individual supplier prominence,
out-degree centrality was calculated following Kinsella's normalized
formula. To capture the overall degree of supplier concentration in the
network as a whole, Kinsella's group centralization was also computed.
Since magnitude of these relations is also important for understanding
the structure of the network, this study includes it through the
Herfindahl-Hirschman Index (HHI)[^1], which measures concentration based
on transfer volume rather than the mere number of trading partners. This
allows the analysis to test whether the degree-based and volume-based
measures points in the same direction, providing a more robust basis for
evaluating supplier concentration than either measure alone.

It should be noted that the SIPRI TIV (SIPRI, n.d.) is based on the
known unit production costs of a core set of weapons and is intended to
represent the transfer of military resources rather than the financial
value of the transfer; it therefore does not reflect actual sales
prices. Furthermore, SIPRI records transfers at the level of major
weapons systems, while major sub-systems --- such as engines, radars or
sonar systems --- are recorded separately only when they originate from
a supplier state different from that of the platform. In case of
multinational production programmes, transfers are attributed to the
state in which final assembly takes place. Consequently, the supplier
centralization measures presented in this study primarily reflect the
distribution of platform suppliers and final assemblers, supplemented by
separately recorded transfers of selected major sub-systems, rather than
the complete international production network underlying modern weapon
system. In addition, multiple transfers of different weapon categories
between the same supplier and recipient within a period were aggregated
into a single weighted edge. Accordingly, the analysis captures the
intensity of bileteral transfer relationships rather than variation
across weapon categories. Component-level transfer account for
approximately 10 per cent of total TIV across all sub-periods, a share
that remains stable over time, suggesting that their inclusion does not
drive the centralization trend reported here.

**Results**

Table 1 presents the network's density, centralization, nodes and edged
across five annual cross-sections.

> Table 1: Network Properties of the Arms Trade, 2005-2025

+---------+-----------+------------------+-------------+-------------+
| > Year  | > Density | > Centralization | > N. Nodes  | > N. Edges  |
+=========+===========+==================+=============+=============+
| > 2,005 | > 0.0242  | > 0.3604         | > 118       | > 334       |
+---------+-----------+------------------+-------------+-------------+
| > 2,010 | > 0.0263  | > 0.3989         | > 128       | > 428       |
+---------+-----------+------------------+-------------+-------------+
| > 2,015 | > 0.0275  | > 0.4839         | > 132       | > 476       |
+---------+-----------+------------------+-------------+-------------+
| > 2,020 | > 0.0250  | > 0.5360         | > 124       | > 381       |
+---------+-----------+------------------+-------------+-------------+
| > 2,025 | > 0.0277  | > 0.5353         | > 120       | > 396       |
+---------+-----------+------------------+-------------+-------------+

Density remains broadly stable across the observed period, ranging from
0.024 to 0.028, indicating a sparse network in which the vast majority
of possible amrs-transfer relationship are not realized. This is
consistent with Kinsella's (2003) observations that network density
levelled off in the post-Cold War era and has remained stable since.
However, density alone does not directly test Kinsella's marketization
argument. For this, we turn to the centralization findings.

Centralization increases steadily across the observed period, ranging
from 0.36 in 2005 to 0.54 in 2025, indicating the arms trade network has
become more concentrated rather than more dispersed. This finding stands
in contrast to Kinsella's (2003) expectation that the supplier structure
of the arms trade would become progressively less centralized as
marketization proceeded.

Figures 1a--1e present the arms trade network for each cross-section.
Node size and color reflect out-degree centrality; larger and darker
nodes indicate more central suppliers.

![](media/image1.png){width="5.153496281714785in"
height="4.417361111111111in"}![](media/image2.png){width="5.115293088363955in"
height="4.384615048118985in"}![](media/image3.png){width="5.2307688101487315in"
height="4.483595800524935in"}![](media/image4.png){width="5.12in"
height="4.388650481189852in"}![](media/image5.png){width="5.436569335083115in"
height="4.66in"}

Table 2 shows Top 20 Arms Suppliers by Out-Degree Centrality. The
out-degree centrality findings reveal a clear divergence among the
leading suppliers. The United States remains the most central supplier
across all five cross-sections, with its centrality score rising
steadily from 0.385 in 2005 to 0.563 in 2025. In contrast, Russia's
centrality declines consistently over the observed period, from 0.214 in
2005 to 0.179 in 2020, and falls out of the top 10 entirely by 2025.
Notably, Türkiye enters the top 10 for the first time in 2025, with a
centrality score of 0.168.

+---+------------+------------+------------+------------+------------+
| > | > 2025     | > 2020     | > 2015     | > 2010     | > 2005     |
|   |            |            |            |            |            |
| R |            |            |            |            |            |
| a |            |            |            |            |            |
| n |            |            |            |            |            |
| k |            |            |            |            |            |
+===+============+============+============+============+============+
| > | > United   | > United   | > United   | > United   | > United   |
|   | > States   | > States   | > States   | > States   | > States   |
| 1 | > (0.563)  | > (0.561)  | > (0.511)  | > (0.425)  | > (0.385)  |
+---+------------+------------+------------+------------+------------+
| > | > France   | > France   | > France   | > Russia   | > Germany  |
|   | > (0.277)  | > (0.276)  | > (0.321)  | > (0.291)  | > (0.239)  |
| 2 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Germany  | > Germany  | > Germany  | > France   | > France   |
|   | > (0.261)  | > (0.252)  | > (0.275)  | > (0.276)  | > (0.231)  |
| 3 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Israel   | > Russia   | > Russia   | > Germany  | > Russia   |
|   | > (0.235)  | > (0.179)  | > (0.229)  | > (0.252)  | > (0.214)  |
| 4 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Italy    | > Israel   | > Italy    | > Italy    | > United   |
|   | > (0.21)   | > (0.163)  | > (0.221)  | > (0.228)  | > Kingdom  |
| 5 |            |            |            |            | > (0.197)  |
+---+------------+------------+------------+------------+------------+
| > | > Turkiye  | > United   | > Israel   | > Israel   | > Israel   |
|   | > (0.168)  | > Kingdom  | > (0.183)  | > (0.22)   | > (0.188)  |
| 6 |            | > (0.154)  |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > United   | > Italy    | > China    | > China    | > Italy    |
|   | > Kingdom  | > (0.138)  | > (0.168)  | > (0.197)  | > (0.188)  |
| 7 | > (0.134)  |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Sweden   | > South    | > N        | > Sweden   | > Ukraine  |
|   | > (0.126)  | > Korea    | etherlands | > (0.142)  | > (0.128)  |
| 8 |            | > (0.122)  | > (0.168)  |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Canada   | > China    | > Canada   | > Ukraine  | > Canada   |
|   | > (0.118)  | > (0.106)  | > (0.145)  | > (0.126)  | > (0.111)  |
| 9 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > China    | > South    | > United   | > United   | > N        |
|   | > (0.109)  | > Africa   | > Kingdom  | > Kingdom  | etherlands |
| 1 |            | > (0.106)  | > (0.13)   | > (0.126)  | > (0.111)  |
| 0 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > South    | > Spain    | > Spain    | > South    | > Sweden   |
|   | > Korea    | > (0.106)  | > (0.115)  | > Africa   | > (0.111)  |
| 1 | > (0.101)  |            |            | > (0.118)  |            |
| 1 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Russia   | > Turkiye  | > Sweden   | > Canada   | > China    |
|   | > (0.092)  | > (0.098)  | > (0.099)  | > (0.11)   | > (0.103)  |
| 1 |            |            |            |            |            |
| 2 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > N        | > Sweden   | > South    | > N        | > South    |
|   | etherlands | > (0.089)  | > Africa   | etherlands | > Africa   |
| 1 | > (0.067)  |            | > (0.092)  | > (0.094)  | > (0.068)  |
| 3 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Norway   | > Canada   | > S        | > Austria  | > unknown  |
|   | > (0.067)  | > (0.081)  | witzerland | > (0.079)  | > s        |
| 1 |            |            | > (0.092)  |            | upplier(s) |
| 4 |            |            |            |            | > (0.051)  |
+---+------------+------------+------------+------------+------------+
| > | > United   | > N        | > Ukraine  | > S        | > Czechia  |
|   | > Arab     | etherlands | > (0.092)  | witzerland | > (0.043)  |
| 1 | > Emirates | > (0.081)  |            | > (0.079)  |            |
| 5 | > (0.067)  |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Poland   | > United   | > Czechia  | > Spain    | > Spain    |
|   | > (0.059)  | > Arab     | > (0.061)  | > (0.071)  | > (0.043)  |
| 1 |            | > Emirates |            |            |            |
| 6 |            | > (0.065)  |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > South    | > S        | > Turkiye  | > Belarus  | > S        |
|   | > Africa   | witzerland | > (0.061)  | > (0.039)  | witzerland |
| 1 | > (0.059)  | > (0.057)  |            |            | > (0.043)  |
| 7 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Spain    | > Ukraine  | > United   | > Brazil   | > Turkiye  |
|   | > (0.059)  | > (0.057)  | > Arab     | > (0.039)  | > (0.034)  |
| 1 |            |            | > Emirates |            |            |
| 8 |            |            | > (0.061)  |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Czechia  | > Norway   | > Bulgaria | > Turkiye  | > Belarus  |
|   | > (0.05)   | > (0.049)  | > (0.053)  | > (0.039)  | > (0.026)  |
| 1 |            |            |            |            |            |
| 9 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Finland  | >          | > unknown  | > unknown  | > Finland  |
|   | > (0.05)   |  Australia | > s        | > s        | > (0.026)  |
| 2 |            | > (0.041)  | upplier(s) | upplier(s) |            |
| 0 |            |            | > (0.053)  | > (0.039)  |            |
+---+------------+------------+------------+------------+------------+

> Table 2: Top 20 Arms Suppliers by Out-Degree Centrality, 2005-2025

The HHI scores increase steadily across the observed period, rising from
0.180 in 2005 to 0.205 in 2025. According to standard concentration
thresholds --- where values below 0.15 indicate low concentration,
0.15--0.25 moderate concentration, and above 0.25 high concentration ---
the arms trade supplier market falls within the moderate concentration
band throughout the period (Bromberg, 2026). However, the consistent
upward trend suggests that supplier concentration is deepening over
time, moving toward the upper bound of this band.

> Table 3: Supplier Concentration (HHI) and Top Supplier Market Share,
> 2005-2025

+-----------+-------------+---------------------+---------------------+
| > Year    | > HHI       | > Top Supplier      | > Market Share      |
+===========+=============+=====================+=====================+
| > 2005    | > 0.1797    | > United States     | > 0.3144            |
+-----------+-------------+---------------------+---------------------+
| > 2010    | > 0.1808    | > United States     | > 0.3234            |
+-----------+-------------+---------------------+---------------------+
| > 2015    | > 0.1887    | > United States     | > 0.3591            |
+-----------+-------------+---------------------+---------------------+
| > 2020    | > 0.2052    | > United States     | > 0.4045            |
+-----------+-------------+---------------------+---------------------+
| > 2025    | > 0.2051    | > United States     | > 0.4169            |
+-----------+-------------+---------------------+---------------------+

Table 4 disaggregates this concentration further by presenting the
market share of the top 10 suppliers for each cross-section. United
States market share score increases over the years.

Table 4: Top 10 Suppliers by Market Share (TIV), 2005-2025

+---+------------+------------+------------+------------+------------+
| > | > 2005     | > 2010     | > 2015     | > 2020     | > 2025     |
|   |            |            |            |            |            |
| R |            |            |            |            |            |
| a |            |            |            |            |            |
| n |            |            |            |            |            |
| k |            |            |            |            |            |
+===+============+============+============+============+============+
| > | > United   | > United   | > United   | > United   | > United   |
|   | > States   | > States   | > States   | > States   | > States   |
| 1 | > (0.314)  | > (0.323)  | > (0.359)  | > (0.404)  | > (0.417)  |
+---+------------+------------+------------+------------+------------+
| > | > Russia   | > Russia   | > Russia   | > Russia   | > France   |
|   | > (0.243)  | > (0.241)  | > (0.202)  | > (0.152)  | > (0.1)    |
| 2 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Germany  | > Germany  | > France   | > France   | > Israel   |
|   | > (0.097)  | > (0.092)  | > (0.078)  | > (0.095)  | > (0.078)  |
| 3 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > France   | > China    | > China    | > Germany  | > South    |
|   | > (0.077)  | > (0.059)  | > (0.064)  | > (0.048)  | > Korea    |
| 4 |            |            |            |            | > (0.06)   |
+---+------------+------------+------------+------------+------------+
| > | > United   | > United   | > Germany  | > Spain    | > Russia   |
|   | > Kingdom  | > Kingdom  | > (0.063)  | > (0.042)  | > (0.058)  |
| 5 | > (0.046)  | > (0.044)  |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Italy    | > France   | > United   | > Italy    | > Italy    |
|   | > (0.039)  | > (0.034)  | > Kingdom  | > (0.034)  | > (0.057)  |
| 6 |            |            | > (0.041)  |            |            |
+---+------------+------------+------------+------------+------------+
| > | > Sweden   | > Israel   | > Spain    | > South    | > Germany  |
|   | > (0.025)  | > (0.027)  | > (0.034)  | > Korea    | > (0.051)  |
| 7 |            |            |            | > (0.034)  |            |
+---+------------+------------+------------+------------+------------+
| > | > Israel   | > Sweden   | > Italy    | > China    | > China    |
|   | > (0.024)  | > (0.024)  | > (0.023)  | > (0.027)  | > (0.026)  |
| 8 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+
| > | > N        | > Italy    | > Israel   | > United   | > United   |
|   | etherlands | > (0.022)  | > (0.02)   | > Kingdom  | > Kingdom  |
| 9 | > (0.023)  |            |            | > (0.027)  | > (0.021)  |
+---+------------+------------+------------+------------+------------+
| > | > China    | > Ukraine  | > S        | > N        | > N        |
|   | > (0.016)  | > (0.02)   | witzerland | etherlands | etherlands |
| 1 |            |            | > (0.017)  | > (0.021)  | > (0.018)  |
| 0 |            |            |            |            |            |
+---+------------+------------+------------+------------+------------+

**Discussion**

Kinsella (2003) anticipated that the end of Cold War bipolarity would
open the arms trade to broader market competition, producing a more
dispersed and less centralized supplier structure as former Eastern and
Western blocs increasingly traded across old divide. The evidence
assembled here does not support this expectation. Between 2005 and 2025,
network centralization rose from 0.36 to 0.54, and the HHI rose in
parallel, from 0.18 to 0.21, placing the arms trade at the upper edge of
the moderate-concentration band throughout the period. The two measures
move together: growing supplier dominance is visible both in how many
states the leading suppliers reach (centralization) and in how much of
total transfer value they control (HHI). Over the same period, the
leading supplier's share of global transfer value rose from 31 to 42 per
cent. Two decades on from the period Kinsella examined, the arms trade
has become more concentrated, not less.

This aggregate trend, however, conceals a more complex dynamic
underneath it. Concentration has deepened at the top of the supplier
hierarchy at the same time as new states have entered the tier below it
-- a pattern of simultaneous consolidation and diversification rather
than uniform marketization or uniform concentrations.

The clearest illustration of the first half of this pattern is Russia's
declining position. Russia's out-degree centrality fell from 0.291 in
2010 to 0.092 by 2025, dropping out of the top ten suppliers for the
first time in the series, and its share of transfer value fell out of
the top five altogether. The decline sharpened after 2020 and matches
with Russia's full-scale invasion of Ukraine in 2022. SIPRI own's
account attributes the fall -- 64 per cent between 2015-19 and 2020-24
-- to a decisive shift Russia'a global standing, which pushed it to
third place among arms exporters behind the United States and France
(George et al., 2025, 2026). More specifically, the decline is linked to
Russia redirecting weapons production toward its own armed forces rather
than export markets, the effect of multilateral sanctions, and
diplomatic pressure discouraging states from purchasing Russian arms.

This retreat from the export market has not been accompanied by a
retreated from military production. Russia's military expenditure
reached an estimated \$ 190 billion in 2025, a futher 5.9 per cent
increase reached on 2024 -- the slowest annual growth rate since the
invasion began, but growth nonetheless -- equivalent to 7.5 per cent of
GDP and 20 per cent of total government spending the highest share SIPRI
has recorded for Russia (Liang et al., 2026). As the war has settled
into attrition, Russian procurement has shifted toward cheaper,
mass-producible systems, particularly drones, to offset the loss of
costlier platforms such as aircraft and armoured vehicles. Russia's
declining out-degree thus reflects a redirection of military-industrial
capacity inward, toward a lower-cost mode of warfare, rather than a
decline in that capacity itself -- and, notably, this reliance on
inexpensive, rapidly fielded drone systems is a feature Russia now
shares with the rising suppliers discussed next.

This shift is directly visible in the network data itself. The ratio
between Russia's out-degree and in-degree --- 25:0 in 2005 --- narrowed
to roughly 3.7:1 by 2025 (11 out-degree, 3 in-degree), with 2025
recording the second-highest inbound transfer value (129 TIV) of the
five cross-sections. The suppliers behind this figure are themselves
telling: Iran (80 TIV), North Korea (44 TIV, across five separate
transfers), and China (5 TIV) --- precisely the states with which Russia
has deepened ties during the war in Ukraine. Russia remains, by count, a
net supplier; but the balance between its supplying and receiving roles
has narrowed sharply at exactly the moment its outward reach has
contracted most.

The lower tier of the network shows the opposite movement. Turkiye's
out-degree centrality rose steadily across the period, from 0.034 in
2005 to 0.168 in 2025, entering the top ten suppliers for the first time
in the final cross-section examined here. South Korea, absent from the
top twenty suppliers before 2020, appeared at rank eight in 2020 and
rank eleven in 2025, also entering the top ten by transfer value for the
first time. Both trajectories are consistent with reporting on the
drivers of these emerging suppliers: Turkiye's drone exports, led by the
Bayraktar TB2 and Akıncı platforms, have reached more than thirty states
across Africa, the Middle East, Asia, and Eastern Europe, aided by a
combat-proven reputation from their use in Libya, Nagorno-Karabakh, and
Ukraine, competitive pricing, and an export posture less constrained by
the licensing regimes governing many Western systems (Egeli et al.,
2024; Kurç, 2024). Turkiye's total arms exports rose by over 100 per
cent between the 2014--18 and 2019--23 periods, making it the
fourth-largest supplier to Sub-Saharan Africa by 2024. These entrants
show that concentration at the top of the network has not foreclosed the
emergence of new, lower-tier suppliers --- a pattern the aggregate
density and centralization measures alone do not capture. 

As noted in the Method section, two qualifications apply to these
findings. First, because SIPRI records subsystem-level transfers as
separate ties only when supplied independently of the platform, and
attributes multinational production to the state of final assembly, the
network captures the distribution of platform suppliers and final
assemblers rather than the complete underlying production network; since
component-level transfers account for a stable share of roughly 10 per
cent of total TIV across sub-periods, this is unlikely to drive the
centralization trend reported here, though it may understate
diversification occurring at the component level specifically. Second,
the SIPRI TIV reflects the transfer of military resources rather than
financial value, so the market-share findings above should be read as
measures of resource flow rather than commercial revenue.

These findings raise a further question this study does not address: how
resilient is the network's current structure to the removal of its most
central suppliers? Future work will extend this analysis with network
resilience measures --- for instance, simulating the effect of removing
the top supplier(s) on overall connectivity and density --- to assess
whether the arms trade\'s historically high concentration would prove
fragile or robust to a shock affecting a dominant supplier such as the
United States.

**Bibliography**

Bromberg, M. (2026, April 28). *Herfindahl-Hirschman Index (HHI):
Definition, Formula, and Example*. Investopedia. Investopedia.
https://www.investopedia.com/terms/h/hhi.asp

Egeli, S., Güvenç, S., Kurç, Ç., & Mevlütoğlu, A. (2024). *From Client
to Competitor: The Rise of Turkiye's Defence Industry*.

George, M., Djokic, K., Hussain, Z., Wezeman, P. D., & Wezeman, S. T.
/SIPRI. (2025). Trends in International Arms Transfers, 2024. *SIPRI
Fact Sheet*.

George, M., Djokic, K., Hussain, Z., Wezeman, P. D., & Wezeman, S. T.
/SIPRI. (2026). Trends in International Arms Transfers, 2025. *SIPRI
Fact Sheet*.

Kinsella, D. T. (2003). *Changing structure of the arms trade: A social
network analysis*.
https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1018&context=polisci_fac

Kurç, Ç. (2024). No Strings Attached: Understanding Turkey's Arms
Exports to Africa. *Journal of Balkan and Near Eastern Studies*,
*26*(3), 378--395. https://doi.org/10.1080/19448953.2023.2236515

Liang, X., Tian, N., Diego, L. da S., Scarazzato, L., Karim, Z., &
Guiberteau Ricard, J. (2026). Trends in World Military Expenditure,
2025. *SIPRI Fact Sheet*.

SIPRI. (n.d.). *Sources and methods: SIPRI Arms Transfers Database*.
SIPRI. Stockholm International Peace Research Institute. Retrieved
https://www.sipri.org/databases/armstransfers/sources-and-methods

[^1]: Used to measure market monopolization in the field of economics,
    this index is adapted in network theory to measure how centralized
    or concentrated a node or a specific resource is in the system
    (Bromberg, 2026).
