def book_seat(booked, seat, total):
    if seat not in booked and 1 <= seat <= total:
        booked.append(seat)
    return booked


def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    return booked


def available_seats(total, booked):
    return [s for s in range(1, total + 1) if s not in booked]


total_seats = 10
booked_seats = [2, 5, 7]
booked_seats = book_seat(booked_seats, 3, total_seats)
booked_seats = cancel_seat(booked_seats, 5)
print("Available seats:", available_seats(total_seats, booked_seats))
