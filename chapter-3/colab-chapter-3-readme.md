## Colabで本のChapter 3を動かす

### 本の環境（ローカルのJupyter Notebook）とColabでの違い

- ライブラリのインストール方法が違う

- ライブラリをインストールしてもマイクが認識されない

- プログラムを動かして何かしゃべっても、無音のままと同じ

<br>

### ColabでChapter 3に取り組む準備

- p.82〜89で作る関数 `record` を、独自に作成した関数に置き換える。具体的には以下の手順で

- 新しいセルを作る

- このリポジトリにある [record.py](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record.py) を開き、右上にある `Raw` の右隣のアイコンを押してクリップボードにコピーし、セルに貼り付け

  <img width="256" src="https://github.com/user-attachments/assets/14c9322d-b2f6-4f37-ad0d-71cd18ab3eea" />

- セルを実行する。マイク使用許可を求める表示が出たら許可する（出ない時が多いが）。エラーなく終了し出力欄に「録音準備完了」と表示されたらOK

<br>

## Chapter 3 の各セクションの取り扱い

### 3-1. PCのマイクを探してみよう（p.70〜）

- セクション全体を割愛（ColabではPCのマイクを認識できないため）

- 意欲ある人は、本を読み同じ環境（Jupyter Notebook）を自分のPCに構築してチャレンジしてもよいです。行き詰まったら質問して下さい

- p.78に説明がある「辞書型」はChapter 4のp.116以降で再登場するので、その際に振り返る予定

<br>

### 3-2. マイクで音声を録音しよう（p.82〜）

- 次のようにして、セクション最後のp.90 `3-2-8` と同じ実行結果が得られます

- 関数 `record` を貼り付けたセルを、一度も実行してなければ実行（エラーが出なければOK）

- 新規セルに下記を入力（一部は `3-2-8` と同じ）

    ```Python
    # 計測条件を設定して録音関数を実行
    duration = 5
    waveform, sampling_rate = record(duration)
    print(len(waveform), waveform)
    ```

- セルを初めて実行すると、マイク使用許可の確認モーダル（その一）が出るので許可する。いったんエラーで終わるはず

  確認モーダルはおそらく画面中央に ↓ こんな感じで出る（日本語の場合あり）

  <img height="190" src="https://github.com/user-attachments/assets/f5fccddf-7e9a-4c16-b57e-ae31c867eccc" />


- もう一度実行すると、画面にマイク使用許可を求める表示（その二）が出るので許可する

  こちらの確認モーダルはおそらくブラウザの左上に ↓ こんな感じで出る（日本語の場合あり）

  <img height="190" src="https://github.com/user-attachments/assets/be4bb9c7-5f74-422a-8794-72e184e77e56" />


- 今度はエラーにならずColabの出力欄に「録音中」と5秒間表示された後、下記のような表示になればOK（数値は毎回異なる）

    ```
    録音終了
    240640 [ 0.00000000e+00  0.00000000e+00  0.00000000e+00 ...  3.35703604e-04
    9.15555284e-05 -6.10370190e-05]
    ```

- 初回実行をエラーにしない方法があるかもしれず、調査中（改善できたらこの資料に反映予定）

- 何度実行してもエラーになる場合はマイク、OS、ブラウザ等が関係していると思われ、個別にサポートします

<br>

### 3-3. 音声をグラフに描画しよう（p.91〜）

- 前項で作ったセルに以下の追加を行うことで、同じ実行結果が得られます

- P.91 `3-3-1` の行 `2` , `3` , `60〜73` をセルの先頭に挿入

- p.92 `3-3-2` の行 `90〜93` をセルの末尾に追加

    - 92行目 `np.arange` はアレンジ `arrange` と違い `r` が一つなので注意

- コードは次のようになるはず

    ```Python
    import numpy as np
    from matplotlib import pyplot as plt

    def graph_plot(x, y):
      """波形をグラフにする関数"""

      # グラフの設定
      fig, ax = plt.subplots()
      ax.set_xlabel('Time[s]')
      ax.set_ylabel('Amplitude')

      # データのプロット
      ax.plot(x, y)
      plt.show()
      plt.close()

    # 計測条件を設定して録音関数を実行
    duration = 5
    waveform, sampling_rate = record(duration)
    print(len(waveform), waveform)

    # グラフをプロットする
    dt = 1 / sampling_rate
    t = np.arange(0, len(waveform) * dt, dt)
    graph_plot(t, waveform)
    ```

- 実行し、5秒間「録音中」と表示された後、音声波形のグラフが表示されたらOK

- 何度か実行し、録音中に発声する内容によってグラフが変化するのを確認

<br>

### 3-4. 音声をファイルに保存して聴いてみよう（p.95〜）

- 前項で作ったセルに以下の追加を行うことで、同じ実行結果が得られます

- P.95〜96 `3-4-1` の行 `4` , `96〜98` をそれぞれ同様の場所に追加

  - 作業中の行番号が本と異なるので、追加する場所をコードの内容から判断して下さい

- 画面左側のフォルダアイコンを押してファイル一覧を表示してからセルを実行。終了後少し待つと音声ファイル `recorded.wav` が現れる

- ファイルを右クリックしてダウンロードできる。再生すると、自分が発した声が録音されているのが分かる

<br>

### 3-5. 音声を加工しよう（p.97〜）

- 前項で作ったセルに以下の追加を行うことで、同じ実行結果が得られます

- P.97 `3-5-1` の行 `5` , `101〜106` をそれぞれ同様の場所に追加

- 実行すると2つの音声ファイル `recorded.wav` , `pitch_shifted.wav` がある

