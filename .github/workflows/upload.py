from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive.file']

creds = service_account.Credentials.from_service_account_file(
    'creds.json',
    scopes=SCOPES
)

service = build('drive', 'v3', credentials=creds)

file_metadata = {
    'name': 'mc-backup.zip',
    'parents': ['13DpC78es9LwuNV_ebHlGoisQ7QbVJo0U']
}

media = MediaFileUpload('mc-backup.zip', mimetype='application/zip')

file = service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()

print("Uploaded:", file.get('id'))
