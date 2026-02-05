# YAML to JSON: a file converter

### Summary
I really don't like JSON notation, and I never have. YAML is more convienient for me in many ways, especially in its readability. So I made a converter. There are far better ones out there I'm sure, but it's also been a learning experience for me.

### Requirements
This program was made in Python 3.14, and requires the Python interpreter to run.

### Usage
python3 main.py [infile-name]

When running `python3 main.py`, the program looks in its directory for a file matching the name selected by the user. If no file is given, it will look for `test.yaml` instead. After being converted to YAML, the resulting text will be stored in a json file with the same file name as the input.

### Limitations / Future Goals
This is a continuing work in progress, so the following aspects of YAML are not yet supported:
- **Objects within lists.** All list items must be a single value. Objects within lists will result in a program crash
