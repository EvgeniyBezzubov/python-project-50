import gendiff.scripts.gendiff as gendiff
import json
import pytest
def test_reverse():
    print(str(gendiff.generate_diff("file1.json", "file2.json"))=="{'- follow': False, 'host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}")

    assert gendiff.generate_diff("file1.json", "file2.json") == "{'- follow': False, 'host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True}"
