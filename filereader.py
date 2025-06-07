# Define a basic class to read files using a generator
class FileReader:
    def init(self, filename):
        # Initialize the object with a filename
        self._filename = filename

    @property
    def filename(self):
        # Getter method for filename
        return self._filename

    @filename.setter
    def filename(self, value):
        # Setter method for filename
        self._filename = value

    def read_lines(self):
        # Generator function that yields one line at a time from the file
        with open(self._filename, 'r') as f:
            for line in f:
                yield line.strip()  # Remove newline and spaces

    @staticmethod
    def static_info():
        # A static method that doesn't depend on instance or class
        return "Static method: FileReader reads files."

    @classmethod
    def class_info(cls):
        # A class method that gets the class as the first argument
        return f"Class method: {cls.name} is ready!"

    def add(self, other):
        # Special method to use + operator to combine two FileReader objects
        new_file = "concatenated_output.txt"
        with open(new_file, 'w') as out:
            with open(self._filename, 'r') as f1, open(other.filename, 'r') as f2:
                out.write(f1.read())  # Write content of first file
                out.write("\n")       # Add a newline between files
                out.write(f2.read())  # Write content of second file
        return FileReader(new_file)  # Return new FileReader instance

# Define a subclass with additional functionality
class AdvancedFileReader(FileReader):
    def line_count(self):
        # Count number of lines using the generator
        return sum(1 for _ in self.read_lines())

    def word_count(self):
        # Count total words in the file
        return sum(len(line.split()) for line in self.read_lines())

# Decorator that changes the text color using ANSI escape codes
def color_decorator(color):
    # Dictionary of ANSI color codes
    color_codes = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'reset': '\033[0m'
    }

    def decorator(func):
        # Inner decorator function
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # Call the original function
            return f"{color_codes.get(color, '')}{result}{color_codes['reset']}"
        return wrapper

    return decorator

# Example usage of the decorator
@color_decorator('red')
def greeting():
    # Function that returns a string
    return "Hello, colorful world!"
