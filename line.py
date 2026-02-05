SPACES_PER_TAB = 2
BONUS_INDENTS = 1

class Line():
    def __init__(self, text):
        self.text = text
        self.is_list_item = self.text.strip().startswith("-")
        self.indents_next = self.text.endswith(":")
        self.indent = self.nesting()
        # Parse text once flags are triggered
        self.text = self.parse_text()
    
    def nesting(self):
        # Count total whitespace at the beginning of a line
        counter = 0
        for c in self.text:
            if c == " ":
                counter += 1
            else:
                break
        return (counter // SPACES_PER_TAB) + BONUS_INDENTS
    
    def parse_text(self):
        return self.text.strip().strip("-").strip()