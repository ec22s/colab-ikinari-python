#@title (以下、第12回で予定) 独自関数 play_video : 保存した動画をColab内で自動再生

# 本の方法で作成した動画は、そのままではColab内で再生できない
# (動画の「コーデック」という仕様が関係している模様)
# FFmpegというツールで変換すると再生できる

from IPython.display import HTML
from base64 import b64encode
import os

def play_video(movie_file, video_height=240):
  if not os.path.isfile(movie_file):
    print(f"Error: file '{movie_file}' not found")
    return
  tmp_file = "tmp.mp4"
  !ffmpeg -i $movie_file $tmp_file -y -loglevel 0
  mp4 = open(tmp_file, "rb").read()
  display(HTML(f"""
    <video height="{video_height}" autoplay controls>
      <source src="data:video/mp4;base64,{b64encode(mp4).decode()}">
    </video>
  """));

print("再生準備完了")
