## Colabで本のChapter 4を動かす

### 概要

- Chapter 3と同じくマイクを使うため、学習会独自の `record_auto_stop` 関数を使う

- 音声認識ライブラリを使い、マイクに話した音声を日本語の文字列に変換する

- 文字列を変換する関数を作り、「話した言葉が丁寧語に変換される」の基礎を体験する

<br>

## Chapter 4 各セクションの取り扱い

### 4-1. 音声認識の準備をしよう（p.106〜）

- セクション全体を割愛（ColabではPCのマイクを認識できないため）

<br>

### 4-2. 音声をテキストに変換しよう（p.109〜）

- 本 p.112 のコード `4-2-2` と同様の結果を得るため、以下の手順で作業します

- セルを追加し、Chapter 3 で作った `record_auto_stop` 関数をコピぺ

  - ない人はこちらから → [chapter-3/record_auto_stop.py](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record_auto_stop.py)

<br>

- 関数の29行目 `+=` を `=` に変更

  ```JavaScript
  - target.innerHTML += `${text}<br>`;
  + target.innerHTML = `${text}<br>`;
  ```

  - 修正の理由：最後に行う「繰り返し処理」の便宜上（メッセージの量を減らす）

<br>

- 関数の64行目 `message('録音中');` をコメントアウト（コメント記号がPythonの #
 でない）

  ```JavaScript
  - message('録音中');
  + // message('録音中');
  ```

  - 修正の理由：上と同様、繰り返し処理でメッセージの量を減らす

<br>

- 関数の87行目 `録音開始` をマイク絵文字に変更（見やすさのため）

  ```JavaScript
  - message('録音開始');
  + message('🎤');
  ```

<br>

  - 関数の123行目 `return sf.read(buffer)` を `return buffer` に修正

    ```Python
    - return sf.read(buffer)
    + return buffer
    ```

    - 修正の理由：WAVファイルのデータを直接使うため

<br>

- 関数のセルを実行し、エラーが出ないのを確認

- セルを追加し、以下のコードを書く（コメントは省いてもよい）

  ```Python
  SILENCE_RMS = 0.01 # 無音レベルの指標（環境音が大きければ増やす）
  SILENCE_SEC = 2    # 秒. 無音がこの時間続いたら録音終了

  !pip install SpeechRecognition # 2回目以降の実行ではコメントアウトしてもよい
  import speech_recognition as sr

  memory_file = record_auto_stop(SILENCE_RMS, SILENCE_SEC)

  try:
    r = sr.Recognizer()
    with sr.AudioFile(memory_file) as source:
      audio = r.record(source)
    recognized_text = r.recognize_google(audio, language='ja')
    print(f'音声認識結果「{recognized_text}」')
  except sr.UnknownValueError:
    print('認識できません')
  ```

- 実行して動作を確かめる

- Chapter 3の時と同様、マイク使用を求める2つのダイアログが出たら許可する

- 自動的に音声認識ライブラリのインストールが始まる

  ```
  Collecting SpeechRecognition
  Downloading speechrecognition-3.15.1-py3-none-any.whl.metadata (31 kB)
  Requirement already satisfied: typing-extensions in /usr/local/lib/python3.12/dist-packages (from SpeechRecognition) (4.15.0)
  Downloading speechrecognition-3.15.1-py3-none-any.whl (32.9 MB)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.9/32.9 MB 47.2 MB/s eta 0:00:00
  Installing collected packages: SpeechRecognition
  Successfully installed SpeechRecognition-3.15.1
  ```

- その後 🎤 が表示されたら何か話す

- 話し終えたら自動的に録音が終わり、音声認識結果が示されればOK

  ```
  録音終了
  音声認識結果「＊＊＊＊＊」
  ```

- これが本 p.112 `4-2-2` と同様の動きになります

- コードを比較して、本と違う箇所の理由を考えると良いです. 不明な点は質問して下さい

<br>

### 本にない工夫：マイク録音と音声認識を一つの関数にまとめよう

- 前項の処理を一つの関数 `mic_to_recognize` にまとめます

- そうすると後々の作業が楽で、コードも見やすいです

- 新しいセルに以下のコードを書きます. 前項の処理をコピペし編集してもいいです

- 書き終えたらセルを1回実行します（関数を別のセルで使うため. Colab特有）

  ```Python
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
  ```

<br>

- 前項の「関数でない」処理と少し違う点があります

  - マイク録音用の関数 `record_auto_stop` が使えるかのチェックを追加

  - 想定外の場合は `return` で空文字を返す. 関数を使う時のエラーチェックが簡単になります

- 関数のテストとして、新しいセルに以下のコードを書きます（コメントは省いても可）

  ```Python
  # mic_to_ecognize関数のテスト

  text = mic_to_recognize(0.01, 2) # 無音判定する音量, 秒数
  if text:
    print(f'音声認識結果「{text}」')
  ```

- 実行して 🎤 が表示されたら何か話し、音声認識の結果が表示されればOK

