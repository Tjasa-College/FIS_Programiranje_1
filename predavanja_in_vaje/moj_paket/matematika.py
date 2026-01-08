def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("n mora biti celo število (int).")
    if n < 0:
        raise ValueError("n mora biti >= 0.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def faktorial(n):
    if not isinstance(n, int):
        raise ValueError("n mora biti celo število (int).")
    if n < 0:
        raise ValueError("n mora biti >= 0.")

    fakt = 1
    for i in range(2, n + 1):
        fakt *= i
    return fakt
