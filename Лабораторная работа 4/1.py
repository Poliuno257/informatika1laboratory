import json


def task() -> float:
    fname = "input.json"
    with open(fname) as file:
        data = json.load(file)  # читает json файл


    tyt = [g["score"]*g["weight"] for g in data]
    return round(sum(tyt), 3)

print(task())