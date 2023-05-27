# Создайте пользовательский аналог метода map()

collection = range(10)
def my_func(x):
    return x**4

print('map:', list(map(my_func, collection)))

print('Списковое включение:', [my_func(x) for x in collection])

result = []
for item in collection:
    result.append(my_func(item))

print('for:', result)
