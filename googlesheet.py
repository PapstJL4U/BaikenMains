#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
_scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
_creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', _scope)
client = gspread.authorize(_creds)
