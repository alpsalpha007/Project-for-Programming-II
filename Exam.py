def color_decorator(color): """function called color_decorator uses ANSI escape codes to"""
    codes = { """this part has the colors, and the with the ANSI code"""
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m",
    }

    def decorator(func): """the function that wraps itself around the other function, and takes in a function to execute the change"""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{codes.get(color, '')}{result}{codes['reset']}"

        return wrapper

    return decorator


class FileReader: """object tpe to read files line by line"""
    def __init__(self, filename):
        self._filename = filename

    @property """Decorator that lets uyou access a objects attributes"""
    def filename(self):
        return self._filename

    @filename.setter """Decides what happens when you are assigning a new value to file name"""
    def filename(self, value):
        self._filename = value

    def read_lines(self): """function that reals lines"""
        with open(self._filename, "r") as f:
            for line in f:
                yield line.strip()

    @staticmethod
    def static_info():
        return "Static method: FileReader reads files."

    @classmethod
    
    def class_info(cls):
        return f"Class method: {cls.__name__} is ready"

    def __str__(self): """shows how the code will look in string"""
        return f"FileReader(filename='{self._filename}')"

    def __add__(self, other): """function to add the two files that have been opened together"""
        combined_file = "concatenated_output.txt"
        with open(combined_file, "w") as out:
            with open(self._filename, "r") as f1, open(other.filename, "r") as f2:
                out.write(f1.read())
                out.write("\n")
                out.write(f2.read())
        return FileReader(combined_file)

    @color_decorator("green") """applies the color_decorator and returns the file's name in green"""
    def display_info(self):
        return f"Reading file: {self._filename}"


class MultiFileReader(FileReader): """new function with more functionality"""
    def __str__(self):
        return f"MultiFileReader(filename='{self._filename}')"

    def unique_wordcount(self): """a function that counts the number of unique words"""
        words = []
        count = 0
        with open(self._filename, "r") as f:
            for line in f:
                for word in line.split():
                    if word not in words:
                        words.append(word)
                        count += 1
        return count

    def longest_line(self): """it sees which line amongst the files is the biggest"""
        with open(self._filename, "r") as f:
            longest_line = max(f, key=len)
        return longest_line.strip()

    def concat_multiple_files(self, *others): """functions that concatinates multiple number of files"""
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

    @color_decorator("red") """using the color_decorator function to show the unique word count result and the longest line"""
    def get_stats(self):
        return f"Lines: {self.longest_line()}, Words: {self.unique_wordcount()}"


file_one = FileReader("text1.txt")
file_two = FileReader("text2.txt")

print(file_one.display_info())
print(file_two.display_info())

combined_files = file_one + file_two
print(f"\nCombined file created: {combined_files.filename}\n")

for line in combined_files.read_lines():
    print(line)

print("\n" + FileReader.static_info())
print(FileReader.class_info())
print("\n")
mfr_file1 = MultiFileReader("text1.txt")
mfr_file2 = MultiFileReader("text2.txt")
mfr_file3 = MultiFileReader("text3.txt")

# combined_reader = AdvancedFileReader("multi_concatenated_output.txt")


combined_multi_files = mfr_file1.concat_multiple_files(mfr_file2, mfr_file3)
for line in combined_multi_files.read_lines():
    print(line)


print(combined_multi_files.get_stats())
