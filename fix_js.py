import re

with open('script.js', 'r') as f:
    js = f.read()

# Remove the old global filter logic block
pattern = r'// 6\. Portfolio Gallery Filter Logic.*?\}\);\s*\}\);'
js = re.sub(pattern, '', js, flags=re.DOTALL)

# Let's also fix a syntax error or dangling bracket if there is one.
# My previous replacement ended with `});\n    }` which might be an extra bracket.
# Let's check line 231-235.
