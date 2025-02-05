import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

def detect__objects_in_image(image_path):
  # モデルの読み込み関数
  model = YOLO('yolov8n.pt')

  # 画像の読み込み
  if image_path is not None:
    
    cv2_img = cv2.imread(image_path)
    
    # 物体検出
    results = model(cv2_img, conf=0.5, classes=[0])
    
    # 結果を描画
    output_img = results[0].plot(labels=True, conf=True)
    output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
    
    # 人の数をカウント
    categories = results[0].boxes.cls
    person_num = len(categories)
    
    # 出力
    st.image(output_img, caption='出力画像')
    st.text(f'人数は {person_num} 人です。')
