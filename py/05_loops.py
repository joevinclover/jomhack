


num = 5
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

for num in range(2, limit +1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
