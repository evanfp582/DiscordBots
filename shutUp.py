import discord
#from helperFunctions import test

class ShutUpBot(discord.Client):
    async def on_ready(self):
        print(f'(self.user) has connected to Discord!')
        input('ass')
        #test()


    async def on_message(self, message):
        print(message.content)
        discordText=message.content
        if message.author == self.user:
            return
        if message.author.name == "Murphinata":
            await message.channel.send("Shut up clown 🤡")
        if message.content =="pog":
            await message.channel.send("I guess you are my little pogchamp UwU!!")
            #print(message.content)
            print(self.user.id)

