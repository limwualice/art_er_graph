import pandas as pd
import numpy as np
import os
import json


############# This function gives us the directory that we want to go to #############

def file_location(folder_name):
    #this is our current directory
    current_dir=os.getcwd()

    #this is where the csv's that I'm interested are located
    file_loc = os.path.join(os.path.dirname(current_dir), folder_name)

    return file_loc




indicator_dict={'df_art_piece.csv':('title',['untitled'],['catalog_number','title','sale_code', 'object_type']),
               'df_artist.csv':('artist_name_1',['anonym','anonyme','unbekannt','anonymous'],['artist_name_1','art_authority_1','nationality_1','artist_ulan_1']),
               'df_auction_house.csv':('auction_house_1',['anonymous'],['auction_house_1']),
                'df_auction.csv':(None,None,['lot_number','price_amount_1','lot_sale_year','lot_sale_month','lot_sale_day']),
               'df_auctioneer.csv':('expert_auth_1',['anonyme'],['expert_auth_1']),
               'df_commissaire.csv':('commissaire_pr_1',['anonyme'],['commissaire_pr_1']),
                'df_buyer.csv':(None, None,['buy_name_1','buy_auth_name_1','buy_ulan_1']),
               'df_seller.csv':('sell_name_1',['aus privatbesitz'],['sell_name_1','sell_auth_name_1','sell_ulan_1'])}



for i,j in indicator_dict.items():
    
    df=pd.read_csv(file_location('concatenated_getty')+'/'+i, low_memory=False)
    print('*****************',i,'*****************')
    df=df[j[2]]
    if j[0]==None:
        pass
    else:
        df['indicator']=~((df[j[0]].isin(j[1]))|(df[j[0]].isna()))
        df=df[df['indicator']==True]
    df.to_csv(file_location('getty_pre_blocking'+'/'+i)
    print(df.head())