import json
import hashlib


def hasher(contrasena):
    return hashlib.sha256(str(contrasena).encode('utf8')).hexdigest()


def validate_password(contrasena, contrasena_hash):
    return hasher(contrasena) == contrasena_hash


def user_validate(u, contrasena):
    with open('app/files/users.json', 'r') as file:
        users = json.load(file)
        if u in users:
            return validate_password(contrasena, users[u])
        else:
            return False


def get_all_persons():
    with open('app/files/persons.json', 'r') as file:
        persons = json.load(file)
    return persons


def get_person_by_id(persona_id):
    with open('app/files/persons.json', 'r') as file:
        persons = json.load(file)
    for p in persons:
        if p['id'] == persona_id:
            return p
    return None


def add_person(new_person):
    with open('app/files/persons.json', 'r') as archivo:
        persons = json.load(archivo)
    if not persons:
        new_id = 1
    else:
        new_id = int(max(persons, key=lambda x: x['id'])['id']) + 1
    new_person['id'] = new_id
    persons.append(new_person)
    with open('app/files/persons.json', 'w') as archivo:
        json.dump(persons, archivo, indent=4)


def delete_person(person_id):
    person_id = int(person_id)
    with open('app/files/persons.json', 'r') as file:
        persons = json.load(file)
    persons = [p for p in persons if p['id'] != person_id]
    with open('app/files/persons.json', 'w') as file:
        json.dump(persons, file, indent=4)
