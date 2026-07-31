import emoji
import re

for filename in ['script.js', 'style.css']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    content_no_emoji = emoji.replace_emoji(content, replace='')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content_no_emoji)

print("Done stripping emojis from JS and CSS.")
