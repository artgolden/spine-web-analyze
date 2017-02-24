def fibonachi(a, b, i, end):
    print b
    if i <= end:
        fibonachi(b, a + b, i + 1, end)
fibonachi(0,1, 2, 20)
