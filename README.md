# YAML to JSON: a file converter

### Summary
I really don't like JSON notation, and I never have. YAML is more convienient for me in many ways, especially in its readability. So I made a converter. There are far better ones out there I'm sure, but it's also been a learning experience for me.

### Requirements
This program was made in Python 3.14, and requires the Python interpreter to run.

### Usage
When running `python3 main.py`, the program looks in its directory for a file named `test.yaml`. After being converted to YAML, the resulting text will be stored in file `test.json`.

### Limitations
This is a continuing work in progress, so the following aspects of YAML are not yet supported:
- **Objects within lists.** All list items must be a single value. Objects within lists will result in a program crash
