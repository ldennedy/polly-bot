from statement import Statement
from random import randint

statements = [Statement("Hello!")]

# Function for how the bot should choose a response
def choose_statement(message):
    message_words = message.split()
    # List that will be generated with statements that could fit
    possible_responses = []
    for s in statements:
        for m in message_words:
            if m in s.context:
                # Update context for a statement if an appropriate one was found
                s.context.append(message_words)
                # And add it to the list
                possible_responses.append(s)
    
    # If the list is populated
    if possible_responses:
        # Random selected from specific list
        return possible_responses[randint(0, len(possible_responses)-1)].sentence
    else:
        # Else, random selected from all statements
        return statements[randint(0, len(statements)-1)].sentence

# Main loop for interacting with the bot
user = ""
chosen_s = ""
while user.lower() != "exit":
    chosen_s = choose_statement(user)
    print(chosen_s)
    user = input()
    response_recorded = False
    for s in statements:
        if user == s.sentence:
            response_recorded = True
    if not response_recorded:
        # Update the statments list if it doesn't already exist
        statements.append(Statement(user, chosen_s))
