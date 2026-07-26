# colab-ikinari-python

2026年1月〜7月、Google Colaboratory（Colab）で本『いきなりプログラミング Python』に取り組んだ学習会の資料・独自ソース

<br>

## 自習用ひな型

- Chapter 1&thinsp;〜&thinsp;5：整理中

  - 整理前のものは、次々項「学習会の概要」にある各回の&thinsp;URL&thinsp;から閲覧可

- Chapter 6 (各リンクを開くと本リポジトリの&thinsp;ipynb&thinsp;が&thinsp;Colab&thinsp;で開かれます）

  - [その1](https://colab.research.google.com/github/ec22s/colab-ikinari-python/blob/main/base/base_chapter_6_1.ipynb)　[その2](https://colab.research.google.com/github/ec22s/colab-ikinari-python/blob/main/base/base_chapter_6_2.ipynb)　[その3](https://colab.research.google.com/github/ec22s/colab-ikinari-python/blob/main/base/base_chapter_6_3-4.ipynb)

<br>

## 学習会用に作った独自関数・クラス

- [`record_auto_stop.py`](chapter-4/record_auto_stop.py) Colab&thinsp;で&thinsp;PC&thinsp;のマイクから録音する関数 (Chapter 3・4&thinsp;で使用)

- [`ColabCap2.py`](util/ColabCap2.py) Colab&thinsp;で&thinsp;PC&thinsp;のカメラ画像を取得するクラス (Chapter 5・6&thinsp;で使用)

- [`VideoWriter.py`](chapter-5/VideoWriter.py) Colab&thinsp;で&thinsp;PC&thinsp;のカメラから動画を撮影・保存する関数 (Chapter 5&thinsp;で使用)

  - 本が使う&thinsp;OpenCV&thinsp;の&thinsp;VideoWriter&thinsp;メソッドの代用なので、スネークケースでなく同じ名前にした

- [`play_video.py`](chapter-5/play_video.py) Colab&thinsp;で動画を再生する関数 (Chapter 5&thinsp;で使用)

- [`colab_imshow.py`](util/colab_imshow.py) Colab&thinsp;で複数の画像を切り替えて表示する関数 (Chapter 6&thinsp;で使用)

  - Colab&thinsp;標準の関数&thinsp;cv2_imshow&thinsp;は不便なので作った

<br>

## 学習会の概要

- 組織内のクローズドなものとして実施

- 想定した対象者と学習会の位置づけ

  - プログラミング未経験者 → 最初のプログラミング体験として

  - 初心者・Python&thinsp;未経験者 → Python&thinsp;入門として

  - Colab&thinsp;や各種ライブラリの未経験者 → その入門として

- 各回の開催記録

  - [第18回 (2026.7.24)](day-18/day-18-summary.md)　Chapter 6 続き〜最後まで（動画から笑顔の人数をカウント、全員笑顔の時を記録）

  - [第17回 (2026.7.17)](day-17/day-17-summary.md)　Chapter 6 続き（前回の自習課題の確認、次回向け動画の準備〜人数カウントまで）

  - [第16回 (2026.7.10)](day-16/day-16-summary.md)　Chapter 6 続き（既存の動画を読み込んで物体検出, 人の数をカウント）

  - [第15回 (2026.6.25)](day-15/day-15-summary.md)　Chapter 6 初回（パッケージインストール, 動画撮影＆リアルタイム物体検出）

  - [第14回 (2026.6.18)](day-14/day-14-summary.md)　作業手順の改善、Chapter 5&thinsp;最後（動画撮影〜色変換・エッジ抽出して再生）

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

## 本『いきなりプログラミング Python』について
- wat 著

- 発売 2024.6.25

- 出版社（翔泳社）のページ https://www.shoeisha.co.jp/book/detail/9784798184869

- 著者のサポートページ https://watlab-blog.com/ikinari-python-book/

<br>

## 学習会の趣旨

### 何より本が良く、未経験者・初心者におすすめ

  - まず作って楽しむ方向がプログラミング入門に最適

  - レイアウトが読みやすく図が多い

  - 正規表現や&thinsp;OpenCV&thinsp;など中級者にも有用

  - 一部の内容は初心者にやや難しいが、後々読み返して理解を試みると役に立つ

<br>

### Colabで動かす利用とオリジナリティ

  - 本の内容だけ扱うなら学習会をするまでもない（自習と個別サポートで十分）

  - Chapter 3&thinsp;以降は本のままだとColabで動かず、学習会独自の&thinsp;+&thinsp;α&thinsp;が必要

    → オリジナルの関数・クラスを作り、Chapter 3&thinsp;以降も本と同様のことが&thinsp;Colab&thinsp;でできるようにした

    → 詳細は各章の&thinsp;readme&thinsp;やフォルダ内を参照

  - ローカル環境より&thinsp;Colab&thinsp;でやる方がシェアしやすく発展性がある

  - Colab&thinsp;に慣れれば他のことにも使える（データ分析や機械学習等）

<br>

### GitHubにも慣れる（資料、学習会オリジナルのコードはここに集約）

  - ソースコードの共有ツールとして事実上デファクト

  - 仕事で開発するなら必須、早いうちに慣れるとよい（情報を見るだけでも）

<br>

## 各回に共通のアドバイス（主に初心者向け）

### プログラミングとタイピング

  - タッチタイプ（キーボードを見ずホームポジションから打つ）は必須

    - そこそこ速く、できるだけ間違えず、疲れを少なく打つ

  - アルファベット以外もたくさん打つ（カーソル、数字、記号、ショートカット等）

    - これもなるべくキーボードを見ないで打てるとよい

  - 頻度の多いマウス（ポインタ）操作は、ショートカットキーを調べて覚える

  - 範囲選択はできるだけマウスを使わず、Shift&thinsp;+&thinsp;カーソルキーやダブル（トリプル）クリック等を活用する

<br>

### Colab でコードを書く時の補足

  - コードに問題あれば赤字や波下線で画面に示され、修正するとそれらの表示が消える

  - コードに問題ある状態で実行すると途中で止まり、エラー情報が結果表示欄に出る

    - エラー情報の最下部に直接の原因が表示されることが多い

  - プログラム実行アイコン（黒丸に右向き三角）を押すと黒丸の中が四角に変わる。再び押すと中止できるが、その際多くのエラー情報が表示される。正常な挙動なので気にしない

<br>

### Colab 用の便利な設定：行番号とインデント（字下げ）の縦線を表示

  - 右上の歯車アイコンで設定画面を開く → 左側でエディタをクリック → 少し下へスクロール → 行番号とインデントガイトを各々チェック

  - Pythonはインデントを正しく揃えないとエラーになる。確認のため縦線があると良い

<br>

### Colab の入力補完を活用しよう

  - 候補の選択はキーボードの上下カーソルで、確定はタブでできる

  - 候補が一つになったらタブだけで確定できる

<br>

### Colab のセルにタイトルを付けると便利

  - セルの中で `#@title 〜` を入力すると 〜 部分がタイトルになる

  - \# と @ の間に空白を入れても可、この方が見やすいかも

    ```Python
    # @title セルのタイトル<br>改行もできる
    ```

  - タイトルがあるとセルの折り畳み・展開ができる

  - タイトル内で&thinsp;HTML&thinsp;タグが使える（BR&thinsp;で改行等）

  - Python&thinsp;の文法上は単なるコメント、処理に影響しない

<br>

### このリポジトリにある&thinsp;ipynb&thinsp;ファイルを、Colab&thinsp;の新しいノートブックとして読み込む

  - 方法&thinsp;1：ブラウザで&thinsp;URL&thinsp;を直接指定

    - 読み込む&thinsp;ipynb&thinsp;の&thinsp;GitHub&thinsp;でのアドレスを調べる

      例：https://github.com/ec22s/colab-ikinari-python/blob/main/base/base_chapter_6_1.ipynb

    - アドレスのうち先頭の `https://github.com` を `https://colab.research.google.com/github` に変え、ブラウザで開く

      例：https://colab.research.google.com/github/ec22s/colab-ikinari-python/blob/main/base/base_chapter_6_1.ipynb

  - 方法&thinsp;2：Colab&thinsp;で「ノートブックを開く」メニューから

    - [<ins>Colab&thinsp;のトップ</ins>](https://colab.research.google.com)&thinsp;を開くか、Colab&thinsp;のファイルメニュー（左上）から選択

    - ノートブックを開く画面が出たら、タブ（左側）で&thinsp;GitHub&thinsp;を選択

      ⚠️ GitHub&thinsp;へのログインや&thinsp;Colab&thinsp;との連携を促すダイアログが出たら、何もせず閉じて右上の「プライベートリポジトリを含める」チェックを外す。このリポジトリはプライベートでないのでそれらは不要

    - GitHub&thinsp;を開く画面で、一番上の検索欄にこのリポジトリの情報 `ec22s/colab-ikinari-python` を入力し検索

    - ipynb&thinsp;ファイルのリストが出たら、対象のファイルを探してクリック

  - 読み込みまたは初回のセル実行前に警告が出る（Colab&thinsp;の外で作成されたファイルだから）

  - 正常に開けたら、ファイル名（左上）の先頭に&thinsp;GitHub&thinsp;のアイコンがあるはず

  - このノートブックを編集したり、実行して結果を保存したい場合、左上のファイルメニューから&thinsp;Google Drive&thinsp;にコピー保存してから行う

    GitHub&thinsp;への保存もできるが少々説明が要るので、学習会では割愛した

<br>

---
