from mccurrencyhelper import helperfunctions as hf

def test_reduce():
    assert hf.reduce([0,9,4,0,9]) == [1,1,0,1,0]

def test_add():
    assert hf.add([1,1,1,1,1], [1,1,1,1,1]) == [2,2,2,2,2]
    assert hf.add([0,8,3,0,8], [0,0,1,0,1]) == [1,0,0,1,0]

def test_subtract():
    assert hf.subtract([1,1,1,1,1], [1,1,1,1,1]) == [0,0,0,0,0]
    assert hf.subtract([1,0,0,1,0], [0,1,0,0,1]) == [0,8,0,0,8]
    assert hf.subtract([0,1,0,0,0], [0,0,1,0,0]) == [0,0,3,0,0]

def test_lessthan():
    assert hf.lessthan([1,0,0,0,0], [2,0,0,0,0]) == True
    assert hf.lessthan([2,0,0,0,0], [1,0,0,0,0]) == False

def test_greaterthan():
    assert hf.greaterthan([1,0,0,0,0], [2,0,0,0,0]) == False
    assert hf.greaterthan([2,0,0,0,0], [1,0,0,0,0]) == True