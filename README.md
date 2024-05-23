# Schools_Insights
**Objective**:
The primary goal was to analyze and transform "Education and training statistics for the UK"
data to gain insights into various educational metrics, such as increase in the number of schools over time, student demographics, performance, and school distributions, and to prepare the data for further analysis and reporting.

**Data Sources**: "C:\Users\anjal\Desktop\Arbor_\ETS23-24\data\uk_schools.csv"

**ETL (Extract, Transform, Load) Process**:

1. **Extract**:
   - Data was extracted from PostgreSQL databases.

2. **Transform**:
   - Data Cleaning: Removed duplicates, handled missing values, and corrected data inconsistencies.
   - Data Normalization: Standardized data formats, such as dates and categorical values.   
   - Feature Engineering: Created new features, such as average exam scores and student-teacher ratios.
   - Aggregation: Summarized data at various levels, such as school, district, and national levels.

3. **Load**:
   - Loaded the transformed data into PostgreSQL database for easy access and analysis.
   - Ensured data integrity and consistency during the loading process.
