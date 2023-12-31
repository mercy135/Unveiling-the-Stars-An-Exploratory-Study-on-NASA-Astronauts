#.... TASK 1 .....
/*Import Pandas as 'pd'.
Read the CSV file nasa.csv into a Pandas DataFrame named 'df'.
Inspect the data by calling the variable 'df'*/

  
#--- Import Pandas ---
import pandas as pd
#--- Read in dataset ----
df =  pd.read_csv('nasa.csv')
# ---WRITE YOUR CODE FOR TASK 1 ---
#--- Inspect data ---
df


#.... TASK 2 .....
/*Counting Null Values.
Use the isnull() function to mark null (missing) values in each column of the 'df' DataFrame.
Apply the sum() function to calculate the sum of these marked null values for each column and store the counts in a variable called 'null_values'.
Display 'null_values' to show the count of null values for each column in 'df'.*/

# --- WRITE YOUR CODE FOR TASK 2 ---
null_values=df.isnull().sum()
#--- Inspect data ---
null_values

/* Module 1 - Task 3
Data Cleaning and Filtering Operations.
Remove rows with missing values in the 'Alma_Mater' column using dropna() and applies the changes directly to the DataFrame 'df' with inplace=True.
Filter rows where 'Death_Mission' column is null and 'Death_Date' column is not null using the .index method. Then, remove those rows from the DataFrame 'df' by using the .drop() function with the inplace=True parameter.
Use pd.to_datetime() with the dayfirst=True parameter to convert the 'Birth_Date' and 'Death_Date' columns to datetime format with day-first parsing separately.
Inspect the data by calling the variable 'df' */

#--- WRITE YOUR CODE FOR TASK 3 ---
df.dropna(subset=['Alma_Mater'], inplace=True)
index_to_drop = df[(df['Death_Mission'].isnull()) & (df['Death_Date'].notnull())].index
df.drop(index_to_drop, inplace=True)
df['Birth_Date']= pd.to_datetime(df['Birth_Date'], dayfirst=True)
df['Death_Date']= pd.to_datetime(df['Death_Date'], dayfirst=True)
df
#--- Inspect data ---


/* Module 1 - Task 4
Exporting DataFrame.
Export the 'df' DataFrame to a CSV file named 'astronauts.csv'.
Exclude the index from being written to the CSV file by setting 'index' to False.
Before running this task in your notebook, please ensure that you have previously executed the necessary data processing tasks for the 'df' DataFrame.
Run the code in Jupyter Notebook once to export the file before proceeding to the 'Run Test'.
Note: Make sure to hide or comment .to_csv() function code before running test case.*/

/*Module 1 - Task 5
Data Download, Import, and Database Connection.
Download the dataset astronauts.csv which is exported in Module 1 - Task 4.
Create the table on MYSQL using your credentials provided here
Use the provided login information to access the database by clicking the ""localhost"" link located on the Database Info tab. Once there, you need to upload the required datasets in the specific database mentioned in the database info tab. Rename the table to 'astronauts' using the Operations tab within the database interface and then click on ""Run test"" to complete the task.
Use the %load_ext sql command to load the SQL extension in your Jupyter Notebook environment. This extension allows you to run SQL commands directly within your notebook.
Use the %sql magic command to specify the connection string for your MySQL database. Replace <user>, <password>, and <db_name> with your actual database credentials and details.*/
