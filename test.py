def test0(*args):
    print(args)
    
def test(*args):
    test0(*args)
    
    
test(1,22,3,4,5,6)