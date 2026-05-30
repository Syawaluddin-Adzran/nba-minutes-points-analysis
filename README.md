# NBA 2023-24: Do Minutes Played Predict Points Scored?

**Author:** Muhammad Syawaluddin Bin Adzran

**Data Source:** [NBA.com Official Statistics](https://www.nba.com/stats/players/traditional?PerMode=Totals&Season=2023-24)



## Project Overview

This project analyzes the relationship between total minutes played and total points scored for the 30 NBA players with the most minutes in the 2023-24 regular season.

**Motivation:** The NBA introduced a new 65-game rule for award eligibility (MVP, Defensive Player of the Year), making minutes played more important than ever. This analysis asks: Does playing more minutes actually lead to more points?

## Key Findings

## Key Findings

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Correlation (r) | 0.14 | Weak positive relationship |
| R-squared (r²) | 0.02 | Only 2% of scoring variation explained by minutes |
| Regression Equation | Points = 0.44 × Minutes + 505.77 | Each additional minute = 0.44 more points |

**Conclusion:** Among high-minute players, playing time is a poor predictor of scoring. Efficiency, role, and skill matter far more.

## Interesting Insights

- **Luka Doncic** scored 2,370 points (2nd most) while playing only 2,624 minutes (20th most)
- **Josh Hart** played 2,707 minutes (11th most) but scored only 761 points – he contributes through defense and rebounding
- **Most efficient scorer:** Giannis Antetokounmpo (0.866 points per minute)

## Files in This Repository

| File | Description |
| :--- | :--- |
| `data/nba_players.csv` | Raw data (30 players, minutes, points) |
| `scripts/analysis.py` | Complete Python analysis script |
| `outputs/scatter_plot.png` | Scatter plot with regression line |
| `outputs/analysis_results.csv` | Full results including efficiency metric |

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