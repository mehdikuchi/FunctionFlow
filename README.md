# Check-FunctionFlow
The library is designed for developers who want to implement a validity check on the order of their function calls.



## Installation

You can install the Check-FunctionFlow from [PyPI](https://pypi.org/project/Check-FunctionFlow/):

    python -m pip install Check-FunctionFlow

## How to use
The code snippet below shows how the Verifier class should be sub-classed in order to define the required pattern to be checked against the usage of the user
```python
    from FunctionFlow import Verifier

    class Verifier_Withorder(Verifier):
        def __init__(self):
            super().__init__()
            
        def validity_check(self):
            if len(self.order)==len(self):
                funcnames = [d for d in self.keys()]
                if self.order.index(funcnames[0])>self.order.index(funcnames[1]):
                    self.order = []
                    raise Exception("Invalid function sequence used")
        
    verify = Verifier_Withorder()
    @verify.addfunc
    def test_sum(a,b):
        return a+b

    @verify.addfunc
    def test_diff(a,b):
        return a-b


    if __name__=="__main__":
        print(test_sum(2,4))
        print(test_diff(2,4))
        try:
            print(test_diff(2,4))
            print(test_sum(2,4))
        except Exception as e:        
            print(str(e))
        
        print(test_sum(2,4))
        print(test_diff(2,4))
```

