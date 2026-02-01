# 本 p.82 `3-2-1` から作るrecord関数のColab版

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import soundfile as sf
import io
import numpy as np

def record(duration):
  """PCのマイクで録音する関数"""

  display(Javascript('''
    const message = (text) => {
      const domId = 'message';
      const output = document.querySelector('#output-area');
      let target = document.querySelector(`#${domId}`);
      if (!target) {
        target = document.createElement('div');
        target.id = domId;
        output.insertBefore(target, output.firstChild);
      }
      target.textContent = text;
    };

    const sleep = async (sec) => {
      return new Promise(resolve => setTimeout(resolve, sec * 1000));
    };

    async function recordAudio(duration) {
      const chunks = [];
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      const fr = new FileReader();
      recorder.ondataavailable = e => chunks.push(e.data);
      recorder.onstop = e => fr.readAsDataURL(new Blob(chunks));
      await recorder.start();
      message('録音中･･･');
      await sleep(duration);
      await recorder.stop();
      message('録音終了');
      return await new Promise(resolve => {
        fr.onloadend = () => resolve(fr.result);
      });
    }
  '''))

  data = eval_js(f'recordAudio({duration})')
  waveform, sampling_rate = sf.read(
    io.BytesIO(b64decode(data.split(',')[1])),
    dtype='int16' # 無指定なら自動で正規化されるが、あえて本と同じ正規化処理をするため指定
  )

  # バイトデータを数値データに変換
  byte_to_num = np.frombuffer(waveform, dtype='int16')

  # 最大値を計算
  max_value = float((2 ** 16 / 2) - 1)

  # 波形を正規化
  normalized_waveform = byte_to_num / max_value

  return normalized_waveform, sampling_rate

print('録音準備完了')
