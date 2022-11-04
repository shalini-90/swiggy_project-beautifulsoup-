import csv
from curses import keyname
import json
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint as pp
from google.oauth2 import service_account
from googleapiclient.discovery import build
# import googleapiclient 
from google.oauth2.credentials import Credentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
	    "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/zec/Desktop/swiggy1/env/swig.json",scope)
client = gspread.authorize(creds)
sheet = client.open("swigy_prroject").sheet1   
#/home/zec/Desktop/swiggy1/env/swig.json

DATA_SPREADSHEET_ID='162XkHjOEpIk2Dwyr6ZU8lqceBRQasuD7INUuoknRUAk' 

def append_googlesheet(zoo):
# def append_googlesheet(res_name,str(list1)):

    # values = [value1]
    
    service = build('sheets','v4',credentials=creds) 
    # response = service.spreadsheets().values().append(spreadsheetId=DATA_SPREADSHEET_ID,
    # # valueInputOption='USER_ENTERED', range="Sheet1A1:B2, D4:E6", body={"values": values}).execute() 
    # valueInputOption='USER_ENTERED', range="Sheet1!A2", body={"values": res_name}).execute()  

    response = service.spreadsheets().values().append(spreadsheetId=DATA_SPREADSHEET_ID,
    valueInputOption='USER_ENTERED', range="Sheet1!A2", body={"values": zoo}).execute()  


# def append_googlesheet(value1): 
#     values = [value1]
    
#     service = build('sheets','v4',credentials=creds) 
#     response = service.spreadsheets().values().append(spreadsheetId=DATA_SPREADSHEET_ID,
#     # valueInputOption='USER_ENTERED', range="Sheet1A1:B2, D4:E6", body={"values": values}).execute() 
#     valueInputOption='USER_ENTERED', range="Sheet1!A2:B2", body={"values": values}).execute()  

    # response = service.spreadsheets().values().append(spreadsheetId=DATA_SPREADSHEET_ID,
    # valueInputOption='USER_ENTERED', range="Sheet1!B2", body={"values": zoo}).execute() 






    # valueInputOption='USER_ENTERED', range="Sheet1A1:B2, D4:E6", body={"values": values}).execute() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # A1:B2, D4:E6 
    # range=="Sheet1!A2:E2
