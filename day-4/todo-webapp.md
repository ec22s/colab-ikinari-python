### Todo: Webアプリについて

- ページタイトルを `nicegui-ikinari-python` に変更

- 背景色を付ける（ないとキャプチャ時にページ範囲が分からない）

- 上部タイトルの見映えよくする

- 同じDockerコンテナをAWSとGCP (Cloud Run) でデプロイする手順調査

  - Renderより面倒なはず、それを確認する

<br>

### Plan

- 説明ではWebアプリソースの `README` から主要部分だけ使う

  - 冒頭「PythonのWebフレームワーク `NiceGUI` を用い、他の言語は使いません」

  - 前半「Webアプリ化の趣旨」の「本当のアプリ vs Jupyter Notebook vs Colab」

  - 後半「デプロイ手順」の冒頭（Renderを選択した理由）

<br>

### 検討時の覚え書

  - アーキテクチャ : NiceGUI + Dockerが良い
  - フロントエンド／バックエンドの分離（APIでやり取り）は今回割愛
    - Jupyter Notebookが両者一体、NiceGUIも同じ、ノートブックの雰囲気をなるべく活かす

  - デプロイ先 : Rendarがデモ用には良い
    - 同じことを安定的にしようと思ったらAWSかCloud Runでとても面倒 (なはず)

    - Herokuは最低でも費用かかる、費用抑えるため一時的に起動するのは面倒
