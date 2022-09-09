def prime_factors(num):
    factors = []
    i = 2

    if type(num) != int:
        raise ValueError("illegal symbols used")

    if num % 2 != 0:
        factors.append(num)
        raise ValueError(num, "is a prime number")

    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)

    return factors

print(prime_factors(3958159172))
