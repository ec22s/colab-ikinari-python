# 第1回 (6) 時間が余った人向け作業の補足

<br>

## プログラム変更 (1)

- 全体の例 https://github.com/ec22s/colab-ikinari-python/blob/day-1/day-1/enhance-ex-1.py

<br>

- 元プログラムの問題点

  - 起動して「数字を思い浮かべて･･･」と表示した直後に「50より大きいですか？」と聞かれる（早過ぎ）

<br>

- この改良例として考えたもの

  - 開始してまず「思い浮かべましたか？」と聞き `yes` が入力されたら質問を始める

<br>

- 変更は次の2つ

  - 元プログラムの1行目と2行目の間に ↓ を挿入
    https://github.com/ec22s/colab-ikinari-python/blob/b9f53a3dfd62717e0dc4482df25e449c13f8be8f/day-1/enhance-ex-1.py#L3-L7

  - 変更後の8行目以降をインデント (でないとエラー)

<br>

- 変更後5行目 `!=` の意味は本 `p.32` を参照

  - これが `==` だと、`else` までの間に元あった多くの行数を入れる必要がある

  - そうした条件分岐の先が見にくいプログラムは「見通しが悪い」と批判されがち

<br>

- 変更後6行目 `いったん終了します` と言いながら実際は終了処理をしていない

  - もし `if .. else ..` の後に行があればそれが実行されてしまう

  - あえてそうしたのは、Google Colabはプログラムを途中終了する機能がない（！）から

  - 今後もGoogle Colabの特殊性として要注意

<br>

## プログラム変更 (2) 改良例 A

- 全体の例 https://github.com/ec22s/colab-ikinari-python/blob/day-1/day-1/enhance-ex-2A.py

- 元プログラムの問題点

  - 質問への答で `yes` を `YES` と誤入力すると、`no` と同じ扱いになる

<br>

- この改良例 A として考えたもの

  - 答が `YES` なら `yes` と同じ結果にする

<br>

- 変更は次の2つ

  - 元プログラムの22行目と23行目の間（`else` と `high = guess` の間）に ↓ を挿入
    https://github.com/ec22s/colab-ikinari-python/blob/3a580f98f17c54b38a1e217bb5cd83e0193eecbb/day-1/enhance-ex-2A.py#L24-L26

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

## プログラム変更 (2) 改良例 B

- 全体の例 https://github.com/ec22s/colab-ikinari-python/blob/day-1/day-1/enhance-ex-2B.py

- 元プログラムの問題点は前項と同じ。この改良例 B として考えたもの

  - 答が `yes/no` 以外なら、1回だけ「小文字のyesかnoで答えて下さい」と尋ね直す

<br>

- 変更は次の2つ

  - 元プログラムの22行目と23行目の間（`else` と `high = guess` の間）に ↓ を挿入
    https://github.com/ec22s/colab-ikinari-python/blob/3a580f98f17c54b38a1e217bb5cd83e0193eecbb/day-1/enhance-ex-2B.py#L24-L31

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

## 今回のゲームを「誰でも遊べるWebアプリ」にする方法

- こちら → https://github.com/ec22s/nicegui-ikinari-python

- 公開中のWebアプリ https://nicegui-ikinari-python.onrender.com/

  <img height="192" src="https://github.com/user-attachments/assets/9c0f0bbe-6fbe-473f-b7ff-ae2c271baf70" />

  - 15分間アクセスないと休止、再開時は約1分待つ

  - `chapter-1-a` ほぼ本と同じ

  - `chapter-1-b` 少しアレンジ（ユーザが数を思い浮かべてからスタートする等）

