!pip install SpeechRecognition # 2回目以降の実行ではコメントアウトしてもよい
import speech_recognition as sr
import soundfile as sf

def mic_to_recognize(SILENCE_RMS, SILENCE_SEC): # 無音判定する音量, 秒数
  """マイク録音と音声認識をまとめて行う関数"""

  # 必要な関数を使えるかチェック
  try:
    record_auto_stop
  except NameError:
    print('先にrecord_auto_stop関数のセルの実行が必要です')
    return ''

  memory_file = record_auto_stop(SILENCE_RMS, SILENCE_SEC)

  try:
    r = sr.Recognizer()
    with sr.AudioFile(memory_file) as source:
      audio = r.record(source)
    return r.recognize_google(audio, language='ja')
  except sr.UnknownValueError:
    # print('認識できません') # 繰り返し処理時のメッセージを減らすためコメント化
    return ''
