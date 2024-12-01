def restaurant_bot():
    print("Welcome to Gourmet Restaurant!")
    print("I'm here to help you reserve a table.")

    # collect reservation details
    name = input("May I have your name, please? ")
    date = input(f"Hi {name}, what date would you like to book a table? (e.g., DD-MM-YYYY): ")
    time = input("At what time? (e.g., 19:00): ")
    people = input("For how many people? ")
    phone = input("Lastly, your phone number, please: ")

    # print confirm the reservation
  

# run chatbot
restaurant_bot()