from preprocessing import clean
from pathlib import Path

path=Path(__file__).parent.parent / "dataset/input.txt"
with open(path, "r") as f:
        dataset=f.read()

chars=clean(dataset)


def encoder(text):
    return [chars.index(c) for c in text]
def decoder(indices):
    return ''.join([chars[i] for i in indices])

print(encoder("hello world"))
print(decoder(encoder("hello world")))