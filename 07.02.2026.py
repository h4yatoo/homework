def h(n, a, b):
    if n:
        h(n-1, a, 6-a-b)
        print(a, "->", b)
        h(n-1, 6-a-b, b)
h()