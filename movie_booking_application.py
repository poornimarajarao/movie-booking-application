class Movie:
    def __init__(self, name, showtimes, max_seats):
        self.name = name
        #Each showtime has its own seat count
        self.shows = {time: max_seats for time in showtimes}
    
    def available_shows(self):
        for time, seats in self.shows.items():
            print(f"{time} - Available seats: {seats}")
    
    def book_tickets(self, showtime, num_tickets):
        if showtime not in self.shows:
            print("Invalid showtime.")
            return False
        if self.shows[showtime] >= num_tickets:
            self.shows[showtime] -= num_tickets
            print("Booking successful.")
            return True
        else:
            print("Not enough seats available.")
            return False


class User:
    def __init__(self, name):
        self.name = name
        self.bookings = []

    def add_booking(self, movie_name, showtime, num_tickets):
        self.bookings.append({
            'movie': movie_name,
            'showtime': showtime,
            'tickets': num_tickets
        })

    def view_bookings(self):
        if not self.bookings:
            print("No bookings found.")
        else:
            print(f"\n Booking history for {self.name}:")
            for i, b in enumerate(self.bookings, start=1):
                print(f"{i}) {b['movie']} at {b['showtime']} - {b['tickets']} tickets")


class BookingSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}

    def add_movie(self, movie):
        self.movies[movie.name.lower()] = movie

    def register_user(self, username):
        if username.lower() not in self.users:
            self.users[username.lower()] = User(username)
        return self.users[username.lower()]

    def list_movies(self):
        print("\n Available Movies:")
        for i, movie in enumerate(self.movies.values(), start=1):
            print(f"{i}) {movie.name}")
        print()

    def get_movie_by_index(self, index):
        try:
            return list(self.movies.values())[index - 1]
        except IndexError:
            return None

    def run(self):
        print("Welcome to the Movie Booking System [OPP]")
        username = input("Enter your name: ").strip()
        user = self.register_user(username)

        while True:
            print("\n1) View Movies")
            print("2) Book Tickets")
            print("3) My Bookings")
            print("4) Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.list_movies()

            elif choice == '2':
                self.list_movies()
                try:
                    movie_index = int(input("Select a movie by number: "))
                    movie = self.get_movie_by_index(movie_index)
                    if movie:
                        movie.available_shows()
                        showtime = input("Enter desired showtime (example = 10AM): ").strip()
                        num = int(input("How many tickets? "))
                        success = movie.book_tickets(showtime, num)
                        if success:
                            user.add_booking(movie.name, showtime, num)
                    else:
                        print("Invalid movie selection.")
                except ValueError:
                    print("Invalid input.")

            elif choice == '3':
                user.view_bookings()

            elif choice == '4':
                print("Thank you for using the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
                
#Create booking system
system = BookingSystem()

#Add some movies with showtimes
m1 = Movie("The Pursuit of Happyness", ["10AM", "1PM", "4PM"], 100)
m2 = Movie("Zathura: A Space Adventure", ["11AM", "3PM", "6PM"], 80)
m3 = Movie("The Terminal", ["9AM", "12PM", "5PM"], 120)

#Add movies to the system
system.add_movie(m1)
system.add_movie(m2)
system.add_movie(m3)

#Start the app
system.run()

                                                                                                                            
