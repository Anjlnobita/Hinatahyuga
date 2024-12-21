import random
import threading
from typing import Union
from Hinatahyuga.modules.sql import nobita, client

DEFAULT_WELCOME = "Hey {first}, how are you?"
DEFAULT_GOODBYE = "Nice knowing ya!"

DEFAULT_WELCOME_MESSAGES = [
    "{first} is here!",
    "Ready player {first}",
    "Genos, {first} is here.",
    "A wild {first} appeared.",
    "{first} came in like a Lion!",
    "{first} has joined your party.",
    "Arre dekho dekho koun aaya\n{first} aaya {first} aaya",
    "{first} just joined. Can I get a heal?",
    "{first} just joined the chat - asdgfhak!",
    "{first} just joined. Everyone, look busy!",
    "Welcome, {first}. Stay awhile and listen.",
    "Welcome, {first}. We were expecting you ( ͡° ͜ʖ ͡°)",
    "Welcome, {first}. We hope you brought pizza.",
    "Welcome, {first}. Leave your weapons by the door.",
    "Swoooosh. {first} just landed.",
    "Brace yourselves. {first} just joined the chat.",
    "{first} just joined. Hide your bananas.",
    "{first} just arrived. Seems OP - please nerf.",
    "{first} just slid into the chat.",
    "A {first} has spawned in the chat.",
    "Big {first} showed up!",
    "Where’s {first}? In the chat!",
    "{first} hopped into the chat. Kangaroo!!",
    "{first} just showed up. Hold my beer.",
    "Challenger approaching! {first} has appeared!",
    "It's a bird! It's a plane! Nevermind, it's just {first}.",
    "It's {first}! Praise the sun! \o/",
    "Never gonna give {first} up. Never gonna let {first} down.",
    "Ha! {first} has joined! You activated my trap card!",
    "Hey! Listen! {first} has joined!",
    "We've been expecting you {first}",
    "It's dangerous to go alone, take {first}!",
    "{first} has joined the chat! It's super effective!",
    "Cheers, love! {first} is here!",
    "{first} is here, as the prophecy foretold.",
    "{first} has arrived. Party's over.",
    "{first} is here to kick butt and chew bubblegum. And {first} is all out of gum.",
    "Hello. Is it {first} you're looking for?",
    "{first} has joined. Stay awhile and listen!",
    "Roses are red, violets are blue, {first} joined this chat with you",
    "Welcome {first}, Avoid Punches if you can!",
    "It's a bird! It's a plane! - Nope, its {first}!",
    "{first} Joined! - Ok.",
    "All Hail {first}!",
    "Hi, {first}. Don't lurk, only Villans do that.",
    "{first} has joined the battle bus.",
    "A new Challenger enters!",
    "Ok!",
    "{first} just fell into the chat!",
    "Something just fell from the sky! - oh, its {first}.",
    "{first} Just teleported into the chat!",
    "Hi, {first}, show me your Hunter License!",
    "I'm looking for Garo, oh wait nvm it's {first}.",
    "Welcome {first}, leaving is not an option!",
    "Run Forest! ..I mean...{first}.",
    "{first} do 100 push-ups, 100 sit-ups, 100 squats, and 10km running EVERY SINGLE DAY!!!",
    "Huh?\nDid someone with a disaster level just join?\nOh wait, it's just {first}.",
    "Hey, {first}, ever heard the King Engine?",
    "Hey, {first}, empty your pockets.",
    "Hey, {first}!, are you strong?",
    "Call the Avengers! - {first} just joined the chat.",
    "{first} joined. You must construct additional pylons.",
    "Ermagherd. {first} is here.",
    "Come for the Snail Racing, Stay for the Chimichangas!",
    "Who needs Google? You're everything we were searching for.",
    "This place must have free WiFi, cause I'm feeling a connection.",
    "Speak friend and enter.",
    "Welcome you are",
    "Welcome {first}, your princess is in another castle.",
    "Hi {first}, welcome to the dark side.",
    "Hola {first}, beware of people with disaster levels",
    "Hey {first}, we have the droids you are looking for.",
    "Hi {first}\nThis isn't a strange place, this is my home, it's the people who are strange.",
    "Oh, hey {first} what's the password?",
    "Hey {first}, I know what we're gonna do today",
    "{first} just joined, be at alert they could be a spy.",
    "{first} joined the group, read by Mark Zuckerberg, CIA and 35 others.",
    "Welcome {first}, watch out for falling monkeys.",
    "Everyone stop what you’re doing, We are now in the presence of {first}.",
    "Hey {first}, do you wanna know how I got these scars?",
    "Welcome {first}, drop your weapons and proceed to the spy scanner.",
    "Stay safe {first}, Keep 3 meters social distances between your messages.",
    "Hey {first}, Do you know I once One-punched a meteorite?",
    "You’re here now {first}, Resistance is futile",
    "{first} just arrived, the force is strong with this one.",
    "{first} just joined on president’s orders.",
    "Hi {first}, is the glass half full or half empty?",
    "Yipee Kayaye {first} arrived.",
    "Welcome {first}, if you’re a secret agent press 1, otherwise start a conversation",
    "{first}, I have a feeling we’re not in Kansas anymore.",
    "They may take our lives, but they’ll never take our {first}.",
    "Coast is clear! You can come out guys, it’s just {first}.",
    "Welcome {first}, pay no attention to that guy lurking.",
    "Welcome {first}, may the force be with you.",
    "May the {first} be with you.",
    "{first} just joined. Hey, where's Perry?",
    "{first} just joined. Oh, there you are, Perry.",
    "Ladies and gentlemen, I give you ...  {first}.",
    "Behold my new evil scheme, the {first}-Inator.",
    "Ah, {first} the Platypus, you're just in time... to be trapped.",
    "{first} just arrived. Diable Jamble!",
    "{first} just arrived. Aschente!",
    "{first} say Aschente to swear by the pledges.",
    "{first} just joined. El Psy congroo!",
    "Irasshaimase {first}!",
    "Hi {first}, what is 1000-7?",
    "Come. I don't want to destroy this place",
    "I... am... Whitebeard!...wait..wrong anime.",
    "Hey {first}...have you ever heard these words?",
    "Can't a guy get a little sleep around here?",
    "It's time someone put you in your place, {first}.",
    "Unit-01's reactivated..",
    "Prepare for trouble...And make it double",
    "Hey {first}, are You Challenging Me?",
    "Oh? You're Approaching Me?",
    "Ho… mukatta kuruno ka?",
    "I can't beat the shit out of you without getting closer",
    "Ho ho! Then come as close as you'd like.",
    "Hoho! Dewa juubun chikazukanai youi",
    "Guess who survived his time in Hell, {first}.",
    "How many loaves of bread have you eaten in your lifetime?",
    "What did you say? Depending on your answer, I may have to kick your ass!",
    "Oh? You're approaching me? Instead of running away, you come right to me? Even though your grandfather, Joseph, told you the secret of The World, like an exam student scrambling to finish the problems on an exam until the last moments before the chime?",
    "Rerorerorerorerorero.",
    "{first} just warped into the group!",
    "I..it's..it's just {first}.",
    "Sugoi, Dekai. {first} Joined!",
    "{first}, do you know gods of death love apples?",
    "I'll take a potato chip.... and eat it",
    "Oshiete oshiete yo sono shikumi wo!",
    "Kaizoku ou ni...nvm wrong anime.",
    "{first} just joined! Gear.....second!",
    "Omae wa mou....shindeiru",
    "Hey {first}, the leaf village lotus blooms twice!",
    "{first} Joined! Omote renge!",
    "{first}! I, Madara! declare you the strongest",
    "{first}, this time I'll lend you my power. ",  # Kyuubi to naruto
    "{first}, welcome to the hidden leaf village!",  # Naruto thingies end here
    "In the jungle, you must wait...until the dice read five or eight.",  # Jumanji stuff
    "Dr.{first} Famed archeologist and international explorer,\nWelcome to Jumanji!\nJumanji's Fate is up to you now.",
    "{first}, this will not be an easy mission - monkeys slow the expedition.",  # End of Jumanji stuff
    "Remember, remember, the Fifth of November, the Gunpowder Treason and Plot. I know of no reason why the Gunpowder Treason should ever be forgot.",  # V for Vendetta
    "The only verdict is vengeance; a vendetta, held as a votive not in vain, for the value and veracity of such shall one day vindicate the vigilant and the virtuous.",  # V for Vendetta
    "Behind {first} there is more than just flesh. Beneath this user there is an idea... and ideas are bulletproof.",  # V for Vendetta
    "Love your rage, not your cage.",  # V for Vendetta
    "Get your stinking paws off me, you damned dirty ape!",  # Planet of the apes
    "Elementary, my dear {first}.",
    "I'm back - {first}.",
    "Bond. {first} Bond.",
    "Come with me if you want to live",
]
DEFAULT_GOODBYE_MESSAGES = [
    "{first} will be missed.",
    "{first} just went offline.",
    "{first} has left the lobby.",
    "{first} has left the clan.",
    "{first} has left the game.",
    "{first} has fled the area.",
    "{first} is out of the running.",
    "Nice knowing ya, {first}!",
    "It was a fun time {first}.",
    "We hope to see you again soon, {first}.",
    "I donut want to say goodbye, {first}.",
    "Goodbye {first}! Guess who's gonna miss you :')",
    "Goodbye {first}! It's gonna be lonely without ya.",
    "Please don't leave me alone in this place, {first}!",
    "Good luck finding better shit-posters than us, {first}!",
    "You know we're gonna miss you {first}. Right? Right? Right?",
    "Congratulations, {first}! You're officially free of this mess.",
    "{first}. You were an opponent worth fighting.",
    "You're leaving, {first}? Yare Yare Daze.",
    "Bring him the photo",
    "Go outside!",
    "Ask again later",
    "Think for yourself",
    "Question authority",
    "You are worshiping a sun god",
    "Don't leave the house today",
    "Give up!",
    "Marry and reproduce",
    "Stay asleep",
    "Wake up",
    "Look to la luna",
    "Steven lives",
    "Meet strangers without prejudice",
    "A hanged man will bring you no luck today",
    "What do you want to do today?",
    "You are dark inside",
    "Have you seen the exit?",
    "Get a baby pet it will cheer you up.",
    "Your princess is in another castle.",
    "You are playing it wrong give me the controller",
    "Trust good people",
    "Live to die.",
    "When life gives you lemons reroll!",
    "Well, that was worthless",
    "I fell asleep!",
    "May your troubles be many",
    "Your old life lies in ruin",
    "Always look on the bright side",
    "It is dangerous to go alone",
    "You will never be forgiven",
    "You have nobody to blame but yourself",
    "Only a sinner",
    "Use bombs wisely",
    "Nobody knows the troubles you have seen",
    "You look fat you should exercise more",
    "Follow the zebra",
    "Why so blue?",
    "The devil in disguise",
    "Go outside",
    "Always your head in the clouds",
]

