import random

# define some responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "what is your name": ["my name is mrs eric bot"],
    "where were you born": ["i was born in a computer ", "still figuring the date i was created"],
    "are you married": ["i am a bot and dont need to be married", "my married status remains unknown to me only"],
    "how are you": ["I'm doing well, thank you.", "I'm good, thanks for asking."],
    "bye": ["Goodbye!", "See you later!", "Farewell!"],
}

# define a function to generate a response


def generate_response(user_input):
    # convert user input to lowercase
    user_input = user_input.lower()
    # check if input matches a response key
    for key in responses.keys():
        if user_input in key:
            return random.choice(responses[key])
    # if no key matches, return a default response
    return "I'm sorry, I didn't understand what you said."


# main loop
while True:
    # get user input
    user_input = input("You: ")
    # generate and print response
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)
