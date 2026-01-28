SPACES_PER_TAB = 2

def main():
    with open("test.yaml", "r") as infile:
        outfile = open("test.json", "w")
        lines = infile.readlines()
        current_indent = 0
        for line in lines:
            line = line.strip("\n")
            print(line)
            indent = nesting(line)
            print(indent)
            # Add closing braces when the indent decreases
            while indent < current_indent:
                outfile.write(f'{" " * current_indent * SPACES_PER_TAB}}}\n')
                current_indent -= 1
            message = '"' + line + '"\n'
            outfile.write(message)
            current_indent = indent
        outfile.close()

def nesting(line):
    counter = 0
    for c in line:
        if c == " ":
            counter += 1
    return counter // SPACES_PER_TAB


if __name__ == "__main__":
    main()