def is_prime(number):

    if number<2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def prime_numbers(n):
    for number in range(2, n + 1):
        if is_prime(number):
            yield number

result = prime_numbers(20)

for number in result:
    print(number)
