#Data Extraction

import psycopg2
import pandas as pd

# PostgreSQL connection details
conn_details = {
    "user": "username",
    "password": "password",
    "host": "hostname",
    "port": "port address",
    "database": "db name"
}

#select data from ets_data.UK_schools
query = "SELECT * FROM ets_data.UK_schools;"

try:
    #Connect to the PostgreSQL db
    conn = psycopg2.connect(**conn_details)
    #Create a cursor object
    cursor = conn.cursor()

    #Execute the query
    cursor.execute(query)
    #Fetch all rows from the result set
    data = cursor.fetchall()

    #Close cursor and connection
    cursor.close()
    conn.close()  
    
    df_ets= pd.DataFrame(data, columns=['time_period','time_identifier','geographic_level','country_code',
                                       'country_name','region_code','region_name','phase','t_schools'])

        
    #df_ets = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])


    print("EDUCATION TRAINING STATISTICS")
    display(df_ets)

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)
