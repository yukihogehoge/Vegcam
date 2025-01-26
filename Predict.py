from tensorflow.keras.models import load_model
import cv2
import numpy as np

# モデルをロード
model = load_model('vegetable_classifier.keras')

image_path = Vegcam/test_carrot.png

# 推論関数
def predict(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  # バッチ次元を追加
    predictions = model.predict(img)
    class_index = np.argmax(predictions)
    class_name = list(train_data.class_indices.keys())[class_index]
    print(class_name)
    return class_name
