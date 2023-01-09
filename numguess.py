from random import randint


# Generate answer
answer = randint(1,100)

# Print answer for debugging
print(answer)

# User interaction
username = input("Hi there, What is your name?")
print(f"Hi,{username}! Please be my guest!!")
# Get and print User's guess
guess = int(input(f"So {username}, Guess the number(1-100): "))
print(f'Well choice {username}~~ You picked {guess}!!')
