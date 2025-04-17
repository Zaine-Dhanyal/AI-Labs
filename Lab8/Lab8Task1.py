import random
environment = {
    'A': random.choice([0, 1]),
    'B': random.choice([0, 1]),
    'C': random.choice([0, 1]),
    'D': random.choice([0, 1])
}
def vacuum_cleaner():
    for location, state in environment.items():
        print(f"Location {location} is {'Dirty' if state == 1 else 'Clean'}")
        if state == 1:
            environment[location] = 0
            print(f"Cleaning {location}...")
vacuum_cleaner()
print("Final Environment State:", environment)
