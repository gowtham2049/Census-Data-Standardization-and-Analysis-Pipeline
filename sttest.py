import sqlalchemy
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
#MySQL database URL
url = 'mysql://root:mysqlpass%40123@localhost:3306/db_guvi'

# Create SQLAlchemy engine to connect to the MySQL database
engine = create_engine(url)

st.title('Querying MySQL database and showing output in streamlit')

with engine.connect() as connection:
    query_1 = connection.execute(text("""select District,sum(Population) as Total_Population 
                                        from census 
                                        group by District 
                                        order by District"""))
    output_1 = query_1.fetchall()
df1 = pd.DataFrame(output_1)
st.markdown(" **1.What is the total population of each district?**  \n **Output:** ")
st.dataframe(df1)

#QUERY2
with engine.connect() as connection:
    query_2 = connection.execute(text("""SELECT 
                                                District,
                                                SUM(Literate_Male) AS Literate_Male,
                                                SUM(Literate_Female) AS Literate_Female
                                            FROM
                                                census
                                            GROUP BY District
                                            ORDER BY District"""))
    output_2 = query_2.fetchall()
df2 = pd.DataFrame(output_2)
st.markdown(" **2.How many literate males and females are there in each district?**  \n **Output:** ")
st.dataframe(df2)

#QUERY3
with engine.connect() as connection:
    query_3 = connection.execute(text("""SELECT 
                                                District,
                                                CONCAT(ROUND((SUM(workers) / SUM(population)) * 100),"%") as Percentage_of_workers,
                                                CONCAT(ROUND((SUM(Male_Workers) / SUM(Male)) * 100),"%") AS Male_Worker_Percent,
                                                CONCAT(ROUND((SUM(Female_Workers) / SUM(Female)) * 100),"%") AS Female_Worker_Percent
                                            FROM
                                                census
                                            GROUP BY District
                                            ORDER BY District"""))
    output_3 = query_3.fetchall()
df3 = pd.DataFrame(output_3)
st.markdown(" **3.What is the percentage of workers (both male and female) in each district?** \n **Output:** ")
st.dataframe(df3)

#QUERY4
with engine.connect() as connection:
    query_4 = connection.execute(text("""SELECT 
                                                District,
                                                SUM(LPG_or_PNG_Households) AS LPG_or_PNG_Households
                                            FROM
                                                census
                                            GROUP BY State_UT,District
                                            ORDER BY District;"""))
    output_4 = query_4.fetchall()
df4 = pd.DataFrame(output_4)
st.markdown(" **4.How many households have access to LPG or PNG as a cooking fuel in each district?**  \n **Output:** ")
st.dataframe(df4)

#QUERY5

with engine.connect() as connection:
    query_5 = connection.execute(text("""SELECT 
                                            District,
                                            CONCAT(ROUND((SUM(Hindus) / SUM(Population)) * 100,1),"%") AS Hindus,
                                            CONCAT(ROUND((SUM(Muslims) / SUM(Population)) * 100,1),"%") AS Muslims,
                                            CONCAT(ROUND((SUM(Christians) / SUM(Population)) * 100,1),"%") AS Christians,
                                            CONCAT(ROUND((SUM(Sikhs) / SUM(Population)) * 100,1),"%") AS Sikhs,
                                            CONCAT(ROUND((SUM(Buddhists) / SUM(Population)) * 100,1),"%") AS Buddhists,
                                            CONCAT(ROUND((SUM(Jains) / SUM(Population)) * 100,1),"%") AS Jains,
                                            CONCAT(ROUND((SUM(Others_Religions) / SUM(Population)) * 100,1),"%") AS Others_Religions,
                                            CONCAT(ROUND((SUM(Religion_Not_Stated) / SUM(Population)) * 100,1),"%") AS Religion_Not_Stated
                                        FROM
                                            census
                                        GROUP BY State_UT,District
                                        ORDER BY District"""))
    output_5 = query_5.fetchall()
df5 = pd.DataFrame(output_5)
st.markdown(" **5.What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?**  \n **Output:** ")
st.dataframe(df5)

#QUERY6
with engine.connect() as connection:
    query_6 = connection.execute(text("""SELECT 
                                            District,
                                            SUM(Households_with_Internet) AS Households_with_Internet
                                        FROM
                                            census
                                        GROUP BY State_UT,District
                                        ORDER BY District"""))
    output_6 = query_6.fetchall()
df6 = pd.DataFrame(output_6)
st.markdown(" **6.How many households have internet access in each district?** \n**Output:** ")
st.dataframe(df6)

