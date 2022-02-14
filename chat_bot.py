# asking name of user to start conversation
bot = 'Jerry' 
user_name = (input(f"{bot}: What is your name? \n You: ")).capitalize()

# restriction on user_name
#if user_name:


print(f"{bot}: Hello {user_name}!")
print(f"{bot}: My momma called me {bot} because she love this name.")
print(f"{bot}: By the way {user_name} is also a very beautiful name, I love it!\n")

# taking about user's mood
mood_list = {'funny' : 'Wow that\'s great, Let me tell you a joke!',
             'sad' : 'Oh no, I\'m sorry to hear that, Tell me what can I do for you, if anything',
             'angry' : 'Oh no, I\'m sorry to hear that, Tell me what can I do for you, if anything',
             'happy' : 'Oh Wow, I\'m happy too!',
             'excited' : 'Oh Wow, I can\'t stop myself to here, why you are excited',}

try:
    input_mood = input(f"{bot}: How are you feeling today? \n You: ")
    print(f"{bot}: {mood_list[input_mood.lower()]}")
except KeyError :
    print(f"{bot}: I'm sorry {user_name}, I did not learn that mood yet. You can choose from the following:")
    for key in mood_list:
        print(f"{key}")
except :
    print(f'{bot}: Sorry, I did not understand that. Please try again.')

# creating conversation dictionary
response_dict = {'What is your name?' : f"{bot}: My name is {bot}",
                'How are you feeling today?' : f"{bot}: I'm feeling great, thanks for asking",
                'color' : f"{bot}: My favorite color is blue",
                'food' : f"{bot}: My favorite food is pizza",
                'movie' : f"{bot}: My favorite movie is Sanam Teri Kasam",
                'song' : f"{bot}: My favorite song is Ajanabi by Bhuvan Bam",
                'sport' : f"{bot}: My favorite sport is cricket",
                'animal' : f"{bot}: My favorite animal is dog",
                'book' : f"{bot}: My favorite book is Talking to Human by Frank Rimalovski",
}

flag = True
while flag == True:
    new_input = input(f"{bot}: Ask me something about me hehe...\n You: ")
    if new_input.lower() == 'stop':
        print(f'{bot}: Ok, bye.... \n {bot}: See you next time')
    else:
        if new_input in response_dict[new_input]:
            try:
                print(f"{bot}: {response_dict[new_input]}")
            except KeyError:
                print(f'{bot}: Sorry, I have not learnt this yet I hope my programmer will train me for this soon' )
        else:
            print(f"{bot}: Sorry, I did not understand that. Please try again.")
        