import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

def detect__objects_in_image(image_path):
  # モデルの読み込み関数
  model = YOLO('yolov8n.pt')

  # 画像の読み込み
  if image_path is not None:
    results = model(image_path)
    
    bytes_data = image_path.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8),cv2.IMREAD_COLOR)
    results = model(cv2_img,conf=0.5,classes=[0])
    output_img = results[0].plot(labels=True,conf=True)
    output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

    categories = results[0].boxes.cls
    person_num = len(categories)

    #output
    st.image(output_img, caption = '出力画像')
    st.text(f'人数は{person_num}人です。')
