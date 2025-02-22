import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from Email_notifier import send_email_gmail

# メール通知先
EMAIL_RECIPIENTS = {
    "バナナ": "banana_producer@example.com",
    "りんご": "apple_producer@example.com",
    "オレンジ": "orange_producer@example.com", # 自分へ送信
    "ブロッコリー": "broccoli_producer@example.com",
    "にんじん": "vegcam117@gmail.com"
}

# 検出対象クラス
CLASS_NAMES = ["バナナ", "りんご", "オレンジ", "ブロッコリー", "にんじん"]
CLASS_IDS = [46, 47, 49, 50, 51]

def detect_objects_in_image(image_path):
    model = YOLO('yolov8n.pt')

    # 画像の読み込み
    if image_path is not None:
        cv2_img = cv2.imread(image_path)

        # 物体検出
        results = model(cv2_img, conf=0.2, classes=CLASS_IDS)

        # 結果を描画
        output_img = results[0].plot(labels=True, conf=True)
        output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

        # クラスの取得（検出された野菜・果物）
        categories = results[0].boxes.cls

        # 各クラスの個数をカウント
        counts = {name: (categories == id).sum().item() for name, id in zip(CLASS_NAMES, CLASS_IDS)}

        # 出力
        st.image(output_img, caption='出力画像')
        for name, count in counts.items():
            st.text(f'{name}の個数: {count} 個')

            # 在庫が2個以下ならメール通知
            if count <= 2:
                subject = f"[在庫警告] {name}の在庫が少なくなっています！"
                body = f"現在の在庫: {count} 個です。補充をお願いします。" + "https://sites.google.com/view/vegcam"
                send_email_gmail(EMAIL_RECIPIENTS[name], subject, body, name)

        return counts
