def color_decorator(color):
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m",
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{codes.get(color, '')}{result}{codes['reset']}"

        return wrapper

    return decorator


class FileReader:
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def read_lines(self):
        with open(self._filename, "r") as f:
            for line in f:
                yield line.strip()

    @staticmethod
    def static_info():
        return "Static method: FileReader reads files."

    @classmethod
    # @color_decorator('yellow')
    def class_info(cls):
        return f"Class method: {cls.__name__} is ready"

    def __str__(self):
        return f"FileReader(filename='{self._filename}')"

    def __add__(self, other):
        combined_file = "concatenated_output.txt"
        with open(combined_file, "w") as out:
            with open(self._filename, "r") as f1, open(other.filename, "r") as f2:
                out.write(f1.read())
                out.write("\n")
                out.write(f2.read())
        return FileReader(combined_file)

    @color_decorator("green")
    def display_info(self):
        return f"Reading file: {self._filename}"


class AdvancedFileReader(FileReader):
    def __str__(self):
        return f"AdvancedFileReader(filename='{self._filename}')"

    def unique_wordcount(self):
        words = []
        count = 0
        with open(self._filename, "r") as f:
            for line in f:
                for word in line.split():
                    if word not in words:
                        words.append(word)
                        count += 1
        return count

    def longest_line(self):
        with open(self._filename, "r") as f:
            longest_line = max(f, key=len)
        return longest_line.strip()

    def concat_multiple_files(self, *others):
        combined_file = "multi_concatenated_output.txt"
        with open(combined_file, "w") as out:
            with open(self._filename, "r") as f:
                out.write(f.read())
                out.write("\n")
            for other in others:
                with open(other.filename, "r") as f:
                    out.write(f.read())
                    out.write("\n")
        return AdvancedFileReader(combined_file)

    @color_decorator("red")
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
adv_file1 = AdvancedFileReader("text1.txt")
adv_file2 = AdvancedFileReader("text2.txt")
adv_file3 = AdvancedFileReader("text3.txt")

# combined_reader = AdvancedFileReader("multi_concatenated_output.txt")


combined_adv_files = adv_file1.concat_multiple_files(adv_file2, adv_file3)
for line in combined_adv_files.read_lines():
    print(line)


print(combined_adv_files.get_stats())
