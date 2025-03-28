import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "trade.csv"
df = pd.read_csv(file_path)

sns.set_theme(style="whitegrid")

df_filtered = df.groupby("Year")[["average_value_Merchandise exports (current US$)", 
                                  "average_value_Merchandise imports (current US$)"]].sum().dropna()

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle("Trade Trends Visualizations", fontsize=16)

axes[0, 0].plot(df_filtered.index, df_filtered["average_value_Merchandise exports (current US$)"], 
                marker='o', label="Exports", color='blue')
axes[0, 0].set_title("Global Merchandise Exports Over Time")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Exports (US$ Trillions)")
axes[0, 0].legend()

df_service = df.groupby("Year")[["average_value_Commercial service exports (current US$)", 
                                 "average_value_Commercial service imports (current US$)"]].sum().dropna()
axes[0, 1].plot(df_service.index, df_service["average_value_Commercial service exports (current US$)"], 
                label="Service Exports", color='green')
axes[0, 1].plot(df_service.index, df_service["average_value_Commercial service imports (current US$)"], 
                label="Service Imports", color='red')
axes[0, 1].set_title("Service Exports vs Imports Over Time")
axes[0, 1].set_xlabel("Year")
axes[0, 1].set_ylabel("US$ Trillions")
axes[0, 1].legend()

latest_year = df["Year"].max()
df_tech = df[df["Year"] == latest_year].nlargest(10, "average_value_High-technology exports (current US$)")

sns.barplot(y="Country Name", x="average_value_High-technology exports (current US$)", 
            data=df_tech, ax=axes[1, 0], palette="viridis")
axes[1, 0].set_title(f"Top 10 Countries in High-Technology Exports ({latest_year})")
axes[1, 0].set_xlabel("High-Tech Exports (US$ Billions)")
axes[1, 0].set_ylabel("Country")

axes[1, 1].plot(df_filtered.index, df_filtered["average_value_Merchandise exports (current US$)"] - 
                df_filtered["average_value_Merchandise imports (current US$)"], marker='s', color='purple')
axes[1, 1].set_title("Global Trade Balance Over Time")
axes[1, 1].set_xlabel("Year")
axes[1, 1].set_ylabel("Trade Balance (US$ Trillions)")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
