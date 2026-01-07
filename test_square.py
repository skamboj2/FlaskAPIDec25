from square import get_square

def test_num():
    x=3
    res=get_square(3)
    assert res==9

def test_float():
    x=2.5
    res=get_square(x)
    assert res==6.25

