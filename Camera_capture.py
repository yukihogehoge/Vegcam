# カメラ制御のためのクラスであるpicamera2をインポート
from picamera2 import Picamera2
# controlsはカメラ設定の調整時に使用（このコードでは使用しない）
# from libcamera import controls
# 一定時間停止するためにPython標準ライブラリのtimeモジュールからsleep関数をインポート
import os
from time import sleep
"""
日付や時刻を扱うためのdatetimeモジュールをインポート
ファイル名作成時に使用
"""
from datetime import datetime

from Detect import detect__objects_in_image

from Google_drive_upload import upload_to_google_drive

def capture_images():
  # Picamera2の初期化
  # Picamera2のインスタンスを作成
  picam2 = Picamera2()
  # 高品質な写真を撮るための設定を生成
  picam2.configure(picam2.create_still_configuration())

  # 保存フォルダの指定
  save_dir = "/home/bejikame/Vegcam/picturebox"
  os.makedirs(save_dir, exist_ok=True)

  # カメラを起動
  picam2.start()

  try:
    while True:
      # 現在時刻でファイル名を生成
      timestamp = datetime.now().strftime("%Y年%m月%d日%H時%M分%S秒")
      filename = os.path.join(save_dir, f"image_{timestamp}.jpg")

      # 写真を撮影して保存
      print(f"撮影中: {filename}")
      # 現在の映像を静止画として保存
      picam2.capture_file(filename)

      # 画像と検出結果をwebページ上に表示
      detect__objects_in_image(filename)

      # 写真をGoogle driveに保存
      print("google driveにアップロード中…")
      upload_to_google_drive(filename)
      
      # 15分間待機
      sleep(60)

  except KeyboardInterrupt:
    print("キーボード入力が行われたので終了します。")

  finally:
    # カメラを停止
    picam2.stop()
