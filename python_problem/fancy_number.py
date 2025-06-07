def generate_fancy_numbers():
    print("Fancy 4-digit vehicle numbers are:")
    for d1 in range(1, 10):  # 1st digit can't be 0
        for d2 in range(0, 10):
            d3 = d1 - d2
            d4 = d1 + d3
            # Check if d3 and d4 are valid digits (0-9)
            if 0 <= d3 <= 9 and 0 <= d4 <= 9:
                total = d1 + d2 + d3 + d4
                if total == 12:
                    fancy_number = f"{d1}{d2}{d3}{d4}"
                    print(fancy_number)

generate_fancy_numbers()