#QUERY7
with engine.connect() as connection:
    query_7 = connection.execute(text("""SELECT 
                                            District,
                                            CONCAT(ROUND((SUM(Below_Primary_Education) / SUM(Literate_Education)) * 100,1),"%") AS Below_Primary_Education,
                                            CONCAT(ROUND((SUM(Primary_Education) / SUM(Literate_Education)) * 100,1),"%") AS Primary_Education,
                                            CONCAT(ROUND((SUM(Middle_Education) / SUM(Literate_Education)) * 100,1),"%") AS Middle_Education,
                                            CONCAT(ROUND((SUM(Secondary_Education) / SUM(Literate_Education)) * 100,1),"%") AS Secondary_Education,
                                            CONCAT(ROUND((SUM(Higher_Education) / SUM(Literate_Education)) * 100,1),"%") AS Higher_Education,
                                            CONCAT(ROUND((SUM(Graduate_Education) / SUM(Literate_Education)) * 100,1),"%") AS Graduate_Education,
                                            CONCAT(ROUND((SUM(Other_Education) / SUM(Literate_Education)) * 100,1),"%") AS Other_Education
                                        FROM
                                            census
                                        GROUP BY State_UT,District
                                        ORDER BY District"""))
    output_7 = query_7.fetchall()
df7 = pd.DataFrame(output_7)
st.markdown(" **7.What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?**   \n **Output:** ")
st.dataframe(df7)

#QUERY8
with engine.connect() as connection:
    query_8 = connection.execute(text("""SELECT 
                                                District,
                                                SUM(Households_with_Bicycle) AS Households_with_Bicycle,
                                                SUM(Households_with_Car_Jeep_Van) AS Households_with_Car_Jeep_Van,
                                                SUM(Households_with_Radio_Transistor) AS Households_with_Radio_Transistor,
                                                SUM(Households_with_Scooter_Motorcycle_Moped) AS Households_with_Scooter_Motorcycle_Moped
                                            FROM
                                                census
                                            GROUP BY State_UT,District
                                            ORDER BY District
                                            """))
    output_8 = query_8.fetchall()
df8 = pd.DataFrame(output_8)
st.markdown(" **8.How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?** \n**Output:** ")
st.dataframe(df8)

#QUERY9
with engine.connect() as connection:
    query_9 = connection.execute(text("""SELECT 
                                                District,
                                                SUM(Condition_of_occupied_census_houses_Dilapidated_Households) AS Dilapidated_Households,
                                                SUM(Households_with_separate_kitchen_Cooking_inside_house) AS Houses_with_separate_kitchen,
                                                SUM(Having_bathing_facility_Total_Households) AS Houses_with_bathing_facility,
                                                SUM(Having_latrine_facility_within_the_premises_Total_Households) AS Houses_with_latrine_facility
                                            FROM
                                                census
                                            GROUP BY State_UT,District
                                            ORDER BY District"""))
    output_9 = query_9.fetchall()
df9 = pd.DataFrame(output_9)
st.markdown(" **9.What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?**  \n**Output:** ")
st.dataframe(df9)

#QUERY10
with engine.connect() as connection:
    query_10 = connection.execute(text("""
with cte1 as (select State_UT,
	District,Household_size_1_to_2_persons,
    Household_size_3_persons_Households,
    Household_size_4_persons_Households,
    Household_size_5_persons_Households,
    Household_size_6_8_persons_Households,
    Household_size_9_persons_and_above_Households,
    coalesce(Household_size_1_to_2_persons,0)+
    coalesce(Household_size_3_persons_Households,0)+
    coalesce(Household_size_4_persons_Households,0)+
    coalesce(Household_size_5_persons_Households,0)+
    coalesce(Household_size_6_8_persons_Households,0)+
    coalesce(Household_size_9_persons_and_above_Households,0) 
    as House_size 
    from census c) 
SELECT 
    T2.District,
    CONCAT(ROUND((SUM(T2.Household_size_1_to_2_persons) / SUM(T2.House_size)) * 100,1),"%") AS House_size_1_to_2_ppl,
    CONCAT(ROUND((SUM(T2.Household_size_3_persons_Households) / SUM(T2.House_size)) * 100,1),"%") AS House_size_3_ppl,
    CONCAT(ROUND((SUM(T2.Household_size_4_persons_Households) / SUM(T2.House_size)) * 100,1),"%") AS House_size_4_ppl,
    CONCAT(ROUND((SUM(T2.Household_size_5_persons_Households) / SUM(T2.House_size)) * 100,1),"%") AS House_size_5_ppl,
    CONCAT(ROUND((SUM(T2.Household_size_6_8_persons_Households) / SUM(T2.House_size)) * 100,1),"%") AS House_size_6_8_ppl,
    CONCAT(ROUND((SUM(T2.Household_size_9_persons_and_above_Households) / SUM(T2.House_size)) * 100,1),"%") AS House_size_9_ppl_above
FROM
    cte1 T2
GROUP BY T2.State_UT,T2.District
ORDER BY T2.District
"""))
    output_10 = query_10.fetchall()
