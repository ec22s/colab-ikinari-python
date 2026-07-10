from base64 import b64encode
from google.colab.output import eval_js
from IPython.display import display, Javascript
import cv2

def colab_imshow(ext, ndarray, height=240):
  ret, buf = cv2.imencode(f'.{ext}', ndarray)
  b64 = b64encode(buf.tobytes()).decode()

  display(Javascript("""
    const IMG_DOM_ID = "imageOutput";
    const output = document.querySelector("#output-area");
    let imgDom = output.querySelector(`#${IMG_DOM_ID}`);
    if (!imgDom) {
      imgDom = document.createElement("img");
      imgDom.id = IMG_DOM_ID;
      imgDom.style.marginLeft = "1em";
      output.appendChild(imgDom);
    }

    function drawImage(ext, b64, height) {
      imgDom.height = height;
      imgDom.src = `data:image/{ext};base64,${b64}`;
    }
  """))
  eval_js(f"""drawImage("{ext}", "{b64}", {height})""")
