import re
from pathlib import Path


pattern = re.compile(r"  title={(.*)},")

def changeling(line):
    return pattern.match(line)


lines = Path("data.txt").read_text()
lines = lines.replace("\r", " ")
lines = lines.split("\n")


new_file = ""

for line in lines:

    match = changeling(line)

    this_line = line

    if match is not None:
        title = match.groups()[0]
        new_title = r"  title={{" + title + r"}}" + ","
        print(line, "->", new_title)

        this_line = new_title
    
    new_file += f"{this_line}\n"

my_path = Path("my_data.txt")

my_path.write_text(new_file)
