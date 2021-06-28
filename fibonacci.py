
fib = []
for i in range(0, 45):
    if i <= 1:
        fib.append(i)
    else:
        var = fib[i - 2] + fib[i - 1]
        fib.append(var)
for num in fib:
    print(num)