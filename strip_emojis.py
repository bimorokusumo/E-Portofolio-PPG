import re

def remove_emojis(text):
    # This regex matches most emoji characters
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])|"  # flags (iOS)
        u"([\u2600-\u26FF])|"        # miscellaneous symbols
        u"([\u2700-\u27BF])|"        # dingbats
        u"(\U0001f600-\U0001f64f)|"  # emoticons
        u"(\U0001f300-\U0001f5ff)|"  # symbols & pictographs
        u"(\U0001f680-\U0001f6ff)|"  # transport & map symbols
        u"(\U0001f1e0-\U0001f1ff)|"  # flags
        u"(\U0001f900-\U0001f9ff)|"  # supplemental symbols and pictographs
        u"(\U0001fa70-\U0001faff)"   # symbols and pictographs extended-A
        "+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Also remove common emoji characters not caught by the above, or specific empty span patterns
# We will use the emoji library for robustness if possible, but let's stick to regex first.
# Wait, python's standard library doesn't have an `emoji` module installed by default.
# Let's try to install `emoji` module and use it, it's much safer.
