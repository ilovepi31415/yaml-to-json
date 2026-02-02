from line import Line
SPACES_PER_TAB = 2

def main():
    with open("test.yaml", "r") as infile:
        outfile = open("test.json", "w")
        lines = infile.readlines()
        current_indent = 0
        outfile.write("{\n")
        for i in range(len(lines)):
            line = Line(lines[i].strip("\n"))
            if i + 1 < len(lines):
                nextline = lines[i+1].strip("\n")
            else:
                nextline = ""
            if i > 0:
                prevline = lines[i-1].strip("\n")
            else:
                prevline = ""
            nextline = Line(nextline)
            prevline = Line(prevline)
            print(line.text)

            # Categorize line
            indent = line.indent
            print(indent, line.is_list_item, line.indents_next)
            
            if len(line.text.split(":")) > 1:
                key, value = line.text.split(":")

            # Add closing braces when the indent decreases
            while indent < current_indent:
                if prevline.is_list_item:
                    outfile.write(f'{" " * current_indent * SPACES_PER_TAB}]\n')
                else:
                    outfile.write(f'{" " * current_indent * SPACES_PER_TAB}}}\n')
                current_indent -= 1

            # Add line to file
            if value:
                message = '  "' + key.strip() + '":"' + value.strip() + '"'
            else:
                message = '  "' + line.text.strip(":") + '"'
            
            # Check for special line cases
            if line.indents_next:
                message += ":"
                if nextline.is_list_item:
                    message += "["
                else:
                    message += "{"

            # Check for commas
            if line.indent == nextline.indent and nextline.text:
                message += ","

            message += "\n"

            outfile.write(message)
            current_indent = indent
        outfile.write("}")
        outfile.close()

if __name__ == "__main__":
    main()