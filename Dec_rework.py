def print_log(func):
    def status(x):
        st = f'Function {func.__name__} was complete'
        print(st)
        return func(x)

    return status


@print_log
def multi(x):
    return x * x


print(multi(5))
