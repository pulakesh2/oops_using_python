import threading


class MovieTicketBookingSystem:
    # TODO: Initialises lock,total seats and available seats for reservation
    def __init__(self, total_seats):
        self.available_seats = total_seats
        self.lock = threading.Lock()
        self.total_seats = total_seats


    def reserve_seats(self, num_seats):
        # TODO: acquire the lock before starting the operation and write the logic to reserve seats
        with self.lock:
            if (self.available_seats - num_seats) > 0:
                self.available_seats -= num_seats
                return True
            else:
                return False

    def get_available_seats(self):
        with self.lock:
            return self.available_seats


def book_seats(booking_system, num_seats):
    success = booking_system.reserve_seats(num_seats)
    if success:
        print(f"Successfully booked {num_seats} seats")
    else:
        print(f"Failed to book {num_seats} seats")