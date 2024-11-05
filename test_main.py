import pytest
from main import printName
from io import StringIO
import sys

def test_printName(capsys):
    printName("Merhaba")
    captured = capsys.readouterr()
    assert captured.out == "Hello Merhaba\n"

