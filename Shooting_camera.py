# カメラ制御のためのクラスであるpicamera2をインポート
from picamera2 import Picamera2
# controlsはカメラ設定の調整時に使用（使用していない）
# from libcamera import controls
# 一定時間停止するためにPython標準ライブラリのtimeモジュールからsleep関数をインポート
from time import sleep
"""
日付や時刻を扱うためのdatetimeモジュールをインポート
ファイル名作成時に使用
"""
from datetime import datetime

# Picamera2の初期化
# Picamera2のインスタンスを作成
picam2 = Picamera2()
# 高品質な写真を撮るための設定を生成
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
        # 現在の映像を静止画として保存
        picam2.capture_file(filename)

        # 15分間待機
        sleep(60 * 15)

except KeyboardInterrupt:
    print("キーボード入力が行われたので終了します。")

finally:
    # カメラを停止
    picam2.stop()
