from pathlib import Path

path=Path(__file__).parent.parent / "dataset/input.txt"

with open(path, "r") as f:
        dataset=f.read()
        
def clean(dataset):
    chars=sorted(list(set(dataset)))
    vocab_size=len(chars)
    print("vocab size:", vocab_size)
    print(''.join(chars))
    return chars




