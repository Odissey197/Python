worker = {
    "name": "Иван",
    "fname": "Иванов",
    "age": 25,
    "profession": "Баскетболист",
    "salary": 500_000
}

worker["start_date"] = "12.12.12"

# print(worker)
print(f"{worker['profession']} по имени {worker['name']}, по фамилии {worker['fname']}, которому {worker['age']}, по профессии {worker['profession']}, который получает {worker['salary']}")