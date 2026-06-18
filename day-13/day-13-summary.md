## 第13回 summary

### 概要
- 2026.6.5 at 15:00〜16:00 オンライン

- 参加者数 3（講師 1, 全体参加 2）

- 録画なし（今回のみ）

<br>

### 内容

- (1) 今日の進め方について

  - 1人の参加者が画面共有して&thinsp;Chapter 5&thinsp;＋α&thinsp;の続きに取り組む（&thinsp;[<ins>解説その&thinsp;2&thinsp;の途中から</ins>](../chapter-5/colab-chapter-5-readme-2.md#%E6%9C%AC-p172173-%E3%81%A8%E5%90%8C%E6%A7%98%E3%81%AB%E5%8B%95%E7%94%BB%E3%81%AE%E8%89%B2%E5%A4%89%E6%8F%9B%E3%81%BC%E3%81%8B%E3%81%97%E3%82%92%E8%A1%8C%E3%81%84%E8%87%AA%E5%8B%95%E5%86%8D%E7%94%9F)&thinsp;）

  - 他の人は同じ箇所を自分でやってみる


<br>

- (2) 作業内容（&thinsp;Chapter 5&thinsp;＋α&thinsp;の続き）

  - まず本&thinsp;p.172〜173&thinsp;と同等の動画編集（色変換＋ぼかし）を試す

    - 本の当該頁に掲載されているコードだけでは動かない。p.160〜以降に登場した関数定義等を持ってくる

    - 処理の概略：

      1. 既にある動画を読み込む（なければ学習会独自の関数 [`VideoWriter`](../chapter-5/VideoWriter.py) を用いカメラで撮影し保存）

      1. 編集後の動画ファイルを準備

      1. 動画の&thinsp;1&thinsp;フレームずつを取り出し、画像処理を加える

      1. 処理した画像を、編集後の動画ファイルに書き込む

      1. 完了したら&thinsp;Colab&thinsp;上で再生（学習会独自の関数 [`play_video`](../chapter-5/play_video.py) を使用）

  - 動画のフレームレートに関し、作業者の環境で問題が発生

    - 既存の動画を&thinsp;OpenCV&thinsp;で読み込み取得したフレームレートの値がおかしい。FPS&thinsp;=&thinsp;30&thinsp;のはずが&thinsp;FPS&thinsp;=&thinsp;1000&thinsp;と認識され、編集後の動画が超早送りになった（Windows&thinsp;+&thinsp;Chrome&thinsp;で）

    - 検証は今後の課題とし、今回は編集後の動画のフレームレートに直接&thinsp;30&thinsp;を指定し問題を回避した

    - その後、独自関数 `VideoWriter` が動画を作る時点でフレームレートの設定がおかしいと分かり修正した

    - macOS&thinsp;+&thinsp;Chrome, Firefox&thinsp;では、フレームレートがおかしい動画も再生時にフレームレートが何となく是正され、問題に気付くのが遅れた

  - 続いて、本&thinsp;p.175&thinsp;と同じ「色変換＋エッジ強調」の画像処理に取り組む

    - 変更点は色変換のパラメータと画像処理だけ

    - 画像処理の変更は&thinsp;while&thinsp;ループ内だが、本のコードからはそれを見逃す可能性がある。前段で「画像処理はループで&thinsp;1&thinsp;フレームずつ取り出して行う」と理解することが大事

  - Chapter 5&thinsp;＋α&thinsp;の最後（カメラで動画撮影〜画像処理〜再生を一気に）は次回送りとし、今回はここまで

<br>

- (3) クロージング

  - 質問は特になし

  - 次回の日時を相談

<br>

---
