from src.mathsoperation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,6)==7
    

def test_sub():
    assert sub(2,3)==-1
    assert sub(1,6)==-5
    assert sub(3,1)==1

