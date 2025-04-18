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


    
#####################################################################################
###This function deletes the columns that only contain one value, for each dataframe.
#####################################################################################

def delete_columns_one_value(df):
    to_drop=[]
    for j in df.columns:
        if len(df[j].value_counts().values)==1:
            to_drop.append(j)
    df=df.drop(to_drop, axis=1)
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


#######################################################
###This deletes the missing columns for each dataframe.
#######################################################
print('********************** deleting nan columns **********************')
for i in range(1,n+1):
    print(f'dataframe {i} starts with ', len(dataframes[f'df{i}'].columns), ' columns')
    dataframes[f'df{i}']=delete_missing_cols(dataframes[f'df{i}'])
    print('after deleting: ', len(dataframes[f'df{i}'].columns), ' columns') 


    
#########################################################
###This deletes the one value columns for each dataframe.
#########################################################
print('********************** deleting 1-value columns **********************')
for i in dataframes:
    dataframes[i]=delete_columns_one_value(dataframes[i])
    print(f'dataframe {i} after deleting: ', len(dataframes[i].columns.to_list()))



    
####################################################################################
###Save to folder
####################################################################################

clean_file_location = os.path.join(os.path.dirname(current_dir), 'clean_getty_csvs')
for i in range(1, n+1):
    dataframes[f'df{i}'].to_csv(clean_file_location+f'/df{i}.csv', index=False)





    