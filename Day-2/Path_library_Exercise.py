from pathlib import Path

path = Path() 
for files in path.glob("*.py"):
    print(files)

path = Path("Day-2")
print(path.exists())