import numpy as np
import json
from flask import Flask, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.image import rgb_to_grayscale
from PIL import Image, ImageOps

model = load_model('mymodel.h5')
print("model: ", model.get_config()['layers'][0]['config']['batch_input_shape'])

app = Flask(__name__)
@app.route('/model', methods=['POST'])
def run_model():
  req_data = request.get_json(force=True)
  image_data = req_data['img']
  img = np.array(image_data).reshape(28, 28, 1)

  image = np.array(image_data).reshape(1, 28, 28, 1)
  pred = model.predict(image)
  digit = np.argmax(pred)
  return str(digit)

if __name__ == '__main__':
  app.run()

  img = load_img('digit2.png', target_size=(28, 28))
  ing = ImageOps.invert(img)
  img = img_to_array(img)
  img = rgb_to_grayscale(img)
  img = img / 255.0
  
  img_lst = np.squeeze(img).tolist()
  data = json.dumps({'img':img_lst})
  url = 'http://127.0.0.1:5000/model'
  
  response = request.post(url, data)
  print('Digit =', response.text)
