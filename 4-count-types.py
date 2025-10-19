def count_types(arr):
    cnt = {} 
    for value in arr:
        type_name = type(value).__name__ 
        cnt[type_name] = cnt.get(type_name, 0) + 1
    return cnt

if __name__ == "__main__":
    array = [True, "hello", 6, 13.17, "laba", False, 1, 10, None]
    result = count_types(array)
    print(f"Результат підрахунку: {result}")
