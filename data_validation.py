# Data Validation

db_user = 'postgres'
db_password = 'postgres'
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
schema_name = 'ets_data'
table_name_ets = 't_uk_schools'

engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/postgres')

query = f'SELECT * FROM ets_data.t_uk_schools;'
df_ets = pd.read_sql(query, con=engine)
#df_ets = pd.read_sql(t_uk_schools, con=engine)

# Infer the schema of the DataFrame
data_types = df_ets.dtypes


################################################# "Schema-Validation" ############################################################

# Perform basic schema validation checks
for column, data_type in data_types.items():
    # Check for null values
    if df_ets[column].isnull().any():
        print(f"Warning: Null values found in column '{column}'")
    
    # Check if data type is numeric or string
    if data_type in ['int64', 'object']:
        print(f"'{column}' passes schema validation.")
    
    # Check if data type is datetime
    elif data_type == 'datetime64[ns]':
        print(f"'{column}' passes schema validation.")

        
############################################## "Completeness-Check" ############################################################

completeness_check_results = {}

for column in df_ets.columns:
    # Calculate the percentage of missing values in the column
    missing_percentage = df_ets[column].isnull().mean() * 100
    completeness_check_results[column] = missing_percentage


print("\nCompleteness Check Results:")
for column, missing_percentage in completeness_check_results.items():
    print(f"{column}: {missing_percentage:.2f}% missing")
 
engine.dispose()
