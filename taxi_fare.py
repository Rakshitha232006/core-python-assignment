def calculate_fare(distance):
    base = 50
    per_km = 10
    return base + (per_km * distance)


trips = [5, 10, 3]
total = 0

for i, d in enumerate(trips, 1):
    fare = calculate_fare(d)
    total += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total}")
