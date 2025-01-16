from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def upload_to_google_drive(file_path):
    # Google Drive APIの認証
    gauth = GoogleAuth()
    gauth.settings_file = "settings.yaml"  # settings.yaml を適用
    gauth.LocalWebserverAuth()  # ブラウザを使用して認証
    drive = GoogleDrive(gauth)

    # アップロード先のフォルダID
    folder_id = "1is749wEyc_7X-9s-oUx5cbJvjQguK9Yv"

    # ファイルをアップロード
    file_name = file_path.split('/')[-1]
    file = drive.CreateFile({
        'title': file_name,       # Google Drive上のファイル名
        'parents': [{'id': folder_id}]  # アップロード先フォルダを指定
    })
    file.SetContentFile(file_path)
    file.Upload()

    # アップロードしたファイルの共有リンクを取得
    file.InsertPermission({
        'type': 'anyone',  # 全員に公開
        'value': 'anyone',
        'role': 'reader'   # 読み取り専用
    })

    print(f"Uploaded file URL: {file['alternateLink']}")
    return file['alternateLink']
