import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#pandas
df = pd.read_excel("Fifa_master_v2.xlsx")

print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df["year"].dtype)
print(df["year"].unique())
df
df["squad_value_m"] = df["squad_total_market_value_eur"] / 1_000_000 ## Convert squad value from euros to millions
print(df[["team", "year", "squad_value_m"]].head(10))


df["round_score"] = 0

df.loc[df["quarter_finalist"] == 1, "round_score"] = 2
df.loc[df["semi_finalist"] == 1, "round_score"] = 3
df.loc[df["finalist"] == 1, "round_score"] = 4
df.loc[df["winner"] == 1, "round_score"] = 5
print(df[["team","year","round_score"]].head(10))


df["Roi"]=df["round_score"]/df["squad_value_m"] #Roi Values
print(df[["team","year","Roi"]].head(5))

df['Roi']=(df["Roi"]*100).round(2)  #Simplifying
print(df[["team","year","Roi",]].head(10))

df["team_year"] = df["team"] + " (" + df["year"].astype(str) + ")"

Top_10=df.sort_values("Roi",ascending=False).head(10) #Top 10 Roi
Top_10 = Top_10.sort_values("Roi")
print(Top_10[["team","year","squad_value_m","Roi"]])
df
big_spenders=df[df['squad_value_m'] > 300] 
worst_10=big_spenders.sort_values('Roi' , ascending=True).head(10) 
print(worst_10[["team","year","squad_value_m","Roi"]])


df[["squad_value_m","round_score"]].corr()
print(df[["squad_value_m", "round_score"]].corr())#Correlation Analysis

top_value = df.sort_values("squad_value_m" , ascending=False)

print(top_value[["team","year","squad_value_m"]].head(10)) #Top10 expensive squads

bottom_value = df.sort_values("squad_value_m")
print(bottom_value[["team","year","squad_value_m"]].head(10)) #Top10 cheapest squads

print(df.groupby("year")["squad_value_m"].mean()) #Average Squad Value by Year

print(df.groupby("year")["Roi"].mean()) #Average Performance Efficiency by Year


#matplotlib
# top 10 roi teams
colors = ["steelblue"] * 9 + ["gold"] #Inserting Colour for highlighting

plt.figure(figsize=(17,15))
plt.barh(Top_10['team_year'],Top_10['Roi'],color=colors)
plt.title("Top 10 Value-for-Money World Cup Teams (2010–2022)")
plt.xlabel("Return of Investment Score")
plt.ylabel("Teams")

plt.savefig(
    "charts/top_10_roi.png",     dpi=300,     bbox_inches="tight"
)
plt.show()



# relationship between spending and success
years = [2010, 2014, 2018, 2022]

for year in years:

 print("=" * 30)
 print(f"Processing Year: {year}")

year_df = df[df["year"] == year]

print(f"Rows found: {len(year_df)}")

plt.figure(figsize=(10,7))

plt.scatter(
      year_df["squad_value_m"],
        year_df["round_score"],
        alpha=0.7,
        s=70,
        edgecolor="black",
        linewidth=0.5
    )
# Correlation
corr = year_df["squad_value_m"].corr(year_df["round_score"])

plt.title(
        f"Does Squad Market Value Influence Success? ({year})\nCorrelation = {corr:.2f}"
    )

plt.xlabel("Squad Market Value (€ Million)")
plt.ylabel("Tournament Performance Score")


  

plt.savefig(
        f"charts/scatter_{year}.png",
        dpi=300,
        bbox_inches="tight"
    )

plt.show()
plt.close()

# biggest underperforming expensive teams
# Rank teams by spending WITHIN their own year (1 = most expensive that year)
df['value_rank_in_year'] = df.groupby('year')['squad_value_m'].rank(ascending=False, method='min')

# Disappointments = top 8 spenders that year (real favorites) who still exited group stage
disappointments = df[(df['value_rank_in_year'] <= 5) & (df['round_score'] <= 2)]
disappointments = disappointments.sort_values('squad_value_m', ascending=True)

print(disappointments[['team_year','year','squad_value_m','value_rank_in_year','round_score']])

plt.figure(figsize=(13,10))
plt.barh(disappointments["team_year"], disappointments["squad_value_m"], color="crimson")
plt.title("Biggest World Cup Disappointments\nTop 5 Favorites Each Year, Exited by Quarterfinals")
plt.xlabel("Squad Value (€ Million)")
plt.ylabel("Teams")
plt.savefig("charts/biggest_disappointments.png", dpi=300, bbox_inches="tight")
plt.show()

# Yearly Roi trend vs Yearly spending trend
yearly_spending = df.groupby('year')["squad_value_m"].mean()
plt.figure(figsize=(10,6))

plt.plot(yearly_spending.index, yearly_spending.values, marker='o', linewidth=2, color='green')
plt.title('Average Squad Market Value by World Cup Year')
plt.xlabel('Year')
plt.ylabel('Average Squad Market Value (€ Million)')
plt.savefig("charts/yearly_Spending_trend.png", dpi=300, bbox_inches="tight")
plt.show()

