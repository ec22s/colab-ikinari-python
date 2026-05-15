## 第11回 summary

### 概要
- 2026.4.28 at 13:30〜14:30 オンライン

- 参加者数 4（講師 1, 全体参加 3）

- 録画あり（120日有効）

<br>

### 内容

- (1) 今日の進め方について

  - 1人の参加者が画面共有して Chapter 5 に取り組み（[解説](../chapter-5/colab-chapter-5-readme.md)&thinsp;に沿ってほぼ初めから）、他の人は自分で Chapter 5 に取り組む（または作業の様子を聴く）回とした

<br>

- (2) 本の Chapter 5 ほぼ初めから&thinsp;5-4&thinsp;まで＋α

  - 最初に学習会独自のクラス [`ColabCap`](../chapter-5/ColabCap.py) を準備（Colab&thinsp;で&thinsp;PC&thinsp;のカメラを使うのに必要）

  - 静止画を撮影

    - 本の&thinsp;5-1。環境は&thinsp;Windows + Chrome、カメラは&thinsp;PC&thinsp;内蔵

  - 通常の動画を撮影

    - 本の&thinsp;5-2。本と違ってスリープ処理を省きフレームレートを下げる理由を解説。Colab&thinsp;利用なので1枚1枚の撮影がどうしても遅く、スリープしなくても精々&thinsp;10&thinsp;コマ/秒程度にしかならない

  - タイムラプス動画を撮影

    - 本の&thinsp;5-3。タイムラプス撮影の概略や各パラメータの意味を説明。今度は撮影間隔が長いので&thinsp;Colab&thinsp;利用でも本と概ね同じ結果を出せる

    - ただしスリープ処理に付随してタイムラグが発生するため、撮影に必要な時間は本より長い

  - 静止画を編集

    - 本の&thinsp;5-4。OpenCV&thinsp;と&thinsp;NumPy&thinsp;を使い&thinsp;3&thinsp;種類の画像処理を実施（色変換、エッジ抽出、ぼかし）

  - 動画の編集（本の&thinsp;5-5）は次回とし、5-5&thinsp;と&thinsp;Chapter 6&thinsp;の準備として、Colab&thinsp;で動画撮影・保存するもう一つの独自関数 [`VideoWriter`](../chapter-5/VideoWriter.py) を試した

    - 結果OK。1枚1枚の撮影をしないので本と同程度のフレームレートで動画を撮れた

    - ただしデータ送信や&thinsp;Colab&thinsp;での処理に時間がかかると判明、今後改善を試みる

<br>

- (3) クロージング

  - 参加者の感想：Chapter 5&thinsp;でカメラ・画像を扱うようになり、従前の内容に比べ面白くなった

  - Chapter 5&thinsp;の解説で本のコードを編集する箇所が分かりにくく、次回までに改善したい

  - 次回の日時を相談

<br>

---
