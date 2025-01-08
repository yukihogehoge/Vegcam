import cv2
from time import sleep
from datetime import datetime

# カメラの初期化
for i in range(0, 100):
  cap = cv2.VideoCapture(i)

  if not cap.isOpened():
    print("正常に読み込めませんでした。")
    continue

  try:
    while True:
      # frameをキャプチャ
      ret, frame = cap.read()
      if not ret:
        print("フレームが取得できませんでした。")
        break

      # 現在時刻でファイル名を生成
      timestamp = datetime.now().strftime("%Y年%m月%d日%H時%M分%S秒")
      filename = f"image_{timestamp}.jpg"

      # 写真を保存
      print(f"撮影中:{filename}")
      cv2.imwrite(filename, frame)

      # 15分間待機
      sleep(60 * 15)

  except KeyboardInterrupt:
    print("キーボード入力が行われたので終了します。")

  finally:
    cap.release()
    cv2.destroyAllWindows()