INSERTION_LOCK = threading.RLock()

class Welcome:
    def __init__(self, chat_id, should_welcome=True, should_goonobitaye=True):
        self.chat_id = chat_id
        self.should_welcome = should_welcome
        self.should_goonobitaye = should_goonobitaye
        self.custom_content = None
        self.custom_welcome = random.choice(DEFAULT_WELCOME_MESSAGES)
        self.welcome_type = "text"
        self.custom_leave = DEFAULT_GOODBYE
        self.leave_type = "text"
        self.clean_welcome = None

    def save(self):
        nobita.welcome_pref.update_one({'chat_id': self.chat_id}, {'$set': self.__dict__}, upsert=True)

class WelcomeButtons:
    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = chat_id
        self.name = name
        self.url = url
        self.same_line = same_line

    def save(self):
        nobita.welcome_urls.update_one({'chat_id': self.chat_id, 'name': self.name}, {'$set': self.__dict__}, upsert=True)

class GoonobitayeButtons:
    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = chat_id
        self.name = name
        self.url = url
        self.same_line = same_line

    def save(self):
        nobita.leave_urls.update_one({'chat_id': self.chat_id, 'name': self.name}, {'$set': self.__dict__}, upsert=True)

class WelcomeMute:
    def __init__(self, chat_id, welcomemutes):
        self.chat_id = chat_id
        self.welcomemutes = welcomemutes

    def save(self):
        nobita.welcome_mutes.update_one({'chat_id': self.chat_id}, {'$set': self.__dict__}, upsert=True)

