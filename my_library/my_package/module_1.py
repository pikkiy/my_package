# 加算関数
def add(a, b):
    return a + b

# 減算関数
def sub(a, b):
    return a - b

# 乗算関数
def mul(a, b):
    return a * b

# 除算関数
def div(a, b):
    if b == 0:
        raise ValueError("0による除算")
    return a / b