df10 = pd.DataFrame(output_10)
st.markdown(" **10.How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?**  \n**Output:** ")
st.dataframe(df10)

#QUERY11
with engine.connect() as connection:
    query_11 = connection.execute(text("""
                                            SELECT 
                                            `State_UT`,
                                            SUM(COALESCE(Households_Rural, 0)) + SUM(COALESCE(Households_Urban, 0)) AS Total_Households
                                        FROM
                                            census
                                        GROUP BY `State_UT`
                                        ORDER BY `State_UT`"""))
    output_11 = query_11.fetchall()
df11 = pd.DataFrame(output_11)
st.markdown(" **11.What is the total number of households in each state?**  \n**Output:** ")
st.dataframe(df11)

#QUERY12
with engine.connect() as connection:
    query_12 = connection.execute(text("""SELECT 
                                                `State_UT`,
                                                SUM(Having_latrine_facility_within_the_premises_Total_Households) AS    
                                                Households_latrine_facility_within_the_premises
                                            FROM
                                                census
                                            GROUP BY `State_UT`
                                            ORDER BY `State_UT`"""))
    output_12 = query_12.fetchall()
df12 = pd.DataFrame(output_12)
st.markdown(" **12.How many households have a latrine facility within the premises in each state?**  \n**Output:** ")
st.dataframe(df12)

#QUERY13

with engine.connect() as connection:
    query_13 = connection.execute(text("""SELECT 
                                        `State_UT`,
                                        ROUND(AVG(COALESCE(Household_size_1_to_2_persons, 0))) AS Household_size_1_to_2_persons,
                                        ROUND(AVG(COALESCE(Household_size_3_persons_Households, 0))) AS Household_size_3_persons_Households,
                                        ROUND(AVG(COALESCE(Household_size_4_persons_Households, 0))) AS Household_size_4_persons_Households,
                                        ROUND(AVG(COALESCE(Household_size_5_persons_Households, 0))) AS Household_size_5_persons_Households,
                                        ROUND(AVG(COALESCE(Household_size_6_8_persons_Households, 0))) AS Household_size_6_8_persons_Households,
                                        ROUND(AVG(COALESCE(Household_size_9_persons_and_above_Households,0))) AS Household_size_9_persons_and_above_Households
                                    FROM
                                        census
                                    GROUP BY `State_UT`
                                    ORDER BY `State_UT`"""))
    output_13 = query_13.fetchall()
df13 = pd.DataFrame(output_13)
st.markdown(" **13.What is the average household size in each state?**   \n **Output:** ")
st.dataframe(df13)

#QUERY14
with engine.connect() as connection:
    query_14 = connection.execute(text("""SELECT 
                                                `State_UT`,
                                                SUM(COALESCE(Ownership_Owned_Households, 0)) AS Owned_Households,
                                                SUM(COALESCE(Ownership_Rented_Households, 0)) AS Rented_Households
                                            FROM
                                                census
                                            GROUP BY `State_UT`
                                            ORDER BY `State_UT`"""))
    output_14 = query_14.fetchall()
df14 = pd.DataFrame(output_14)
st.markdown(" **14.How many households are owned versus rented in each state?**  \n**Output:** ")
st.dataframe(df14) 

#QUERY15
with engine.connect() as connection:
    query_15 = connection.execute(text("""SELECT 
                            `State_UT`,
                            SUM(Type_of_latrine_facility_Pit_latrine_Households) AS Type_of_latrine_facility_Pit_latrine_Households,
                            SUM(Type_of_latrine_facility_Other_latrine_Households) AS Type_of_latrine_facility_Other_latrine_Households,
                            SUM(Latrine_Facility_Night_Soil_Disposed_Open_Drain_Households) AS Latrine_Facility_Night_Soil_Disposed_Open_Drain_Households,
                            SUM(Latrine_Facility_Flush_Connected_Other_System_Households) AS Latrine_Facility_Flush_Connected_Other_System_Households
                        FROM
                            census
                        GROUP BY `State_UT`
                        ORDER BY `State_UT`"""))
    output_15 = query_15.fetchall()
df15 = pd.DataFrame(output_15)
st.markdown(" **15.What is the different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?**   \n **Output:** ")
st.dataframe(df15) 

#QUERY16
with engine.connect() as connection:
    query_16 = connection.execute(text("""SELECT 
                            `State_UT`,
                            SUM(Location_of_drinking_water_source_Near_the_premises_Households) AS 
                                                    Location_of_drinking_water_source_Near_the_premises_Households
                        FROM
                            census
                        GROUP BY `State_UT`
                        ORDER BY `State_UT`"""))
    output_16 = query_16.fetchall()
