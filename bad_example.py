def average_age(records):
    total = 0
    for record in records:
        total += record['age']
    return total / len(records)
    


if __name__ == '__main__':
    sample = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Piotr', 'age': 23},
        {'name': 'Maria', 'age': 25},
    ]
    print(average_age(sample))
