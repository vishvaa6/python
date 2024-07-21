
my_list = [42, 'hello', 3.14, 'world', 123]

check_element = lambda x: isinstance(x, (int, str))

result = all(check_element(elem) for elem in my_list)

print(f"Are all elements integers or strings? {result}")