- 前項のような長いコードを書かずに、マイク録音と音声認識が可能になりました

- 関数がエラーなく文字を返した時だけ（ `if text:` ）音声認識結果を表示します

<br>

### 4-3. 音声をテキストに変換しよう（p.114〜）

- 本と同様に「タメ口を丁寧語に変換する関数」を作ります

- 新しいセルに以下のコードを書きます. このセクションで作る関数の完成形になります

  - コードの詳しい説明は本 p.116〜119 にあります. 不明な点は質問して下さい

  ```Python
  # 本 4-3 (p.114-120) で作る関数の完成形

  def tamego_to_teineigo(text):
    """タメ口を丁寧語に変換する関数"""

    # 変換パターン
    patterns = {
      'だね': 'ですね',
      'こんにちは': 'ごきげんよう',
      'だ': 'です'
    }

    # テキストをスペースで分離する
    sentences = text.split(' ')

    # 変換
    teineigo_sentences = []
    for sentence in sentences:
      for pattern, replacement in patterns.items():
        sentence = sentence.replace(pattern, replacement)
      teineigo_sentences.append(sentence)

    joined_text = ' '.join(teineigo_sentences)

    return joined_text
    ```

- 書き終えたらセルを1回実行します（関数を別のセルで使うため. Colab特有）

- この関数と、前項で作った関数を使い「マイク録音→音声認識→丁寧語変換」を短いコードで行います

- 新しいセルに以下のコードを書きます

  ```Python
  # 2つの関数を利用して「マイク録音→音声認識→丁寧語変換」を短いコードで行う

  text = mic_to_recognize(0.01, 2) # 無音判定する音量, 秒数
  if text:
    print(f'音声認識結果「{text}」')
    print(f'丁寧語変換結果「{tamego_to_teineigo(text)}」')
  ```

- 実行して 🎤 表示の間に「〜だね」と話し、丁寧語変換の結果に「〜ですね」と出ればOK

- その他「こんにちは」と話すと「ごきげんよう」に、「〜だ」と話すと「〜です」に変換されるはず

- 今回の文字列変換関数は単純なので、言葉に含まれる「だ」の全てが「です」になります

  - 例えば「だんだん〜」→「ですんですん〜」

- 丁寧語変換をちゃんと実装するには、語尾の「だ」だけを「です」に変換したり様々な工夫が要ります. それを行うのが次のセクション `4-4` で、「正規表現」という文法や、変換しない語をいったん「ダミー文字列」にして後で戻す等、込み入った処理をします. それはひとまず割愛し（次章以降の、カメラを使って画像処理や物体検知をするのを早めに体験してもらうため）、希望があれば後で実施します

<br>

### 4-5. 繰り返し変換できるようにしよう

- Chapter 4の最後のセクション `4-5`（p.134〜）で登場する繰り返し処理を行います

- 新しいセルに以下のコードを書きます

  ```Python
  # 2つの関数を繰り返し呼び出し、「プログラム終了」と言ったら終わる
  # 本 4-5-1 (p.134) の簡略版

  while(True):
    text = mic_to_recognize(0.01, 2) # 無音判定する音量, 秒数
    if text == 'プログラム終了':
      print('終了しました')
      break
    if text:
      print(f'音声認識結果「{text}」')
      print(f'丁寧語変換結果「{tamego_to_teineigo(text)}」')
  ```

- 実行すると 🎤 と「録音終了」が互い違いに表示され、🎤 表示の間に何か話すと音声認識・丁寧語変換結果が表示される状態が続きます

- 🎤 表示の間に「プログラム終了」と話すと終わります

- 実行例は下記のようになります

  ```
  録音終了
  音声認識結果「あ」
  丁寧語変換結果「あ」
  音声認識結果「こんにちは」
  丁寧語変換結果「ごきげんよう」
  音声認識結果「だんだん暖かくなる」
  丁寧語変換結果「ですんですん暖かくなる」
  終了しました
  ```

- 今回は僅かな文字列変換をしただけですが、音声認識した言葉に対し何らかリアクションを生成して返すようにすれば自動チャットになります. 本の `4-5-2` (p.136〜) がその例です. さらに回答生成をAIで行い、一連のやり取りを記憶して回答に反映させれば「生成AIによるチャットエージェント」そのものです. 最新の技術も、根本的な仕組みは意外に単純と言えるかもしれません

<br>

### 学習会独自のお手本コード

- 以上で作ったセルの全ては、このリポジトリにある [chapter-4/colab-chapter-4.ipynb](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-4/colab-chapter-4.ipynb) にあります

- 個別の関数も、同じディレクトリの下記それぞれにあります

  - `record_auto_stop.py`

  - `mic_to_recognize.py`

  - `tamego_to_teineigo.py`

- 動作確認環境

  - OS : `macOS 26.3`

  - Webブラウザ : `Firefox 148.0` , `Chrome 145.0.7632.160`

<br>

---
