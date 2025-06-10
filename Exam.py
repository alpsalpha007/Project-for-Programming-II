def color_decorator(color):
    """
    Function called color_decorator uses ANSI escape codes to add color to text output.
    """
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m",
    }

    def decorator(func):
        """
        The function that wraps itself around another function to modify its output.
        """

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{codes.get(color, '')}{result}{codes['reset']}"

        return wrapper

    return decorator


class FileReader:
    """Object type to read files line by line."""

    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        """Decorator that lets you access an object's attributes."""
        return self._filename

    @filename.setter
    def filename(self, value):
        """Decides what happens when you assign a new value to filename."""
        self._filename = value

    def read_lines(self):
        """Generator function that reads lines from the file."""
        with open(self._filename, "r") as f:
            for line3 in f:
                yield line3.strip()

    @staticmethod
    def static_info():
        """Static method describing the class functionality."""
        return "Static method: FileReader reads files."

    @classmethod
    def class_info(cls):
        """Class method describing the class."""
        return f"Class method: {cls.__name__} is ready"

    def __str__(self):
        """String representation of the object."""
        return f"FileReader(filename='{self._filename}')"

    def __add__(self, other):
        """Add two files by concatenating their contents into a new file."""
        combined_file = "concatenated_output.txt"
        with open(combined_file, "w") as out:
            with open(self._filename, "r") as f1, open(other.filename, "r") as f2:
                out.write(f1.read())
                out.write("\n")
                out.write(f2.read())
        return FileReader(combined_file)

    @color_decorator("red")
    def display_info(self):
        """Returns the file's name colored green."""
        return f"Reading file: {self._filename}"

#blahblah
class MultiFileReader(FileReader):
    """Subclass of FileReader with more functionality."""

    def __str__(self):
        """String representation for MultiFileReader."""
        return f"MultiFileReader(filename='{self._filename}')"

    def unique_wordcount(self):
        """Counts the number of unique words in the file."""
        words = []
        count = 0
        with open(self._filename, "r") as f:
            for line2 in f:
                for word in line2.split():
                    if word not in words:
                        words.append(word)
                        count += 1
        return count

    def longest_line(self):
        """Finds the longest line in the file."""
        with open(self._filename, "r") as f:
            longest_line = max(f, key=len)
        return longest_line.strip()

    def concat_multiple_files(self, *others):
        """Concatenates multiple files into a new file."""
        combined_file = "multi_concatenated_output.txt"
        with open(combined_file, "w") as out:
            with open(self._filename, "r") as f:
                out.write(f.read())
                out.write("\n")
            for other in others:
                with open(other.filename, "r") as f:
                    out.write(f.read())
                    out.write("\n")
        return MultiFileReader(combined_file)

    @color_decorator("red")
    def get_stats(self):
        """Returns stats about longest line and unique word count, colored red."""
        return f"Lines: {self.longest_line()}, Words: {self.unique_wordcount()}"


file_one = FileReader("text1.txt")
file_two = FileReader("text2.txt")

print(file_one.display_info())
print(file_two.display_info())

combined_files = file_one + file_two
print(f"\nCombined file created: {combined_files.filename}\n")

for line1 in combined_files.read_lines():
    print(line1)

print("\n" + FileReader.static_info())
print(FileReader.class_info())
print("\n")

mfr_file1 = MultiFileReader("text1.txt")
mfr_file2 = MultiFileReader("text2.txt")
mfr_file3 = MultiFileReader("text3.txt")

combined_multi_files = mfr_file1.concat_multiple_files(mfr_file2, mfr_file3)
for line in combined_multi_files.read_lines():
    print(line)

print(combined_multi_files.get_stats())
