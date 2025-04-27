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





##################################################################################
### This function does simple cleaning, like trimming whitespace and lowercasing. 
##################################################################################

import pandas as pd
import re
from datetime import datetime

def clean_dataframe(df):
    """
    Cleans a pandas DataFrame by trimming whitespace, removing special characters,
    standardizing date formats, replacing abbreviations, and handling potential
    data entry errors.

    Args:
        df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """

    for col in df.columns:
        if df[col].dtype == 'object':  # Process only string columns
            # Trim leading/trailing whitespace and remove special characters
            df[col] = df[col].str.strip().str.replace(r'[^\w\s]', '', regex=True).str.lower()

            # Standardize date formats
            try:
                df[col] = df[col].apply(lambda x: datetime.strptime(str(x), '%Y-%m-%d').strftime('%Y-%m-%d')
                                       if re.match(r'\d{4}-\d{2}-\d{2}', str(x))
                                       else (datetime.strptime(str(x), '%m/%d/%Y').strftime('%Y-%m-%d')
                                             if re.match(r'\d{2}/\d{2}/\d{4}', str(x))
                                             else x))
            except ValueError:
                pass  # If not a recognizable date format, leave as is

            # Replace abbreviations
            df[col] = df[col].str.replace(r'\bSt\.\b', 'Street', regex=True)
            df[col] = df[col].str.replace(r'\bRd\.\b', 'Road', regex=True)
            df[col] = df[col].str.replace(r'\bAve\.\b', 'Avenue', regex=True)
            df[col] = df[col].str.replace(r'\bDr\.\b', 'Drive', regex=True)


    return df





#############################################
###ALL 503 columns categorized into entities 
###ulan: union list of artist names
#############################################





codes=['catalog_number', 'sale_code']
lot_info=['lot_number', 'lot_sale_year','lot_sale_month','lot_sale_day', 'lot_sale_mod', 'lot_notes']
auction_house=['auction_house_1','auction_house_2','auction_house_3','auction_house_4']
title=['title','title_modifier', 'title_translation']



###should we split up the artists or keep them as one entity?
artist1=['artist_name_1','artist_info_1','art_authority_1','nationality_1','attrib_mod_1','attrib_mod_auth_1','artist_ulan_1']
artist2=['artist_name_2','artist_info_2','art_authority_2','nationality_2','attrib_mod_2','attrib_mod_auth_2','artist_ulan_2']
artist3=['artist_name_3','artist_info_3','art_authority_3','nationality_3','attrib_mod_3','attrib_mod_auth_3','artist_ulan_3']
artist4=['artist_name_4','artist_info_4','art_authority_4','nationality_4','attrib_mod_4','attrib_mod_auth_4','artist_ulan_4']
artist5=['artist_name_5','artist_info_5','art_authority_5','nationality_5','attrib_mod_5','attrib_mod_auth_5','artist_ulan_5']




art_info=['hand_note_1','hand_note_so_1','hand_note_2','hand_note_so_2','hand_note_3','hand_note_so_3','hand_note_4','hand_note_so_4',
          'hand_note_5','hand_note_so_5','hand_note_6','hand_note_so_6', 'hand_note_7','hand_note_so_7','object_type','materials',
          'dimensions','formatted_dimens','format','genre','subject','inscription']

 
 
 
#names of auctioner
auctioner1=['expert_auth_1','expert_ulan_1']
auctioner2=['expert_auth_2','expert_ulan_2']
auctioner3=['expert_auth_3','expert_ulan_3']
auctioner4=['expert_auth_4','expert_ulan_4']



#Commissaire: Name of the first Commissaire-priseur (legally appointed auctioneer).
commissaire1=['commissaire_pr_1','comm_ulan_1'] 
commissaire2=['commissaire_pr_2','comm_ulan_2']
commissaire3=['commissaire_pr_3','comm_ulan_3']
commissaire4=['commissaire_pr_4','comm_ulan_4']
 



###should we split up the sellers or keep them as one entity?

