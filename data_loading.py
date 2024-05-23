# Data Loading

############################################ "Loading data into PostgreSQL-db" #############################################

#PostgreSQL db connetcion

db_user = 'postgres'
db_password = 'postgres'
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
schema_name = 'ets_data'
table_name_ets = 't_uk_schools'
table_name_pivot = 'pivot_ets'

engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/postgres')

# Store the DataFrame df_ets into PostgreSQL database as a new table in ets_data schema
df_ets.to_sql(name= 't_uk_schools', con=engine, schema='ets_data', index=False, if_exists='replace')

# Store the DataFrame pivot_ets into PostgreSQL database as a new table in ets_data schema
pivot_ets.to_sql(name= 'pivot_ets', con=engine, schema='ets_data', index=False, if_exists='replace')

#Data fetching
query = f'SELECT * FROM ets_data.t_uk_schools LIMIT 10;'
result = engine.execute(query)
for row in result:
    print(row)
    
# Fetch from the pivot_ets table
query_pivot = f'SELECT * FROM ets_data.pivot_ets LIMIT 10;'
result_pivot = engine.execute(query_pivot)
print("\nRows from pivot_ets table:")
for row in result_pivot:
    print(row)

# Close the database connection
engine.dispose()


############################################ "Loading data into .csv-file" #############################################

# File path to save the CSV file
csv_file_path = 'C:\\Users\\anjal\\Arbor_\\ETS23-24\\transformed_ukSchools\\t_uk_schools.csv'

# Save the DataFrame df_ets to a CSV file
df_ets.to_csv(csv_file_path, index=False)


