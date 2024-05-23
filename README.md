# Schools_Insights

**Objective**:
The primary goal was to analyze and transform "Education and training statistics for the UK"
data to gain insights into various educational metrics, such as increase in the number of schools over time, student demographics, performance, and school distributions, and to prepare the data for further analysis and reporting.

**Data Sources**: [Download Here](https://content.explore-education-statistics.service.gov.uk/api/releases/3255e10a-92c5-4cc0-adb1-08db7e23d3a0/files)

**ETL (Extract, Transform, Load) Process**:

1. **Extract**:
   - Data was extracted from PostgreSQL databases.

2. **Transform**:
   - Data Cleaning: Removed duplicates, handled missing values, and corrected data inconsistencies, schema mapping.
   - Data Normalization: Standardized data formats, such as dates and categorical values.   
   - Feature Engineering: Created new features, such as the sum of total schools and pivoted the data.
   - Aggregation: Summarized data at various levels, such as schools, regions, phases, and geographic levels.
   - Data Mapping: Mapped the data by finding the unique combinations of region code and geographic level.

3. **Load**:
   - Loaded the transformed data into the PostgreSQL database for easy access and analysis.
   - Ensured data integrity and consistency during the loading process.

**Data Validation**:

1. **Schema Validation**:
     - Null Value Check: For each column, the data was checked for the presence of null values. If any null values were found, a warning message was generated indicating which column contained null values.
     - Data Type Check: Each column's data type was verified against the expected data types. If a column's data type matched the expected data type, a message was generated indicating that the column passed 	 
       the schema validation.

2. **Completeness Check**:
     - Calculate the percentage of missing values for each column.
  
**Data Analysis**:

1. **Descriptive Statistics**:
     - Evaluated school distribution metrics, such as the number of schools across time and region.

2. **Visualization**:
    - Created visualizations to illustrate key insights, such as the distribution of schools across regions, and the total number of schools  trends over time.
    - Used tools like Power BI and Python Matplotlib for interactive and static visualizations.

3. **Insights**:
     - Identified trends in school formation across periods. 
     - Highlighted disparities in educational outcomes based on demographics and regions.
