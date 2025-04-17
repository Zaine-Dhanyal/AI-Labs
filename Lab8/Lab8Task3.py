def smart_door(person, time, has_access=False):
    if time == "Night":
        if person and has_access:
            return "Door is Unlocked"
        return "Door Remains Locked"
    else:
        return "Door Opens" if person else "Door Remains Shut"
motion = input("Is motion detected? (yes/no): ") == "yes"
Time = input("Is it daytime or nighttime? (Day/Night): ")
access= input("Does the person have access? (yes/no): ") == "yes"

print("Door Status:", smart_door(motion, Time, access))
