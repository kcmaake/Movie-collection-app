print("Welcome!\n")

user_choice = input("Type 'a' to add new movie, 'v' to view movie collection or 'q' to exit: ").lower()

movies = []

while user_choice != 'q':
  if user_choice == 'a':
    user_movie = input("\nEnter movie name: ")
    movies.append(user_movie)

    user_choice = input("\nType 'a' to add new movie, 'v' to view movie collection or 'q' to exit: ").lower()
  elif user_choice == 'v':
    print(movies)

    user_choice = input("\nType 'a' to add new movie, 'v' to view movie collection or 'q' to exit: ").lower()
  else:
    print("\nInvalid option")
    
    user_choice = input("\nType 'a' to add new movie, 'v' to view movie collection or 'q' to exit: ").lower()
