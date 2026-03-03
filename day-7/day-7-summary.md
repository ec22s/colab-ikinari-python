## 第7回 summary

### 概要
- 2026.2.27 at 13:30〜14:30 オンライン

- 参加者数 4（講師 1, 全体参加 2, 部分参加 1）

- 録画あり（120日有効）

### 内容

- (1) 今日の進め方・内容について

  - Chapter 2 までが未了の人もいるが、相談の結果、今日は Chapter 3 に入った人が画面共有しながら作業を進め、他の人はそれを見て Chapter 3 を予習する回とした

  - 不参加の人も、今日の録画を見れば Chapter 3 を自習する際に役立つはず

- (2) Chapter 3 続き

  - 基本、こちらで作った解説 [(→ リンク)](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3-readme.md) に沿って作業

  - Colab用に作ったマイク録音用関数 [`record.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record.py) のセルを準備し直す（Chrome でも動くようになった）

  - `record.py` を使う以外は本と同じコードで一連の機能を実装してもらい、いずれも正常に機能した

    - 録音

    - グラフ描画

    - WAVファイル出力

    - ボイスチェンジ

  - 本にない独自の工夫を2点試してもらい、いずれも期待通り機能した

    - (1) ボイスチェンジした音声をColab上で再生

    - (2) より便利な関数 [`record_auto_stop.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record_auto_stop.py) を使う

      - `record.py` は録音時間をソースに記述しており柔軟性に欠けるが、`record_auto_stop.py` はマイクへ発話している間は録音し続け、無音になったら自動で録音を終える

      - Chanpter 4 でも使う想定で作成した（音声をテキスト認識させるのに便利）

  - 予定の実装・動作確認が全て終わった時にほぼ終了時間となった

  - `record.py` が前回 Chrome で動かなかった原因について質問があり、説明した

    - Webブラウザ上で動く Colab でマイクの音声をデータ化するため、ブラウザ上で動く JavaScript の `MediaRecorder` オブジェクトを使っている

    - `MediaRecorder` の本来の仕様は、データ化する音声のフォーマットを指定できるはずだが、現状その動作にならない

      - Firefoxでは `Ogg`、Chromeでは `WebM` というフォーマットの音声データしか得られない

      - ブラウザの実装が追いついていないのか、Colabの特殊性なのかは未調査

    - 前回、Pythonが音声データをJavaScriptから受け取る処理で `soundfile` というライブラリを用いていた。この内部のCライブラリが `WebM` に対応していないため、ChromeではエラーになりFirefoxでは問題なかった

    - 今回は別のライブラリを追加し、Pythonが音声データを受け取ったら自動的に `WAV` フォーマットに変換して `soundfile` に渡すよう修正して解決した

<br>

- (3) クロージング

  - 次回の日時・内容予定：

    - 都合により2週間後（2026.3.13 金）13時30分〜14時30分

    - Chapter 4 をColabで実行する準備をしておくが、それ以前を作業中の人も参加してOK（必要があれば説明・サポートを行う）

<br>

---
