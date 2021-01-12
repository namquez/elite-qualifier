import random
quit = "bye"
user_input = ""
pos_response = False
neg_response = False
greet_response = False
thank_response = False
botname_response = False
idk_response = False
mood_response = False
eat_response = False
fun_response = False
bye_response = False
joke_response = False

def generate_pos_response(user_input):
  responses = [
    "Glad to hear!",
    "You don't say!",
    "That's quite fancy!",
    "Nice lad!!"
  ]
  return random.choice(responses)

def generate_neg_response(user_input):
  responses = [
    "Sorry to hear!",
    "Oh no! Here, take some figgy pudding :)",
    "I hope you feel better!",
    "Here, take a crumpet!"
  ]
  return random.choice(responses)

def generate_greet_response(user_input):
  responses = [
    "Why hello there!",
    "G'day!",
    "How do you do?",
    "Sup bruv?"
  ]
  return random.choice(responses)

def generate_thank_response(user_input):
  responses = [
    "No problem!",
    "You're welcome!",
    "Of course!",
    "No, thank you for chatting with me!"
  ]
  return random.choice(responses)

def generate_botname_response(user_input):
  responses = [
    "I am Oliver!",
    "Oliver's the name!",
    "My name is Oliver, and I am your personal British chat bot!",
    "My full name is Oliver Charleston Harry Rupert Scrivener, but you can call me Oliver!"
  ]
  return random.choice(responses)

def generate_idk_response(user_input):
  responses = [
    "Who do you think I am, Google? I'm just a simple chat bot created by a 16 year old, so please, speak in simpler terms.",
    "I'm not too sure what you mean.",
    "I'm not coded well enough to respond to that.",
    "I cannot respond to that."
  ]
  return random.choice(responses)+(" Consider using correct grammar or asking me one of these questions instead: \n'what do you like to eat?'\n'what do you do for fun?'\n'how are you?'\n'who are you?'\n'tell me a joke'")

def generate_mood_response(user_input):
  responses = [
    "I'm doing swell, thank's for asking! How are you?",
    "I'm doing great, how about you?",
    "I'm good, thank you. Whats good with you?",
    "I'm doing fine, and you?"
  ]
  return random.choice(responses)

def generate_eat_response(user_input):
  responses = [
    "Fish and Chips are my favorite!",
    "I like to eat figgy pudding. A lot of figgy pudding.",
    "Have you ever tried Cottage Pie? It's the best.",
    "Chips and biscuits. Not 'fries' and 'cookies'."
  ]
  return random.choice(responses)

def generate_fun_response(user_input):
  responses = [
    "I like to eat figgy puddding in my free time!",
    "I like to play Minecraft.",
    "Sometimes I just like to sit back and drink a nice cup of tea.",
    "Talking to you is pretty fun!"
  ]
  return random.choice(responses)

def generate_joke_response(user_input):
  responses = [
    "What does the Loch Ness monster eat? Fish and ships.",
    "Why can British people lose weight faster? Because every time they buy something, they lose some pounds!",
    "Why don’t you ever see penguins in Great Britain? Because they’re scared of Wales!",
    "What are British people’s favorite nuts? Chess Nuts"
  ]
  return random.choice(responses)


print("G'day! I am Oliver the British chat bot. How do you do?")

while quit != True:

  user_input = str.lower(input(""))
  user_input = str.strip(user_input)
  if user_input == "good" or user_input == "well" or user_input == "great" or   user_input == "awesome" or user_input == "i'm good" or user_input == "i'm great" or   user_input == "i'm awesome" or user_input == "i'm doing well" or user_input == "nice" or   user_input == "cool" or user_input == "haha" or user_input == "lol" or   user_input == "ha" or user_input == "cool" or user_input == "sweet" or   user_input == "yes":
    pos_response = True
  elif user_input == "bad" or user_input == "sad" or user_input == "not good" or user_input == "not happy" or user_input == "upset" or user_input == "i'm sad" or user_input == "i'm not good" or user_input == "i'm not happy" or user_input == "i'm upset" or user_input == "no":
    neg_response = True
  elif user_input == "hello" or user_input == "good morning" or user_input == "hey" or user_input == "sup" or user_input == "hi" or user_input == "what's up" or user_input == "yo":
    greet_response = True
  elif user_input == "thanks" or user_input == "thank you":
    thank_response = True
  elif user_input == "who are you" or user_input == "what's your name" or user_input == "who are you?" or user_input == "what's your name?" or user_input == "what are you called" or user_input == "what are you called?" or user_input == "what do I call you?" or user_input == "what do I call you" or user_input == "what is your name" or user_input == "what is your name?":
    botname_response = True
  elif user_input == "how are you" or user_input == "how do you feel" or user_input == "what's up?" or user_input == "how are you doing?" or user_input == "how is life" or user_input == "how are you?" or user_input == "how is life?" or user_input == "how are you doing" or user_input == "how do you feel?":
    mood_response = True
  elif user_input == "what do you like to eat" or user_input == "what do you like to eat?" or user_input == "what is your favorite food" or user_input == "what is your favorite food?" or user_input == "what do you eat?" or user_input == "what do you eat":
    eat_response = True
  elif user_input == "what do you do for fun" or user_input == "what do you do for fun?" or user_input == "what do you like to do for fun" or user_input == "what do you like to do for fun?" or user_input == "fun?" or user_input == "fun":
    fun_response = True
  elif user_input == "bye" or user_input == "cya" or user_input == "bye bye" or user_input == "talk to you later" or user_input == "see you later" or user_input == "goodbye" or user_input == "bye!" or user_input == "cheerio" or user_input == "goodbye!":
    bye_response = True
  elif user_input == "joke" or user_input == "can you tell me a joke?" or user_input == "tell me a joke" or user_input == "please say a joke" or user_input == "please tell me a joke":
    joke_response = True
  else:
    idk_response = True

  if pos_response==True:
    print(generate_pos_response(user_input))
    pos_response = False
  elif neg_response ==True:
    print(generate_neg_response(user_input))
    neg_response = False  
  elif greet_response == True:
    print(generate_greet_response(user_input))
    greet_response = False
  elif thank_response ==True:
    print(generate_thank_response(user_input))
    thank_response = False
  elif botname_response == True:
    print(generate_botname_response(user_input))
    botname_response = False    
  elif idk_response == True:
    print(generate_idk_response(user_input))
    idk_response = False
  elif mood_response == True:
    print(generate_mood_response(user_input))
    mood_response = False
  elif eat_response == True:
    print(generate_eat_response(user_input))
    eat_response = False
  elif fun_response == True:
    print(generate_fun_response(user_input))
    fun_response = False
  elif joke_response == True:
    print(generate_joke_response(user_input))
    joke_response = False
  elif bye_response == True:
    print("Cheerio!")
    quit = True

