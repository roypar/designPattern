import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return

    @classmethod
    def getAll(cls, dbName):
        db = open(dbName, 'r')
        result = []
        json_list = json.loads(db.read())['data']

        for entry in json_list:
            result.append(Person(entry['name'], entry['age']))

        return result
