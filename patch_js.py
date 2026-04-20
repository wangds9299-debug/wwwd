import re

with open("index.html", "r") as f:
    content = f.read()

# Fix context menu to allow it on text-selectable elements
search_str = """    // 禁用右键菜单
    document.addEventListener('contextmenu',e=>e.preventDefault());"""

replace_str = """    // 禁用右键菜单，但允许在可选中文字的区域使用右键（以便复制）
    document.addEventListener('contextmenu',e=>{
        const isTextSelectable = window.getSelection().toString().length > 0 ||
            ['INPUT', 'TEXTAREA'].includes(e.target.tagName) ||
            e.target.closest('.prompt-block') ||
            e.target.closest('.bubble-ai') ||
            e.target.closest('.bubble-user') ||
            e.target.closest('.gal-detail-prompt');
        if (!isTextSelectable) e.preventDefault();
    });"""

content = content.replace(search_str, replace_str)

with open("index.html", "w") as f:
    f.write(content)
