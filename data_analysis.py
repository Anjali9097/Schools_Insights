######################################################################## Number of Schools by Country and Region ####################################################################################################

# Grouping by country and region and calculating the count of schools
schools_by_region = df_ets.groupby(['country_name', 'region_name'])['t_schools'].sum().reset_index()
schools_by_region_sorted = schools_by_region.sort_values(by='t_schools', ascending=False)
schools_by_region_sorted

# Plotting the distribution of schools by country and region
plt.figure(figsize=(10, 6))
plt.bar(schools_by_region_sorted['region_name'], schools_by_region_sorted['t_schools'])
plt.title('Comparison of School Distribution Across Regions')
plt.xlabel('region_name')
plt.ylabel('Total Number of Schools')
plt.xticks(rotation=45)
plt.show()

######################################################################## Total Number of Schools by Country and Phase ##############################################################################################

# Total number of schools by country and phase
total_schools_by_country = df_ets.groupby(['country_name', 'phase'])['t_schools'].sum().unstack()
total_schools_by_country

# Plotting
total_schools_by_country.plot(kind='bar', stacked=True)
plt.title('Total Number of Schools by Country and Phase')
plt.xlabel('Country')
plt.ylabel('Number of Schools')
plt.xticks(rotation=45)
plt.legend(title='Phase')
plt.show()

######################################################################### Percentage of Schools by Geographic_Level ###############################################################################################

# Calculate the percentage of schools by geographic_level
total_schools = pivot_ets.loc[pivot_ets['geographic_level'] == 'Total_tSchools', 'Total_tSchools'].values[0]
percentage_by_phase = pivot_ets[['Middle', 'Non-maintained mainstream', 'Nursery', 'Primary', 'Secondary', 'Special']].sum() / total_schools * 100
percentage_by_phase

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(percentage_by_phase, labels=percentage_by_phase.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Schools by Geographic_level')
plt.show()

################################################################################### Total Number of Schools Over Time ###############################################################################################

# Group by time_period and calculate total number of schools
total_schools_over_time = df_ets.groupby('time_period')['t_schools'].sum()
total_schools_over_time

# Plotting trend of total number of schools over time
plt.plot(total_schools_over_time.index, total_schools_over_time.values, marker='o')
plt.title('Trend of Total Number of Schools Over Time')
plt.xlabel('Time Period')
plt.ylabel('Total Number of Schools')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


