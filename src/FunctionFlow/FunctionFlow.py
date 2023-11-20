class wrapper(object):
    def __init__(self, func) -> None:
        self.func = func
        self.data = []
        self.name = func.__name__

    def manage_args(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        self.manage_args(*args, **kwargs)
        return self.func(*args)


class Verifier(dict):
    def __init__(self):
        super(Verifier, self).__init__()
        self.order = []

    def addfunc(self, func):
        self.update({func.__name__: wrapper(func)})

        def wrapperfunc(*args, **kwargs):
            if func.__name__ in self.order:
                self.order.pop(self.order.index(func.__name__))
                self.order.append(func.__name__)
            else:
                self.order.append(func.__name__)

            self.validity_check()
            return self[func.__name__](*args, **kwargs)
        return wrapperfunc

    def validity_check(self):
        pass
