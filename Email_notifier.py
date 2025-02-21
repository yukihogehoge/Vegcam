import base64
import pickle
import json
import os
import time
from email.mime.text import MIMEText
from googleapiclient.discovery import build

LAST_SENT_FILE = "last_sent.json"

# 認証情報の読み込み
def load_credentials():
    with open("token.pickle", "rb") as token:
        return pickle.load(token)

# 最後にメールを送信した時間を保存/取得
def load_last_sent():
    if os.path.exists(LAST_SENT_FILE):
        with open(LAST_SENT_FILE, "r") as file:
            return json.load(file)
    return {}

def save_last_sent(last_sent):
    with open(LAST_SENT_FILE, "w") as file:
        json.dump(last_sent, file)

# メール送信
def send_email_gmail(recipient, subject, body, item_name):
    creds = load_credentials()
    service = build("gmail", "v1", credentials=creds)

    # 1時間以内の重複送信を防ぐ
    last_sent = load_last_sent()
    current_time = time.time()

    if item_name in last_sent and current_time - last_sent[item_name] < 3600:
        print(f"⏳ {item_name} の通知は1時間以内に送信済みのためスキップ")
        return False

    message = MIMEText(body)
    message["to"] = recipient
    message["subject"] = subject
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        service.users().messages().send(userId="me", body={"raw": encoded_message}).execute()
        print(f"✅メール送信成功: {recipient}（{item_name}）")

        # 送信時間を記録
        last_sent[item_name] = current_time
        save_last_sent(last_sent)
        return True
    except Exception as e:
        print(f"❌メール送信失敗: {e}")
        return False
