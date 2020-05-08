#import pytest
from madlib_lab.madlib import file_initial_read,split_content,merge

def test_file_initial_read():
    actual = file_initial_read('madlib_lab/assets/Contents.txt')
    expected = "A {Adjective} and {Noun} and {Adjective}"
    assert actual == expected

def test_split_content():
    actual = split_content('A {Adjective} and  {Noun} and {Adjective}')
    expected = ['Adjective', 'Noun'],"A {} and  {} and {}"
    assert actual == expected

def test_merge():
    actual = merge(['Rose', 'Beautifull','Fragrent'],'A {} and  {}')
    expected = "A Rose and  Beautifull and Fragrent"
    assert actual == expected