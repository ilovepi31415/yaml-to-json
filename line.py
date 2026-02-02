SPACES_PER_TAB = 2

class Line():
    def __init__(self, text):
        self.text = text
        self.is_list_item = self.text.strip().startswith("-")
        self.indents_next = self.text.endswith(":")
        self.indent = self.nesting()
    
    def nesting(self):
        counter = 0
        for c in self.text:
            if c == " ":
                counter += 1
        return counter // SPACES_PER_TAB