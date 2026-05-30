"""
NBA 2023-24 Analysis: Minutes Played vs Points Scored
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# Create outputs folder
os.makedirs('../outputs', exist_ok=True)

# ============================================
# PART 1: LOAD DATA
# ============================================
df = pd.read_csv('../data/nba_players.csv')
print("✅ Data loaded")
print(f"   {len(df)} players\n")

# ============================================
# PART 2: DESCRIPTIVE STATISTICS
# ============================================
print("="*50)
print("DESCRIPTIVE STATISTICS")
print("="*50)

print(f"\nMean Minutes: {df['Minutes'].mean():.2f}")
print(f"Mean Points:  {df['Points'].mean():.2f}")

print(f"\nMedian Minutes: {df['Minutes'].median():.2f}")
print(f"Median Points:  {df['Points'].median():.2f}")

print(f"\nRange Minutes: {df['Minutes'].max() - df['Minutes'].min():.1f}")
print(f"Range Points:  {df['Points'].max() - df['Points'].min():.0f}")

print(f"\nVariance Minutes: {df['Minutes'].var():.2f}")
print(f"Variance Points:  {df['Points'].var():.2f}")

print(f"\nStd Dev Minutes: {df['Minutes'].std():.2f}")
print(f"Std Dev Points:  {df['Points'].std():.2f}")

cv_minutes = (df['Minutes'].std() / df['Minutes'].mean()) * 100
cv_points = (df['Points'].std() / df['Points'].mean()) * 100
print(f"\nCV Minutes: {cv_minutes:.2f}%")
print(f"CV Points:  {cv_points:.2f}%")

q1_m, q3_m = df['Minutes'].quantile(0.25), df['Minutes'].quantile(0.75)
q1_p, q3_p = df['Points'].quantile(0.25), df['Points'].quantile(0.75)
print(f"\nIQR Minutes: {q3_m - q1_m:.1f}")
print(f"IQR Points:  {q3_p - q1_p:.0f}")

# ============================================
# PART 3: CORRELATION & REGRESSION (using sklearn)
# ============================================
print("\n" + "="*50)
print("CORRELATION & REGRESSION")
print("="*50)

correlation = df['Minutes'].corr(df['Points'])
r_squared = correlation ** 2

print(f"\nCorrelation (r):  {correlation:.4f}")
print(f"R-squared (r²):   {r_squared:.4f}")

# Linear Regression using sklearn
X = df[['Minutes']].values  # Note: double brackets for DataFrame
y = df['Points']

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_

print(f"\nRegression Equation:")
print(f"Points = {slope:.2f} × Minutes + {intercept:.2f}")

# ============================================
# PART 4: SCATTER PLOT WITH REGRESSION LINE
# ============================================
print("\n" + "="*50)
print("CREATING VISUALIZATIONS")
print("="*50)

fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot
ax.scatter(df['Minutes'], df['Points'], s=100, alpha=0.7,
           color='steelblue', edgecolors='white', linewidth=1.5)

# Regression line
x_line = np.array([[df['Minutes'].min(), df['Minutes'].max()]]).T
y_line = model.predict(x_line)
ax.plot(x_line, y_line, color='crimson', linewidth=2,
        label=f'Regression (r = {correlation:.2f})')

# Labels
ax.set_xlabel('Total Minutes Played', fontsize=12, fontweight='bold')
ax.set_ylabel('Total Points Scored', fontsize=12, fontweight='bold')
ax.set_title('NBA 2023-24: Minutes vs Points\nTop 30 Players by Minutes Played',
             fontsize=14, fontweight='bold')

# Statistics box
stats_text = f'r = {correlation:.3f}\nr² = {r_squared:.3f}\nn = {len(df)} players'
ax.text(0.05, 0.95, stats_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../outputs/scatter_plot.png', dpi=300)
plt.show()

# ============================================
# PART 5: EFFICIENCY ANALYSIS
# ============================================
df['Points_Per_Minute'] = df['Points'] / df['Minutes']

print("\n" + "="*50)
print("EFFICIENCY ANALYSIS")
print("="*50)

print("\nTop 5 Most Efficient Scorers:")
print(df.nlargest(5, 'Points_Per_Minute')[['Player', 'Points_Per_Minute', 'Points']].to_string(index=False))

print("\nBottom 5 Least Efficient:")
print(df.nsmallest(5, 'Points_Per_Minute')[['Player', 'Points_Per_Minute', 'Points']].to_string(index=False))

# ============================================
# PART 6: SAVE RESULTS
# ============================================
df.to_csv('../outputs/analysis_results.csv', index=False)
print("\n✅ Results saved to outputs/")