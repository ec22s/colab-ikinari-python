## 第5回 summary

### 概要
- 2026.2.6 at 11:00〜12:00 オンライン

- 参加者数 6（主催 1, 全体参加 5）

- 録画あり（120日有効）

<br>

### 内容

- (1) Chapter 2 のアプリ（Hit & Blow ゲーム）各自の進捗確認、サポート、質疑応答

  - 作業中の人を画面を見て、切り良い所までサポート

  - Colabの入力補完を活用しよう

    - 候補の選択はキーボードの上下カーソルで、確定はタブでできる

    - 候補が一つになったらタブだけで確定できる

  - 考察：この本は「楽しく」が趣旨なのでよいが、本来はエラー回避処理を入れるべき所が複数ある

    - 最終形の11〜12行目（関数 `check_hit_and_blow` の中）

      ```Python
      for i in range(len(secret)): # secretの要素の数だけ、iに添字が入る
        if secret[i] == guess[i]:  # guessの要素数がsecretより少なければエラー
      ```

    - 最終形の33行目あたり、整数以外が入力されたら `int` 関数がエラーを起こす

      ```Python
      n = int(input('何桁の数字でゲームをしますか？ (1〜9)：'))
      ```

    - 最終形の53〜54行目あたり、こちらも同様

      ```Python
      for char in guess_number:      # guess_numberを1字ずつ区切って取り出し
        guess_list.append(int(char)) # その字が整数以外だとエラー
      ```

<br>

- (2) Colabで作ったアプリを「普通のWebアプリ」にするには

  - 食事に例えると Colab → 自炊、普通のWebアプリ → レストラン

    - Colab：自分で作り、自分で食べる（アプリを使う）

    - 普通のWebアプリ：誰でも、入って注文すれば（ブラウザを開けば）食べられる

  - Colabの出力欄だけ別ページにして一般に公開できたら一応Webアプリと言えるが

    - Colabにはその機能がない

    - 外部サービスを用いグラフ等をWebアプリ化する方法はあるが、汎用的な用途には不向き

  - Colabの位置づけ

    - Pythonを使い簡単にプログラミング入門ができる

    - データ分析が目標なら、単独で十分使える

    - Webアプリ作成が目標なら、<ins>主な流れまでは</ins>作れる

      - その後何をすれば完成するのか → 次で説明

<br>

- (3) Chapter 1, 2 のゲームを簡単なWebアプリにしてみた

  - URL：https://nicegui-ikinari-python.onrender.com

    - 黒い背景の画面が出たら、起動に約1分待つ（理由は後述の&thinsp;★&thinsp;）


  - Webアプリ化に最低限必要な要素は

    - バックエンド ≒ Webサーバソフト + アプリの内部処理をするプログラム

    - フロントエンド ≒ ユーザのWebブラウザで動く、UIを表示しバックエンドと連携するプログラム

    - ホスティング先 ≒ バックエンドを常時稼動させユーザを待ち受け、ユーザにフロントエンドを提供する、ネット上のコンピュータ

  - バックエンドとフロントエンドを分離する（別々のプログラムとする）のもよくある方法だが

    - Colabに書いたPythonプログラムは両者が一体

    - これを活かせるよう、Pythonでバックエンドとフロントエンド一体で書けると望ましい

    - 一からその仕組みを作るのは大変だが、`NiceGUI` という便利な「フレームワーク」がある

      - NiceGUI：https://nicegui.io

      - フレームワーク：Webアプリなど特定の種類のシステムを簡単に作れるプログラム群

  - ホスティング先：今回、無料枠でデモ程度には使えるクラウドサービス `Render` を利用

      - Render：https://render.com

      - いわゆる `PaaS` Platform as a Service、利用者はプログラムを用意するだけ

      - ★ 無料枠で15分アクセスがないと休止状態になり、次回起動に約1分かかる

  - Webアプリ単独のリポジトリ：https://github.com/ec22s/nicegui-ikinari-python

    - 現状まだprivate、見たい人は招待します

    - Chapter 3とそれ以降もWebアプリ化できたらpublicにする予定

  - 質問：NiceGUIでDBは使える？

    - おそらくYes、正確なところは調べて次回回答。[トップのREADME](https://github.com/ec22s/colab-ikinari-python)にも記載予定

  - 追記：NiceGUIと同様フロントエンド・バックエンド両方を書けるフレームワーク `Streamlit` の本

    - https://www.amazon.co.jp/dp/4295603511

    - https://www.amazon.co.jp/dp/4297147645

      - レビューにも「フロントエンド・バックエンド両方を書けて便利」とあり

    - NiceGUIは、Streamlitの「状態管理」が煩雑だとして後から生まれた

<br>

- (4) 相談：このリポジトリのpublic（誰でも見れる）化について

  - Chapter 3の準備で[学習会独自のコード](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3-readme.md)ができ、privateのままでは勿体ない

  - 今後、ColabとGitHubの連携の体験として各自のコードをアップロードしてもらう予定。publicの場合、コードをアップロードした参加者は `Contributors` の一覧に載る

  - そこから各自のプロフィールページを誰でも開けるが、支障ある人はコードのアップロードをスキップすればOK。またプロフィールページの表示項目をidと名前だけにすることもできる

  - README冒頭に「所属組織内のクローズドな学習会」と断っている。社外で参加希望者がいたら別途相談する

  - 以上を話し了承された → 学習会終了後publicにする予定

<br>

- (5) クロージング

  - 次回の日時：

    - 従来同様、1週間後 (2026.2.20 Fri) 13時30分〜14時30分

  - 次回の内容

    - 話す時間なかったが、Chapter 2の続きと、終わった人はChapter 3の自習など[（資料は準備済み）](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3-readme.md)

<br>

---