- `pitch_shifted.wav` をダウンロードして再生すると、音声の変化が確認できる

- p.99〜100 `3-5-2` の行 `71〜72` , `96` , `109〜110` をそれぞれ同様の場所に追加

- 実行し、前項と同様のグラフに加えてp.101のようなグラフが表示されればOK

<br>

### 第7回用の独自追加 (1) 加工した音声を再生しよう

- 3-5. で作った音声加工のセルに以下2つ追加を行うと、加工した音声が自動再生されます

- (1) 冒頭のライブラリ読込ブロック（5〜9行あたり）に下記を追加

  ```Python
  from IPython.display import Audio, display
  ```

- (2) 最後に下記を追加

  ```Python
  # ボイスチェンジ音声を再生
  display(Audio(f'/content/pitch_shifted.wav', autoplay=True))
  ```

- 最初の実行時はグラフ描画に時間がかかるかもしれません。その後に音声が再生されます

- デフォルトの録音時間は5秒ですが、長くしたければ26行目あたり `duration` の値を増やします。

- 録音時間を増やすとグラフ描画が重くなり、音声再生までの待ち時間が長くなります。それを避けるには、2箇所あるグラフ描画の行 `graph_plot(...` をコメントアウトします（32・46行目あたり）

<br>

### 第7回用の独自追加 (2) より便利な関数 `record_auto_stop` を使おう

- これまで用いてきた独自の関数 `record.py` を改良した関数 `record_auto_stop.py` を作りました。改良点は以下二つです

  - マイクが無音状態を検知したら自動で録音を止める

    - これまで録音時間は関数内の `duration` で設定していた → 新関数を使えばマイクに向かって話す間ずっと録音され、発話を終えれば自動で録音が止まる

  - マイク使用を許可する前のエラー表示をなくし、ガイダンスを表示

    - 詳細は、後述するテスト時の流れで説明

<br>

- 新関数を使う準備

  - 新しいセルを作る

  - このリポジトリにある [record_auto_stop.py](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record_auto_stop.py) を開き、右上にある `Raw` の右隣のアイコンを押してクリップボードにコピーし、セルに貼り付け

    <img width="256" src="https://github.com/user-attachments/assets/14c9322d-b2f6-4f37-ad0d-71cd18ab3eea" />

  - セルを実行。エラーなく出力欄に「録音準備完了」と表示されたら準備完了

<br>

- 新関数の利用例 ①

  - 新しいセルを作り、以下のコードを入力する（コメントは省いても可）

    ```Python
    from IPython.display import Audio

    SILENCE_RMS = 0.01 # 無音レベルの指標（環境音が大きければ増やす）
    SILENCE_SEC = 2    # 秒. 無音がこの時間続いたら録音終了

    try:
      record_auto_stop
    except NameError:
      print('先にrecord_auto_stop関数のセルの実行が必要です')
    else:
      # 実行後、無音になるまで録音し再生
      waveform, sampling_rate = record_auto_stop(SILENCE_RMS, SILENCE_SEC)

      if len(waveform) > 0:
        display(Audio(data=waveform, rate=sampling_rate, autoplay=True))
    ```

  - セルを実行する。事前に `record_auto_stop` 関数のセルが未実行の場合、出力欄に「先にrecord_auto_stop関数のセルの実行が必要です」と表示されて終わる

    - TODO：画像を挿入

  - 開いたノートブックで初めてマイクを使う時は、ブラウザ画面の中央にマイク使用を求める表示が出る。その際は、新関数が出力欄に説明を表示して終了するので、再度セルを実行し直す（下図参照）

    - TODO：画像を挿入

  - 上とは別のマイク使用を求める表示が出る場合がある（下図参照）。その際はユーザが可否を選ぶまで実行が中断される。

    - TODO：画像を挿入

  - マイク使用の可否が選択されたら、マイクが使える時は録音を開始し、使えない時は出力欄に「マイクを使用できません」と表示して終わる

    - TODO：画像を挿入

  - 録音が始まったら何か発話してみる。録音中は出力欄に1秒毎にステータスが表示される。発話を終えたら自動的に録音が終わり、話した音声が再生される

    - TODO：画像を挿入

  - 周囲の環境音が大きい場合、発話を止めてもプログラムが無音と認識できず録音が止まらない。その際はセルに入力した3行目 `SILENCE_RMS` の値を適当に大きくし調整する

<br>

- 新関数の利用例 ② 録音した声をボイスチェンジして自動再生

  - 前項のセルを複製し、最後の行を消して以下のコードを入力する（コメントは省いても可）

    ```Python
    # ボイスチェンジ
    n_steps = 8
    waveform_shifted = librosa.effects.pitch_shift(
      waveform, sr=sampling_rate, n_steps=n_steps
    )

    # ボイスチェンジ音声を再生
    display(Audio(data=waveform_shifted, rate=sampling_rate, autoplay=True))
    ```

  - 実行手順は前項と同じ。正常に実行され何か発話すると、高い声に変換して再生される。

<br>

### 学習会独自のお手本コード

- 以上で作ったセルの全ては、このリポジトリにある [chapter_3.ipynb](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3.ipynb) にあります。

  - 動作確認環境

    - OS : `macOS 15.7.3` , `macOS 26.3`

    - Webブラウザ : `Firefox 147.0.1` , `Chrome 144.0.7559.133`

- chapter_3.ipynb には本 p.102の「周波数分析」を行うセルもあります。本で紹介されている著者ブログを参考に作成しました。またColabでマイクを使うため試したものの結局動かなかったコードも、記録として収録しました

<br>

---
