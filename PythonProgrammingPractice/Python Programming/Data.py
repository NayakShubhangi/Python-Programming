user_num = int(input("Enter the number of people coming to watch a movie: "))
for i in range(len(user_num)):
    movie_names = [i for i in input("Enter the names of the movies (separated by only a space): ").split()]
    ticket_num = int(input("Enter how many tickets you would like: "))
    movies_available = {"Avengers", "Spiderman", "Ironman"}
    num_available_seats = 30
    for i in movie_names:
        if(i not in movies_available):
            print("We don't have that movie available.")
            print(f"Here are the movies we have available: {movies_available}")
            user_continue = input("Are you interested in the movies available (enter yes or no): ").lower()
            if(user_continue == "yes"):
                movie_num = int(input("Enter the number of movies you would like to watch: "))
                movie_names = [i for i in input("Enter the names of the movies (separated by only a space): ").split()]
                ticket_num = int(input("Enter how many tickets you would like: "))
            elif(user_continue == "no"):
                break
            else:
                print("I did not get a valid response.")
    if(ticket_num>num_available_seats):
        print("We don't have that many seats available.")
    print("Thank you for coming.")