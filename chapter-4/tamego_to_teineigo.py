# 本 4-3 (p.114-120) で作る関数の完成形

def tamego_to_teineigo(text):
  """タメ口を丁寧語に変換する関数"""

  # 変換パターン

  patterns = {
    'だね': 'ですね',
    'こんにちは': 'ごきげんよう',
    'だ': 'です'
  }

  # テキストをスペースで分離する
  sentences = text.split(' ')

  # 変換
  teineigo_sentences = []
  for sentence in sentences:
    for pattern, replacement in patterns.items():
      sentence = sentence.replace(pattern, replacement)
    teineigo_sentences.append(sentence)

  joined_text = ' '.join(teineigo_sentences)

  return joined_text
