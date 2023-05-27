def retry(attempts=5, desired_value=None):
    def decorator(func):
        def wrapper(n):
            for i in range(attempts):
                n = func(n)
                if n == desired_value:
                    return f'получили {n} за {i} итераций'
            if desired_value is not None and n != desired_value:
                return f'не удалось достичь желаемого значения, текущее {n}'
            else:
                return f'{n}'

        return wrapper

    return decorator


@retry(3, 8)
def foo(n):
    print(f'{n} + {n}')
    return n + n


print(foo(2))
