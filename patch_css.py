import re

with open("index.html", "r") as f:
    content = f.read()

# Add user-select text to bubble-ai and bubble-user
search_str = """        /* 对话气泡 */
        .bubble-ai { background:#fff; border:1px solid var(--border-soft); border-radius:4px 18px 18px 18px; }
        .bubble-user { background:var(--brand-black); color:#fff; border-radius:18px 4px 18px 18px; }"""

replace_str = """        /* 对话气泡 */
        .bubble-ai { background:#fff; border:1px solid var(--border-soft); border-radius:4px 18px 18px 18px; -webkit-user-select:text !important; -moz-user-select:text !important; user-select:text !important; cursor:text; }
        .bubble-user { background:var(--brand-black); color:#fff; border-radius:18px 4px 18px 18px; -webkit-user-select:text !important; -moz-user-select:text !important; user-select:text !important; cursor:text; }"""

content = content.replace(search_str, replace_str)

with open("index.html", "w") as f:
    f.write(content)
