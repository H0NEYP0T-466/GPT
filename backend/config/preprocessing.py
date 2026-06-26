import logging
from pathlib import Path

path=Path(__file__).parent.parent / "dataset/input.txt"

def data_Reading():
    with open(path, "r") as f:
        dataset=f.read()
    return len(dataset)

num=data_Reading()
print(num)


