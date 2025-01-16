import requests

# GoogleフォームのURLとフォームフィールドIDを設定
GOOGLE_FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScZWODMbyFmIh4YE4DGyNHe0puGx4IWbydBOf_jMLiaXBtV5A/formResponse"
FIELD_PHOTO = "entry.1391783452"  # 写真アップロード用フィールドID
FIELD_TIME = "entry.923261887"   # 日付入力用フィールドID

# 写真をGoogleフォームに送信する関数
def send_to_google_form(photo_path, time):
    with open(photo_path, 'rb') as photo:
        files = {
            FIELD_PHOTO: photo,
        }
        data = {
            FIELD_TIME: time,
        }
        response = requests.post(GOOGLE_FORM_URL, files=files, data=data)
        if response.status_code == 200:
            print("Successfully sent to Google Form!")
        else:
            print(f"Failed to send: {response.status_code}")