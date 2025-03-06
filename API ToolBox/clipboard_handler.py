import pyperclip


def paste_from_clipboard():
    """从剪切板读取内容"""
    try:
        return pyperclip.paste()
    except Exception as e:
        return f"读取剪切板失败：{e}"
