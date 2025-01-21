import re

html_content = """
"""

# 提取所有<span>标签内的文本
pattern = re.compile(r'<span[^>]*>(.*?)</span>', re.DOTALL)
matches = pattern.findall(html_content)

# 打印提取的文本
for match in matches:
    print(match.strip())