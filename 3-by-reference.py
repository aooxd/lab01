def inc_obj(obj):
    if isinstance(obj, dict) and "n" in obj:
        obj["n"] += 1

if __name__ == "__main__":
    obj = {"n": 5}
    inc_obj(obj)
    print(f"Оновлений об'єкт: {obj}")
