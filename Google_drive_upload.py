import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# 認証情報の読み込み
def load_credentials():
    with open("token.pickle", "rb") as token:
        return pickle.load(token)

# Google Drive へのアップロード
def upload_to_google_drive(file_path):
    creds = load_credentials()
    service = build("drive", "v3", credentials=creds)

    folder_id = "1rAbRMiX2mAmBHIPmbrAbp0eBGEW6eYp7"  # アップロード先フォルダID
    file_name = file_path.split('/')[-1]

    file_metadata = {
        "name": file_name,
        "parents": [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(body=file_metadata, media_body=media, fields="id, webViewLink").execute()

    # 共有設定（全員に閲覧可能にする）
    permission = {
        "type": "anyone",
        "role": "reader"
    }
    service.permissions().create(fileId=file["id"], body=permission).execute()

    print(f"✅ アップロード成功！URL: {file['webViewLink']}")
    return file["webViewLink"]
