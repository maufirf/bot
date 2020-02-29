import json
import os
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from dotenv import load_dotenv

def get_all_values():
    load_dotenv()
    GDRIVE_VAL = eval(os.getenv("GDRIVE_VAL"))
    if not os.path.exists('temp'):
        os.makedirs('temp')
    with open('temp/hendrarnohasasmalldick.json','w') as f:
        json.dump(GDRIVE_VAL,f)
        f.close()
    
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('temp/hendrarnohasasmalldick.json', scope)
    client = gspread.authorize(creds)

    os.remove('temp/hendrarnohasasmalldick.json')
    os.removedirs('temp')

    sheet = client.open('bot_botwordinput').sheet1
    return sheet.get_all_records()