df16 = pd.DataFrame(output_16)
st.markdown(" **16.How many households have access to drinking water sources near the premises in each state?** \n**Output:** ")
st.dataframe(df16) 

#QUERY17
with engine.connect() as connection:
    query_17 = connection.execute(text("""SELECT 
                                                `State_UT`,
                                                ROUND(AVG(COALESCE(Power_Parity_Less_than_Rs_45000, 0))) AS Power_Parity_Less_than_Rs_45000,
                                                ROUND(AVG(COALESCE(Power_Parity_Rs_45000_150000, 0))) AS Power_Parity_Rs_45000_150000,
                                                ROUND(AVG(COALESCE(Power_Parity_Rs_150000_330000, 0))) AS Power_Parity_Rs_150000_330000,
                                                ROUND(AVG(COALESCE(Power_Parity_Rs_330000_545000, 0))) AS Power_Parity_Rs_330000_545000,
                                                ROUND(AVG(COALESCE(Power_Parity_Above_Rs_545000, 0))) AS Power_Parity_Above_Rs_545000
                                            FROM
                                                census
                                            GROUP BY `State_UT`
                                            ORDER BY `State_UT`"""))
    output_17 = query_17.fetchall()
df17 = pd.DataFrame(output_17)
st.markdown(" **17.What is the average household income distribution in each state based on the power parity categories?**  \n**Output:** ")
st.dataframe(df17)

#QUERY18
with engine.connect() as connection:
    query_18 = connection.execute(text("""WITH temp AS (
                        SELECT `State_UT`,
                        		Married_couples_1_Households,
                                Married_couples_2_Households,
                                Married_couples_3_Households,
                                Married_couples_4_Households,
                                Married_couples_5__Households,
                                COALESCE(Married_couples_1_Households,0)+
                                COALESCE(Married_couples_2_Households,0)+
                                COALESCE(Married_couples_3_Households,0)+
                                COALESCE(Married_couples_4_Households,0)+
                                COALESCE(Married_couples_5__Households,0) AS married_couples_total FROM census)
                        SELECT 
                            c.`State_UT`,
                            ROUND((SUM(c.Married_couples_1_Households) / SUM(married_couples_total)) * 100,2) AS Married_couples_1_Households,
                            ROUND((SUM(c.Married_couples_2_Households) / SUM(married_couples_total)) * 100,2) AS Married_couples_2_Households,
                            ROUND((SUM(c.Married_couples_3_Households) / SUM(married_couples_total)) * 100,2) AS Married_couples_3_Households,
                            ROUND((SUM(c.Married_couples_4_Households) / SUM(married_couples_total)) * 100,2) AS Married_couples_4_Households,
                            ROUND((SUM(c.Married_couples_5__Households) / SUM(married_couples_total)) * 100,2) AS Married_couples_5_Households
                        FROM
                            temp c
                        GROUP BY c.`State_UT`
                        ORDER BY c.`State_UT`"""))
    output_18 = query_18.fetchall()
df18 = pd.DataFrame(output_18)
st.markdown(" 18.What is the percentage of married couples with different household sizes in each state? \n**Output:** ")
st.dataframe(df18) 

#QUERY19
with engine.connect() as connection:
    query_19 = connection.execute(text("""SELECT 
                                                    `State_UT`,
                                                    SUM(COALESCE(Power_Parity_Less_than_Rs_45000, 0)) AS Power_Parity_Less_than_Rs_45000,
                                                    SUM(COALESCE(Power_Parity_Rs_45000_150000, 0)) AS Power_Parity_Rs_45000_150000,
                                                    SUM(COALESCE(Power_Parity_Rs_150000_240000, 0)) AS Power_Parity_Rs_150000_240000
                                                FROM
                                                    census
                                                GROUP BY `State_UT`
                                                ORDER BY `State_UT`"""))
    output_19 = query_19.fetchall()
df19 = pd.DataFrame(output_19)
st.markdown(" 19.How many households fall below the poverty line in each state based on the power parity categories? \n**Output:** ")
st.dataframe(df19) 

#QUERY20
with engine.connect() as connection:
    query_20 = connection.execute(text("""SELECT 
                                                `State_UT`,
                                                CONCAT(ROUND((SUM(Literate) / SUM(Population)) * 100,2),"%") AS Literacy_Rate
                                            FROM
                                                census
                                            GROUP BY `State_UT`
                                            ORDER BY `State_UT`"""))
    output_20 = query_20.fetchall()
df20 = pd.DataFrame(output_20)
st.markdown(" 20.What is the overall literacy rate (percentage of literate population) in each state? \n**Output:** ")
st.dataframe(df20) 









