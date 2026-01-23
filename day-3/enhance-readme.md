# 第3回 Chapter 1「数当てられゲーム」の改良等の解説

<br>

## 改良①

- 元プログラムの問題点と改良点

  - 起動して「数字を思い浮かべて･･･」と表示した直後に「50より大きいですか？」と聞かれる（早過ぎ）

    → 開始してまず「思い浮かべましたか？」と聞き `yes` が入力されたら質問を始める

<br>

- 変更箇所

  - 元プログラムの1行目と2行目の間に ↓ を挿入
    https://github.com/ec22s/colab-ikinari-python/blob/deaac08a99d9d881844321cf0c785769eff49535/day-3/enhance-ex-1.py#L3-L7

  - 変更後の8行目以降をインデント (でないとエラー)

<br>

- 変更後5行目 `!=` の意味は本 `p.32` を参照

  - `==` を使っても同じ改良はできるが、`if .. else` の間に元あった多くの行を入れる必要がある

  - そうした条件分岐の先が見にくいプログラムは「見通しが悪い」

<br>

- 変更後6行目 `いったん終了します` と言いながら実際は終了処理をしていない

  - もし `if .. else ..` の後に行があればそれが実行されてしまう

  - あえてそうしたのは、Google Colabはプログラムを途中終了する機能がない（！）から

  - 今後もGoogle Colabの特殊性として注意

<br>

- 改良したコード全体 →  https://github.com/ec22s/colab-ikinari-python/blob/main/day-3/enhance-ex-1.py

  新しいセルに貼り付けて動作確認できます

<br>

## 改良② A

- 元プログラムの問題点と改良点

  - 質問への答で `yes` を大文字の `YES` と誤入力すると、`no` と同じ扱いになる

    → 答が `YES` なら小文字の `yes` と同じ結果にする

<br>

- 変更箇所

  - 元プログラムの22行目と23行目の間（`else` と `high = guess` の間）に ↓ を挿入
    https://github.com/ec22s/colab-ikinari-python/blob/deaac08a99d9d881844321cf0c785769eff49535/day-3/enhance-ex-2A.py#L24-L26

  - 変更後の27行目 `high = guess` のインデントを1つ深く (でないとエラー)

<br>

- 変更内容について

  - 答が `yes` でない場合に、もう一つ `if .. else .. ` を追加し `YES` とそれ以外で場合分け

  - 本当は答が `yes または YES` で一つの `if` にまとめたいが（OR条件）それはこの本に出てこない

    - `p.116` からの単語変換を無理矢理使えば出来ないことはないが、大変

  - 総じてこの本にある条件分岐パターンは少なく、学習会で補足する予定

    - `if` のAND条件は1回だけ `p.204` に出てくるが詳しい説明なし

    - `if` に続けて別の条件を指定する `elif` は出てこない

<br>

- 改良したコード全体 → https://github.com/ec22s/colab-ikinari-python/blob/main/day-3/enhance-ex-2A.py

  新しいセルに貼り付けて動作確認できます

<br>

## 改良② B

- 元プログラムの問題点は前項と同じ。この改良例として

  - 答が `yes/no` 以外なら、1回だけ「小文字のyesかnoで答えて下さい」と尋ね直す

<br>

- 変更箇所

  - 元プログラムの22行目と23行目の間（`else` と `high = guess` の間）に ↓ を挿入
    https://github.com/ec22s/colab-ikinari-python/blob/deaac08a99d9d881844321cf0c785769eff49535/day-3/enhance-ex-2B.py#L24-L31

  - 変更後の32行目 `high = guess` のインデントを2つ深く (でないとエラー)

<br>

- 改良結果

  - 答の1回目に `yes/no` 以外で答えると「小文字のyesかnoで答えて下さい」と尋ね直す

  - 尋ね直しに対し再び `yes/no` 以外で答えると `no` と同じ扱いになる

  - 中途半端な改良だが、これまで出た文法だけを使う場合は仕方ない

<br>

- 徹底して `yes/no` どっちか答えるまで尋ね直すためには

  - 本 `p.44` で出る `whileループ` を使う（条件を満たすまで永遠に繰り返す）

  - これをマスターした後再びこの改良に取り組めば、よい復習になる

<br>

- 改良したコード全体 → https://github.com/ec22s/colab-ikinari-python/blob/main/day-3/enhance-ex-2B.py

  新しいセルに貼り付けて動作確認できます

<br>

## 今回のゲームを「誰でも遊べるWebアプリ」にするには

- こちらでWebアプリ公開中 → https://nicegui-ikinari-python.onrender.com/

  <img height="192" src="https://github.com/user-attachments/assets/9c0f0bbe-6fbe-473f-b7ff-ae2c271baf70" />

  - 15分間アクセスないと休止、再開時は約1分待つ

  - `chapter-1-a` ほぼ本と同じ

  - `chapter-1-b` 少しアレンジ（ユーザが数を思い浮かべてからスタートする等）

<br>

- Webアプリ化の詳細は https://github.com/ec22s/nicegui-ikinari-python

  - 現状、プライベートリポジトリ（見たい人は招待しますので連絡を）

  - 専門的な内容を含みます
