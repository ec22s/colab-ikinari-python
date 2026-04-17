## 第9回 summary

### 概要
- 2026.3.27 at 13:30〜14:30 オンライン

- 参加者数 5（講師 1, 全体参加 4）

- 録画あり（120日有効）

<br>

### 内容

- (1) 今日の進め方・内容について

  - Chapter 3 未着手の人が画面共有しながら章の最初から作業を行い、他の人は Chapter 4 に独習で（&thinsp;[本リポジトリの解説](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-4/colab-chapter-4-readme.md)&thinsp;を見て）着手する回とした

  - 今日の録画が、Chapter 3 自習用に最も役立つと思われる

  - 最後の方で Chapter 4 の動作について質疑応答を行った

  - Chapter 4 に着手した人いずれも [`4-2`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-4/colab-chapter-4-readme.md#4-2-%E9%9F%B3%E5%A3%B0%E3%82%92%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%81%AB%E5%A4%89%E6%8F%9B%E3%81%97%E3%82%88%E3%81%86p109) が正常動作するところまで進んだ

<br>

- (2) Chapter 3 最初から

  - 基本、[本リポジトリの解説](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3-readme.md)&thinsp;に沿って作業

  - Colab用に作ったマイク録音用関数 [`record.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record.py) を使う. それ以外は本と同じコードで下記の機能を実装し、いずれも正常に機能した

    - 録音

    - グラフ描画

    - WAVファイル出力

    - ボイスチェンジ

  - 本にない＋αの1（ボイスチェンジした音声をColab上で再生）、2（より便利な関数 `record_auto_stop.py` を使う）も期待通り機能した

  - 時間あったので本 p.102 の周波数分析も本リポジトリのソース[（&thinsp;`colab-chapter-3.jpynb` の7番目のセル）](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3.ipynb)を元に試してもらい、期待通り機能した

  - マイク録音用関数 [`record.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record.py) でのJavaScriptソース埋め込みの概要を説明した

<br>

- (3) Chapter 4 質疑応答（学習会終了後の対応も含む）

  - 当初、「録音開始までは正常に動作するが、録音中に発話してもテキスト認識されない」現象が複数発生したが、どちらもマイク設定を変更することでテキスト認識されるようになった

    - チャットツールでもマイクを使用中で、環境が特殊だったかもしれない

    - 設定変更の詳細は各々の環境によるので省略

    - 問題の切り分けのため、録音した音声を再生できると良い

      - 終了後 [`record_auto_stop.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-4/record_auto_stop.py) 関数をそのように改良し、chapter 4のREADMEにも反映した

  - [本リポジトリの解説](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-4/colab-chapter-4-readme.md)&thinsp;の下記のようなコード修正記法について一部で誤解があり、説明した

    ```
    - return sf.read(buffer)
    + return buffer
    ```

    とあったら次のように理解する

      - `-` で始まる行は、`-` を除く `return sf.read(buffer)` という内容の行を修正する

      - 修正内容は、`+` で始まる行の `+` を除いた部分。ここでは `return buffer`

      - 従って `-` で始まる行と `+` で始まる行が1つずつ書かれていれば、全体の行数は増えず、ある1行を修正するだけ

<br>

- (4) クロージング

  - 次回の日時・内容予定：

    - 今回同様、2週間後（2026.4.10 金）13時30分〜14時30分 → その後変更あり

    - Chapter 5 も途中の `5-3` までColabで動かす解説が準備できており[（&thinsp;リンク↗&thinsp;）](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-5/colab-chapter-5-readme.md)、いずれ Chapter 5 の残りも解説を追加する予定 → その後次回までに完了した

<br>

---
