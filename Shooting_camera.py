from picamera2 import Picamera2, Preview
from libcamera import controls
from time import sleep
from datetime import datetime

# Picamera2の初期化
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())

# カメラを起動
picam2.start()

try:
    while True:
        # 現在時刻でファイル名を生成
        timestamp = datetime.now().strftime("%Y年%m月%d日%H時%M分%S秒")
        filename = f"image_{timestamp}.jpg"

        # 写真を撮影して保存
        print(f"撮影中: {filename}")
        picam2.capture_file(filename)

        # 15分間待機
        sleep(60 * 15)

except KeyboardInterrupt:
    print("キーボード入力が行われたので終了します。")

finally:
    # カメラを停止
    picam2.stop()
