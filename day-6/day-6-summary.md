## 第6回 summary

### 概要
- 2026.2.13 at 13:30〜14:30 オンライン

- 参加者数 5（主催 1, 全体参加 3, 部分参加 1）

- 録画あり（120日有効）

### 内容

- 報告：このリポジトリをpublicにした件

  > 予定していたが割愛（未知の参加者がいなかったため）

<br>

- (1) Chapter 2 までの進捗確認・サポート・質疑応答

  - Chapter 2 まで終わった人数：3

  - 嵌まりがちな所：インデント

    - 誤ったインデント（空白）に赤い波線が出る。それを消せば良い場合が多い

  - 質問 1：変数を文字列に埋め込む場合、数値など「文字でない変数」もそのまま埋め込んでよい？

    - 基本はOK。自動的に文字に変換される。変換後が予想できない変数（割り切れない数など）は注意が必要

      ```Python
      num_a = 1
      print(f'num_a={num_a}') # 出力：num_a=1

      num_b = 1/3
      print(f'num_b={num_b}') # 出力：num_b=0.3333333333333333

      list = [1,2,3]
      print(f'list={list}') # 出力：list=[1, 2, 3] カンマの後に自動的に空白が入る
      ```

  - 質問 2：本 p.26 の構文 `for 変数 in range(繰り返す回数)` は一つの構文？

    - そうではなく `for 変数 in 配列` が構文。`range(...)` は配列の一例

    - この構文は配列の要素一つずつを変数に入れてループする。インデックス（添字）は登場しない

    - 本にある `for i in ...` の `i` は単なる変数で、添字ではない（紛わしい）

    - 添字も一緒にループさせる場合は `for 添字, 変数 in enumerate(配列)`

      ```Python
      for index, value in enumerate(["a", "b", "c"]):
        print(index, value)

      """
      出力結果
      0 a
      1 b
      2 c
      """
      ```

  - 質問 3：PythonのWebフレームワーク `NiceGUI` でDBを使える？（前回の後に寄せられた質問）

      - Yes/Noで言えばYes。ただしNiceGUIにDB用の特別な機能はなく、何らかのDBライブラリを使ってデータを読み込み、それをNiceGUIに持っていく。例えばMySQLなら ↓ のようなイメージ

        ```Python
        import mysql.connector
        from nicegui import ui

        # DBへ接続
        db = mysql.connector.connect(
            host="****",
            user="****",
            password="****",
            database="****"
        )

        # DBにクエリしてデータ取得
        cursor = db.cursor()
        query = "SELECT 列名, 列名, ... FROM テーブル;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # 取得したデータをNiceGUIの表などに入れる方法あるはず、詳細は未調査
        # 参考 https://github.com/zauberzeug/nicegui/discussions/1868
        ui.table( ... )

        # DBから切断
        cursor.close()
        db.close()

        # NiceGUIで画面表示
        ui.run()
        ```

      - より進んだ例

        https://github.com/zauberzeug/nicegui/blob/main/examples/sqlite_database/main.py

        `Tortoise ORM` という、SQLを使わないDBライブラリを用いて `SQLite` のデータを操作

      - 引き続き調査中、進展したらリポジトリトップのREADMEに書きます

<br>

- (2) Chapter 3 の初回

  - 参加者の画面を共有してもらい、資料[（Colabで動かす方法）](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3-readme.md)を説明、作業開始

  - マイク録音用の独自関数 `record.py` を新しいセルに準備

  - この関数の最初のテスト[（3-2. マイクで音声を録音しよう）]()が、ブラウザによっては失敗することが判明

    - 具体的にはGoogle ChromeだとNG、FirefoxならOK

    - OSによる違いはなかった

    - ここで時間になり続きは次回とした

  - その後の参加者の調査：Chromeは `webm` 形式の音声を返すが、それを処理するPythonライブラリの `soundfile` が使う `libsndfile` というCライブラリが対応していない

  - `record.py` は学習会終了後に修正され（ブラウザの音声を `wav` 形式に変換）、Chromeでも動くようになった

<br>

- (3) クロージング

  - 次回の日時：

    - 都合により2週間後（2026.2.27 金）13時30分〜14時30分

  - 次回以降の進め方について

    - 各自の進度に差が出てきたので、もくもく会＋必要に応じて説明・サポートのようになるかも

<br>

---
