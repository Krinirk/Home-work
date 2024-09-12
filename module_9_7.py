def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result % result == 0 and result != 0:
            print("Простое")
            return result
        else:
            print("Составное")
            return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
