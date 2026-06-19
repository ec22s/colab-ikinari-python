from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import numpy as np
import cv2

class ColabCap2:

  _js = '''
    let video = document.createElement('video');
    let canvas = document.createElement('canvas');
    let stream = null;

    async function createDom(preview) {
      if (stream) return;
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      video.srcObject = stream;
      if (preview) document.querySelector("#output-area").appendChild(video);
      await video.play();
    }

    async function stop() {
      await stream.getVideoTracks()[0].stop();
      video = null;
      stream = null;
      canvas = null;
    }

    async function cap(quality, waitSec, preview) {
      if (!stream) await createDom(preview);
      await new Promise((resolve) => setTimeout(resolve, waitSec * 10**3));
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      return canvas.toDataURL('image/jpeg', quality);
    }
  '''

  is_opened = False

  def __init__(self, quality=0.8, first_wait_sec=0.25, preview=True):
    self.quality = quality
    self.first_wait_sec = first_wait_sec
    self.preview = "true" if preview else "false"
    display(Javascript(self._js))
    self.is_opened = True

  def isOpened(self):
    return self.is_opened

  def read(self):
    try:
      data = eval_js(
        f"cap({ self.quality }, { self.first_wait_sec }), { self.preview })"
      )
      self.first_wait_sec = 0
      image_bytes = b64decode(data.split(',')[1])
      jpg_as_np = np.frombuffer(image_bytes, dtype=np.uint8)
      return True, cv2.imdecode(jpg_as_np, flags=1)
    except Exception as err:
      print(str(err))
      self.is_opened = False
      return False, None

  def release(self):
    self.is_opened = False
    eval_js('stop()')
