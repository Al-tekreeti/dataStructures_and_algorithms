from ..select import select
import pytest

# 1.Test when the asked element position is bigger than the array size
def test_select1(capsys):
    arr1 = [6, 3, 11, 5, 91, 42, 53, 2]
    pos = 10
    select(arr1, pos)
    out, err = capsys.readouterr()
    assert out == "The required element position is beyond the array size\n"

# 2.Test when the asked element position is within the array size
def test_select2():
    arr1 = [6, 3, 11, 5, 91, 42, 53, 2]
    pos = 1
    assert select(arr1, pos) == sorted(arr1)[pos - 1]




if __name__ == "__main__":
    test_select1()
    test_select2()