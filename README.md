# NBA 2023-24: Minutes vs Points Analysis

**Author:** Muhammad Syawaluddin Bin Adzran

**Data Source:** [NBA.com Official Statistics](https://www.nba.com/stats/players/traditional?PerMode=Totals&Season=2023-24&sort=MIN&dir=-1&SeasonType=Regular+Season)

---

## Project Overview

This project analyzes the relationship between total minutes played and total points scored for the 30 NBA players with the most minutes in the 2023-24 regular season.

**Motivation:** The NBA introduced a new 65-game rule for award eligibility (Most Valuable Player, Defensive Player of the Year, All-NBA teams, All-Defensive Teams), making minutes played more important than ever. This analysis asks: *Does playing more minutes actually lead to more points?*

---

## Key Findings

| Metric              | Value                            | Interpretation                                    |
|:--------------------|:---------------------------------|:--------------------------------------------------|
| Correlation (r)     | 0.14                             | Weak positive relationship                        |
| R-squared (r²)      | 0.02                             | Only 2% of scoring variation explained by minutes |
| Regression Equation | Points = 0.44 × Minutes + 505.77 | Each additional minute = 0.44 more points         |

**Conclusion:** Among high-minute players, playing time is a poor predictor of scoring. Efficiency, role, and skill matter far more.

---

## The 65-Game Rule Context

The 2023-24 NBA season introduced a new rule which is the players must play at least 65 games to be eligible for major awards including:

- Most Valuable Player (MVP)
- Defensive Player of the Year (DPOY)
- All-NBA Teams
- All-Defensive Teams

This rule changed how coaches manage minutes. Players who want awards must play but playing more minutes doesn't guarantee scoring.

### Award Winners in This Dataset

| Award            | Winner                  | Minutes Played | Minutes Rank (Top 30) | Points Per Game |
|:-----------------|:------------------------|:---------------|:----------------------|:----------------|
| MVP              | Nikola Jokic            | 2736.5         | #12                   | 26.4            |
| MVP Runner-Up    | Shai Gilgeous-Alexander | 2552.7         | #28                   | 30.9            |
| DPOY             | Rudy Gobert             | 2593.1         | #22                   | 14.0            |
| All-NBA 1st Team | Luka Doncic             | 2624.0         | #20                   | 32.9            |
| All-NBA 1st Team | Shai Gilgeous-Alexander | 2552.7         | #28                   | 30.9            |
| All-NBA 1st Team | Giannis Antetokounmpo   | 2567.2         | #26                   | 30.8            |
| All-NBA 1st Team | Nikola Jokic            | 2736.5         | #12                   | 26.4            |
| All-NBA 1st Team | Jayson Tatum            | 2645.2         | #15                   | 27.0            |

**Key observation:** Minutes played varies widely among award winners. Jokic played 2736 minutes (rank #12). Gobert played 2593 minutes (rank #22) and won DPOY primarily through defense, not scoring as he averaged only 14.0 points per game. Minutes alone do not determine award-worthiness.

---

## Regression Analysis

### The Equation

`Points = (0.46 × Minutes) + 452.08`

### What This Means

| Term                   | Value                                                        | Interpretation                               |
|:-----------------------|:-------------------------------------------------------------|:---------------------------------------------|
| **Slope (0.46)**       | Each additional minute played adds 0.46 points               | Very small effect as minutes barely matter    |
| **Intercept (452.08)** | A player with 0 minutes would theoretically score 452 points | Not realistic, but mathematically necessary  |
| **R-squared (0.02)**   | Minutes explain only 2% of scoring variation                 | 98% of scoring is explained by OTHER factors |

### Prediction Example

If a player plays 2500 minutes:

`Points = (0.46 × 2500) + 452.08 = 1150 + 452.08 = 1602.08`

If a player plays 3000 minutes:

`Points = (0.46 × 3000) + 452.08 = 1380 + 452.08 = 1832.08`

**Conclusion:** Even at very high minutes, predicted points are modest. Scoring depends more on who you are than how long you play.

---

## Interesting Insights

- **Luka Doncic** scored 2,370 points (2nd most) while playing only 2,624 minutes (20th most)
- **Josh Hart** played 2,707 minutes (11th most) but scored only 761 points as he contributes through defense and rebounding
- **Rudy Gobert** won DPOY while rank number 22 in minutes played and averaging only 14.0 points per game proving that defensive impact matters more than scoring or playing time

---

## Files in This Repository

| File                           | Description                              |
|:-------------------------------|:-----------------------------------------|
| `data/nba_players.csv`         | Raw data (30 players, minutes, points)   |
| `scripts/analysis.py`          | Complete Python analysis script          |
| `outputs/scatter_plot.png`     | Scatter plot with regression line        |
| `outputs/analysis_results.csv` | Full results including efficiency metric |

---

## How to Reproduce

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Syawaluddin-Adzran/nba-minutes-points-analysis.git
cd nba-minutes-points-analysis

# Install dependencies
pip install pandas matplotlib scipy scikit-learn

# Run the analysis
python scripts/analysis.py