class WelcomeMuteUsers:
    def __init__(self, user_id, chat_id, human_check):
        self.user_id = user_id
        self.chat_id = chat_id
        self.human_check = human_check

    def save(self):
        nobita.human_checks.update_one({'user_id': self.user_id, 'chat_id': self.chat_id}, {'$set': self.__dict__}, upsert=True)

class CleanServiceSetting:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.clean_service = True

    def save(self):
        nobita.clean_service.update_one({'chat_id': self.chat_id}, {'$set': self.__dict__}, upsert=True)

def welcome_mutes(chat_id):
    return nobita.welcome_mutes.find_one({'chat_id': chat_id})

def set_welcome_mutes(chat_id, welcomemutes):
    with INSERTION_LOCK:
        welcome_mute = WelcomeMute(chat_id, welcomemutes)
        welcome_mute.save()

def set_human_checks(user_id, chat_id):
    with INSERTION_LOCK:
        human_check = WelcomeMuteUsers(user_id, chat_id, True)
        human_check.save()

def get_human_checks(user_id, chat_id):
    return nobita.human_checks.find_one({'user_id': user_id, 'chat_id': chat_id})

def get_welc_pref(chat_id):
    welc = nobita.welcome_pref.find_one({'chat_id': chat_id})
    if welc:
        return (
            welc['should_welcome'],
            welc['custom_welcome'],
            welc['custom_content'],
            welc['welcome_type'],
        )
    return True, DEFAULT_WELCOME, None, "text"

def set_clean_welcome(chat_id, clean_welcome):
    with INSERTION_LOCK:
        welcome = nobita.welcome_pref.find_one({'chat_id': chat_id})
        if welcome:
            welcome['clean_welcome'] = int(clean_welcome)
            nobita.welcome_pref.update_one({'chat_id': chat_id}, {'$set': welcome})
        else:
            Welcome(chat_id).save()

def migrate_chat(old_chat_id, new_chat_id):
    with INSERTION_LOCK:
        welcome = nobita.welcome_pref.find_one({'chat_id': old_chat_id})
        if welcome:
            welcome['chat_id'] = new_chat_id
            nobita.welcome_pref.update_one({'chat_id': old_chat_id}, {'$set': welcome})

        nobita.welcome_urls.update_many({'chat_id': old_chat_id}, {'$set': {'chat_id': new_chat_id}})
        nobita.leave_urls.update_many({'chat_id': old_chat_id}, {'$set': {'chat_id': new_chat_id}})
