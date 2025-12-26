def sum_mul(n: int, m: int):
    """
    Finds the sum of all multiples of n below m.
    Returns "INVALID" for non-natural numbers.
    """
    if n <= 0 or m <= 0:
        return "INVALID"
    
    return sum(range(n, m, n))
