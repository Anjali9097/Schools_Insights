# Data Transformation

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

#changing the t_schools data type to integer

df_ets['t_schools'] = df_ets['t_schools'].fillna(0).astype('int64')
df_ets.dtypes

#checking for NULL values
df_ets.isnull().sum()

#fill the null value columns in the "region_code" field using the "country_code" when it satisfies the codition geographic_leve== National     
# and
##fill the null value columns in the "region_name" field using the "country_name" when it satisfies the codition geographic_leve== National        
 
def fill_region_info(row):
    if row['geographic_level'] == 'National':
        if pd.isnull(row['region_code']):
            row['region_code'] = row['country_code']
            
        if pd.isnull(row['region_name']):
            row['region_name'] = row['country_name']
    return row

# Apply the function to fill null fields
df_ets = df_ets.apply(fill_region_info, axis=1)

df_ets.tail(30)    

############################################ "DATA MAPPING" ###############################################################

# Group the DataFrame by unique combinations of region_code and geographic_level
grouped = df_ets.groupby(['region_code', 'geographic_level'])

region_mapping = {}

# Iterate over each group and extract the region_name
for group, data in grouped:
    region_code, geographic_level = group
    region_name = data['region_name'].iloc[0]  # Get the region_name for the group
   
    # Add the mapping to the dictionary
    if region_code not in region_mapping:
        region_mapping[region_code] = {}
    region_mapping[region_code][geographic_level] = region_name


for region_code, mappings in region_mapping.items():
    print(f"Region Code: {region_code}")
    for geographic_level, region_name in mappings.items():
        print(f"  Geographic Level: {geographic_level}, Region Name: {region_name}")

################################################### "DATA PIVOTING" #########################################################

#pivot the data based on 'phase' to see if the Regional partcipation of a country is equivalent to National participation of that country
pivot_ets = df_ets.pivot_table(index=['geographic_level','country_name'],
                              columns='phase',
                              values='t_schools',
                              aggfunc='sum',
                              margins=True,  # Add margins for total
                              margins_name='Total_tSchools',  
                              fill_value=0) 

# Reset index to make the pivot result look similar to the original DataFrame
pivot_ets.reset_index(inplace=True)
pivot_ets

###################################################### "DATA-FORMAT CHANGING" #################################################

# Convert time_period values from 'YYYYYY' to 'YYYY-YYYY'

# Convert to string
df_ets['time_period'] = df_ets['time_period'].astype(str)

#df_ets['time_period'] = df_ets['time_period'].str[:4] + '-' + df_ets['time_period'].str[:2] + df_ets['time_period'].str[4:]
df_ets['time_period'] = df_ets['time_period'].apply(lambda x: x[:4] + '-' + str(int(x[:2])) + x[-2:])
df_ets.head(10)

############################################### "DUPLICATE RECORDS" #########################################################

duplicates = df_ets[df_ets.duplicated()]
duplicates

############################################### "DATA SORTING" ##############################################################

df_ets = df_ets.sort_values(by='time_period',ascending=False,ignore_index=True)
df_ets.head(10)
