## Colabで本のChapter 5を動かす (2)

### 概要

- 学習会独自の&thinsp;2&thinsp;つの関数を使い、Colabで動画の再生、撮影・保存、編集をする

- 本のように&thinsp;1&thinsp;枚&thinsp;1&thinsp;枚の静止画から生成した動画を&thinsp;Colab&thinsp;で再生する方法が判明（第11回の宿題）

  - 関数 play_video

  - p.172〜の動画編集も&thinsp;1&thinsp;枚&thinsp;1&thinsp;枚の静止画に処理を加えて動画にしており、それを&thinsp;Colab&thinsp;で再生できる

- そもそも本のように&thinsp;1&thinsp;枚&thinsp;1&thinsp;枚の静止画をカメラで撮って動画を生成するのは&thinsp;Colab&thinsp;で厳しく、別の方法でカメラから動画を直に出力する

  - 関数 VideoWriter（本の `cv2.VideoWriter` の代替）

  - 第11回の最後に紹介したが、その後改良したので改めて使ってみる

    - 以前は&thinsp;Colab&thinsp;で再生できる形式への変換処理を含み、遅かった

  - この関数で、Chapter 6&thinsp;で行う「動画からの物体検出」もしやすくなる

<br>

### まず本と同じ方法で動画 `movie.mp4` を作る

