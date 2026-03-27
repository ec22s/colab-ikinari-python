from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import numpy as np
import cv2

class ColabCap:
  # 本の cap = cv2.VideoCapture(0) の代用クラス
  # TODO: 動画撮影用メソッド追加 https://qiita.com/sueasen/items/abf2d27c888c4d6d268d
  # サイズやフレームレートも変更可 https://qiita.com/yusuke84/items/35750017a6b12199aa39
  # https://developer.mozilla.org/ja/docs/Web/API/Media_Capture_and_Streams_API/Constraints

  _js = '''
    let video = document.createElement('video');
    let canvas = document.createElement('canvas');
    let stream = null;

    async function createDom() {
      if (stream) return;
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      video.srcObject = stream;
      await video.play();
    }

    async function removeDom() {
      await stream.getVideoTracks()[0].stop();
      video = null;
      stream = null;
      canvas = null;
    }

    async function cap(quality, waitSec) {
      if (!stream) await createDom();
      await new Promise((resolve) => setTimeout(resolve, waitSec * 10**3));
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      return canvas.toDataURL('image/jpeg', quality);
    }
  '''

  def __init__(self, quality=0.8, first_wait_sec=0.25):
    self.quality = quality
    self.first_wait_sec = first_wait_sec
    display(Javascript(ColabCap._js))

  def read(self):
    try:
      data = eval_js(f'cap({ self.quality }, { self.first_wait_sec })')
      self.first_wait_sec = 0
      image_bytes = b64decode(data.split(',')[1])
      jpg_as_np = np.frombuffer(image_bytes, dtype=np.uint8)
      return True, cv2.imdecode(jpg_as_np, flags=1)
    except Exception as err:
      print(str(err))
      return False, None

  def release(self):
    eval_js('removeDom()')
