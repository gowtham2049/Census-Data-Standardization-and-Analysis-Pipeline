# Census Data Standardization and Analysis Pipeline

## Project Description  
The **Census Data Standardization and Analysis Pipeline** is a comprehensive solution designed to clean, process, and analyze census data effectively. Census data often comes in raw, inconsistent formats, making it challenging to derive meaningful insights. This project addresses these challenges by standardizing the data and ensuring its accuracy, uniformity, and accessibility for further analysis and visualization.

### Key Tasks  
1. **Data Cleaning**  
   - Renaming columns for consistency and clarity.  
   - Addressing missing data through appropriate imputation techniques or removal based on defined rules.  

2. **Data Standardization**  
   - Normalizing state and Union Territory (UT) names to a consistent format.  
   - Handling new state or UT formations by mapping them appropriately within the dataset.  

3. **Data Transformation**  
   - Creating new features or derived variables necessary for analysis.  
   - Applying scaling or normalization to ensure uniform data representation.  

4. **Data Storage**  
   - Storing cleaned data in MongoDB for initial processing.  
   - Transferring structured data to a MySQL database for efficient querying and analysis.  

5. **Database Querying and Visualization**  
   - Establishing database connections to run structured queries.  
   - Leveraging Streamlit to build an interactive web interface for data exploration and visualization.  

### Objective  
This project is essential for ensuring that census data is not only reliable but also easily accessible for policymakers, researchers, and analysts. By implementing a robust cleaning, processing, and analysis pipeline, it paves the way for deriving actionable insights and making data-driven decisions.
#### Tools Used : Python, Pandas, Streamlit, MYSQL connector, SQLAlchemy 

# Data Processing Tasks

## Task 1: Rename Column Names  
Standardize column names for clarity and uniformity. Ensure names do not exceed 60 characters.  

## Task 2: Rename State/UT Names  
Standardize State/UT names using title case. Replace `&` with `and`.  

## Task 3: New State/UT Formation  
Update state/UT names based on reorganization in 2014 (Telangana) and 2019 (Ladakh).  

## Task 4: Process Missing Data  
Identify, calculate, and fill missing data using derived formulas.  

## Task 5: Save Data to MongoDB  
Store the processed data in MongoDB under the collection `census`.  

## Task 6: Database Connection and Data Upload  
Fetch data from MongoDB and upload it to a relational database with proper constraints.  

## Task 7: Run Queries on Database and Display Output on Streamlit
### Streamlit Setup
To run the Streamlit app that shows the output of the queries, use the following command:

```bash
streamlit run <sttest.py>
```

### Queries for District-Level Analysis:
1. What is the total population of each district?
2. How many literate males and females are there in each district?
3. What is the percentage of workers (both male and female) in each district?
4. How many households have access to LPG or PNG as a cooking fuel in each district?
5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?
6. How many households have internet access in each district?
7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?
8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?
9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?
10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?

### Queries for State-Level Analysis:
1. What is the total number of households in each state?
2. How many households have a latrine facility within the premises in each state?
3. What is the average household size in each state?
4. How many households are owned versus rented in each state?
5. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?
6. How many households have access to drinking water sources near the premises in each state?
7. What is the average household income distribution in each state based on the power parity categories?
8. What is the percentage of married couples with different household sizes in each state?
9. How many households fall below the poverty line in each state based on the power parity categories?
10. What is the overall literacy rate (percentage of literate population) in each state?

