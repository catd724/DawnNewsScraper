import os


def textSave(text,destination):
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination,"w", encoding="utf-8") as f:
        f.write(text)
        print("text written to ", destination)