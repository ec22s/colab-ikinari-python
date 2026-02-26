# 独自のrecord_auto_stop関数 (record関数の自動停止版、無音を検知するまで録音)
# 参考 https://pavi2410.com/blog/detect-silence-using-web-audio/

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
from pydub import AudioSegment
import soundfile as sf
import io

error_count = 0

def record_auto_stop(
  SILENCE_RMS,      # 無音レベルの大きさの指標
  SILENCE_SEC,      # 秒. 無音がこの時間続いたら録音終了
):
  display(Javascript('''

    // メッセージ表示
    const message = (text) => {
      const domId = 'message';
      const output = document.querySelector('#output-area');
      let target = document.querySelector(`#${domId}`);
      if (!target) {
        target = document.createElement('div');
        target.id = domId;
        output.insertBefore(target, output.firstChild);
      }
      target.innerHTML += `${text}<br>`;
    };

    // 音量の指標を計算
    const calculateRMS = (data) => {
      let sum = 0;
      for (let i = 0; i < data.length; i++) {
        const normalized = data[i] / 128 - 1;
        sum += normalized * normalized;
      }
      return Math.sqrt(sum / data.length);
    };

    async function recordAndAutoStop(SILENCE_RMS, SILENCE_SEC) {
      // マイク使用可否チェック
      let stream = null;
      try {
        stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      } catch(e) {
        return;
      }

      const audioContext = new AudioContext();
      const source = audioContext.createMediaStreamSource(stream);
      const analyser = audioContext.createAnalyser();
      source.connect(analyser);

      analyser.fftSize = 2048;
      const bufferLength = analyser.fftSize;
      const dataArray = new Uint8Array(bufferLength);
      let silenceStart = performance.now();

      const chunks = [];
      const recorder = new MediaRecorder(stream);
      recorder.ondataavailable = e => {
        message('録音中');
        chunks.push(e.data);
      };

      // 無音検知
      const detectSilence = () => {
        analyser.getByteTimeDomainData(dataArray);
        if (calculateRMS(dataArray) < SILENCE_RMS) {
          const now = performance.now();
          if (now - silenceStart > (SILENCE_SEC * 10**3)) {
            recorder.stop();
            return;
          }
        } else {
          silenceStart = performance.now();
          if (recorder.state === 'inactive') {
            recorder.start();
          }
        }
        requestAnimationFrame(detectSilence);
      }

      const fr = new FileReader();
      message('録音開始');
      recorder.onstop = e => {
        message('録音終了');
        fr.readAsDataURL(new Blob(chunks))
      };
      recorder.start(1000);
      detectSilence();

      return await new Promise(resolve => {
        fr.onloadend = () => resolve(fr.result);
      });
    };
  '''))

  data = eval_js(f'recordAndAutoStop({SILENCE_RMS}, {SILENCE_SEC})')

  # 簡易エラー処理
  global error_count
  if data == None:
    if error_count == 0:
      error_count += 1
      print('''
        ブラウザ画面の中央にマイク使用を求める表示があると思います。
        許可を選択し、もう一度セルを実行して下さい。
        また別のマイク使用を求めるポップアップが出たら、許可して下さい。
      '''.replace(' ', ''))
    else:
      print('マイクを使用できません')
    return [], 0

  # WAV形式に統一
  buffer = io.BytesIO()
  AudioSegment.from_file(
    io.BytesIO(b64decode(data.split(',')[1]))
  ).export(buffer, format="wav")
  buffer.seek(0)
  return sf.read(buffer)

print('録音準備完了')
