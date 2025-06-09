import os
import pytest
from Exam import FileReader, MultiFileReader, color_decorator
def test_read_lines():
    fr = FileReader("text1.txt")
    assert list(fr.read_lines()) == ["Roses are red", "im in my head"]

def test_display_info_color():
    assert "\033[92m" in FileReader("test1.txt").display_info()

def test_add_files():
    combined = FileReader("text1.txt") + FileReader("text2.txt")
    assert combined.filename == "concatenated_output.txt"
    lines = list(combined.read_lines())
    assert "Roses are red" in lines
    assert "im in my head" in lines
    assert "" in lines
    assert "violets are blue" in lines
    assert "thinking bout you" in lines

def test_static_and_class_info():
    assert "Static method" in FileReader.static_info()
    assert "FileReader" in FileReader.class_info()

def test_advanced_unique_wordcount():
    afr = MultiFileReader("text1.txt")
    assert afr.unique_wordcount() == 7

def test_advanced_longest_line():
    assert MultiFileReader("text3.txt").longest_line() == "my heart is dead im such a fool"

def test_concat_multiple_files():
    mfr1 = MultiFileReader("text1.txt")
    combined = mfr1.concat_multiple_files(MultiFileReader("text2.txt"), MultiFileReader("text3.txt"))
    assert combined.filename == "multi_concatenated_output.txt"


def test_get_stats_color():
    assert "\033[91m" in MultiFileReader("text1.txt").get_stats()