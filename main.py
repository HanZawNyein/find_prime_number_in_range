def find_prime_number_range(low: int = 2, *, high: int) -> list:
    prime_numbers = []
    for i in range(low, high + 1):
        flag = 0
        if i < 2:
            continue
        if i == 2:
            prime_numbers.append(2)
            continue
        for x in range(2, i):
            if i % x == 0:
                flag = 1
                break
        if flag == 0:
            prime_numbers.append(i)
    return prime_numbers


if __name__ == "__main__":
    while True:
        start: int = int(input("Enter your low (ဘာမှ မထည့်ပဲ enter နိုင်သည်): ") or 0)
        end: int = int(input("Enter your High : "))
        primes: list = find_prime_number_range(low=start, high=end)
        print(f"result : {primes}\n")
