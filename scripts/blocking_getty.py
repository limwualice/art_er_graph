import pandas as pd
import numpy as np
import os
import json

############# This function gives us the directory that we want to go to #############

def file_location(folder_name):
    #this is our current directory
    current_dir=os.getcwd()

    #this is where the csv's that I'm interested are located
    file_location = os.path.join(os.path.dirname(current_dir), folder_name)

    return file_location

############# This cell reads in 13 cleaned up dataframes#############
#this is where the getty csv's are
file_location = file_location('clean_getty_csvs')

#dictionary
dataframes={}

#number of csv files
n=13

for i in range(1,n+1):
    print(i)
    df=pd.read_csv(f'{file_location}/df{i}.csv', low_memory=False)
    dataframes[f'df{i}']=df




############# Concatenate dataframes based on entity types #############

file_path = f'{file_location('text_files')}/entities.json' 
with open(file_path, 'r') as f:
    data_dictionary = json.load(f)


concatenated_dfs={}

if data_dictionary: # Check if data_dictionary is not empty
    concatenated_file_location=file_location('concatenated_getty_parquet')

    for key, column_names_to_keep in data_dictionary.items():  # Iterate through the dictionary items
        list_of_valid_dataframes = []  # Reset for each entity

        for df_name, df in dataframes.items(): # Iterate through dataframe dictionary
            existing_columns = [col for col in column_names_to_keep if col in df.columns]

            if existing_columns:
                list_of_valid_dataframes.append(df[existing_columns])

        if list_of_valid_dataframes:
            df_new = pd.concat(list_of_valid_dataframes, ignore_index=True)
        else:
            df_new = pd.DataFrame(columns=column_names_to_keep)

        concatenated_dfs[key] = df_new  # Store the concatenated DataFrame
        concatenated_dfs[key].to_csv(f'{concatenated_file_location}/df_{key}')
        print(f"Concatenated DataFrame for entity '{key}':")
        # print(df_new)

else:
    print("JSON file was empty or not found.  No concatenation performed.")