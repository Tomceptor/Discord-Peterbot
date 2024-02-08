import keep_alive
import os
import discord
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)




@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  

  if "wer" in message.content.lower().split():
      await message.channel.send("Nein, wer gefraaaaaaagt hat",     reference=message)
      return

  
  if "reddit" in message.content.lower().split():
    await message.channel.send("Du fucking Incel benutzt Reddit? Maximales cringe level brudi",     reference=message)
    return
  
  
  
  if "peter" in message.content.lower().split():
      await message.channel.send(":right_facing_fist::bus::left_facing_fist::handshake:",     reference=message)
      return


  
  if "milliatome" in message.content.lower().split():
      await message.channel.send("Sag mal hast du Lack gesoffen?",     reference=message)
      return

  
  if "mercy" in message.content.lower().split():
      emoji = '<:JenniePog:1097973176463544501>'
      await message.add_reaction(emoji)
      return


  if "soldier" in message.content.lower().split():
      await message.add_reaction("🍆")
      return


  if "Bausparvetrag" in message.content.lower().split():
      emoji = '<:KonniPog:1097976533571866664>'
      await message.add_reaction(emoji)
      return
    
  if "Bausparer" in message.content.lower().split():
      emoji = '<:KonniPog:1097976533571866664>'
      await message.add_reaction(emoji)
      return
    
  if "Bausparen" in message.content.lower().split():
      emoji = '<:KonniPog:1097976533571866664>'
      await message.add_reaction(emoji)
      return

  if "moira" in message.content.lower().split():
      emoji = '<:KonniPog:1097976533571866664>'
      await message.add_reaction(emoji)
      return

  if "was" in message.content.lower().split():
      await message.add_reaction("🍍")
      return

  if "satisfactory" in message.content.lower().split():
      await message.channel.send("DIE ULTIMATIVE OPTIMIERUNG <:KonstiPog:1097973424091058276>", reference = message)
      return

  if "sus" in message.content.lower().split():
      emoji = '<:Amogus:1102298282253893632>'
      await message.add_reaction(emoji)
      return


  
  if "bronze" in message.content.lower().split():
      await message.channel.send("Junge bist du scheiße", reference = message)
      return
    
  if "gold" in message.content.lower().split():
      await message.channel.send("Sag mal hast du skill issue? Plat ist gold bloß für gute Spieler", reference = message)
      return
    
  if "silber" in message.content.lower().split():
      await message.channel.send("Das ist halt einfach glänzendes Bronze", reference = message)
      return
    
  if "plat" in message.content.lower().split():
      await message.channel.send("Ey langsam wirste gut. Machst mir ja richtig Konkurrenz. 1v1?", reference = message)
      return
    
  if "dia" in message.content.lower().split():
      await message.channel.send("Ok brudi komm runter. Das ist ein bisschen zu high level für diesen server", reference = message)
      return
    
  if "master" in message.content.lower().split():
      await message.channel.send("Ja geh doch einfach weg alter. Brauchst nicht so zu flexen", reference = message)
      return
    
  if "gm" in message.content.lower().split():
      await message.channel.send("Bitte carry mich, ich lutsch auch deine Luststange", reference = message)
      return

  if "hs" in message.content.lower().split():
      await message.channel.send("nein du bist ein hs", reference = message)
      return
    
  if "hurensohn" in message.content.lower().split():
      await message.channel.send("nein du bist ein hurensohn", reference = message)
      return


  

  if "chess" in message.content.lower().split():
      await message.channel.send("los, komm her 1v1. du Pisser denkst wohl du bist intellenter als ich?", reference = message)
      return
    
  if "schach" in message.content.lower().split():
      await message.channel.send("los, komm her 1v1. du Pisser denkst wohl du bist intellenter als ich?", reference = message)
      return

  if "cringe" in message.content.lower().split():
      await message.channel.send("ne du bist cringe", reference = message)
      return
    
  if "wirt" in message.content.lower().split():
      await message.channel.send("verWIRT", reference = message)
      return
    
  if "digga" in message.content.lower().split():
      await message.channel.send("https://media.discordapp.net/attachments/571397755143192576/1151458088017199134/image.png?width=623&height=671", reference = message)
      return
    
  if "diggah" in message.content.lower().split():
      await message.channel.send("https://media.discordapp.net/attachments/571397755143192576/1151458088017199134/image.png?width=623&height=671", reference = message)
      return
    

  if "league" in message.content.lower().split():
      await message.channel.send("Das ist das Spiel, dass <@538815797141831738> zu viel spielt", reference = message)
      return

#Anarchy Chess Responses:

  if "Google en passant" in message.content.lower().split():
      await message.channel.send("Holy hell", reference=message)
      return
  
  if "holy hell" in message.content.lower().split():
      await message.channel.send("New Response just Dropped", reference=message)
      return

  if "New response just dropped" in message.content.lower().split():
      await message.channel.send("Actual Zombie", reference=message)
      return

  if "Actual Zombie" in message.content.lower().split():
      await message.channel.send("Call the exorcist", reference=message)
      return

  if "call the exorcist" in message.content.lower().split():
      await message.channel.send("Bishop goes on vacation and never comes back", reference=message)
      return

  if "Bishop goes on vacation and never comes back" in message.content.lower().split():
      await message.channel.send("Queen Sacrifice, anyone?", reference=message)
      return

  if "Queen sacrifice, anyone?" in message.content.lower().split():
      await message.channel.send("Pawn Storm incoming", reference=message)
      return

  if "Pawn storm incoming" in message.content.lower().split():
      await message.channel.send("Ignite the chessboard", reference=message)
      return

  if "ignite the chessboard" in message.content.lower().split():
      await message.channel.send("Rooks in the corner plotting world domination", reference=message)
      return

  if "Rooks in the corner plotting world domination" in message.content.lower().split():
      await message.channel.send("Jessica comes with Knook to beat the rook", reference=message)
      return

  if "King says: Jessica isnt fucking welcome here" in message.content.lower().split():
      await message.channel.send("Pawn says: OR is it?", reference=message)
      return

  if "Pawn says: OR is it?" in message.content.lower().split():
      await message.channel.send("or isnt welcome here as well", reference=message)
      return

  if "or isnt welcome here as well" in message.content.lower().split():
      await message.channel.send("Lets play Checkers instead", reference=message)
      return

  if "Lets play checkers instead" in message.content.lower().split():
      await message.channel.send("What is checkers?", reference=message)
      return

  if "What is checkers?" in message.content.lower().split():
      await message.channel.send("idk but what is dementia?", reference=message)
      return

  if "idk but what is dementia" in message.content.lower().split():
      await message.channel.send("I think it a type of pasta", reference=message)
      return
#slash-commands

@bot.hybrid_command()
async def test(message):
    await message.send("This is a hybrid command!")

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1094324563376095383))
    print("Ready!")
  

keep_alive.keep_alive()
bot.run(os.environ['disc_token'])