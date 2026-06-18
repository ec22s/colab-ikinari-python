# colab-ikinari-python
Google Colaboratory（Colab）で本『いきなりプログラミング Python』に取り組む初心者向け学習会の資料

- 現状、所属組織内のクローズドな学習会です

- 参加希望の方は[プロフィール](//github.com/ec22s)のメールアドレスへご連絡下さい

<br>

## 次回予定 & 開催記録

- [第14回 (日程調整中)](#%E7%AC%AC14%E5%9B%9E%E4%BA%88%E5%AE%9A%E6%97%A5%E7%A8%8B%E8%AA%BF%E6%95%B4%E4%B8%AD)

- [第13回 (2026.6.5)](day-13/day-13-summary.md)　Chapter 5（Colab&thinsp;で撮影した動画に色変換・ぼかし・エッジ抽出をして再生）

- [第12回 (2026.5.22)](day-12/day-12-summary.md)　Chapter 5（独自の関数を追加し、Colab&thinsp;での動画撮影〜保存〜再生を簡単に行う）

- [第11回 (2026.4.28)](day-11/day-11-summary.md)　Chapter 5（独自のColab用関数を使い、本と同じ撮影・録画・画像処理を実施）

- [第10回 (2026.4.17)](day-10/day-10-summary.md)　参加者の進度別に作業：Chapter 4（音声認識）, Chapter 5（画像処理）

- [第9回 (2026.3.27)](day-9/day-9-summary.md)　Chapter 3（未着手の参加者サポート）, Chapter 4（音声認識）初回

- [第8回 (2026.3.13)](day-8/day-8-summary.md)　Chapter 3 続き（未完の参加者サポート）, Chapter 4（音声認識）準備まで

- [第7回 (2026.2.27)](day-7/day-7-summary.md)　Chapter 3 続き（独自に準備したColab用関数を使い、本と同じ機能＋αを実施）

- [第6回 (2026.2.13)](day-6/day-6-summary.md)　Chapter 2 までの進捗確認・質問・サポート、Chapter 3（声変わり機）初回

- [第5回 (2026.2.6)](day-5/day-5-summary.md)　Chapter 2 進捗確認、質疑応答、Chapter 1と2をWebアプリ化した例の紹介

- [第4回 (2026.1.30)](day-4/day-4-summary.md)　本 Chapter 2（p.38〜66）の説明、各自作業

- [第3回 (2026.1.23)](day-3/day-3-summary.md)　本 `1ｰ3` の質疑応答（文字列の部分一致）、ゲームの改良

- [第2回 (2026.1.16)](day-2/day-2-summary.md)　本 `1ｰ3`（p.23〜36）最初のアプリ（数当てられゲーム）

- [第1回 (2026.1.9)](day-1/day-1-summary.md)　本の説明、GitHubとColabの設定、最初のプログラム（Hello World）

<br>

## 本『いきなりプログラミング Python』
- wat 著

- 発売 2024.6.25

- 出版社（翔泳社）のページ https://www.shoeisha.co.jp/book/detail/9784798184869

- 著者のサポートページ https://watlab-blog.com/ikinari-python-book/

<br>

## 学習会の趣旨
- 何より本が良い

  - まず作って楽しむ方向がプログラミング入門に最適

  - レイアウトが読みやすく図が多い

  - 正規表現やOpenCVなど中級者にも有用

  - 一部の内容は初心者にやや難しいが、後々読み返して理解を試みると役に立つ

<br>

- Colabで動かすオリジナリティと良さ

  - 本の内容だけ扱うなら学習会をするまでもない（自習と個別サポートで十分）

  - Chapter 3以降は本のままだとColabで動かず、学習会オリジナルのお手本が必要

    → 学習会独自の&thinsp;[Colab&thinsp;で本の&thinsp;Chapter 3&thinsp;を動かす](chapter-3/colab-chapter-3-readme.md)&thinsp;,&thinsp;[Chapter 4&thinsp;を動かす](chapter-4/colab-chapter-4-readme.md)&thinsp;,&thinsp;[Chapter 5&thinsp;を動かす](chapter-5/colab-chapter-5-readme.md)&thinsp;コードを作った

    → Chapter 5 以降もColab用の改変を準備済み、後日このリポジトリに掲載予定

  - ローカル環境よりColabでやる方がシェアしやすく発展性がある

  - Colabに慣れれば他のことにも使える（データ分析や機械学習等）

<br>

- GitHubにも慣れる（資料、学習会オリジナルのコードはここに集約）

  - ソースコードの共有ツールとして事実上デファクト

  - 仕事で開発するなら必須、早いうちに慣れるとよい（情報を見るだけでも）

<br>

## 過去回のサマリから

- プログラミングとタイピング

  - タッチタイプ（キーボードを見ずホームポジションから打つ）は必須

    - そこそこ速く、できるだけ間違えず、疲れを少なく打つ

  - アルファベット以外もたくさん打つ（カーソル、数字、記号、ショートカット等）

    - これもなるべくキーボードを見ないで打てるとよい

  - 頻度の多いマウス（ポインタ）操作は、ショートカットキーを調べて覚える

<br>

- コードを書く時の補足

  - コードのうちコメント（`#` で始まる行）は時間節約のため入力しなくても可

  - コードに問題あれば赤字や波下線で画面に示され、修正するとそれらの表示が消える

  - コードに問題ある状態で実行すると途中で止まり、エラー情報が結果表示欄に出る

    - エラー情報の最下部に直接の原因が表示されることが多い

  - インデント／スペースは本どおりでなくとも<ins>コードが問題なく動けば</ins>可

    - 例えば `=` の前後のスペースを省く等

    - 正統なインデント／スペースの入れ方をしたい人は本のコードどおりに

  - プログラム実行アイコン（黒丸に右向き三角）を押すと黒丸の中が四角に変わる。再び押すと中止できるが、その際多くのエラー情報が表示される。正常な挙動なので気にしない

<br>

- Colab用の便利な設定：行番号とインデント（字下げ）の縦線を表示

  - 右上の歯車アイコンで設定画面を開く → 左側でエディタをクリック → 少し下へスクロール → 行番号とインデントガイトを各々チェック

  - Pythonはインデントを正しく揃えないとエラーになる。確認のため縦線があると良い

<br>

- Colab&thinsp;の入力補完を活用しよう

  - 候補の選択はキーボードの上下カーソルで、確定はタブでできる

  - 候補が一つになったらタブだけで確定できる

<br>

- Colab&thinsp;のセルにタイトルを付けると便利

  - セルの中で `#@title 〜` を入力すると 〜 部分がタイトルになる

  - \# と @ の間に空白を入れても可、この方が見やすいかも

    ```Python
    # @title セルのタイトル<br>改行もできる
    ```

  - タイトルがあるとセルの折り畳み・展開ができる

  - タイトル内で&thinsp;HTML&thinsp;タグが使える（BR&thinsp;で改行等）

  - Python&thinsp;の文法上は単なるコメント、処理に影響しない

<br>

## 第14回予定（日程調整中）

- オンライン（録画忘れずに）

- (1) 前回の振り返り → [<ins>サマリ</ins>](day-13/day-13-summary.md)&thinsp;参照

- (2) 作業をしやすくする方法紹介

  1．[<ins>学習会用の独自関数・クラスを簡単に使う</ins>](util/load-py.md)

  2．[<ins>コードの右側に完成形の&thinsp;ipynb&thinsp;ファイルを表示</ins>](util/show-ipynb.md)

  3．[<ins>コードの右側に&thinsp;Markdown&thinsp;の解説を表示</ins>](util/load-markdown.md)

  4．完成形の&thinsp;ipynb&thinsp;ファイルを&thinsp;GitHub&thinsp;から新しいノートブックとして読み込む（画面で説明します。資料は後日追加予定）

- (3) 参加者の画面を共有してもらい、一緒に作業

  - 前回の続き（Chapter 5&thinsp;の最後）： (2) 4. の便利な方法で

    - GitHub&thinsp;リポジトリ：`ec22s/colab-ikinari-python`

    - ipynb&thinsp;ファイル：`chapter-5/prepare-chapter-5.ipynb`

    - GitHub&thinsp;から上手く読み込めない場合は手動で新しいノートブックを作り&thinsp;(2) 2. の方法で

      ```python
      # @title chapter-5.ipynbをColabに読み込む

      import requests

      ipynb_path = "chapter-5/colab-chapter-5.ipynb"

      branch = "https://github.com/ec22s/colab-ikinari-python/raw/refs/heads/main"
      func_path = "util/show_ipynb.py"
      exec(requests.get(f"{branch}/{func_path}", allow_redirects=True).content)
      show_ipynb(f"{branch}/{ipynb_path}")
      ```

    - 完成形のコードを右側に複製して表示

    - 左側にセルを3つ追加し、右側から以下3つをコピーして順番に実行、結果を確認

      - (2) Chapter 5用の独自クラス・関数をまとめて準備

      - (18) Chapter 5 最後：動画撮影〜色変換とエッジ強調〜自動再生をまとめて

      - 補足：独自関数 VideoWriter の最新版で、動画のフレームレートが正常になった

  - Chapter 6&thinsp;の初回

    - 上と同様、完成形&thinsp;ipynb&thinsp;ファイルを新しいノートブックとして読み込む。対象のファイルだけ変更

      - ipynb&thinsp;ファイル：`chapter-6/prepare-chapter-6-1.ipynb`

    - GitHub&thinsp;から上手く読み込めない場合は手動で新しいノートブックを作り&thinsp;(2) 2. の方法で

      ```
      ipynb_path = "chapter-6/colab-chapter-6-1.ipynb"
      ```

    - 完成形のコードを右側に複製して表示

    - 右側の各セルについて

      - 内容を確認

      - 左側にセルを追加して必要な部分を入力

      - 実行して結果を確認

      - エラーや不明点などあれば質問

  - 画面を共有しない人は

    - 同じ箇所を、画面・リポジトリの解説・本を適宜見ながら自習

    - または、以前の内容でやり残しがあればその自習等

- (4) クロージング

  - 次回の日時・内容・進め方について

    - そろそろ終わりが見えてきたかも？

  - その他あれば

<br>

---
