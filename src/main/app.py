from src.main.lab import invoke_basic_chain, invoke_complex_chain

if __name__ == "__main__":
    try:
        choice = int(input("Enter 1 to test the basic chain, 2 to test the complex chain: "))
    except ValueError:
        print("Invalid input. Exiting.")
        exit()
    if choice == 1:
        topic = input("Enter a topic: ")
        response = invoke_basic_chain(topic)
        print(response)
        exit()
    elif choice == 2:
        movie = input("Enter a movie: ")
        response = invoke_complex_chain(movie)
        print(response)
        exit()