- 手順は&thinsp;[<ins>前の解説&thinsp;の&thinsp;5-2</ins>](./colab-chapter-5-readme.md#5-2-%E5%8B%95%E7%94%BB%E3%82%92%E6%92%AE%E5%BD%B1%E3%81%97%E3%82%88%E3%81%86p149)&thinsp;を参照

<br>

### 独自関数 `play_video` を試す

- セルを追加

- リポジトリにある [`play_video.py`](./play_video.py) を開き、右上にある&thinsp;Raw&thinsp;の右隣のアイコンを押してクリップボードにコピー

  <img width="256" src="https://github.com/user-attachments/assets/14c9322d-b2f6-4f37-ad0d-71cd18ab3eea" />

- セルにクリップボードを貼り付け実行、エラーが出ないのを確認

- もう一つセルを追加し以下の&thinsp;1&thinsp;行を入力、実行して動画が再生されれば&thinsp;OK

  ```Python
  play_video("movie.mp4", 320)
  ```

  - 第&thinsp;2&thinsp;引数は再生時の縦サイズ。画面の大きさ等に合わせて任意に変更可

<br>

### 学習会独自の関数 `VideoWriter` を使う

- [<ins>前の解説</ins>](./colab-chapter-5-readme.md#%E6%9C%AC%E3%81%A8%E9%81%95%E3%81%86%E6%96%B9%E6%B3%95%E3%81%A7%E5%8B%95%E7%94%BB%E3%82%92pc%E3%82%AB%E3%83%A1%E3%83%A9colab%E3%81%A7%E6%92%AE%E3%82%8B)&thinsp;のおさらい。関数は最新版に更新する

- セルを追加

- リポジトリにある [`VideoWriter.py`](./VideoWriter.py) を開き、前項と同様にコピーして実行確認

- もう一つセルを追加し以下のコードを入力

  ```Python
  frame_rate = 30
  duration = 10
  out = VideoWriter('movie.mp4', duration, frame_rate, (640, 480))
  ```

  - `(640, 480)` は撮影する動画の横サイズ, 縦サイズ

- セルを実行。カメラ使用が未許可なら&thinsp;[<ins>前の解説&thinsp;の&thinsp;5-1</ins>](./colab-chapter-5-readme.md#5-1-pc%E3%81%AE%E3%82%AB%E3%83%A1%E3%83%A9%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86p142)&thinsp;と同様に確認ダイアログ2つで許可し再実行

- 正常終了すると&thinsp;Colab&thinsp;のファイルに動画&thinsp;movie.mp4&thinsp;が保存されているはず

- 以上で、本のコード `5-2-2` (p.151) と同じ動作になる

<br>

### 保存した動画を&thinsp;Colab&thinsp;で再生

- 前々項のセル（以下の&thinsp;1&thinsp;行だけ）を再実行すると、いま撮影した動画が再生されるはず

  ```Python
  play_video("movie.mp4", 320)
  ```

  - 第&thinsp;2&thinsp;引数は再生時の縦サイズ。画面の大きさ等に合わせて任意に変更可

<br>

### 動画撮影〜保存〜再生を一度に

- セルを追加し以下のコードを入力し実行

  ```Python
  out_file = "movie.mp4"
  duration = 10
  frame_rate = 30

  if VideoWriter(out_file, duration, frame_rate, (640, 480)):
    play_video(out_file, 320)
  ```

  - `(640, 480)` は動画のサイズ、最終行の `320` は再生時の縦サイズ。いずれも任意に変更可

- 2&thinsp;つの関数を使うことで、わずかな行数で動画撮影〜保存〜再生ができる

<br>

### 本 p.172〜173 と同様に動画の色変換・ぼかしを行い、自動再生

- セルを追加、本のコード `5-5-1` を元に以下修正

  - 動画ファイル名を変更

  - 本で省略されている既出部分を、これまでの箇所から持ってくる

  - 色変換設定を自分の好みに

  - 最後に動画再生を追加

- 自力でできそうな人は挑戦を、難しければ下記の完成例を入力

  ```Python
  import cv2
  import numpy as np

  def apply_color_tone(img):
    """画像に色効果を適用する関数"""

    # セピア以外の変換の例 本p.166 ⑥全体的に明るくする
    filter = np.array([
      [3, 0, 0],
      [0, 3, 0],
      [0, 0, 3]
    ])
    applied_img = cv2.transform(img, filter)

    # 値を0〜255の範囲に変更
    applied_img = np.clip(applied_img, 0, 255).astype(np.uint8)

    return applied_img

  def apply_blur(img):
    """画像全体にぼかし効果を追加する関数"""
    kernel = (15, 15)
    return cv2.GaussianBlur(img, kernel, 0)

  # 動画ファイルの読み込み
  cap = cv2.VideoCapture("movie.mp4")

  # フレームレートの取得
  frame_rate = cap.get(cv2.CAP_PROP_FPS)

  # 注：本の55行目 interval はどこからも呼ばれず不要

  # 動画の幅と高さを取得
  w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  # 動画保存条件
  fourcc = cv2.VideoWriter_fourcc(*"mp4v")
  out = cv2.VideoWriter("movie_1_edited.mp4", fourcc, frame_rate, (w, h))

  # 画像処理
  while cap.isOpened():
    ret, img = cap.read()
    if not ret:
      break
    applied_img = apply_color_tone(img)
    out.write(apply_blur(applied_img))

  # ファイルの解放
  cap.release()
  out.release()

  play_video("movie_1_edited.mp4", 240)
  ```

<br>

- 実行して動画の色変換とぼかしがされていれば&thinsp;OK

- 元動画がぼやけていると、ぼかし効果は分かりづらいかも

- p.175 `5-5-2` は、ぼかし処理をエッジ検出に差し替えるだけ。こちらは各自で挑戦を

<br>

### Chapter 5 + 独自関数の総まとめ

- p.175 `5-5-2` を発展させ、既存動画でなくカメラで撮影した動画を編集し、最後に自動再生する

- 自力でできそうな人は挑戦を、難しければ下記の完成例を入力して実行

  ```Python
  from IPython.display import HTML
  from base64 import b64encode
  import cv2
  import numpy as np

  def apply_color_tone(img):
    filter = np.array([
      [5, 0, 0],
      [0, 5, 0],
      [0, 0, 5]
    ])
    applied_img = cv2.transform(img, filter)

    # 値を0〜255の範囲に変更
    return np.clip(applied_img, 0, 255).astype(np.uint8)

  def apply_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # エッジを太くする
    kernel = np.ones((3, 3), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)

    # エッジを黒色で描画
    img[edges_dilated == 255] = (0, 0, 0)

    return img

  # PCカメラから動画ファイルを保存し読み込み
  frame_rate = 30
  duration = 10
  VideoWriter("movie_3.mp4", duration, frame_rate, (640, 480))
  cap = cv2.VideoCapture("movie_3.mp4")

  # フレームレートの取得
  frame_rate = cap.get(cv2.CAP_PROP_FPS)
  # 動画の幅と高さを取得
  w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  # 編集した動画の保存条件
  fourcc = cv2.VideoWriter_fourcc(*"mp4v")
  out = cv2.VideoWriter("movie_3_edited.mp4", fourcc, frame_rate, (w, h))

  # 動画編集
  while cap.isOpened():
    ret, img = cap.read()
    if not ret:
      break

    # 画像処理を実行
    applied_image = apply_color_tone(img)
    applied_image = apply_edges(applied_image)
    out.write(applied_image)

  # ファイルの解放
  cap.release()
  out.release()

  play_video("movie_3_edited.mp4", 240)
  ```
<br>

## 全体のソースコード

- [<ins>前の解説</ins>](./colab-chapter-5-readme.md)&thinsp;の内容も含め、すべて [`colab-chapter-5.ipynb`](./colab-chapter-5.ipynb) に収録

- 動作確認済&thinsp;Web&thinsp;ブラウザ（&thinsp;2026&thinsp;年&thinsp;6&thinsp;月）

  - Chrome 148.0

  - Firefox 151.0

<br>

---
