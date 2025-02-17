from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def authenticate_google_drive():
    """
    Google Drive APIの認証を行い、GoogleDriveオブジェクトを返す。
    """
    gauth = GoogleAuth()
    gauth.settings_file = "settings.yaml"  # 修正した設定ファイルを適用
    gauth.LoadCredentialsFile("saved_credentials.json")  # 認証情報の読み込み

    if gauth.credentials is None:
        print("新しい認証を実行します...")
        gauth.CommandLineAuth()  # コンソール認証
        gauth.SaveCredentialsFile("saved_credentials.json")  # 認証情報を保存
    elif gauth.access_token_expired:
        print("アクセストークンが期限切れのため、更新します...")
        gauth.Refresh()  # トークンを更新
    else:
        print("既存の認証情報を使用します。")
        gauth.Authorize()

    return GoogleDrive(gauth)

def upload_to_google_drive(file_path):
    """
    指定したGoogle Driveフォルダにファイルをアップロードし、共有リンクを返す。
    """
    drive = authenticate_google_drive()

    # アップロード先のフォルダID
    folder_id = "1rAbRMiX2mAmBHIPmbrAbp0eBGEW6eYp7"

    # ファイルをアップロード
    file_name = file_path.split('/')[-1]
    file = drive.CreateFile({
        'title': file_name,
        'parents': [{'id': folder_id}]
    })
    file.SetContentFile(file_path)
    file.Upload()

    # アップロードしたファイルの共有リンクを取得
    file.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'
    })

    print(f"Uploaded file URL: {file['alternateLink']}")
    return file['alternateLink']

if __name__ == "__main__":
    file_path = "example.jpg"
    upload_to_google_drive(file_path)
