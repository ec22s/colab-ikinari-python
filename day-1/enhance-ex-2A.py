# 第1回 (5) プログラム変更 (2) 改良例 A
print('1から100までの間で好きな数字を一つ思い浮かべて下さい。')
print('あなたの考えている数字を7回以内に当ててみましょう。')

# low: 最小値, high: 最大値
low = 1
high = 100
print(low, high)

for i in range(7):
  # low と high が同じならループを抜ける
  if low == high:
    break

  # コンピュータの推測値を確認
  guess = (low + high) // 2
  print('あなたの数字は', guess, 'より大きいですか？ (yes/no)')
  answer = input()

  # ユーザの答えにより分岐
  if answer == 'yes':
    low = guess + 1
  else:
    if answer == 'YES':
      low = guess + 1
    else:
      high = guess

print('あなたの思い浮かべた数字は', low, 'ですね！')
