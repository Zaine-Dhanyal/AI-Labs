def traffic_light_agent(light_color):
    if light_color == "Red":
        return "Stop"
    elif light_color == "Yellow":
        return "Slow down"
    elif light_color == "Green":
        return "Move"
    else:
        return "Invalid color"
light = input("Enter traffic light color (Red/Yellow/Green): ")
print("Action:", traffic_light_agent(light))
