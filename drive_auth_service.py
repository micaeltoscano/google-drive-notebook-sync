import os.path

from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]


creds = None


if os.path.exists("token.json"):

    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )


if not creds or not creds.valid:

    if creds and creds.expired and creds.refresh_token:

        creds.refresh(Request())

    else:

        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(
            port=8080,
            open_browser=True,
            authorization_prompt_message="Acesse: {url}"
)

    with open("token.json", "w") as token:

        token.write(creds.to_json())


service = build(
    "drive",
    "v3",
    credentials=creds
)


results = service.files().list(
    q="sharedWithMe=true",
    pageSize=10,
    fields="files(id, name)"
).execute()


files = results.get("files", [])


if not files:

    print("No files found.")

else:

    print("Files:")

    for file in files:

        print(
            f"{file['name']} ({file['id']})"
        )