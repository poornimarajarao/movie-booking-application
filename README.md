# Movie Booking System (OOP Based - Python)

## What this project is

A simple console-based **Movie Ticket Booking System** built using **Object-Oriented Programming (OOP)** concepts in Python.

---

## What it does

This application allows users to:

- View a list of available movies
- Check showtimes and available seats for each movie
- Book movie tickets for a selected showtime
- Store booking information under each user
- View personal booking history
- Automatically register new users upon login
- Manage seat availability per showtime

Each movie is created as an object of the `Movie` class,
each user is an object of the `User` class,
System is controlled by the `BookingSystem` class.

---

## Class: `Movie`

Manages movie details, available showtimes, and seat availability.

## Constructor (`__init__`)

Initializes a new movie with:

- `name`: Movie name
- `showtimes`: List of showtimes
- `max_seats`: Maximum seats available per showtime each showtime has its own seat count.

## Available Methods

### 1.`available_shows()`

Displays all available showtimes along with remaining seats.

### 2.`book_tickets(showtime, num_tickets)`

Handles ticket booking with:

- Validation of showtime
- Seat availability check
- Updates seat count after successful booking

---

## Class: `User`

Represents an individual user and their booking history.

## Constructor `(__init__)`

- `name`: User’s name
- `bookings`: List to store all bookings made by the user

## Available Methods

### 1.`add_booking(movie_name, showtime, num_tickets)`
Saves booking details (movie, showtime, number of tickets).

### 2.`view_bookings()`
Displays all past bookings for the user.

---

## Class: `BookingSystem`

Controls the overall booking system including movies and users.

## Constructor `(__init__)`

- `movies`: Dictionary to store movies
- `users`: Dictionary to store registered users

## Available Methods

### 1.`add_movie(movie)`
Adds a movie to the system.

### 2.`register_user(username)`
Registers a new user if not already registered.

### 3.`list_movies()`
Displays all available movies.

### 4.`get_movie_by_index(index)`
Retrieves a movie object by its displayed index.

### 5.`run()`
The main loop of the application where the user can:

- View Movies
- Book Tickets
- View My Bookings
- Exit

---

## Example Output

```python
Welcome to the Movie Booking System [OPP]
Enter your name: POORNIMA R

1) View Movies
2) Book Tickets
3) My Bookings
4) Exit
Choose an option: 1

 Available Movies:
1) The Pursuit of Happyness
2) Zathura: A Space Adventure
3) The Terminal


1) View Movies
2) Book Tickets
3) My Bookings
4) Exit
Choose an option: 2

 Available Movies:
1) The Pursuit of Happyness
2) Zathura: A Space Adventure
3) The Terminal

Select a movie by number: 3
9AM - Available seats: 120
12PM - Available seats: 120
5PM - Available seats: 120
Enter desired showtime (example = 10AM): 9AM
How many tickets? 120
Booking successful.

1) View Movies
2) Book Tickets
3) My Bookings
4) Exit
Choose an option: 3

 Booking history for POORNIMA R:
1) The Terminal at 9AM - 120 tickets

1) View Movies
2) Book Tickets
3) My Bookings
4) Exit
Choose an option: 4
Thank you for using the system. Goodbye!