seller1=['sell_name_1','sell_name_so_1','sell_name_ques_1','sell_mod_1','sell_auth_name_1','sell_auth_nameq_1','sell_auth_mod_1','sell_auth_mod_a_1','sell_ulan_1']
seller2=['sell_name_2','sell_name_so_2','sell_name_ques_2','sell_mod_2','sell_auth_name_2','sell_auth_nameq_2','sell auth_mod_2','sell_auth_mod_a_2','sell_ulan_2']
seller3=['sell_name_3','sell_name_so_3','sell_name_ques_3','sell_mod_3','sell_auth_name_3','sell_auth_nameq_3','sell_auth_mod_3','sell_auth_mod_a_3','sell_ulan_3']
seller4=['sell_name_4','sell_name_so_4','sell_name_ques_4','sell_mod_4','sell_auth_name_4','sell_auth_nameq_4','sell_auth_mod_4','sell_auth_mod_a_4','sell_ulan_4']
seller5=['sell_name_5','sell_name_so_5','sell_name_ques_5','sell_mod_5','sell_auth_name_5','sell_auth_nameq_5','sell_auth_mod_5','sell_auth_mod_a_5','sell_ulan_5']
seller6=[ 'sell_name_6','sell_name_so_6','sell_name_ques_6','sell_mod_6','sell_auth_name_6','sell_auth_nameq_6','sell_auth_mod_6','sell_auth_mod_a_6','sell_ulan_6']
seller7=[ 'sell_name_7','sell_name_so_7','sell_name_ques_7','sell_mod_7','sell_auth_name_7','sell_auth_nameq_7','sell_auth_mod_7','sell_auth_mod_a_7','sell_ulan_7']


#One term from a small controlled vocabulary developed by PSCP to describe the nature of the action described in the record.
transaction=['transaction','transaction_so','transaction_cite']


#price_amount_1 is Hammer price or high bid recorded for the lot.
price1=['price_amount_1','price_currency_1','price_note_1','price_source_1','price_citation_1']
price2=['price_amount_2','price_currency_2','price_note_2','price_source_2','price_citation_2']
price3=['price_amount_3','price_currency_3','price_note_3','price_source_3','price_citation_3']



#est_price is Estimated selling price for the lot.
est_price=['est_price','est_price_curr','est_price_desc','est_price_so']


#Starting price for the lot.
start_price=['start_price','start_price_curr','start_price_desc','start_price_so']



#ask_price is Asking price for the lot.
ask_price=['ask_price','ask_price_curr','ask_price_desc','ask_price_so']


 
#buy_name_1: Verbatim name of first buyer
buyer1=['buy_name_1','buy_name_so_1','buy_name_ques_1','buy_name_cite_1','buy_mod_1','buy_auth_name_1','buy_auth_nameQ_1','buy_auth_mod_1','buy_auth_mod_a_1','buy_ulan_1']
buyer2=['buy_name_2','buy_name_so_2','buy_name_ques_2','buy_name_cite_2','buy_mod_2','buy_auth_name_2','buy_auth_nameQ_2','buy_auth_mod_2','buy_auth_mod_a_2','buy_ulan_2']
buyer3=['buy_name_3','buy_name_so_3','buy_name_ques_3','buy_name_cite_3','buy_mod_3','buy_auth_name_3','buy_auth_nameQ_3','buy_auth_mod_3','buy_auth_mod_a_3','buy_ulan_3']
buyer4=['buy_name_4','buy_name_so_4','buy_name_ques_4','buy_name_cite_4','buy_mod_4','buy_auth_name_4','buy_auth_nameQ_4','buy_auth_mod_4','buy_auth_mod_a_4','buy_ulan_4']

 

#Information from catalog or other sources on the history of the object prior to the current sale.
prev_owner1=['prev_owner_1','prev_own_ques_1','prev_own_so_1','prev_own_auth_1','prev_own_auth_D_1','prev_own_auth_E_1','prev_own_auth_P_1','prev_own_auth_L_1','prev_own_auth_Q_1','prev_own_ulan_1']
prev_owner2=['prev_owner_2','prev_own_ques_2','prev_own_so_2','prev_own_auth_2','prev_own_auth_D_2','prev_own_auth_E_2','prev_own_auth_P_2','prev_own_auth_L_2','prev_own_auth_Q_2','prev_own_ulan_2']
prev_owner3=['prev_owner_3','prev_own_ques_3','prev_own_so_3','prev_own_auth_3','prev_own_auth_D_3','prev_own_auth_E_3','prev_own_auth_P_3','prev_own_auth_L_3','prev_own_auth_Q_3','prev_own_ulan_3']
prev_owner4=['prev_owner_4','prev_own_ques_4','prev_own_so_4','prev_own_auth_4','prev_own_auth_D_4','prev_own_auth_E_4','prev_own_auth_P_4','prev_own_auth_L_4','prev_own_auth_Q_4','prev_own_ulan_4']
prev_owner5=['prev_owner_5','prev_own_ques_5','prev_own_so_5','prev_own_auth_5','prev_own_auth_D_5','prev_own_auth_E_5','prev_own_auth_P_5','prev_own_auth_L_5','prev_own_auth_Q_5','prev_own_ulan_5']
prev_owner6=['prev_owner_6','prev_own_ques_6','prev_own_so_6','prev_own_auth_6','prev_own_auth_D_6','prev_own_auth_E_6','prev_own_auth_P_6','prev_own_auth_L_6','prev_own_auth_Q_6','prev_own_ulan_6',]
prev_owner7=['prev_owner_7','prev_own_ques_7','prev_own_so_7','prev_own_auth_7','prev_own_auth_D_7','prev_own_auth_E_7','prev_own_auth_P_7','prev_own_auth_L_7','prev_own_auth_Q_7','prev_own_ulan_7']
prev_owner8=['prev_owner_8','prev_own_ques_8','prev_own_so_8','prev_own_auth_8','prev_own_auth_D_8','prev_own_auth_E_8','prev_own_auth_P_8','prev_own_auth_L_8','prev_own_auth_Q_8','prev_own_ulan_8',]
prev_owner9=['prev_owner_9','prev_own_ques_9','prev_own_so_9','prev_own_auth_9','prev_own_auth_D_9','prev_own_auth_E_9','prev_own_auth_P_9','prev_own_auth_L_9','prev_own_auth_Q_9','prev_own_ulan_9']


