import pandas as pd
import numpy as np
import os



###########################################################
###Here we delete all the columns that are all null values.
###########################################################


def delete_missing_cols(df):
    num_rows=len(df)
    missing_values=df.isna().sum()
    columns_to_delete=missing_values[missing_values.values==num_rows].index.to_list()
    df=df.drop(columns_to_delete, axis=1)
    return df


    
##################################################################################
### This function checks the top 5 value counts for every column in the dataframe. 
##################################################################################
def check_value_counts(df):    
    for c in df.columns:
        print("---- %s ---" % c)
        print(df[c].value_counts().nlargest(5))

        
###########################################################################################################
### This creates a dictionary and puts each dataframe corresponding to a csv file into the dictionary.
###########################################################################################################


#this is our current directory
current_dir=os.getcwd()

#this is where the getty csv's are
file_location = os.path.join(os.path.dirname(current_dir), 'getty_csvs')

#dictionary
dataframes={}

#number of csv files
n=13

for i in range(1,n+1):
    df=pd.read_csv(f'{file_location}/sales_contents_{i}.csv', low_memory=False)
    dataframes[f'df{i}']=df


#
###This deletes the missing columns for each dataframe.
#######################################################

for i in range(1,n+1):
    print(i, len(dataframes[f'df{i}'].columns))
    dataframes[f'df{i}']=delete_missing_cols(dataframes[f'df{i}'])
    print(i, len(dataframes[f'df{i}'].columns)) 





    