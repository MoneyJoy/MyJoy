import re

def convert_html_images_to_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 正则表达式匹配 HTML 图片标签，包括可选的 style 属性
    html_img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*alt="([^"]*)"\s*(?:style="[^"]*")?\s*/?>', re.IGNORECASE)

    # 替换为 Markdown 图片语法
    def replace_with_markdown(match):
        src = match.group(1)
        alt = match.group(2)
        return f'![{alt}]({src})'

    new_content = html_img_pattern.sub(replace_with_markdown, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 使用示例
file_path = 'day14.md'  # 将此路径替换为你的 Markdown 文件路径
convert_html_images_to_markdown(file_path)

