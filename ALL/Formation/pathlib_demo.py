from pathlib import Path

# get your current working directory
print(Path.cwd())

# With Path.cwd() and Path.home(), you can conveniently get a starting point for your Python scripts. \
    # In cases where you need to spell paths out or reference a subdirectory structure, you can instantiate\
        # Path with a string.

print(Path.home())

# This process creates a Path object. Instead of having to deal with a string, you can now work \
    # with the flexibility that pathlib offers.

# Instead of starting in your user’s home directory or your current working directory, you can point \
    # to a directory or file directly by passing its string representation into Path:
path = Path(r"C:\Users\jonathan\Repo\Python\ALL\Formation\pathlib_demo.py")

# On Windows, the path separator is a backslash (\). However, in many contexts, the backslash is also \
    # used as an escape character to represent non-printable characters. To avoid problems, use raw string \
        # literals to represent Windows paths:

# The __file__ attribute contains the path to the file that Python is currently importing or executing. \
    # You can pass in __file__ to Path when you need to work with the path to the module itself. \
        # For example, maybe you want to get the parent directory with .parent.
print(f"You can find me here {Path(__file__)} and my parent: {Path(__file__).parent}!")
path_file = Path(__file__)
string_path = str(Path(f"{path_file}"))
print(string_path)

# Path.home().joinpath("python", "scripts", "test.py")
# PosixPath('/home/gahjelle/python/scripts/test.py')
print(path)
print(path.name)
print(path.stem)
print(path.suffix)
print(path.anchor)
print(path.parent)
