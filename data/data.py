import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_movies.csv')
pd.set_option('display.max_columns', None)
print(df)



filtered_df = df[df['runtime'] > 30]
film_count_by_year = filtered_df['release_year'].value_counts().sort_index()
film_count_df = pd.DataFrame({'Year': film_count_by_year.index, 'Number of Films': film_count_by_year.values})
print(film_count_df)

print("Soale 1 **************************")

filtered_df9 = df[df['runtime'] >= 30]
film_count_by_year = filtered_df9['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.bar(film_count_by_year.index, film_count_by_year.values, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Number of Films')
plt.title('Number of Films Released in Each Year (excluding films under 30m runtime)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

print("Soale 2 **************************")


df_filtered1 = df[df['runtime'] > 30]
mean_runtime = df_filtered1['runtime'].mean()
print("Mean Runtime For All Years (Excluding under 30 values):", mean_runtime)

print("Soale 3**************************")

filtered_df34 = df[df['runtime'] >= 30]
mean_runtime_by_year = filtered_df34.groupby('release_year')['runtime'].mean().sort_index()
print("Mean runtime of films in each year (excluding films under 30m runtime):")
for year, mean_runtime in mean_runtime_by_year.items():
    hours = int(mean_runtime // 60)
    minutes = int(mean_runtime % 60)
    print(f"Year: {year} - Mean Runtime: {hours} hours {minutes} minutes")

print("Soale 4 **************************")


df_filtered = df[df['runtime'] > 30]
max_runtime_row = df_filtered[df_filtered['runtime'] == df_filtered['runtime'].max()]
min_runtime_row = df_filtered[df_filtered['runtime'] == df_filtered['runtime'].min()]
print("Movie with the highest runtime:")
print(f"{max_runtime_row['original_title'].iloc[0]} (Runtime: {max_runtime_row['runtime'].iloc[0]} minutes)")
print("\nMovie with the lowest runtime:")
print(f"{min_runtime_row['original_title'].iloc[0]} (Runtime: {min_runtime_row['runtime'].iloc[0]} minutes)")

print("Soal 5 **************************")

dfff = df[df['runtime'] > 30]
mini=dfff.groupby("release_year")["runtime"].min()

maxi=dfff.groupby("release_year")["runtime"].max()
mini=mini.reset_index()
maxi=maxi.reset_index()
date=list()
mini_list=list()
maxi_list=list()
for i in mini["runtime"]:
    mini_list.append(i)
for i in maxi["runtime"]:
    maxi_list.append(i)
for i in maxi["release_year"]:
    date.append(i)
dataa=list(zip(date,mini_list,maxi_list))
dff=pd.DataFrame(dataa,columns=["date","min","max"])
print(dff)

print("Soale 6 **************************")

filtered_df = df[df['runtime'] >= 30]
mean_runtime_by_year = filtered_df.groupby('release_year')['runtime'].mean().sort_index()
plt.figure(figsize=(12, 6))
plt.bar(mean_runtime_by_year.index, mean_runtime_by_year, color='skyblue')
plt.xlabel('Year')
plt.ylabel('Mean Runtime (in minutes)')
plt.title('Mean Runtime of Films per Year (excluding films under 30m runtime)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

print("Soale 7 **************************")


df_filtered2 = df[df['budget_adj'] > 5000]
mean_budget = df_filtered2['budget_adj'].mean()
print("Mean budget_adj For All Years (Excluding under 5000 values):", mean_budget)

print("Soale 8**************************")

df_filtered3 = df[df['revenue_adj'] > 5000]
mean_revenue = df_filtered3['revenue_adj'].mean()
print("Mean revenue_adj For All Years (excluding under 5000 values):", mean_revenue)

print("Soale 9 **************************")

dff=df[df["budget_adj"] > 5000]
dff=dff[dff["revenue_adj"] > 5000]
mean_bod=dff.groupby("release_year")["budget_adj"].mean()
mean_rev=dff.groupby("release_year")["revenue_adj"].mean()
mean_bod=mean_bod.reset_index()
mean_rev=mean_rev.reset_index()
rev_list=list()
bod_list=list()
date=list()
for i in mean_bod["budget_adj"]:
    bod_list.append(i)
for i in mean_rev["revenue_adj"]:
    rev_list.append(i)
for i in mean_rev["release_year"]:
    date.append(i)

dataa=list(zip(date,bod_list,rev_list))
dff=pd.DataFrame(dataa,columns=["date","mean_bud","mean_rev"])
print(dff)

print("Soale 10 **************************")

filtered_df = df[(df['budget_adj'] > 5000) & (df['revenue_adj'] > 5000)]
mean_budget_by_year = filtered_df.groupby('release_year')['budget_adj'].mean()
mean_revenue_by_year = filtered_df.groupby('release_year')['revenue_adj'].mean()
plt.figure(figsize=(12, 6))
plt.scatter(mean_budget_by_year, mean_revenue_by_year, color='skyblue', edgecolors='black')
plt.xlabel('Mean Budget (adjusted)')
plt.ylabel('Mean Revenue (adjusted)')
plt.title('Relationship between Mean Budget and Mean Revenue per Year')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Soale 11 **************************")

genre_counts = df['genres'].value_counts()
top_20_genres = genre_counts.head(20)
print(f"Number of unique genres: {len(genre_counts)}")
most_used_genre = genre_counts.idxmax()
print(f"The most used genre: {most_used_genre} (Count: {genre_counts.max()})")
plt.figure(figsize=(12, 6))
top_20_genres.plot(kind='bar', color='skyblue')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.title('Number of Films per Genre (Top 20)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

print("Soale 12 **************************")


df_filtered4 = df[(df['revenue_adj'] > 5000) & (df['budget_adj'] > 5000)]
df_filtered4['profit'] = df_filtered4['revenue_adj'] - df_filtered4['budget_adj']
max_profit_row = df_filtered4.loc[df_filtered4['profit'].idxmax()]
print("Movie with the highest profit:")
print("Title:", max_profit_row['original_title'])
print("Profit:", max_profit_row['profit'])


print("Soale 13 **************************")

filtered_df6 = df[(df['runtime'] >= 30) & (df['budget_adj'] >= 5000) & (df['revenue_adj'] >= 5000)]
filtered_df6['profit'] = filtered_df6['revenue_adj'] - filtered_df6['budget_adj']
max_profit_films = filtered_df6.loc[filtered_df6.groupby('release_year')['profit'].idxmax()]
print("Film with the highest profit for each year:")
for index, row in max_profit_films.iterrows():
    print(f"Year: {row['release_year']} - Film: {row['original_title']} - Profit: {row['profit']}")


print("Soale 14 **************************")

filtered_df5 = df[(df['runtime'] < 30) & (df['budget_adj'] < 5000) & (df['revenue_adj'] < 5000)]
production_companies_count = filtered_df5['production_companies'].value_counts()
print("Production company names and the number of their films:")
for company, count in production_companies_count.items():
    print(f"{company} - Number of Films: {count}")
most_repeated_company = production_companies_count.idxmax()
print("\nThe most repeated production company name:")
print(most_repeated_company)

print("Soale 15 **************************")


sorted_df = df.sort_values(by='vote_count', ascending=False)
top_five = sorted_df.head(5)
print("Top five movies with the highest vote_count:")
for index, row in top_five.iterrows():
    print(f"{row['original_title']} - Vote Count: {row['vote_count']}")


print("Soal 16**************************")

filtered_df1 = df[df['vote_count'] >= 1000]
sorted_dff = filtered_df1.sort_values(by='vote_average', ascending=False)
top_five = sorted_dff.head(5)
print("Top five movies with the highest score (with at least 1000 votes each):")
for index, row in top_five.iterrows():
    print(f"{row['original_title']} - Vote Average: {row['vote_average']} (Vote Count: {row['vote_count']})")

print("Soal 17 **************************")












