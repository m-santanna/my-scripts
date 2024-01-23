import os

downloads = os.path.expanduser("~/Downloads")
faculdade = os.path.expanduser("~/Faculdade")

for file in os.listdir(downloads):
    if file.endswith(".pdf"):
        os.rename(os.path.join(downloads, file), os.path.join(faculdade, file))