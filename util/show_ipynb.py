import json
import requests
from IPython.display import display, HTML

def show_ipynb(url = "", css = ""):
  """
  Web公開されているipynbファイルの中身を表示
  """

  if url == "":
    print("ERROR: url is empty")
    return
  if css == "":
    css = "background: #eee; margin-bottom: 1em; padding: 1em"
  try:
    dict = json.loads(requests.get(url).content.decode("utf-8"))
    sources = (_["source"] for _ in dict["cells"] if _["cell_type"] == "code")
    for code in sources:
      display(HTML(f'<pre style="{css}">{"".join(code)}</pre>'))
  except Exception as e:
    print(f"ERROR: {e}")
    return
