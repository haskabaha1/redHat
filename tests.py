from seracherTests import SearcherTests
import pytest


@pytest.mark.filterwarnings('ignore::DeprecationWarning:botocore.*:')
def test_sanityFile():
    """test sanity that checks handlefile functionality
        given: filepath and regex
        expected: given output string"""

    filepath = "-sample.txt"
    reg = "Aya"
    expected = "sample.txt:3:16:Aya"
    s = SearcherTests()
    s.sanityFile(filepath, reg, expected)
    print()


def test_sanityString():
    """test sanity that checks handleString functionality
        given: string and regex
        expected: given output string"""

    string = "This is a COOL string"
    reg = "[A-Z]"
    expected = "user_input:1:0:T"
    s = SearcherTests()
    s.sanityString(string, reg, expected)
    print()
