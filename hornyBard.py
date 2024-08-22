import os
import random
from tokenize import StringPrefix
import discord
from discord.ext import commands
from discord import Client

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

azCounter = 2


BRD = (
   "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTJhZGJtejhlczBzcWc3emdmNDFpazE1YTZhaGd1dThtYWcxYXJmciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5YqKU8tQUQmCLna20m/giphy.gif", 
   "Ah, the Bard. Always the first to flirt with the dragon. Because why use a sword when you can use… innuendo?",
   "The group therapist who also happens to be a walking jukebox. Can't wait for your next rendition of \"Wonderwall.\"",
   "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW5rd3o2cmY4c2k2bTl0NWdmcHZ3OG1jb3k5cXFuNXJkZjd1bXk5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F142T5RvkfYtPQ1ep9/giphy.gif"

)

FGT = (
    "So, you swing your sword... again? You're like a monk, but without all that pesky inner peace.",
    "Master of tactics, or just master of \“I swing my sword\"? The world may never know."
)

PLD = (
    "Gotta have a lawful stupid paladin. High and mighty with a healthy dose of delusional hypocrisy. Really lean into the pretentious condescension to make everyone loathe him.",
    "Another Paladin with a holy quest. You must have a subscription service for that righteous indignation."

)

ROG = (
    "Ah yes, the Rogue. Because clearly, every party needs someone who’s only loyal to their own coin purse.",
)

MGC = (
    "You're basically a walking fireball with a superiority complex. But hey, it's \"natural talent,\" right?",
    "You spent decades studying the arcane arts... and still managed to memorize the wrong spell this morning. Impressive."
)

BRB = (
    "Wow, another Barbarian whose solution to every problem is hitting it with an axe. Truly groundbreaking.",
    "The solution to everything: punch it. Who needs weapons when your fists are this deadly, right?",
    "Wait, your character actually has a backstory? I thought it was just \"Angry. Smash.\""
)

CLC = (
    "Healbot 3000, activate! Because your party forgot that health potions are a thing.",
)

DRD = (
    "Turning into a squirrel during combat? Bold strategy. I'm sure the enemies are terrified.",
    "Saving nature one fireball at a time. Because nothing screams \"environmentalist\" like burning down half the forest."
)

MNK = (
    "The solution to everything: punch it. Who needs weapons when your fists are this deadly, right?",
    "Your fists are deadlier than any weapon... except when the enemy remembers armor exists."
)

WRL = (
    "Sold your soul for power? How original. But please, tell us more about your dark and edgy patron.",
)

RNG = (
    "You're a master of the wilderness... until someone asks you to track something. Then it's like, \"Where did that deer go again?\"",
    "You're great with a bow and arrow... as long as nothing moves, ever."
)

D = (
    1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20
)

BAD = (
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTk0eG5qZmc2dHJ4YmhudWtnaWs5eXhoZmsxZGJuOTFqazduYnB4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oOBTO2UcSoaBJewZT0/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnYzeHRxOGpmZHQ5eG42ZzRnNzRtazE3dDlneG1jdG11NnR2eGNvcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fxe6DIMSIdHoTJ7J51/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG12NWFrMjhhaDJsdWtkbzlsMXcwNmQzdGsweWc2ZWRobm1lOGV2cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ksDqJRfXDW0HTAqfS9/giphy.gif"
)

NCE = (
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnM3bDd5Zmt4aW5ndzByY3NrMHptbGVzeDVrdjRtMjJpbGpmYjVhaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qmjZjcZZPAfdX0YgEP/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDBsamtjanljYms1ZzJqZzByMGk2ODM1Mmt6eGd4NG56Ynp2djB4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5v2cKL4AydL95h33U2/giphy.gif"
)

TIM = (
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTh1cTg3bno1NW82eGZ6NHJwa3pjN3N4eWdwaGo2eXN2eWh6cGNnMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3Wv2P64lfg717Q5xZp/giphy.gif",
)

SIG = (
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGNrbDN2dnR3bTNxcGczaG44d2M2czhxMjNzeGJqaGZvaHRvdWI1MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/THNSYNBpIuwxniG7CK/giphy.gif",
    "https://img.pr0gramm.com/2023/03/06/150f6620456aa3cb.gif",0
)

AZ = (
    "*Hands the tortle some whiskey*",
    "Let's explode the tortle! >:)",
    "*The tortle has been touched by Samael "+azCounter+" times*",
)

BEN = (
    "I can offer tree fiddy for that painting, Samael.",
)

@client.event
async def on_message(msg):
    
    if msg.author == client.user:
        return
    
    print (msg.content) 
    
    text = msg.content.lower() ## Set all text to lower case


    ## REACTIONS
    if "bard" in text:
        await msg.channel.send (random.choice(BRD))
    if "fighter" in text:
        await msg.channel.send (random.choice(FGT))
    if "paladin" in text or "pala" in text:
        await msg.channel.send (random.choice(PLD))
    if "rogue" in text:
        await msg.channel.send (random.choice(ROG))
    if "mage" in text or "sorc " in text or "wizard " in text or "sorcerer " in text:
        await msg.channel.send (random.choice(MGC))    
    if "barb" in text or "barbi " in text or "barbarian " in text:
        await msg.channel.send (random.choice(BRB)) 
    if "cleric" in text:
        await msg.channel.send (random.choice(CLC))    
    if "drui" in text or "druid" in text:
        await msg.channel.send (random.choice(DRD))
    if "monk" in text and not "monke" in text:
        await msg.channel.send (random.choice(MNK))
    if "warlock" in text:
        await msg.channel.send (random.choice(WRL))    
    if "ranger" in text:
        await msg.channel.send (random.choice(RNG))

    ## REACTIONS USERS
    if msg.author.id == 279024999371898882:
        await msg.channel.send (random.choice(TIM))    
    if "siggi" in text or "sigi" in text:
        await msg.channel.send (random.choice(SIG))
    if msg.author.id == 247821469567025154:
        await msg.channel.send (random.choice(AZ))
        azCounter+=1        
    if msg.author.id == 223259938300887040:
        await msg.channel.send(random.choice(BEN))

    ## ACTIONS
    if "1d20" in text or "roll dice" in text:
        answer = random.choice(D)
        if answer >=2 and answer < 20:
            await msg.channel.send (answer)
        elif answer == 1:
            await msg.channel.send (random.choice(BAD))
        elif answer == 20:
            await msg.channel.send (random.choice(NCE))

## for running locally
# with open('hornyBard.txt') as fp:
# client.run(fp.read().strip())

client.run(os.environ["token"])