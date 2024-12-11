import pandas as pd
import zipfile

# Specify the dataset
DATA_FILE = "../DataSet/data.zip"

# Extract the ZIP file to read the contained CSV
with zipfile.ZipFile(DATA_FILE, 'r') as z:
    csv_filename = z.namelist()[0]  # Get the first file name inside the ZIP
    df = pd.read_csv(z.open(csv_filename))

# Display a preview of the dataframe
print(df.head())
# Extract relevant columns# Extract relevant columns# Extract relevant columns
df_cleaned = pd.DataFrame()  # Initialize outside of the loop to accumulate data
i = 0
while i + 5 < df.shape[0]:  # Ensure there's enough data for the next 5 rows
    # Ensure each column is being treated as a string before split
    df_cleaned_temp = pd.DataFrame()
    df_cleaned_temp['Title'] = df.iloc[i]
    df_cleaned_temp['Company Name'] = df.iloc[i+1].astype(str).str.split('|').str[0].str.strip()
    
    # Split and strip data for Experience, Salary, and Locations
    split_data = df.iloc[i+2].astype(str).str.split('|', expand=True).apply(lambda x: x.str.strip())
    
    # Dynamically handle the assignment based on the number of columns in split_data
    num_cols = split_data.shape[1]
    
    if num_cols >= 3:
        df_cleaned_temp[['Experience', 'Salary', 'Locations']] = split_data.iloc[:, :3]
    elif num_cols == 2:
        df_cleaned_temp[['Experience', 'Salary']] = split_data.iloc[:, :2]
        df_cleaned_temp['Locations'] = None  # Fill with None if Locations is missing
    elif num_cols == 1:
        df_cleaned_temp['Experience'] = split_data.iloc[:, 0]
        df_cleaned_temp['Salary'] = None
        df_cleaned_temp['Locations'] = None  # Fill with None if Salary and Locations are missing
    else:
        df_cleaned_temp[['Experience', 'Salary', 'Locations']] = None  # Fill all columns with None if no data
    
    df_cleaned_temp['Descriptions'] = df.iloc[i+3]
    df_cleaned_temp['Skills'] = df.iloc[i+4]
    df_cleaned_temp['Date'] = df.iloc[i+5].astype(str).str.split('|').str[0].fillna("Not Available").str.strip()  # Placeholder if no date is available

    # Handle 'Title' column: Convert to string and check if it's valid
    title_value = str(df_cleaned_temp['Title'].iloc[0])  # Ensure it's a string
    if title_value != 'nan' and title_value != '':
        job_id_prefix = ''.join([word[:2].upper() for word in title_value.split()[:2]])
    else:
        job_id_prefix = 'XX'  # Default prefix if Title is missing or invalid

    # Create Job Id
    df_cleaned_temp['Job Id'] = job_id_prefix + str(i + 1).zfill(4)

    # Append data to the main DataFrame
    df_cleaned = pd.concat([df_cleaned, df_cleaned_temp], ignore_index=True)
    
    # Move to the next set of rows
    i += 6

# Rearrange columns
df_cleaned = df_cleaned[['Job Id', 'Title', 'Company Name', 'Experience', 'Salary', 'Locations', 'Date', 'Descriptions', 'Skills']]

# Save the cleaned dataframe to a new CSV
output_file = "../DataSet/data-set.csv"
df_cleaned.to_csv(output_file, index=False)

print(f"CSV file created successfully at {output_file}.")
