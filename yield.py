def fat():
    n = 1
    f = 1
    while True:
        f = f * n
        yield f
        n = n + 1

a = fat()
for i in range(5):
    print(f'fatorial {i+1}: {next(a)}')
    
print('===================')
    
def fib():
    a, b = 1, 1
    while True:
       yield a
       a, b = b, a + b

b = fib()
for i in range(5):
    print(f'fibonnacci {i+1}: {next(b)}')