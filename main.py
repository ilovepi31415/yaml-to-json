import sys, os

from line import Line
SPACES_PER_TAB = 2

def main():
    # Parse arguments for in- and outfile names
    if len(sys.argv) < 2:
        # Use defaults if none given
        file_in = "test.yaml"
        file_out = "test.json"
    elif len(sys.argv) == 2:
        # Get infile name and check for existence and filetype
        file_in = sys.argv[1]
        if not os.path.exists(file_in):
            print("ERROR: infile does not exist")
            sys.exit(1)
        if not file_in.endswith(".yaml"):
            print("ERROR: invalid file type")
            sys.exit(2)
        file_out = file_in.split('.')[0] + ".json"
    else:
        # Error otherwise
        print("ERROR: too many arguments")
        sys.exit(3)

    with open(file_in, "r") as infile:
        outfile = open(file_out, "w")
        lines = infile.readlines()
        current_indent = 1
        indent_types = []
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
            current_indent = prevline.indent
            while indent < current_indent:
                current_indent -= 1
                outfile.write(f'{" " * current_indent * SPACES_PER_TAB}{indent_types.pop()}')
                if indent == current_indent:
                    outfile.write(",")
                outfile.write("\n")

            # Add line to file
            if value:
                # Display "key":"value"
                message = f'{" " * line.indent * SPACES_PER_TAB}"' + key.strip() + '":"' + value.strip() + '"'
            else:
                # Display "item"
                message = f'{" " * line.indent * SPACES_PER_TAB}"' + line.text.strip(":") + '"'
            value = None

            # Check for special line cases
            if line.indents_next:
                message += ":"
                if nextline.is_list_item:
                    message += "["
                    indent_types.append("]")
                else:
                    message += "{"
                    indent_types.append("}")

            # Check for commas
            if line.indent == nextline.indent and nextline.text:
                message += ","
            message += "\n"

            # Write line of text to outfile
            outfile.write(message)

            # Add brace or bracket after final item
            # print(line.indent, line.text, line.indents_next)
            if not nextline.text or nextline.text == "...":
                while line.indent > 1:
                    line.indent -= 1
                    outfile.write(f"{" " * line.indent * SPACES_PER_TAB}{indent_types.pop()}\n")

            current_indent = indent
        outfile.write("}\n")
        outfile.close()

if __name__ == "__main__":
    main()