#prev_sale_year_1: If lot appears in an earlier sale, year of that sale appears here.
prev_sale1=['prev_sale_year_1','prev_sale_mo_1','prev_sale_day_1','prev_sale_loc_1','prev_sale_lot_1','prev_sale_ques_1','prev_sale_cat_1']
prev_sale2=['prev_sale_year_2','prev_sale_mo_2','prev_sale_day_2','prev_sale_loc_2','prev_sale_lot_2','prev_sale_ques_2','prev_sale_cat_2']
prev_sale3=['prev_sale_year_3','prev_sale_mo_3','prev_sale_day_3','prev_sale_loc_3','prev_sale_lot_3','prev_sale_ques_3','prev_sale_cat_3']
prev_sale4=['prev_sale_year_4','prev_sale_mo_4','prev_sale_day_4','prev_sale_loc_4','prev_sale_lot_4','prev_sale_ques_4','prev_sale_cat_4']
prev_sale5=['prev_sale_year_5','prev_sale_mo_5','prev_sale_day_5','prev_sale_loc_5','prev_sale_lot_5','prev_sale_ques_5','prev_sale_cat_5']
prev_sale6=['prev_sale_year_6','prev_sale_mo_6','prev_sale_day_6','prev_sale_loc_6','prev_sale_lot_6','prev_sale_ques_6','prev_sale_cat_6']
prev_sale7=[ 'prev_sale_year_7','prev_sale_mo_7','prev_sale_day_7','prev_sale_loc_7','prev_sale_lot_7','prev_sale_ques_7','prev_sale_cat_7']

#post_sale_year_1: If lot appears in a later sale, year of that sale appears here.
post_sale1=['post_sale_year_1','post_sale_mo_1','post_sale_day_1','post_sale_loc_1','post_sale_lot_1','post_sale_q_1','post_sale_cat_1']
post_sale2=['post_sale_year_2','post_sale_mo_2','post_sale_day_2','post_sale_loc_2','post_sale_lot_2','post_sale_q_2','post_sale_cat_2']
post_sale3=['post_sale_year_3','post_sale_mo_3','post_sale_day_3','post_sale_loc_3','post_sale_lot_3','post_sale_q_3','post_sale_cat_3']
post_sale4=['post_sale_year_4','post_sale_mo_4','post_sale_day_4','post_sale_loc_4','post_sale_lot_4','post_sale_q_4','post_sale_cat_4']
post_sale5=['post_sale_year_5','post_sale_mo_5','post_sale_day_5','post_sale_loc_5','post_sale_lot_5','post_sale_q_5','post_sale_cat_5']
post_sale6=['post_sale_year_6','post_sale_mo_6','post_sale_day_6','post_sale_loc_6','post_sale_lot_6','post_sale_q_6','post_sale_cat_6']
post_sale7=['post_sale_year_7','post_sale_mo_7','post_sale_day_7','post_sale_loc_7','post_sale_lot_7','post_sale_q_7','post_sale_cat_7']
post_sale8=['post_sale_year_8','post_sale_mo_8','post_sale_day_8','post_sale_loc_8','post_sale_lot_8','post_sale_q_8','post_sale_cat_8']
post_sale9=[ 'post_sale_year_9','post_sale_mo_9','post_sale_day_9','post_sale_loc_9','post_sale_lot_9','post_sale_q_9','post_sale_cat_9'] 

