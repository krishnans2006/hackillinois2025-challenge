import requests

from secret import TOKEN


HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

inputs = requests.get("https://adonix.hackillinois.org/registration/challenge/", headers=HEADERS).json()

print(inputs)

alliances = inputs["alliances"]
people = inputs["people"]

print(len(alliances), len(people))

pantheons = []

for (person1, person2) in alliances:
    person1_pantheon = None
    person2_pantheon = None

    for pantheon in pantheons:
        if person1 in pantheon:
            person1_pantheon = pantheon
        if person2 in pantheon:
            person2_pantheon = pantheon

    if person1_pantheon is None and person2_pantheon is None:
        pantheons.append({person1, person2})
    elif person1_pantheon is not None and person2_pantheon is None:
        person1_pantheon.add(person2)
    elif person1_pantheon is None and person2_pantheon is not None:
        person2_pantheon.add(person1)
    elif person1_pantheon == person2_pantheon:
        continue
    else:
        person1_pantheon.update(person2_pantheon)
        pantheons.remove(person2_pantheon)

    print(pantheons)

for person in people:
    person_pantheon = None

    for pantheon in pantheons:
        if person in pantheon:
            person_pantheon = pantheon

    if person_pantheon is None:
        pantheons.append({person})
        print(pantheons)

print(pantheons)

max_power = 0
max_power_pantheon = None

for pantheon in pantheons:
    power = sum([people[person] for person in pantheon])
    print(power)
    if power > max_power:
        max_power = power
        max_power_pantheon = pantheon

print(max_power, max_power_pantheon)

submission = requests.post("https://adonix.hackillinois.org/registration/challenge/", headers=HEADERS, json={"solution": max_power}).json()

print(submission)
