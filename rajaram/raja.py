import datetime
import pytest
@pytest.fixture
def fun_time():
    datetime_object=datetime.datetime.now()
    print(datetime_object)
def test_set(fun_time):
    set1={1,3,4}
    set2={1,3,4}
    if set1==set2:
        print(set1)
    else:
        print("not equal")

@pytest.mark.parametrize('num,result',[(1,1,),(2,2,),(3,6),(4,24),(5,120)])
def test_fact(num,result,fun_time):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
    assert fact==result
def test_search(fun_time):
    name="rajaram"
    l=["rajaram","mohan","HCL"]
    if name in l:
        print(name)
    else:
        print("not present")