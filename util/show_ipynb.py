import json
import requests
from IPython.display import display, HTML

def show_ipynb(url = ""):
  """
  Web公開されているipynbファイルの中身をセルに表示
  """
  if url == "":
    print("ERROR: url is empty")
    return

  CSS_DIV = "background: #cee; margin-bottom: 1em; padding: 1em 1.25em"
  CSS_CODE = "margin-top: 1em"
  CSS_BORDER = "border-bottom: gray dashed 2px; height: 0; margin-top: 0.75em"
  CSS_BUTTON = "margin-left: 1em"
  SCRIPT_COPY = """
    function copy(button) {
      const code = button.parentNode.querySelector("pre").textContent;
      navigator.clipboard.writeText(code);
      alert(`Copied ${code.length} characters.`);
    }
  """

  try:
    dict = json.loads(requests.get(url).content.decode("utf-8"))
    sources = (_["source"] for _ in dict["cells"] if _["cell_type"] == "code")
    for index, code in enumerate(sources):
      display(HTML(f'''
        <div style="{CSS_DIV}">
          セル - {index+1}
          <button onclick="copy(this)" style="{CSS_BUTTON}">Copy</button>
          <div style="{CSS_BORDER}"></div>
          <pre style="{CSS_CODE}">{"".join(code)}</pre>
        </div>
        <script>{SCRIPT_COPY}</script>
      '''))
  except Exception as e:
    print(f"ERROR: {e}")
    return
