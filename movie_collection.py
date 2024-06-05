print("\n\nWelcome!\n")

movies = []


def main_menu():
  menu = "\nMenu\n--------------------\n1. Add movie\n2. View collection\n3. Search movie\n4. Exit"
  print(menu)

  app_operations()


def navigate():
  nav_menu = "\n1. Add another movie\n2. Main menu\n3. Exit"
  print(nav_menu)
  user_nav = int(input("\nSelect option: "))

  if user_nav == 1:
    user_movie = input("\nEnter name of movie: ").lower()
    movies.append(user_movie)

    navigate()
  elif user_nav == 2:
    main_menu()
  elif user_nav == 3:
    exit()
  else:
    print("\nInvalid option!")
    navigate() 


def app_operations():
  user_choice = int(input("\nSelect option: "))

  while user_choice != 4:
    if user_choice == 1:
      user_movie = input("\nEnter movie name: ").lower()
      movies.append(user_movie)
      print("\nMovie added!")

      navigate()
    elif user_choice == 2:
      print(movies)

      navigate()
    elif user_choice == 3:
      search_movies()
    else:
      print("\nInvalid option")

      main_menu()


def search_movies():
  user_search_query = input("\nEnter movie you want to search for: ").lower()
 
  if user_search_query in movies:
    print("\nMovie found")
    navigate()
  else:
    print("\nMovie not found!")
    navigate()


main_menu()