#post_own_1: Information from catalog annotations or other sources on the history of the object following the current sale.
post_own1=['post_own_1','post_own_q_1','post_own_so_1','post_own_auth_1','post_own_auth_D_1','post_own_auth_E_1','post_own_auth_P_1','post_own_auth_L_1','post_own_auth_Q_1','post_own_ulan_1']
post_own2=['post_own_2','post_own_q_2','post_own_so_2','post_own_auth_2','post_own_auth_D_2','post_own_auth_E_2','post_own_auth_P_2','post_own_auth_L_2','post_own_auth_Q_2','post_own_ulan_2']
post_own3=['post_own_3','post_own_q_3','post_own_so_3','post_own_auth_3','post_own_auth_D_3','post_own_auth_E_3','post_own_auth_P_3','post_own_auth_L_3','post_own_auth_Q_3','post_own_ulan_3']
post_own4=['post_own_4','post_own_q_4','post_own_so_4','post_own_auth_4','post_own_auth_D_4','post_own_auth_E_4','post_own_auth_P_4','post_own_auth_L_4','post_own_auth_Q_4','post_own_ulan_4']
post_own5=['post_own_5','post_own_q_5','post_own_so_5','post_own_auth_5','post_own_auth_D_5','post_own_auth_E_5','post_own_auth_P_5','post_own_auth_L_5','post_own_auth_Q_5','post_own_ulan_5']
post_own6=['post_own_6','post_own_q_6','post_own_so_6','post_own_auth_6','post_own_auth_D_6','post_own_auth_E_6','post_own_auth_P_6','post_own_auth_L_6','post_own_auth_Q_6','post_own_ulan_6']


#pres_loc_geog_1: Present location, if known, including city, state, country, of the owning institution.
pres_loc_1=['pres_loc_geog_1','pres_loc_inst_1','pres_loc_insq_1','pres_loc_insi_1','pres_loc_acc_1','pres_loc_accq_1','pres_loc_note_1']
pres_loc_2=['pres_loc_geog_2','pres_loc_inst_2','pres_loc_insq_2','pres_loc_insi_2','pres_loc_acc_2','pres_loc_accq_2','pres_loc_note_2']


extra=['pg','house_ulan_1','house_ulan_2','house_ulan_3','house_ulan_4','ppg']
 

        
###########################################################################################################
### This creates a dictionary and puts each dataframe corresponding to a csv file into the dictionary.
###########################################################################################################


### This cell creates a dictionary and puts each dataframe corresponding to a csv file into the dictionary.

#this is our current directory
current_dir=os.getcwd()

dtype_dict = {
    # Codes
    'catalog_number': 'string',
    'sale_code': 'string',

    # Lot info
    'lot_number': 'string',
    'lot_sale_year': 'Int64',
    'lot_sale_month': 'Int64',
    'lot_sale_day': 'Int64',
    'lot_sale_mod': 'string',
    'lot_notes': 'string',

    # Auction house
    'auction_house_1': 'string',
    'auction_house_2': 'string',
    'auction_house_3': 'string',
    'auction_house_4': 'string',

    # Title info
    'title': 'string',
    'title_modifier': 'string',
    'title_translation': 'string',

    # Artists
    **{col: 'string' for col in (artist1 + artist2 + artist3 + artist4 + artist5)},

    # Art info
    'hand_note_1': 'string',
    'hand_note_so_1': 'string',
    'hand_note_2': 'string',
    'hand_note_so_2': 'string',
    'hand_note_3': 'string',
    'hand_note_so_3': 'string',
    'hand_note_4': 'string',
    'hand_note_so_4': 'string',
    'hand_note_5': 'string',
    'hand_note_so_5': 'string',
    'hand_note_6': 'string',
    'hand_note_so_6': 'string',
    'hand_note_7': 'string',
    'hand_note_so_7': 'string',
    'object_type': 'string',
    'materials': 'string',
    'dimensions': 'string',
    'formatted_dimens': 'string',
    'format': 'string',
    'genre': 'string',
    'subject': 'string',
    'inscription': 'string',

**{col: 'string' for col in (auctioner1 + auctioner2 + auctioner3 + auctioner4)},
**{col: 'string' for col in (commissaire1 + commissaire2 + commissaire3 + commissaire4)},
**{col: 'string' for col in (seller1 + seller2 + seller3 + seller4 + seller5 + seller6)},
}

#this is where the getty csv's are
file_location = os.path.join(os.path.dirname(current_dir), 'getty_csvs')

#dictionary
dataframes={}

#number of csv files
n=13

for i in range(1,n+1):
    print(i)
    df=pd.read_csv(f'{file_location}/sales_contents_{i}.csv', low_memory=False, dtype=dtype_dict)
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


##################################################################################
### This does simple cleaning, like trimming whitespace and lowercasing. 
##################################################################################


print('********************** cleaning **********************')
for i in range(1,n+1):
    print(i)
    dataframes[f'df{i}']=clean_dataframe(dataframes[f'df{i}'])
    
####################################################################################
###Save to folder
####################################################################################

clean_file_location = os.path.join(os.path.dirname(current_dir), 'clean_getty_csvs')
for i in range(1, n+1):
    dataframes[f'df{i}'].to_csv(clean_file_location+f'/df{i}.csv', index=False)





    