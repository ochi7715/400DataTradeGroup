import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "trade.csv"
df = pd.read_csv(file_path)

sns.set_theme(style="whitegrid")

latest_year = df["Year"].max()
df_trade_volume = df[df["Year"] == latest_year].copy()
df_trade_volume["Total Trade"] = df_trade_volume["average_value_Merchandise exports (current US$)"] + \
                                 df_trade_volume["average_value_Merchandise imports (current US$)"]
df_top_trade = df_trade_volume.nlargest(10, "Total Trade")

plt.figure(figsize=(10, 6))
sns.barplot(y="Country Name", x="Total Trade", data=df_top_trade, palette="magma")
plt.title(f"Top 10 Countries by Total Trade Volume ({latest_year})")
plt.xlabel("Total Trade (US$ Trillions)")
plt.ylabel("Country")
plt.show()

df_growth = df.groupby("Year")["average_value_Merchandise exports (current US$)"].sum().pct_change() * 100

plt.figure(figsize=(10, 5))
plt.plot(df_growth.index, df_growth, marker='o', linestyle='-', color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title("Merchandise Export Growth Rate Over Time")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.show()