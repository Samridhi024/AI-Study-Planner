# from __future__ import print_function
# import datetime
# import os.path
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build

# SCOPES = ['https://www.googleapis.com/auth/calendar']

# def add_study_event(start_hour, end_hour):
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     service = build('calendar', 'v3', credentials=creds)

#     now = datetime.datetime.utcnow().isoformat() + 'Z'
#     today = datetime.date.today()
#     start_time = datetime.datetime(today.year, today.month, today.day, start_hour, 0).isoformat()
#     end_time = datetime.datetime(today.year, today.month, today.day, end_hour, 0).isoformat()

#     event = {
#         'summary': '📚 Study Session',
#         'description': 'Scheduled by AI Study Planner',
#         'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
#         'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'},
#     }

#     event = service.events().insert(calendarId='primary', body=event).execute()
#     print(f"Event created: {event.get('htmlLink')}")

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(summary, start_time, end_time, description=""):
    creds = None
    token_path = "token.json"

    # Load saved credentials if available
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": summary,
        "description": description,
        "start": {
            "dateTime": start_time,
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "Asia/Kolkata",
        }
    }

    event_result = service.events().insert(calendarId="primary", body=event).execute()
    return event_result.get("htmlLink")

