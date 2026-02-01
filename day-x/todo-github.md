### ColabとGitHubの最低限の連携ができればOK

<br>

### 参考 https://note.com/matsuken_rabbit/n/nb884502a1dc4

- これを自力でできれば駆け出しエンジニア

- 今回はその手前、用意されたものの上で何となくGitHubとの読み書きができればOk

<br>

### 準備

- メンバー用のブランチを必要な数だけ事前に作っておき、テスト用 `.ipynb` 置く

- `.ipynb` の中身はブランチ毎に少し変える（間違い防止）

<br>

### 当日の手順

- (1) 各メンバーにブランチを割り当てる（間違い注意）

- (2) 各メンバーがGitHubで自分用のブランチを開き `.ipynb` の中身を確認（間違い防止）

- (3) ColabでOpen Notebook > GitHubを選択 > ここで連携用の設定が要る (面倒かも)
  - 連携できたら自分用のブランチにあるテスト用ファイルを開いて実行

- (4) テスト用ファイルを修正しcopyをGitHubに保存 (Fileメニューから)
  - 保存時に自分用ブランチか確認、コミットメッセージを入力
  - 保存した内容をGitHubリポジトリで確認

<br>

### 説明

- GitHubで `.ipynb` が良しなに表示されるので結構使える、差分も見やすい

- その他（考え中）

<br>

### 準備側メモ

- 今回は単体の `.ipynb` についてのみ、共有でき差分が見れるまでとする

- ColabでGitHubと連携できるのは個々のノートブック(.ipynbファイル)でしかない

- 他のファイル（モジュール等）を含めて連携させるには以下二つが必要、今回は難しい

  - Googleドライブの特定フォルダをマウント
  - そのフォルダ下にGitHubのローカルリポジトリを置きコマンド操作

    - GitHubなしにGoogle Driveドライブだけ使う手もあるが、履歴管理が難しい(はず)
    - Project全体をGitHubで管理する方が共同作業に向く (Issueとか使えるし)

- より進んだ使い方（今回の学習会では紹介も難しそう）

  - https://qiita.com/mokroke/items/1b221891ebe00dd8d4ad

    → https://github.com/mokroke/colab-github-connect-test/blob/main/connect_test.ipynb

  - https://qiita.com/kurilab/items/f6f4374d7b1980060de7

    (username/passwordはトークンに変える必要あり)

  - https://zenn.dev/smiyawaki0820/articles/e346ca8b522356
  - https://zenn.dev/e4exp/articles/a4f6acab34fa48
  - https://note.com/96neko_kurosuke/n/n1a9bb594813d

  - https://note.com/sunwood_ai_labs/n/n3e63e34c7777

    (Personal Access Tokenで良さそう、記事は途中までしか見れない)

  - https://note.com/sunwood_ai_labs/n/nfc5fa59690bd

    (SSH利用は面倒、というか今は使えないかも)
