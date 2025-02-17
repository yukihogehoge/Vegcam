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
    results = model(cv2_img, conf=0.5, classes=[46, 47, 49, 50, 51])
    
    # 結果を描画
    output_img = results[0].plot(labels=True, conf=True)
    output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)

    # クラスの取得（検出された野菜・果物）
    categories = results[0].boxes.cls
    
    # 各クラスの個数をカウント
    class_names = ["バナナ", "りんご", "オレンジ", "ブロッコリー", "にんじん"]
    class_ids = [46, 47, 49, 50, 51]
    counts = {name: (categories == id).sum().item() for name, id in zip(class_names, class_ids)}
    
    # 出力
    st.image(output_img, caption='出力画像')
    for name, count in counts.items():
        st.text(f'{name}の個数: {count} 個')
