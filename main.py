from statement import Statement
from random import randint

statements = [Statement("Hello!")]

def choose_statement(message):
    message_words = message.split()
    possible_responses = []
    for s in statements:
        for m in message_words:
            if m in s.context:
                s.context.append(message_words)
                possible_responses.append(s)
    
    if possible_responses:
        return possible_responses[randint(0, len(possible_responses)-1)].sentence
    else:
        return statements[randint(0, len(statements)-1)].sentence

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
        statements.append(Statement(user, chosen_s))
