from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import os

def get_youtube_service(client_secrets_file, token_file, scopes):
    # Check if the token file exists, if not, initiate the flow.
    if os.path.exists(token_file):
        credentials = Credentials.from_authorized_user_file(token_file, scopes=scopes)
    else:
        # Run the OAuth flow to obtain new tokens
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes=scopes)
        credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'w') as token:
            token.write(credentials.to_json())

    youtube = build('youtube', 'v3', credentials=credentials)
    return youtube

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CLIENT_SECRETS_FILE = 'client_secrets.json'  # Your client secrets, downloaded from the Google Cloud Console
TOKEN_FILE = 'credentials.json'  # File to store user's access and refresh tokens

def main(filepath, caption):
    youtube = get_youtube_service(CLIENT_SECRETS_FILE, TOKEN_FILE, SCOPES)

    video_file = filepath
    media_body = MediaFileUpload(video_file, mimetype='video/*', resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "categoryId": "20",
                "description": caption,
                "title": caption
            },
            "status": {
                "privacyStatus": "public",  # or 'public'/'unlisted'
                "madeForKids": "false"
            }
        },
        media_body=media_body
    )
    response = request.execute()

    print(response)