import random
try:
    from colorama import init, Fore, Back, Style
    init()
except:
    print("an error has occured! Please install the colorama package!")
    exit(0)

AFFIRMATIVE_ANSWERS = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely."
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes."
]
NON_COMMITTAL_ANSWERS = [
    "Reply hazy try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again."
]
NEGATIVE_ANSWERS = [
    "Don\'t count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

def answer():
    answer_type = random.randint(0, 3)
    if answer_type == 3:
        print(Fore.GREEN + random.choice(AFFIRMATIVE_ANSWERS))
        print(Style.RESET_ALL)
    elif answer_type == 2:
        print(Fore.YELLOW + random.choice(NON_COMMITTAL_ANSWERS))
        print(Style.RESET_ALL)
    else:
        print(Fore.RED + random.choice(NEGATIVE_ANSWERS))
        print(Style.RESET_ALL)

print("Just type a question and hit enter!\nIf you need to exit the program at anytime just input \"exit\".")
while True:
    question = input("\nAsk me a question...\n> ")
    if question.lower() == "exit":
        break
    else:
        answer()
