import os
import discord
import random
import praw

from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from keep_alive import keep_alive

client = discord.Client()

deadmemes = ['https://cdn.discordapp.com/attachments/823378608578887700/831884270233583707/the_bagel_song.mp4', 'https://cdn.discordapp.com/attachments/823378608578887700/831885061249826896/lookatallthosechickens.mp4', 'https://cdn.discordapp.com/attachments/823378608578887700/831904492077318154/disaster-girl.jpg', 'https://cdn.discordapp.com/attachments/823378608578887700/831905510793543780/brugatini.jpg']
wiigames = ['https://cdn.discordapp.com/attachments/823378608578887700/833004213151465502/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004244260225024/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004287453298738/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004327752040498/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004370604851231/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004441904742410/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004493037109300/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004532614168606/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833004625879367690/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833005877610545182/image.png', 'https://cdn.discordapp.com/attachments/823378608578887700/833005919310053376/image.png']
bot = commands.Bot(command_prefix= 'o!')
@client.event
async def on_ready():
    print('Starting up...... Logged in as {0.user}'.format(client))
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('OK AND'):
            await message.channel.send('OK AND? (starts eating ice block)')
        elif message.content.startswith('ok androxus'):
            await message.channel.send(
                'every time himesh plays androxus, yea we get curbstomped 4-0. just get good himesh, not that hard.'
            )
        elif message.content.startswith('OK androxus'):
            await message.channel.send(
                'every time himesh plays androxus, yea we get curbstomped 4-0. just get good himesh, not that hard.'
            )
        elif message.content.startswith('sanjiv ok and'):
            await message.channel.send('ok and? (starts eating rock)')
        elif message.content.startswith('Sanjiv ok and'):
            await message.channel.send('ok and? (starts eating rock)')
        elif message.content.startswith('and ok'):
            await message.channel.send(
                'and ok? trinay made this so idk anymore.')
        elif message.content.startswith('And ok'):
            await message.channel.send(
                'and ok? trinay made this so idk anymore.')
        elif message.content.startswith('Ok and'):
            await message.channel.send('ok and? (starts eating ice block)')
        elif message.content.startswith('dontstoler'):
            await message.channel.send(
                'this is made by sriram and a certain sragvee cant take my stuff'
            )
        elif message.content.startswith(
                'https://tenor.com/view/ice-eating-ok-and-gif-19666657'):
            await message.channel.send('ok and? (starts eating ice block)')
        elif message.content.startswith(
                'https://tenor.com/view/ok-and-gif-20518885'):
            await message.channel.send(
                'ok and? (spongebob kinda looking hot ----- what)')
        elif message.content.startswith('gif'):
            await message.channel.send(
                'https://tenor.com/view/ice-eating-ok-and-gif-19666657')
        elif message.content.startswith('rayhan ok and'):
            await message.channel.send(
                'https://tenor.com/view/ok-and-gif-19091302')
        elif message.content.startswith(
                'https://tenor.com/view/ok-and-gif-19091302'):
            await message.channel.send(
                'ok and? (rayhan squealing in the background)')
        elif message.content.startswith(
                'https://tenor.com/view/ok-and-big-chungus-is-funny-gif-20677262'
        ):
            await message.channel.send('ok and? (himesh irl)')
        elif message.content.startswith('im'):
            await message.channel.send('insert dad bot here')
        elif message.content.startswith('Im'):
            await message.channel.send('insert dad bot here')
        elif message.content.startswith('I am'):
            await message.channel.send('insert dad bot here')
        elif message.content.startswith('Gif'):
            await message.channel.send(
                'https://tenor.com/view/ice-eating-ok-and-gif-19666657')
        elif message.content.startswith('rage ok and'):
            await message.channel.send(
                'https://tenor.com/view/suits-louis-litt-angry-rage-say-that-again-gif-14695477'
            )
        elif message.content.startswith('Rage ok and'):
            await message.channel.send(
                'https://tenor.com/view/suits-louis-litt-angry-rage-say-that-again-gif-14695477'
            )
        elif message.content.startswith(
                'https://tenor.com/view/suits-louis-litt-angry-rage-say-that-again-gif-14695477'
        ):
            await message.channel.send(
                'ok and? (watch a 30 second calm video jesus christ man)')
        elif message.content.startswith(
                'https://tenor.com/view/richard-watterson-gumball-ok-and-gif-20195377'
        ):
            await message.channel.send(
                'ok and? (richard weightwatchers before and after pictures)')
        elif message.content.startswith('creatorinfo'):
            await message.channel.send(
                'Version 1.0 of ok and? bot, created by Sriram Sattiraju, discord user cinnamon toast bruh#1204. GIF replies also taken from friends, which are listed using the "mentions" command.'
            )
        elif message.content.startswith('mentions'):
            await message.channel.send(
                'Rayhan - Rage GIF, Trinay - And ok, Himesh - Family Guy GIF, Prady - AWOG GIF, Ethan - ok androxus?'
            )
        elif message.content.startswith('dosa'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823625927820050542/2Q.png'
            )
        elif message.content.startswith('crackheadhimesh'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823628881365434378/unknown.png'
            )
        elif message.content.startswith('dopeyramin'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823629373990633532/raming_gaming.jpg'
            )
        elif message.content.startswith('prateekthegorilla'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/614597078944972810/763948533069119498/image0.png'
            )
        elif message.content.startswith('smolani'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823629698507603998/unknown.png'
            )
        elif message.content.startswith('crackheadramsri'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823629731248209960/ramsripoopyhead.png'
            )
        elif message.content.startswith('samosa'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823640182656991292/9k.png'
            )
        elif message.content.startswith('mettaton ex'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/610225095419494436/823669265038049280/Undertale_OST_068_-_Death_by_Glamour.mp4'
            )
        elif message.content.startswith('Mettaton ex'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/610225095419494436/823669265038049280/Undertale_OST_068_-_Death_by_Glamour.mp4'
            )
        elif message.content.startswith('ramsri + himeshs mom'):
            await message.channel.send(
                'https://tenor.com/view/mom-your-mom-fuck-it-stick-figure-f-your-mom-gif-7973111'
            )
        elif message.content.startswith('jacob + himeshs mom'):
            await message.channel.send(
                'https://tenor.com/view/mom-your-mom-fuck-it-stick-figure-f-your-mom-gif-7973111'
            )
        elif message.content.startswith('himesh + ramsris mom'):
            await message.channel.send(
                'https://tenor.com/view/that-ain-happenin-not-happening-not-gonna-happen-no-nope-gif-7567578'
            )
        elif message.content.startswith('pnj gif'):
            await message.channel.send(
                'https://tenor.com/view/reggie-nintendo-no-gif-5495518')
        elif message.content.startswith('Pnj gif'):
            await message.channel.send(
                'https://tenor.com/view/reggie-nintendo-no-gif-5495518')
        elif message.content.startswith(
                'https://tenor.com/view/reggie-nintendo-no-gif-5495518'):
            await message.channel.send('I agree, stop johning bruh')
        elif message.content.startswith('help'):
            await message.channel.send(
                'bruh you need help, what a loser amirite')
        elif message.content.startswith('Help'):
            await message.channel.send(
                'bruh you need help, what a loser amirite')
        elif message.content.startswith('lob?'):
            await message.channel.send(
                'https://tenor.com/view/lob-londerzeel-londerzeel-badminton-badminton-londerzeel-badminton-gif-17424476'
            )
        elif message.content.startswith(
                'https://tenor.com/view/ok-and-gif-20517422'):
            await message.channel.send(
                'ok and? (help i have prateek syndrome!!!)')
        elif message.content.startswith(
                'https://tenor.com/view/ok-and-gif-20518787'):
            await message.channel.send('ok and? (when the impostor is sus)')
        elif message.content.startswith('nogga'):
            await message.channel.send('GO TO ROTTEN POTATO NOW, BAD WORD')
        elif message.content.startswith('Nogga'):
            await message.channel.send('GO TO ROTTEN POTATO NOW, BAD WORD')
        elif message.content.startswith('freebobux'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/659630509894271001/814122521834160188/video0_12_1.mov'
            )
        elif message.content.startswith('highsriram'):
            await message.channel.send(
                'https://media.discordapp.net/attachments/689291463984676953/818652928389939240/smokeweedeveryday.png'
            )
        elif message.content.startswith('Bergentrückung + ASGORE'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/563154822891700234/823905945654132776/Undertale_OST_-_Bergentruckung__ASGORE_Fixed_loop.mp4'
            )
        elif message.content.startswith('asgore'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/563154822891700234/823905945654132776/Undertale_OST_-_Bergentruckung__ASGORE_Fixed_loop.mp4'
            )
        elif message.content.startswith('Asgore'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/563154822891700234/823905945654132776/Undertale_OST_-_Bergentruckung__ASGORE_Fixed_xloop.mp4'
            )
        elif message.content.startswith('mettaton neo'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/823910230471213126/Undertale_Ost_099_-_Power_of_-NEO-.mp4'
            )
        elif message.content.startswith('Mettaton neo'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/823910230471213126/Undertale_Ost_099_-_Power_of_-NEO-.mp4'
            )
        elif message.content.startswith('mettaton'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/823908687328182312/Undertale_OST_050_-_Metal_Crusher.mp4'
            )
        elif message.content.startswith('Mettaton'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/823908687328182312/Undertale_OST_050_-_Metal_Crusher.mp4'
            )
        elif message.content.startswith('ok and'):
            await message.channel.send('ok and? (starts eating ice block)')
        elif message.content.startswith('idli'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823944404179877938/idli-recipe-1-500x500.png'
            )
        elif message.content.startswith('coolbeans'):
            await message.channel.send(
                'https://tenor.com/view/cool-beans-gif-8765352')
        elif message.content.startswith('prateeksyndrome'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823952193043300393/prateek_syndrome_deepfried.png'
            )
        elif message.content.startswith('doinurmom'):
            await message.channel.send(
                'https://tenor.com/view/me-bois-doin-yah-mom-gif-19931188')
        elif message.content.startswith('coolsanjiv'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/823960558075117608/unknown.png'
            )
        elif message.content.startswith('cheekonhandsanjiv'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/823961118443569167/unknown.png'
            )
        elif message.content.startswith('excuses'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/823962476541378640/unknown.png'
            )
        elif message.content.startswith('deeznutsparty'):
            await message.channel.send(
                'https://tenor.com/view/deez-nuts-party-lol-kool-aid-man-koolaid-gif-19151637'
            )
        elif message.content.startswith(
                'https://tenor.com/view/ok-and-grubhub-gif-20518887'):
            await message.channel.send(
                'ok and? (this guy is actually married to the smoothie girl)')
        elif message.content.startswith('mishabeta'):
            await message.channel.send(
                'https://tenor.com/view/misha-gabriel-gif-5075402 https://tenor.com/view/beta-jesse-lee-peterson-gif-15785063'
            )
        elif message.content.startswith(
                'https://tenor.com/view/so-how-are-those-grades-going-bts-funny-jimin-laugh-gif-11942415'
        ):
            await message.channel.send(
                'the followup, indian parents take out the belt')
        elif message.content.startswith(
                'https://tenor.com/view/crab-rave-ramon-is-gone-gif-14519973'):
            await message.channel.send('EYYY RAMON IS GONE!!!!')
        elif message.content.startswith(
                'https://cdn.discordapp.com/attachments/689291463984676953/829072737736982608/crab.mp4'
        ):
            await message.channel.send('EYYY RAMON IS GONE POGGERS!!!')
        elif message.content.startswith('ramonisgonevideo'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/829072737736982608/crab.mp4'
            )
        elif message.content.startswith('ramonisgone'):
            await message.channel.send(
                'https://tenor.com/view/crab-rave-ramon-is-gone-gif-14519973')
        elif message.author.id == 458808197747048448:
            await message.channel.send(
                'https://tenor.com/view/shut-up-anime-profile-picture-gif-19903708'
            )
        elif message.content.startswith('mishabday'):
            await message.channel.send('HAPPY EARLY BIRTHDAY MISHAB')
        elif message.content.startswith('chugjugwithyou'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/824677995721129994/chugjugwithu.mp4'
            )
        elif message.content.startswith('eminemchugsjugwithu'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/824678357232123934/Eminem_gets_Chug_Jugs_With_You.mp4'
            )
        elif message.content.startswith('halotheme'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/824681028463231051/Halo_Theme_Song_Original.mp4'
            )
        elif message.content.startswith('paladinstie'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/824682493395206157/Paladins_Soundtrack_-_Tiebreaker.mp4'
            )
        elif message.content.startswith('theimpostorissus'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/824688056089968670/amogus.mp4'
            )
        elif message.content.startswith('venusriram'):
            await message.channel.send(
                'https://tenor.com/view/sriram-venu-venusriram-jai-vakeelsaab-gif-20356592'
            )
        elif message.content.startswith('nogga'):
            await message.channel.send('GO TO ROTTEN POTATO NOW!!!!')
        elif message.content.startswith('n||o||gga'):
            await message.channel.send('GO TO ROTTEN POTATO NOW!!!')
        elif message.content.startswith('retard'):
            await message.channel.send(
                '"You cannot say that word because it is bad word to say and is very offensive" - Sanjiv the Samosa, 2021'
            )
        elif message.content.startswith('Retard'):
            await message.channel.send(
                '"You cannot say that word because it is bad word to say and is very offensive" - Sanjiv the Samosa, 2021'
            )
        elif message.content.startswith('feelingdown'):
            await message.channel.send(
                'when ur feeling down remember, the 2nd regiment exists.')
        elif message.content.startswith('dripprateekboost'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/825161403710046208/prateek_syndrome_deepfried_1.mp4'
            )
        elif message.content.startswith('bababooey'):
            await message.channel.send(
                'https://media.discordapp.net/attachments/629063213324959754/825389569691091064/bababooey.gif'
            )
        elif message.content.startswith(
                'https://cdn.discordapp.com/attachments/801888791165403187/825541797123850250/crab.mp4'
        ):
            await message.channel.send('EYYYY PARTH IS GONE')
        elif message.content.startswith('parthisgone'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/801888791165403187/825541797123850250/crab.mp4'
            )
        elif message.content.startswith('richarddancing'):
            await message.channel.send(
                'https://media.discordapp.net/attachments/689291463984676953/826453698556723240/Oh_Oh_Oh_A_Ohhhh_Ohhhh_-_Richard_Waterson_The_Amazing_World_of_Gumball.gif'
            )
        elif message.content.startswith(
                'https://media.discordapp.net/attachments/689291463984676953/826453698556723240/Oh_Oh_Oh_A_Ohhhh_Ohhhh_-_Richard_Waterson_The_Amazing_World_of_Gumball.gif'
        ):
            await message.channel.send('OOOH OOOOH OOOH OOH OOOOOOH OOOOOOH')
        elif message.content.startswith('jokerfinalsmash'):
            await message.channel.send(
                'https://tenor.com/view/joker-final-smash-ssbu-anime-fight-the-show-sover-gif-16256924'
            )
        elif message.content.startswith('ricardofinalsmash'):
            await message.channel.send(
                'https://tenor.com/view/ricardo-persona-the-shows-over-meme-ricardo-milos-gif-17297456'
            )
        elif message.content.startswith('songthatmightplaywhenyoufightsans'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/563154822891700234/827400261022515230/Undertale_OST_072_-_Song_That_Might_Play_When_You_Fight_Sans.mp4'
            )
        elif message.content.startswith('undertale-72'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/563154822891700234/827400261022515230/Undertale_OST_072_-_Song_That_Might_Play_When_You_Fight_Sans.mp4'
            )
        elif message.content.startswith('letsgochamp'):
            await message.channel.send(
                'https://tenor.com/view/lets-go-champ-the-champishere-champ-gif-13636238'
            )
        elif message.content.startswith('mewhendharmann'):
            await message.channel.send(
                'https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')
        elif message.content.startswith('pokemonswordisbad'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/815448284797468712/830064380234170438/sriram_simulator.mp4'
            )
        elif message.content.startswith('fatasscat2'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/830148894792220732/bru.mp4'
            )
        elif message.content.startswith('fatasscat'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/689291463984676953/830145601088913458/fat_ass_cat_in_a_tuxedo.mp4'
            )
        elif message.content.startswith('rlfavorite'):
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/823378608578887700/830150545251500052/rl_favorite.mp4'
            )
        elif message.content.startswith('whoiscreator'):
          await message.channel.send('Who is the creator you ask? The creator is a mega chad that is super muscular and very amazing. He is too good for humanity, so I cannot reveal his name or else I will be banished. However, I can compensate with a picture of his manliness and muscular body. https://cdn.discordapp.com/attachments/560990988378570797/833075721386590258/Photo_on_4-17-21_at_3.25_PM.jpg')
        elif message.content.startswith('did i ask'):
         await message.channel.send('https://tenor.com/view/who-asked-i-asked-bean-killer-bean-nork-gif-19322375')
        elif message.content.startswith('Did I ask'):
         await message.channel.send('https://tenor.com/view/who-asked-i-asked-bean-killer-bean-nork-gif-19322375')
        elif message.content.startswith('Did i ask'):
          await message.channel.send('https://tenor.com/view/who-asked-i-asked-bean-killer-bean-nork-gif-19322375')
        elif message.content.startswith('who asked'):
         await message.channel.send('https://tenor.com/view/who-asked-i-asked-bean-killer-bean-nork-gif-19322375')
        elif message.content.startswith('Who asked'):
         await message.channel.send('https://tenor.com/view/who-asked-i-asked-bean-killer-bean-nork-gif-19322375')
        elif message.content.startswith('https://tenor.com/view/dhar-mann-motivational-video-exciting-favourite-youtuber-best-youtuber-gif-20892541'):
          await message.channel.send('CRINNNNGGEEE')
        elif message.content.startswith('beemovie'):
          await message.channel.send('https://cdn.discordapp.com/attachments/785247336624160779/785654621132816415/Bee.mp4')
        elif message.content.startswith('shrekmov'):
          await message.channel.send('https://imgur.com/gallery/IsWDJWa')
        elif message.content.startswith('abysswatchers'):
          await message.channel.send('https://cdn.discordapp.com/attachments/823378608578887700/831526656556531762/Abyss_Watchers.mp4')
        elif message.content.startswith('gt1030'):
          await message.channel.send('https://cdn.discordapp.com/attachments/689291463984676953/831528775849213962/asus_ph-gt1030-o2g.gif')
        elif message.content.startswith('randomdeadmeme'):
          await message.channel.send(random.choice(deadmemes))
        elif message.content.startswith('legocity'):
          await message.channel.send('https://cdn.discordapp.com/attachments/823378608578887700/831886689269710868/A_Man_Has_Fallen_Into_The_River_In_Lego_City_Commercial.mp4')
        elif message.content.startswith('obamaspeech'):
          await message.channel.send('https://cdn.discordapp.com/attachments/689291463984676953/831944461784711218/obama.mp4')
        elif message.content.startswith('savetheworld'):
          await message.channel.send('https://cdn.discordapp.com/attachments/823378608578887700/831992632514969610/Undertale_Ost_089_-_SAVE_the_World.mp4')
        elif message.content.endswith('bruh'):
          await message.channel.send('gatini alfredo')
        elif message.content == 'hi ok and':
          await message.author.send('Hello!')
        elif message.content.startswith('randomwiigame'):
          await message.channel.send(random.choice(wiigames))
        elif message.content.startswith('genocideundyne'):
          await message.channel.send('https://cdn.discordapp.com/attachments/823378608578887700/833108187581382676/Undertale_Ost_098_-_Battle_Against_a_True_Hero.mp4')


keep_alive()
client.run(os.getenv('TOKEN'))
