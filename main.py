from line import Line
SPACES_PER_TAB = 2

def main():
    with open("test.yaml", "r") as infile:
        outfile = open("test.json", "w")
        lines = infile.readlines()
        current_indent = 0
        outfile.write("{\n")
        for i in range(len(lines)):
            line = lines[i].strip("\n")

            # Catch special YAML format lines
            if line in ["---", "..."]:
                continue

            # Convert current and surrounding lines into Line object
            line = Line(line)
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
            
            if len(line.text.split(":")) > 1:
                key, value = line.text.split(":")

            # Add closing braces when the indent decreases
            indent = line.indent
            while indent < current_indent:
                if prevline.is_list_item:
                    outfile.write(f'{" " * current_indent * SPACES_PER_TAB}]')
                else:
                    outfile.write(f'{" " * current_indent * SPACES_PER_TAB}}}')
                if indent == current_indent - 1:
                    outfile.write(",")
                outfile.write("\n")
                current_indent -= 1

            # Add line to file
            if value:
                # Display "key":"value"
                message = '  "' + key.strip() + '":"' + value.strip() + '"'
            else:
                # Display "item"
                message = '  "' + line.text.strip(":") + '"'
            value = None

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

            # Write line of text to outfile
            outfile.write(message)

            # Add brace or bracket after final item
            if not nextline.text and line.indent > 1:
                if line.is_list_item:
                    outfile.write("]\n")
                else:
                    outfile.write("}\n")

            current_indent = indent
        outfile.write("}\n")
        outfile.close()

if __name__ == "__main__":
    main()