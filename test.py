import gspread as gs
import pandas as pd
import pickle


token = '/Users/antonustimov/py/APIkeygoogle.json' 
link =  'https://docs.google.com/spreadsheets/d/1xQQ1qPgqhygtH_vczhV8rl-CTZSyCrOVGACJQyp0r5M'


gc = gs.service_account(filename=token)
sh = gc.open_by_url(link)

ws = sh.worksheet('Декабрь')


list_of_dicts = ws.get_all_records()
with open('test_sheet.pkl', 'wb') as f:
    pickle.dump(list_of_dicts, f)
#print(list_of_dicts)
