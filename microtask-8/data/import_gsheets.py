#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from configparser import ConfigParser

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


# Updates the sheet with csv data
def upload_csv(csv_path, sheet_id, API):
    with open(csv_path, 'r') as csv_file:
        csvContents = csv_file.read()
    body = {
        'requests': [{
            'pasteData': {
                "data": csvContents,
                "type": 'PASTE_NORMAL',
                "delimiter": ',',
            }
        }]
    }
    # Create API request for updating the sheet data
    request = API.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body=body)
    response = request.execute()
    return response


def main():
    credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    print("Verifying Credentials\n")

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    print("Credentials Verified\n")

    API = build('sheets', 'v4', credentials=credentials)

    config = ConfigParser()
    config.read('config.ini')
    # The ID of spreadsheet.
    sheet_id = config.get('GSheets', 'sheet_id')
    # CSV file to be uploaded
    csv_file = config.get('GSheets', 'csv_file')
    # Path of the CSV file to be uploaded
    path_to_csv = os.path.abspath(csv_file)

    print("Starting Upload\n")
    upload_csv(
        csv_path=path_to_csv,
        sheet_id=sheet_id,
        API=API
    )
    print("Upload Finished\n")


if __name__ == '__main__':
    main()
