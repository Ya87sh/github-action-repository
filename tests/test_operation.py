# Because of __init__.py file in src
# When you import src package, then add and subtract functions are automatically imported
from src import add,sub

# What is pytest:
# It's a testing framework for Python that makes it easy to write and run tests for your code
# pytest automatically finds and runs test files and functions without needing additional configuration
# It looks for files named test_*.py or *_test.py and functions starting with test_

def test_add():
    # The assert statement in Python is used to check if a condition is true.
    # If the condition evaluates to True, the program continues running normally.
    # However, if the condition evaluates to False, Python raises an AssertionError
    # which typically stops the program unless the error is handled.
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1