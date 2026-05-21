from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
        self.void_elements = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.tags.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        
        while self.tags:
            last_tag, pos = self.tags.pop()
            if last_tag == tag:
                return
            else:
                self.errors.append(f"Unclosed tag '{last_tag}' started at {pos} before finding closing tag '{tag}' at {self.getpos()}")
                # Assume it was just unclosed and continue matching the current end tag if we can find it further up
                # Actually, simple stack mismatch logic:
                found = False
                for i in range(len(self.tags)-1, -1, -1):
                    if self.tags[i][0] == tag:
                        found = True
                        break
                if found:
                    continue # Keep looking up
                else:
                    self.tags.append((last_tag, pos)) # Put it back, this closing tag is a stray
                    self.errors.append(f"Stray closing tag '{tag}' at {self.getpos()}")
                    return
        self.errors.append(f"Stray closing tag '{tag}' at {self.getpos()}")

parser = MyHTMLParser()
with open("index.html", "r", encoding="utf-8") as f:
    parser.feed(f.read())

if parser.tags:
    for tag, pos in parser.tags:
        print(f"Unclosed tag '{tag}' started at {pos}")
if parser.errors:
    for err in parser.errors[:10]:
        print(err)
print("Finished checking.")
