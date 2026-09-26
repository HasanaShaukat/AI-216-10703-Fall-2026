temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

below_normal = 0
normal = 0
high = 0

for temperature in temperatures:
    if temperature < 15:
        print(temperature, "°C - Below Normal")
        below_normal += 1
    elif temperature <= 30:
        print(temperature, "°C - Normal")
        normal += 1
    else:
        print(temperature, "°C - High")
        high += 1

print("Below Normal:", below_normal)
print("Normal:", normal)
print("High:", high)