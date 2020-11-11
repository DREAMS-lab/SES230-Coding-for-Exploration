for base_2_power in range(1,3):
    for N in range(0, 101):
        if N % 2**base_2_power == 0:
            print(N, end = ',')