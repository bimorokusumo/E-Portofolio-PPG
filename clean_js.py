with open('script.js', 'r') as f:
    js = f.read()

js = js.replace("    });\n    }\n});\n", "    });\n});\n")

with open('script.js', 'w') as f:
    f.write(js)
