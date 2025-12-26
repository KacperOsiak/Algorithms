def tribonacci(signature, n):
    if n < len(signature):
        return signature[:n]
    
    while len(signature) < n:
        sum_val = 0
        for value in signature[-3:]:
            sum_val += value
        signature.append(sum_val)
    return signature
