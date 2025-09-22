# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the visual style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load your cleaned dataset
df = pd.read_csv("C:/Users/Abi/Documents/data analytics/task1 - Sheet1.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
# Check data types
print("Data Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert specific columns to numeric
df['Installs_Clean'] = pd.to_numeric(df['Installs_Clean'])
df['Size_MB'] = pd.to_numeric(df['Size_MB'])
df['Price_Clean'] = pd.to_numeric(df['Price_Clean'])


# Visualization 1: App Count and Avg Rating by Category

category_stats = df.groupby('Category').agg(
    Avg_Rating=('Rating', 'mean'),
    Count=('App', 'count')
).sort_values('Count', ascending=False)

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(category_stats.index, category_stats['Count'],
              color=plt.cm.viridis(category_stats['Avg_Rating'] / 5))

ax.set_title('App Count and Average Rating by Category', fontsize=16, fontweight='bold')
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Number of Apps', fontsize=12)


ax.set_xticks(range(len(category_stats.index)))
ax.set_xticklabels(category_stats.index, rotation=90)

# Add colorbar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=3.5, vmax=5))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Average Rating', fontsize=12)

plt.tight_layout()
plt.show()


# Visualization 2: Free vs Paid

type_stats = df.groupby('Type').agg(
    Count=('App', 'count'),
    Avg_Rating=('Rating', 'mean')
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.pie(type_stats['Count'], labels=type_stats.index, autopct='%1.1f%%',
        colors=['lightblue', 'lightcoral'])
ax1.set_title('Free vs Paid Apps Distribution')

ax2.bar(type_stats.index, type_stats['Avg_Rating'], color=['lightblue', 'lightcoral'])
ax2.set_title('Average Rating by App Type')
ax2.set_ylabel('Average Rating')
ax2.set_ylim(3.5, 4.5)

plt.tight_layout()
plt.show()


# Visualization 3: Size vs Rating Scatter Plot


scatter_data = df[['Size_MB', 'Rating', 'Installs_Clean']].dropna()

# Fit regression line
z = np.polyfit(scatter_data['Size_MB'], scatter_data['Rating'], 1)
p = np.poly1d(z)

plt.figure(figsize=(12, 8))
scatter = plt.scatter(scatter_data['Size_MB'], scatter_data['Rating'],
                      alpha=0.6, c=scatter_data['Installs_Clean'], cmap='viridis', s=50)

plt.plot(scatter_data['Size_MB'], p(scatter_data['Size_MB']), "r--", alpha=0.8)

plt.colorbar(scatter, label='Install Count')
plt.title('App Size vs Rating Relationship', fontsize=16, fontweight='bold')
plt.xlabel('App Size (MB)', fontsize=12)
plt.ylabel('Rating', fontsize=12)
plt.ylim(0, 5)
plt.tight_layout()
plt.show()


# Visualization 4: Category Performance Quadrant

category_performance = df.groupby('Category').agg(
    Avg_Rating=('Rating', 'mean'),
    Avg_Installs=('Installs_Clean', 'mean'),
    Count=('App', 'count')
).reset_index()

overall_rating_avg = category_performance['Avg_Rating'].mean()
overall_installs_avg = category_performance['Avg_Installs'].mean()

plt.figure(figsize=(14, 10))
scatter = plt.scatter(category_performance['Avg_Installs'],
                      category_performance['Avg_Rating'],
                      s=category_performance['Count'] * 10,
                      alpha=0.7, cmap='tab20')

plt.axhline(y=overall_rating_avg, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=overall_installs_avg, color='gray', linestyle='--', alpha=0.7)

for i, row in category_performance.iterrows():
    plt.annotate(row['Category'],
                 (row['Avg_Installs'], row['Avg_Rating']),
                 xytext=(5, 5), textcoords='offset points',
                 fontsize=9)

plt.title('Category Performance Quadrant Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Average Installs (Log Scale)', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.xscale('log')
plt.grid(True, alpha=0.3)

plt.text(overall_installs_avg * 10, overall_rating_avg * 1.05,
         'Stars', fontsize=12, fontweight='bold', color='darkgreen')
plt.text(overall_installs_avg * 0.1, overall_rating_avg * 1.05,
         'Niche', fontsize=12, fontweight='bold', color='blue')
plt.text(overall_installs_avg * 10, overall_rating_avg * 0.95,
         'Mass Market', fontsize=12, fontweight='bold', color='orange')
plt.text(overall_installs_avg * 0.1, overall_rating_avg * 0.95,
         'Avoid', fontsize=12, fontweight='bold', color='red')

plt.tight_layout()
plt.show()




# Correlation heatmap
correlation_matrix = df[['Rating', 'Reviews', 'Installs_Clean', 'Size_MB', 'Price_Clean']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of App Features', fontsize=16, fontweight='bold')
plt.show()



# Save all visualizations
visualizations = [plt.figure(n) for n in plt.get_fignums()]

for i, fig in enumerate(visualizations):
    fig.savefig(f'visualization_{i+1}.png', dpi=300, bbox_inches='tight')

plt.close('all')  