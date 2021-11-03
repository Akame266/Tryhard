def funcforvalue(*args):  # То что надо эту функции выпихнуть в другой файл знаю, сделал для удобства
    for i in args:
        if type(i) is not int and type(i) is not float:
            return False
    return args


def p_log(cond, msg):
    from functools import wraps

    def outer(func):
        @wraps(func)
        def inside(*args):
            assert cond(*args), msg
            # status = f'function {func.__name__} was complete'  если нужно чтоб выводилась инфа только о корректно
            # завершенной функции
            # print(status)
            return func(*args)

        status = f'function {func.__name__} was complete'
        print(status)
        return inside

    return outer


@p_log(funcforvalue, 'Wrong value')
def multi(*args):
    """последовательное перемножение"""
    a = 1
    for i in args:
        a *= i
    return a


# print(multi(1.1, 2, 3, 4, 1.1, 1))
print(multi(1.1, 2, 3, 4, 1.1, 'fa'))
