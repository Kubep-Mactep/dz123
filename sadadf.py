result = []


def divider(a, b):
    if a < b:
        raise ValueError("Чисельник менше за знаменник")
    if b > 100:
        raise IndexError("Знаменник більше 100")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:

        if not isinstance(key, (int, float)) or not isinstance(value, (int, float)):
            raise TypeError("Ключ і значення повинні бути числовими")

        res = divider(key, value)
        result.append(res)

    except (ValueError, IndexError, TypeError, ZeroDivisionError) as e:
        print(f"Помилка з елементом ({key}: {value}) - {e}")

print("Результат:", result)