with open('script.js', 'r') as f:
    js = f.read()

# Let's split at // 6. Portfolio Gallery Filter Logic
parts = js.split('    // 6. Portfolio Gallery Filter Logic')
if len(parts) > 1:
    new_js = parts[0].rstrip()
    
    # Check if the last character is an extra '}'
    # Currently it ends with:
    #    });
    #    }
    # We want it to end with:
    #    });
    # });
    
    # We'll just force the correct ending.
    if new_js.endswith("    }\n"):
        new_js = new_js[:-6] # remove "    }\n"
        
    new_js += "\n});\n"
    
    with open('script.js', 'w') as f:
        f.write(new_js)

print("Done")
