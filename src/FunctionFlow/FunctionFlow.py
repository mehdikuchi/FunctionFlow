class wrapper(object):
    def __init__(self, fun) -> None:
        self.fun = fun
        self.data = []
        self.name = fun.__name__

    def manage_args(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        self.manage_args(*args, **kwargs)
        return self.fun(*args)


class Verifier(dict):
    def __init__(self):
        super(Verifier, self).__init__()
        self.order = []

    def addfun(self, fun):
        self.update({fun.__name__: wrapper(fun)})

        def wrapperfun(*args, **kwargs):
            if fun.__name__ in self.order:
                self.order.pop(self.order.index(fun.__name__))
                self.order.append(fun.__name__)
            else:
                self.order.append(fun.__name__)

            self.validity_check()
            return self[fun.__name__](*args, **kwargs)
        return wrapperfun

    def validity_check(self):
        pass
