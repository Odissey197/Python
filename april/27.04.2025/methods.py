worker = {
    "name": "Иван",
    "fname": "Иванов",
    "age": 25,
    "profession": "Баскетболист",
    "salary": 500_000
}

# Метод setdefault
worker.setdefault("age", 0)
worker.setdefault("age", 30)
print(worker)

# Метод pop
name = worker.pop("name")
print(f"Удалили из словаря {name}")
print(worker)

# Метод popitem
name = worker.popitem()
print(f"Удалили из словаря {name}")
print(worker)

# Метод clear
worker.clear()
print(worker)

# # Метод copy
# worker1 = worker
# worker1.clear()
# print(worker)
# print(worker1)

worker1 = worker.copy()
worker1.clear()
print(worker)
print(worker1)