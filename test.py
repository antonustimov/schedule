from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError







CREDENTIALS_FILE = 'token.json'
spreadsheet_id = '1xQQ1qPgqhygtH_vczhV8rl-CTZSyCrOVGACJQyp0r5M'

credintails = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www/googleapis.com/auth/spreadsheets',
     'https://www/googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E10',
    majorDimensions='ROWS'
).execute()
pprint(values)
exit()



'''
values = service.spreadsheets().values().batchUpdate(
    spreadsheetsId=spreadsheet_id,
    body={
        'valueInputOption': "USER_ENTERED"
'''
