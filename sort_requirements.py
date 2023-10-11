# sort of requirements file
import sys

for file in sys.argv[1:]:
    with open(file) as f:
        data = f.read().splitlines()
        data.sort()
        sorted_data = "\n".join(data)

    with open(file, mode="w") as f:
        f.write(sorted_data)
