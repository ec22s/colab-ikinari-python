from IPython.display import display
from base64 import b64encode
import subprocess
import os

def play_video(movie_file, video_height=240):
  if not os.path.isfile(movie_file):
    print(f"Error: file '{movie_file}' not found")
    return

  # FFmpegで変換し、最後に一時ファイルを消す
  # GitHubで正しく表示できるよう「!コマンド $変数」は使わない
  tmp_file = "tmp.mp4"
  subprocess.run(["ffmpeg", "-i", movie_file, tmp_file, "-y", "-loglevel", "0"])
  mp4 = open(tmp_file, "rb").read()
  os.remove(tmp_file)

  # FFmpegの変換結果を標準出力で扱えれば一時ファイル不要になるが、それは難しい
  # https://qiita.com/rougemeilland/items/d1c2514caaa7682ff683

  # GitHubで正しく表示できるようHTMLタグを使わない
  display(Javascript(f"""
    const video = document.createElement("video");
    video.height = "{video_height}";
    video.autoplay = true;
    video.controls = true;
    const source = document.createElement("source");
    source.src = "data:video/mp4;base64,{b64encode(mp4).decode()}";
    video.appendChild(source);
    document.querySelector("#output-area").appendChild(video);
  """));

print("再生準備完了")
