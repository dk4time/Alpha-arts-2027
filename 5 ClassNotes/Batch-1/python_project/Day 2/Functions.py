#fn
def add(a, b=0, *nums, **kwargs):
    print(nums, kwargs)
    return a+b

total = add(10, 20)
print(total)

total = add(10)
print(total)

total = add(10, 20, 1, 2, 3, 4, name="Dineshkumar", age=20)

def a():
    def b():
        pass
    return b
