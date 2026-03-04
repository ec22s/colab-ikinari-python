# colab-ikinari-python
Google Colaboratory（Colab）で本『いきなりプログラミング Python』に取り組む初心者向け学習会の資料

- 現状、所属組織内のクローズドな学習会です。参加希望の方は[プロフィール](//github.com/ec22s)のメールアドレスへご連絡下さい

<br>

## 次回予定 & 開催記録

- [第8回 (2026.3.13)](#第8回-2026313-予定)　← 次回　⚠️&thinsp;2週間後

- [第7回 (2026.2.27)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-7/day-7-summary.md)　Chapter 3 続き（独自に準備したColab用関数を使い、本と同じ機能＋αを実施）

- [第6回 (2026.2.13)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-6/day-6-summary.md)　Chapter 2 までの進捗確認・質問・サポート、Chapter 3（声変わり機）初回

- [第5回 (2026.2.6)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-5/day-5-summary.md)　Chapter 2 進捗確認、質疑応答、Chapter 1と2をWebアプリ化した例の紹介

- [第4回 (2026.1.30)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-4/day-4-summary.md)　本 Chapter 2（p.38〜66）の説明、各自作業

- [第3回 (2026.1.23)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-3/day-3-summary.md)　本 `1ｰ3` の質疑応答（文字列の部分一致）、ゲームの改良

- [第2回 (2026.1.16)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-2/day-2-summary.md)　本 `1ｰ3`（p.23〜36）最初のアプリ（数当てられゲーム）

- [第1回 (2026.1.9)](https://github.com/ec22s/colab-ikinari-python/blob/main/day-1/day-1-summary.md)　本の説明、GitHubとColabの設定、最初のプログラム（Hello World）

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

    → 学習会独自の[「Colabで本のChapter 3を動かす」](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/colab-chapter-3-readme.md)コードを作った

    → Chapter 4 以降もColab用の改変を準備済み、後日このリポジトリに掲載予定

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

- Colabの入力補完を活用しよう

  - 候補の選択はキーボードの上下カーソルで、確定はタブでできる

  - 候補が一つになったらタブだけで確定できる

<br>

## 第8回 (2026.3.13) 予定

- 13:30〜14:30 オンライン（録画忘れずに）

  - 録画で見る場合、同じ作業を自分のPCでしながら見ると良いです。不明点等はチャットで質問して下さい

<br>

- (1) 前回の振り返り

  - Chapter 3（本 `p.68〜`）を一通り終えた

    - Colab用に作ったマイク録音用関数 [`record.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record.py) を用い、本と同じ機能（録音, グラフ描画, WAVファイル出力, ボイスチェンジ）を実行した

    - Chapter 4 の準備を兼ねて作成した新しい関数 [`record_auto_stop.py`](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-3/record_auto_stop.py) を試し、マイクへの発話が終わった時に録音が自動終了するのを確認した

    - 本にない独自の＋αとして、音声データをColab上で再生するコードを加えた

<br>

- (2) 各自の進捗に応じて説明・サポート or もくもく

  - Chapter 3 までが未了の人

    - どこかで詰まっている or 説明を聞きたい人：講師と会話・画面共有しながら作業

    - 自分で進められそうな人：できる所まで作業し、詰まったら講師に質問

  - Chapter 3 が終わった人：

    - Chapter 4 に取り組んでみよう

      - Chapter 3 と同様、Colab用に独自に準備した関数を使う（マイク録音のため）

      - 詳細はこちらで準備した手順 [（→ リンク)](https://github.com/ec22s/colab-ikinari-python/blob/main/chapter-4/colab-chapter-4-readme.md) を参照し、不明な点は講師に質問

        ＊リンク先の内容は当日までに書きます

    - または

      - 本にある説明を読む

      - 本と同じ環境（ローカルのJupyter Notebook）を構築し好きな箇所をやってみる

      など自由にしてもらっても可

<br>

- (4) クロージング

  - 次回の日時

    - 来週が祝日のため2週間後 (2026.3.27 Fri) 13時30分〜14時30分でよいか

  - 次回の内容・進め方

  - その他あれば

<br>

---
