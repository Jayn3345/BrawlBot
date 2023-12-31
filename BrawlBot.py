import discord
import random
import json
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

clonebot = False

if clonebot == True:
    cpfx = ","
elif clonebot == False:
    cpfx = "-"

client = commands.Bot(command_prefix=cpfx, intents=intents)

if clonebot == False:
    searchChannel = 854427760389652490
    miscChannel = 854428093459202099
    modChannel = 1029873581158576230
    matchChannel = 854428351800016907
elif clonebot == True:
    searchChannel = 837907088969302019
    miscChannel = 849389145066831913
    modChannel = 837907088969302019
    matchChannel = 840823468362301450

channelList = [searchChannel, miscChannel, modChannel, matchChannel]

join = '🔔'
leave = '🚪'
modkey = '🔑'
stay = '☑'
challenge = '⚔'
rm = '🗡️'
abort = '🔴'
accept = '✅'
cancel = '❌'
versus = '<:vs:843364613986189342>'

BF = '<Battlefield:837907213627686943>'
FD = '<FinalDestination:837907213695057950>'
SV = '<Smashville:837907213678542863>'
YI = '<YoshisIsland:925956998024007680>'
LC = '<LylatCruise:925957016135020545>'
PS = '<PS1:925957052147310622>'
CS = '<CastleSiege:925957337867485284>'
FO = '<FrigateOrpheon:925957063383867483>'
PS2 = '<:PS2:1059009265433596004>'

# BF = client.get_emoji(837907213627686943) # Battlefield
# FD = client.get_emoji(837907213695057950) # FinalDestination
# SV = client.get_emoji(837907213678542863) # Smashville
# YI = client.get_emoji(925956998024007680) # YoshisIsland
# LC = client.get_emoji(925957016135020545) # LylatCruise
# PS = client.get_emoji(925957052147310622) # PS1
# CS = client.get_emoji(925957337867485284) # CastleSiege
# FO = client.get_emoji(925957063383867483) # Frigate Orpheon

# BF = discord.PartialEmoji(name="Battlefield", id=837907213627686943)
# FD = discord.PartialEmoji(name="FinalDestination", id=837907213695057950)
# SV = discord.PartialEmoji(name="Smashville", id=837907213678542863)
# YI = discord.PartialEmoji(name="YoshisIsland", id=925956998024007680)
# LC = discord.PartialEmoji(name="LylatCruise", id=925957016135020545)
# PS = discord.PartialEmoji(name="PS1", id=925957052147310622)
# CS = discord.PartialEmoji(name="CastleSiege", id=925957337867485284)
# FO = discord.PartialEmoji(name="FrigateOrpheon", id=925957063383867483)

# BF = '<:Battlefield:837907213627686943>'
# FD = '<:FinalDestination:837907213695057950>'
# SV = '<:Smashville:837907213678542863>'
# YI = '<:YoshisIsland:925956998024007680>'
# LC = '<:LylatCruise:925957016135020545>'
# PS = '<:PS1:925957052147310622>'
# CS = '<:CastleSiege:925957337867485284>'
# FO = '<:FrigateOrpheon:925957063383867483>'

noBan = '⬜'
completestagelist = [BF, FD, SV, YI, LC, PS, CS, FO]
netpColor = 4312575  # light blue
wifiColor = 16613797  # light pink
defaultColor = 15174967  # orange
netpSymbol = '<:netplay:849372987173371925>'
wifiSymbol = '<:wifi:849372254789828618>'
attributes = {"WIFI": {'symbol': wifiSymbol, 'color': wifiColor}, "NETP": {'symbol': netpSymbol, 'color': netpColor}}

stageTNs = {
    '<:Battlefield:837907213627686943>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081456619814912/Battlefield_Preview.png',
    '<:FinalDestination:837907213695057950>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081454724120576/Final_Destination_Preview.png',
    '<:Smashville:837907213678542863>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081452766298142/Smashville_Preview.png',
    '<:YoshisIsland:925956998024007680>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081450505830420/Yoshis_Preview.png',
    '<:LylatCruise:925957016135020545>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081448805826560/Lylat_Preview.png',
    '<:PS1:925957052147310622>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081446424510474/PS1_Preview.png',
    '<:CastleSiege:925957337867485284>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081434109640714/Castle_Siege_Preview.png',
    '<:FrigateOrpheon:925957063383867483>': 'https://cdn.discordapp.com/attachments/845292400440377374/861081444134813706/Frigate_Orpheon_Preview.png',
    '<:PS2:1059009265433596004>': 'https://cdn.discordapp.com/attachments/845292400440377374/1059013954493497344/PS2TN.png'
}

brawlChara = {"mario": '<:mario:838822011412676708>', "donkey kong": '<:donkeykong:838822011114356760>',
              "dk": '<:donkeykong:838822011114356760>',
              "link": '<:link:838822011286716486>', "samus": '<:samus:838822011009499147>',
              "kirby": '<:kirby:838822010968735796>', "fox": '<:fox:838822011408613396>',
              "melee": '<:fox:838822011408613396>',
              "pikachu": '<:pikachu:838822011341111346>', "marth": '<:marth:838822011122745376>',
              "mr. game & watch": '<:mrgameandwatch:838822011441774642>',
              "mr.game & watch": '<:mrgameandwatch:838822011441774642>',
              "mr.g&w": '<:mrgameandwatch:838822011441774642>',
              "mr game and watch": '<:mrgameandwatch:838822011441774642>',
              "game n watch": '<:mrgameandwatch:838822011441774642>',
              "mr game n watch": '<:mrgameandwatch:838822011441774642>',
              "gnw": '<:mrgameandwatch:838822011441774642>', "mr gnw": '<:mrgameandwatch:838822011441774642>',
              "gandw": '<:mrgameandwatch:838822011441774642>',
              "mr game & watch": '<:mrgameandwatch:838822011441774642>',
              "game & watch": '<:mrgameandwatch:838822011441774642>',
              "gw": '<:mrgameandwatch:838822011441774642>', "mr.game and watch": '<:mrgameandwatch:838822011441774642>',
              "g&w": '<:mrgameandwatch:838822011441774642>', "luigi": '<:luigi:838822011421196358>',
              "diddy": '<:diddykong:838822011337572394>', "green mario": '<:luigi:838822011421196358>',
              "diddy kong": '<:diddykong:838822011337572394>', "zelda": '<:zelda:838822011304280164>',
              "sheik": '<:sheik:838822011308212274>', "pit": '<:pit:838822011084996639>',
              "meta knight": '<:metaknight:838822011248967700>',
              "metaknight": '<:metaknight:838822011248967700>', "mk": '<:metaknight:838822011248967700>',
              "falco": '<:falco:838822011366408302>', "pokemon trainer": '<:pokemontrainer:838822010884194325>',
              "pt": '<:pokemontrainer:838822010884194325>',
              "pokemon": '<:pokemontrainer:838822010884194325>', "trainer": '<:pokemontrainer:838822010884194325>',
              "squirtle": '<:squirtle:838822011202437201>', "ivysaur": '<:ivysaur:838822011420803073>',
              "charizard": '<:charizard:838822011223539752>',
              "ike": '<:ike:838822010921943102>', "snake": '<:snake:838822011328659536>',
              "daisy": '<:peach:838822011030863874>',
              "peach": '<:peach:838822011030863874>', "yoshi": '<:yoshi:838822011164950582>',
              "ganondorf": '<:ganondorf:838822011324203088>', "ganon": '<:ganondorf:838822011324203088>',
              "ice climbers": '<:iceclimbers:838822010992984117>',
              "ics": '<:iceclimbers:838822010992984117>', "ic": '<:iceclimbers:838822010992984117>',
              "king dedede": '<:kingdedede:838822011224195082>', "king ddd": '<:kingdedede:838822011224195082>',
              "ddd": '<:kingdedede:838822011224195082>', "d3": '<:kingdedede:838822011224195082>',
              "wolf": '<:wolf:838822011215413268>', "lucario": '<:lucario:838822011349893181>',
              "ness": '<:ness:838822011031519314>', "sonic": '<:sonic:838822011202961499>',
              "zero suit samus": '<:zerosuitsamus:838822011299037234>',
              "zero suit": '<:zerosuitsamus:838822011299037234>', "zss": '<:zerosuitsamus:838822011299037234>',
              "bowser": '<:bowser:838822011371257918>', "wario": '<:wario:838822011240448051>',
              "toon link": '<:toonlink:838822011181727774>', "tink": '<:toonlink:838822011181727774>',
              "tl": '<:toonlink:838822011181727774>',
              "rob": '<:rob:838822011375452170>', "r.o.b.": '<:rob:838822011375452170>',
              "olimar": '<:olimar:838822011303362610>', "captain falcon": '<:captainfalcon:838822011370340362>',
              "cf": '<:captainfalcon:838822011370340362>',
              "falcon": '<:captainfalcon:838822011370340362>', "jigglypuff": '<:jigglypuff:838822010929807401>',
              "puff": '<:jigglypuff:838822010929807401>', "lucas": '<:lucas:838822011248836668>',
              "random": '<:random:838822010795589673>'}

characterlist = ['<:mario:838822011412676708>', '<:donkeykong:838822011114356760>', '<:link:838822011286716486>',
                 '<:samus:838822011009499147>', '<:zerosuitsamus:838822011299037234>',
                 '<:kirby:838822010968735796>', '<:fox:838822011408613396>',
                 '<:pikachu:838822011341111346>', '<:marth:838822011122745376>', '<:mrgameandwatch:838822011441774642>',
                 '<:luigi:838822011421196358>', '<:diddykong:838822011337572394>', '<:zelda:838822011304280164>',
                 '<:sheik:838822011308212274>', '<:pit:838822011084996639>', '<:metaknight:838822011248967700>',
                 '<:falco:838822011366408302>', '<:pokemontrainer:838822010884194325>', '<:ike:838822010921943102>',
                 '<:snake:838822011328659536>', '<:peach:838822011030863874>', '<:yoshi:838822011164950582>',
                 '<:ganondorf:838822011324203088>', '<:iceclimbers:838822010992984117>',
                 '<:kingdedede:838822011224195082>',
                 '<:wolf:838822011215413268>', '<:lucario:838822011349893181>', '<:ness:838822011031519314>',
                 '<:sonic:838822011202961499>', '<:bowser:838822011371257918>', '<:wario:838822011240448051>',
                 '<:toonlink:838822011181727774>', '<:rob:838822011375452170>', '<:olimar:838822011303362610>',
                 '<:captainfalcon:838822011370340362>', '<:jigglypuff:838822010929807401>',
                 '<:lucas:838822011248836668>']

opponents = {}
players2matches = {}
matches = {}
searching = {"NETP": {"bo3": [], "bo5": [], "bo7": []}, "WIFI": {"bo3": [], "bo5": [], "bo7": []}}
searchMessages = {}
challengeMessages = {}

banned = []
with open("banlistsave.json") as f:
    loadbanned = json.load(f)
    fixbanned = []
    for userID in loadbanned:
        fixbanned.append(int(userID))
    banned = fixbanned
    # print(banned)
global preranked
preranked = {"NETP": {}, "WIFI": {}}
with open("prerankingsave.json") as f:
    loadprerankings = json.load(f)
    fixedprerankingsN = {int(key): value for key, value in loadprerankings["NETP"].items()}
    fixedprerankingsW = {int(key): value for key, value in loadprerankings["WIFI"].items()}
    preranked["NETP"] = fixedprerankingsN
    preranked["WIFI"] = fixedprerankingsW
global rankings
rankings = {"NETP": {}, "WIFI": {}}
with open("rankingsave.json") as f:
    loadRankings = json.load(f)
    fixedRankingsN = {int(key): value for key, value in loadRankings["NETP"].items()}
    fixedRankingsW = {int(key): value for key, value in loadRankings["WIFI"].items()}
    rankings["NETP"] = fixedRankingsN
    rankings["WIFI"] = fixedRankingsW
# print(rankings)

sdplayers = {}
sdgames = {}

searchIcons = [abort, challenge]
searchSelection = [accept, cancel]
winloss = ["<:win:844045482237886465>", "<:loss:844045492798750761>"]
win = "<:win:844045482237886465>"
loss = "<:loss:844045492798750761>"

emotes2stage = {'<:Battlefield:837907213627686943>': "Battlefield",
                '<:FinalDestination:837907213695057950>': "Final Destination",
                '<:Smashville:837907213678542863>': "Smashville",
                '<:YoshisIsland:925956998024007680>': "Yoshi's Island",
                '<:LylatCruise:925957016135020545>': "Lylat Cruise",
                '<:PS1:925957052147310622>': "Pokemon Stadium 1",
                '<:CastleSiege:925957337867485284>': "Castle Siege",
                '<:FrigateOrpheon:925957063383867483>': "Frigate Orpheon",
                '<:PS2:1059009265433596004>': "Pokemon Stadium 2"
                }

# emotes2stage = {'<:Battlefield:837907213627686943>': "Battlefield",
#                 '<:FinalDestination:837907213695057950>': "Final Destination",
#                 '<:Smashville:837907213678542863>': "Smashville",
#                 '<:YoshisIsland:925956998024007680>': "Yoshi's Island",
#                 '<:LylatCruise:925957016135020545>': "Lylat Cruise",
#                 '<:PS1:925957052147310622>': "Pokemon Stadium 1",
#                 '<:CastleSiege:925957337867485284>': "Castle Siege",
#                 '<:FrigateOrpheon:925957063383867483>': "Frigate Orpheon"
#                 }
stage2emotes = {'<:Battlefield:837907213627686943>': BF,
                '<:FinalDestination:837907213695057950>': FD,
                '<:Smashville:837907213678542863>': SV,
                '<:YoshisIsland:925956998024007680>': YI,
                '<:LylatCruise:925957016135020545>': LC,
                '<:PS1:925957052147310622>': PS,
                '<:CastleSiege:925957337867485284>': CS,
                '<:FrigateOrpheon:925957063383867483>': FO,
                '<:PS2:1059009265433596004>': PS2
                }

startersize = 3
if startersize == 3:
    starters = ['<:Battlefield:837907213627686943>', '<:FinalDestination:837907213695057950>',
                '<:Smashville:837907213678542863>']
    counterpicks = ['<:YoshisIsland:925956998024007680>', '<:LylatCruise:925957016135020545>', '<:PS2:1059009265433596004>']
    stages = [BF, FD, SV]

elif startersize == 5:
    starters = ['<:Battlefield:837907213627686943>', '<:FinalDestination:837907213695057950>',
                '<:Smashville:837907213678542863>', '<:YoshisIsland:925956998024007680>',
                '<:LylatCruise:925957016135020545>']
    counterpicks = ['<:PS1:925957052147310622>', '<:CastleSiege:925957337867485284>',
                    '<:FrigateOrpheon:925957063383867483>']
    stages = [BF, FD, SV, YI, LC]
fullstagelist = starters + counterpicks
dsl = True
global decay
decay = False
global noDecayListNetp
noDecayListNetp = []
global noDecayListWifi
noDecayListWifi = []
global minGames
minGames = 3;

sets = ["bo3", "bo5", "bo7"]

def showstagelist(stages):
    text = ""
    for icon in stages:
        text += f"{icon} {emotes2stage[icon]}\n"
    return text


def remainingstagelist(fullstagelist, dsl):
    remainingstages = fullstagelist[:]
    for stage in dsl:
        remainingstages.remove(stage)
    return remainingstages


def sdscoreUpdate(title, username, userID, score, selecting):
    if title == True:
        return username

    elif title == False:
        details = f"Wins: {score} 🏆\n\n"
        if selecting == True:
            details += f"waiting for <@{userID}>\nto pick their character...\n(type it in this chat)"

        return details


def scrambled(inputlist):
    newlist = inputlist
    random.shuffle(newlist)
    return newlist


def randomroster():
    randomlist = scrambled(characterlist)
    randRoster = ""
    newLineCounter = 0
    for character in randomlist:
        randRoster += f"{character}ㅤ"
        newLineCounter += 1
        if newLineCounter == 10:
            randRoster += "\n\n"
            newLineCounter = 0
    return randRoster


def showroster(inputlist, fullroster):
    rostersize = len(inputlist)
    displayRoster = f"Remaining Roster ({rostersize}):\n\n"
    newLineCounter = 0
    for character in fullroster:
        if character in inputlist:
            displayRoster += f"{character}ㅤ"
        else:
            displayRoster += f"<:blank:876316169995431958>ㅤ"
            # <:blank:876316169995431958>
        newLineCounter += 1
        if newLineCounter == 10:
            displayRoster += "\n\n"
            newLineCounter = 0
    displayRoster += "\nㅤ"
    return displayRoster


def showused(username, roster):
    displayRoster = f"{username}\n"
    newLineCounter = 0

    for character in roster:
        displayRoster += f"{character}ㅤ"
        newLineCounter += 1
        if newLineCounter == 10:
            displayRoster += "\n\n"
            newLineCounter = 0
    displayRoster += "\nㅤ"
    return displayRoster


def banCheck(userID):
    if userID in banned:
        return True
    else:
        return False


def saveBanList(banlist):
    with open("banlistsave.json", "w") as f:
        json.dump(banlist, f)


def saveRankings(dictionary):
    with open("rankingsave.json", "w") as f:
        json.dump(dictionary, f)


def savePreRanked(dictionary):
    with open("prerankingsave.json", "w") as f:
        json.dump(dictionary, f)


def ELOCapCheck(playerID, matchType):
    if rankings[matchType][playerID] < 1:
        rankings[matchType][playerID] = 1
    elif rankings[matchType][playerID] > 9999:
        rankings[matchType][playerID] == 9999


def showELOChange(newELO, oldELO):
    sign = "+"
    if newELO < oldELO:
        sign = "-"
    changeValue = str(round(abs(newELO - oldELO)))
    showChange = sign + changeValue
    return showChange


def editPreranked(playerID, matchType):
    if playerID in preranked[matchType].keys():
        preranked[matchType][playerID] -= 1
        if preranked[matchType][playerID] == 0:
            preranked[matchType].pop(playerID)
        savePreRanked(preranked)


def displayELO(playerID, matchType):
    elo = rankings[matchType][playerID]
    questionmark = ""
    if playerID in preranked[matchType].keys():
        questionmark = "(?)"
    showELO = str(round(elo)) + questionmark
    return showELO


def findPlayer(LBType, standing):
    rankingList = rankings[LBType]
    strRankingList = {str(key): value for key, value in rankingList.items()}
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    playerList = list(sortedRankingList.keys())
    playerID = standing
    strPreranked = {str(key): value for key, value in preranked[LBType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)
    if playerID > len(playerList):
        playerID = 0
    else:
        playerID = int(playerList[standing - 1])
    return playerID


def buildLBoard(rankingList, listType, page, matchType):
    strRankingList = {str(key): value for key, value in rankingList.items()}
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    playerList = list(sortedRankingList.keys())
    strPreranked = {str(key): value for key, value in preranked[matchType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)

    LBContent = "```\n"

    part = 10
    max = part * page

    # if there is no one in the leaderboard
    if len(playerList) == 0:
        LBContent += "No players made it to the leaderboard yet..."
        max = len(playerList)
        begin = len(playerList)
        part = len(playerList)

    # if there are less than 10 players in the leaderboard
    elif max > len(playerList) and len(playerList) < 10:
        max = len(playerList)
        begin = len(playerList)
        part = len(playerList)
    # else if there are fewer players than what the user requests to see
    elif max > len(playerList):
        max = len(playerList)
        begin = 10
    # otherwise the leaderboard is created normally
    else:
        max = 10 * page
        begin = 10

    startindex = max - begin
    # print("start index: ", startindex)
    for index in range(part):
        # ("index:", index)
        # print("current index:", startindex + index)
        strPlayerID = playerList[startindex + index]
        intPlayerID = int(strPlayerID)
        playerName = client.get_user(intPlayerID)
        if playerName == None:
            playerName = f"UserID: {strPlayerID}"
        ELO = round(rankings[listType][intPlayerID])
        standing = startindex + index + 1
        player_block = f"{standing}) {playerName}".ljust(41)  # max name length is 32 + room for the #) part
        elo_block = f"[{ELO}]".rjust(6)  # ensure its spaced right
        LBContent += f"{player_block} {elo_block}\n\n"
    return LBContent + "```"


def getPlacement(rankingList, playerID, matchType):
    strPlayerID = str(playerID)
    strRankingList = {str(key): value for key, value in rankingList.items()}
    # print("strRankingList: ", strRankingList)
    sortedRankingList = dict(sorted(strRankingList.items(), key=lambda x: x[1], reverse=True))
    # print("sortedRankingList: ", sortedRankingList)
    playerList = list(sortedRankingList.keys())
    # print("playersList:", playerList)

    strPreranked = {str(key): value for key, value in preranked[matchType].items()}
    prerankedList = list(strPreranked.keys())
    for player in prerankedList:
        playerList.remove(player)

    standing = playerList.index(strPlayerID) + 1
    numOfPlayers = len(playerList)
    return standing, numOfPlayers


def forgetSearch(messageID):
    for messID in searchMessages[messageID]["challenges"]:
        challengeMessages.pop(messID)
    setType = searchMessages[messageID]["setType"]
    matchType = searchMessages[messageID]["matchType"]
    player = searchMessages[messageID]["player"]
    searching[matchType][setType].remove(player)
    searchMessages.pop(messageID)


def forgetMatch(messageID):
    for messID in matches[messageID]["players"].keys():
        opponents.pop(messID)
        players2matches.pop(messID)
    matches.pop(messageID)


def forgetSD(messageID):
    for playerID in sdgames[messageID]["playerlist"]:
        sdplayers.pop(playerID)
    sdgames.pop(messageID)


def forgetMessage(messageID):
    # if the message is a match window
    if messageID in matches.keys():
        forgetMatch(messageID)
    # if the message is a search message
    elif messageID in searchMessages.keys():
        forgetSearch(messageID)
    # if the message is for smashdown
    elif messageID in sdgames.keys():
        forgetSD(messageID)


def addPlayer(player, matchType):
    '''
    adds players to the ranking system
    :param player_id:
    :return:
    '''
    rankings[matchType][player] = 1500
    global minGames
    preranked[matchType][player] = minGames
    saveRankings(rankings)
    savePreRanked(preranked)


def calculateELO(winnerID, loserID, matchType, endCheck, modCheck, wNeeded):
    '''
    Calculates new elos for 2 players after a given game
    :param winnerID:
    winner's rating
    :param loserID:
    losers rating
    :param gameCount
    game count of the set
    :return:
    returns reward points
    '''
    endMultiplier = 1
    if endCheck == True:
        if wNeeded == 2:
            endMultiplier = 0.85
        elif wNeeded == 3:
            endMultiplier = 0.7
        elif wNeeded == 4:
            endMultiplier = 0.6

    elif modCheck == True:
        endMultiplier = 0.5
    winnerRating = rankings[matchType][winnerID]
    loserRating = rankings[matchType][loserID]
    setMultiplier = 1
    wMultiplier = 1
    lMultiplier = 1
    if winnerID in preranked[matchType].keys():
        wMultiplier = 1.5
    if loserID in preranked[matchType].keys():
        lMultiplier = 1.5

    # calculates the likely-hood of the result not occurring
    score = 1 - (1 / (1 + 10 ** ((loserRating - winnerRating) / 400)))
    multiplier = 36

    if endCheck == True or modCheck == True:
        wRewardPoints = round(multiplier * score * wMultiplier * endMultiplier)
        lRewardPoints = round(multiplier * score * lMultiplier * endMultiplier)

    elif endCheck == False:
        wRewardPoints = round(multiplier * score * wMultiplier * endMultiplier, 2)
        lRewardPoints = round(multiplier * score * lMultiplier * endMultiplier, 2)

    rankings[matchType][winnerID] += wRewardPoints
    rankings[matchType][loserID] -= lRewardPoints
    rankings[matchType][winnerID] = round(rankings[matchType][winnerID])
    rankings[matchType][loserID] = round(rankings[matchType][loserID])

    ELOCapCheck(winnerID, matchType)
    ELOCapCheck(loserID, matchType)

    saveRankings(rankings)

    newWinnerELO = rankings[matchType][winnerID]
    newLoserELO = rankings[matchType][loserID]
    # print("updated winner elo: ", newWinnerELO)
    # print("updated loser elo: ", newLoserELO)

    return newWinnerELO, newLoserELO


def createCharaList():
    charaList = "Here's a list of all the character inputs I can recognize:\n"
    charaList += "```"
    charaInputs = list(brawlChara.keys())
    sortedCharaInputs = sorted(charaInputs)
    for input in sortedCharaInputs:
        charaEmote = brawlChara[input]
        charaList += f"{input}\n"
    charaList += "```"
    return charaList


@client.event
async def on_ready():
    helpactivity = discord.Activity(name="-helpme", type=1)
    await client.change_presence(activity=helpactivity)
    print("Bot is ready")
    print(client.user.id)


@client.command()
async def helpme(ctx):
    # fetch change
    user = client.get_user(ctx.message.author.id)
    dm = await user.create_dm()
    await dm.send(f"**command prefix: ``-``**\n"
                  f"(begin every command with ``-`` in order for BrawlBot to recognize your command.)\n"
                  f"\n"
                  f"**__ranked__** ``(Online Type)`` ``(Set Type)``\n"
                  f"> This command begins a search queue for a ranked set. (Only usable in <#{searchChannel}>)\n"
                  f"> Online Type = ``netp`` (if you use netplay) or ``wifi`` (if you use wiimmfi)\n"
                  f"> Set Type = ``bo3`` (best of 3) or ``bo5`` or ``bo7``\n"
                  f"> \n"
                  f"> examples:\n"
                  f"> ``-ranked netp bo3``\n"
                  f"> ``-ranked wifi bo5``\n"
                  f"**__rank__**\n"
                  f"> This command allows you to view your own rank and standing in all ladders you're participating in. (Only usable in <#{miscChannel}>)\n"
                  f"> \n"
                  f"> You can look up another player's ranking info by @'ing them after the command.\n"
                  f"> \n"
                  f"> example: ``-rank @APR Financing``\n"
                  f"> \n"
                  f"> You can also look up a specific player based on standing within a specific ladder.\n"
                  f"> \n"
                  f"> exmaples:\n"
                  f"> ``-rank netp 3`` (retrieves the player who is top 3 in the netplay ladder)\n"
                  f"> ``-rank wifi 5`` (retrieves the player who is top 5 in the wiimmfi ladder)\n"
                  f"**__top__** ``(Online Type)`` ``(Page Number)``\n"
                  f"> Displays a leaderboard of the top 10 players for the specified ladder type. (Only usable in <#{miscChannel}>)\n"
                  f"> Online Type = ``netp`` (if you use netplay) or ``wifi`` (if you use wiimmfi)\n"
                  f"> Page Number = input a number to view a specific page of the leaderboard.\n"
                  f"> If no number is given, default page will be 1.\n"
                  f"> \n"
                  f"> examples:\n"
                  f"> ``-top netp`` (Shows the top 1-10 players in the netplay ladder)\n"
                  f"> ``-top wifi 2`` (Shows the top 11-20 players in the wifi ladder)\n"
                  f"> ``-top wifi 3`` (Shows the top 21-30 players in the wifi ladder)\n"
                  f"**__characters__**\n"
                  f"> This command sends a DM with a list containing all character inputs BrawlBot can recognize.\n"
                  f"> This is only relevant during character selections when in a ranked match.\n"
                  f"**__ironman__**\n"
                  f"> This command will send you a randomized brawl roster.\n"
                  f"> (usable in the freeplay channels)\n"
                  f"**__smashdown__**\n"
                  f"> This command sets up a smashdown card to help keep track of characters and score.\n"
                  f"> (usable in the freeplay channels)")
    await ctx.send("I sent you a DM with a list of my commands.")


@client.command()
async def decayon(ctx):

    if ctx.message.channel.id != modChannel:
        return

    await ctx.send("Decay activated")
    global decay
    decay = True
    global noDecayListNetp
    global noDecayListWifi
    #print(f"already played matches wifi: {noDecayListWifi}")
    #print(f"already played matches netp: {noDecayListNetp}")
    while decay == True:

        decayPeriod = 216000 # 2.5 days
        await asyncio.sleep(decayPeriod)
        global minGames
        for key in list(rankings["NETP"].keys()):

            if key in preranked["NETP"].keys():
                if preranked["NETP"][key] == minGames:
                    continue
            if key not in noDecayListNetp:
                #print(f"decaying netp: {key}")
                rankings["NETP"][key] -= 1
                ELOCapCheck(key, "NETP")
                saveRankings(rankings)


        for key in list(rankings["WIFI"].keys()):

            if key in preranked["WIFI"].keys():
                if preranked["WIFI"][key] == minGames:
                    continue
            if key not in noDecayListWifi:
                #print(f"decaying wifi: {key}")
                rankings["WIFI"][key] -= 1
                ELOCapCheck(key, "WIFI")
                saveRankings(rankings)

        noDecayListNetp = []
        noDecayListWifi = []
        #print(f"wifi list should be empty: {noDecayListWifi}")
        #print(f"netp list should be empty: {noDecayListNetp}")
        #print("decay happened")
    return


@client.command()
async def decayoff(ctx):
    if ctx.message.channel.id != modChannel:
        return
    await ctx.send("Decay deactivated")
    global decay
    decay = False
    return

@client.command()
async def newseason(ctx):
    if ctx.message.channel.id != modChannel:
        return
    await ctx.send("New season started. Ranks were reset.")
    global rankings
    rankings = {"NETP":{}, "WIFI":{}}
    global preranked
    preranked = {"NETP":{}, "WIFI":{}}
    saveRankings(rankings)
    savePreRanked(preranked)


@client.command()
async def smashdown(ctx):
    userID = ctx.message.author.id
    if userID in sdplayers.keys():
        await ctx.message.delete()
        await ctx.send("You already have a smashdown room up...", delete_after=6)
        return

    username = ctx.message.author
    userpfp = ctx.message.author.avatar_url
    embed = discord.Embed(
        title=f"Smashdown!",
        color=defaultColor,
        description=f"Click {join} to play with {username}"
    )
    embed.set_footer(text=f"Click on {leave} to end game.")
    embed.set_thumbnail(url=userpfp)
    await ctx.send("(This smashdown card will be auto deleted after 8 hours.)")
    smashdowngame = await ctx.send(embed=embed, delete_after=28800)
    await smashdowngame.add_reaction(leave)
    await smashdowngame.add_reaction(join)

    gameID = smashdowngame.id

    sdgames[gameID] = {
        "players": {userID: {"character": "n/a", "wins": 0, "selecting": False, "usedCharacters": [], "field": 0}},
        "playerlist": [userID],
        "winner": "n/a",
        "loser": "n/a",
        "messageObj": smashdowngame,
        "winsNeeded": 10,
        "remaining": ['<:mario:838822011412676708>', '<:donkeykong:838822011114356760>', '<:link:838822011286716486>',
                      '<:samus:838822011009499147>', '<:zerosuitsamus:838822011299037234>',
                      '<:kirby:838822010968735796>', '<:fox:838822011408613396>',
                      '<:pikachu:838822011341111346>', '<:marth:838822011122745376>',
                      '<:mrgameandwatch:838822011441774642>',
                      '<:luigi:838822011421196358>', '<:diddykong:838822011337572394>', '<:zelda:838822011304280164>',
                      '<:sheik:838822011308212274>', '<:pit:838822011084996639>', '<:metaknight:838822011248967700>',
                      '<:falco:838822011366408302>', '<:pokemontrainer:838822010884194325>',
                      '<:ike:838822010921943102>',
                      '<:snake:838822011328659536>', '<:peach:838822011030863874>', '<:yoshi:838822011164950582>',
                      '<:ganondorf:838822011324203088>', '<:iceclimbers:838822010992984117>',
                      '<:kingdedede:838822011224195082>',
                      '<:wolf:838822011215413268>', '<:lucario:838822011349893181>', '<:ness:838822011031519314>',
                      '<:sonic:838822011202961499>', '<:bowser:838822011371257918>', '<:wario:838822011240448051>',
                      '<:toonlink:838822011181727774>', '<:rob:838822011375452170>', '<:olimar:838822011303362610>',
                      '<:captainfalcon:838822011370340362>', '<:jigglypuff:838822010929807401>',
                      '<:lucas:838822011248836668>'],
        "closed": False,
    }

    sdplayers[userID] = {"sdgameID": gameID, "messageObj": smashdowngame, "opponent": "n/a"}

    # print(sdgames)
    # print(sdplayers)


@client.command()
async def ironman(ctx):
    username = ctx.message.author
    userpfp = ctx.message.author.avatar_url
    embed = discord.Embed(
        title=f"Randomized Roster for {username}",
        color=defaultColor,
        description=randomroster()
    )
    embed.set_thumbnail(url=userpfp)
    await ctx.send(embed=embed)


@client.command()
async def characters(ctx):
    userID = ctx.message.author.id
    # checks if user is banned
    if banCheck(userID) == True:
        return
    channelOrigin = ctx.message.channel.id
    # fetch change
    discordUser = client.get_user(userID)
    dm = await discordUser.create_dm()
    charaList = createCharaList()
    if channelOrigin in channelList:
        await ctx.send("I've sent you a DM with all character inputs I can currently recognize.")
    await dm.send(content=charaList)


@client.command()
async def ban(ctx):
    # checks if command is from the mod channel
    if ctx.message.channel.id != modChannel:
        return

    playerID = int(ctx.message.content[8:-1])
    # print(playerID)

    # checks if player in question is a real person
    if client.get_user(playerID) == None:
        # print("found no one")
        return

    if playerID in banned:
        await ctx.send("That player is already banned.")
        return

    if playerID in rankings["NETP"].keys():
        rankings["NETP"].pop(playerID)
        # print(rankings["NETP"])

    if playerID in rankings["WIFI"].keys():
        rankings["WIFI"].pop(playerID)
        # print(rankings["WIFI"])

    # print("banning: ", playerID)
    banned.append(int(playerID))
    # print(banned)

    saveBanList(banned)
    await ctx.send(f"<@{playerID}> was successfully banned.")


@client.command()
async def unban(ctx):
    # checks if command is from the mod channel
    if ctx.message.channel.id != modChannel:
        return
    playerID = int(ctx.message.content[10:-1])

    # checks if player in question is a real person
    if client.get_user(playerID) == None:
        return

    # checks if player in question is currently banned, otherwise it returns
    if playerID not in banned:
        return

    banned.remove(playerID)
    # print("removed player: ", banned)

    saveBanList(banned)

    await ctx.send(f"<@{playerID}> was successfully unbanned.")


@client.command()
async def changerank(ctx):
    ladderType = ctx.message.content[12:16].upper()

    if ladderType != "NETP" and ladderType != "WIFI":
        await ctx.send("Please specify what ladder you want to change rankings from.")
        return

    ladderColor = attributes[ladderType]["color"]
    winnerID = int(ctx.message.content[20:38].upper())
    loserID = int(ctx.message.content[43:61].upper())
    winnerName = client.get_user(winnerID)
    loserName = client.get_user(loserID)

    if winnerID not in rankings[ladderType].keys() or loserID not in rankings[ladderType].keys():
        await ctx.send(f"One or both of the users are not in the {ladderType} ladder.")
        return

    # print(ctx.message.content)
    # print("ladderType: ", ladderType)
    # print("winnerID: ", winnerID)
    # print("loserID: ", loserID)

    oldWinnerELO = rankings[ladderType][winnerID]
    oldLoserELO = rankings[ladderType][loserID]
    calculateELO(winnerID, loserID, ladderType, endCheck=False, modCheck=True, wNeeded=2)
    newWinnerELO = displayELO(winnerID, ladderType)
    newLoserELO = displayELO(loserID, ladderType)
    # winnerChange = showELOChange(rankings[ladderType][winnerID], oldWinnerELO)
    # loserChange = showELOChange(rankings[ladderType][loserID], oldLoserELO)
    embed = discord.Embed(
        title=f"Updated ELOs for {winnerName} and {loserName}",
        color=ladderColor,
        description=f"{winnerName} [{newWinnerELO}]\n"
                    f"{loserName} [{newLoserELO}]"
    )
    await ctx.send(embed=embed)


@client.command()
async def top(ctx):
    # checks if command is coming from it's designated channel
    if ctx.message.channel.id != miscChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{miscChannel}>", delete_after=10)
        return

    # checks if the user is banned
    if banCheck(ctx.message.author.id) == True:
        return

    topType = ctx.message.content[4:9].upper().strip()
    page = ctx.message.content[9:].strip()
    if page == "":
        page = 1
    page = int(page)
    if topType == "WIFI" or topType == "NETP":
        symbol = attributes[topType]["symbol"]
        embed = discord.Embed(
            title=f"{symbol} {topType} Leaderboard",
            color=attributes[topType]["color"],
            description=buildLBoard(rankings[topType], topType, page, topType)
        )
        await ctx.send(embed=embed)
        # print("recognized")
    else:
        await ctx.send("Please specify what type of leaderboard you'd like to view. (NETP or WIFI)", delete_after=10)


@client.command()
async def rank(ctx):
    # checks if command is coming from it's designated channel
    if ctx.message.channel.id != miscChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{miscChannel}>", delete_after=10)
        return

    authorID = ctx.message.author.id

    if banCheck(authorID) == True:
        return

    if ctx.message.content[6:10].upper() == "NETP" or ctx.message.content[6:10].upper() == "WIFI":
        boardType = ctx.message.content[6:10].upper()
        standing = ctx.message.content[11:]
        if standing == "":
            await ctx.send("Please specify what player standing you'd like to search for \n (ie. ``-rank wifi 3``)",
                           delete_after=8)
            return
        standing = int(standing)
        # print("boardType: ", boardType)
        # print("standing: ", standing)
        playerID = findPlayer(boardType, standing)


    else:
        playerID = ctx.message.content[9:-1]
        # print("ctx:", ctx.message.content)
        # print("playerID:", playerID)
        if playerID == "":
            playerID = authorID
        else:
            playerID = int(playerID)

    playerInfo = client.get_user(playerID)

    # checks if the user is in the rankings

    if playerID == 0:
        await ctx.send("No user with such standing found...")
        return
    elif playerID not in rankings["NETP"] and playerID not in rankings["WIFI"]:
        await ctx.send("No rankings found...")
        return

    embed = discord.Embed(
        title=f"{playerInfo}",
        colour=discord.Colour(defaultColor)
    )
    embed.set_thumbnail(url=playerInfo.avatar_url)

    if playerID in rankings["NETP"]:
        showNetpELO = displayELO(playerID, 'NETP')
        if playerID in preranked["NETP"].keys():
            gamesNeeded = preranked["NETP"][playerID]
            plural = ""
            if gamesNeeded > 1:
                plural = "s"
            valueContentNetp = f"Player currently unranked. \n{gamesNeeded} more game{plural} needed to be ranked."
        else:
            results = getPlacement(rankings["NETP"], playerID, "NETP")
            netpPlacement = results[0]
            netpNumOfPlayers = results[1]
            valueContentNetp = f"(Top {netpPlacement} out of {netpNumOfPlayers})"
        embed.add_field(name=f"{netpSymbol} NETP ELO: {showNetpELO}",
                        value=valueContentNetp,
                        inline=False)

    if playerID in rankings["WIFI"]:
        showWifiELO = displayELO(playerID, 'WIFI')

        if playerID in preranked["WIFI"].keys():
            gamesNeeded = preranked["WIFI"][playerID]
            plural = ""
            if gamesNeeded > 1:
                plural = "s"
            valueContentWifi = f"Player currently unranked. \n{gamesNeeded} more game{plural} needed to be ranked."

        else:
            results = getPlacement(rankings["WIFI"], playerID, "WIFI")
            wifiPlacement = results[0]
            wifiNumOfPlayers = results[1]
            valueContentWifi = f"(Top {wifiPlacement} out of {wifiNumOfPlayers})"
        embed.add_field(name=f"{wifiSymbol} WIFI ELO: {showWifiELO}",
                        value=valueContentWifi,
                        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ranked(ctx):
    # checks if search message is from the search channel
    if ctx.message.channel.id != searchChannel:
        await ctx.message.delete()
        await ctx.send(f"This command can only be used in <#{searchChannel}>", delete_after=10)
        return
    if banCheck(ctx.message.author.id) == True:
        return
    # if user is already in a match, they will be unable to queue up a search
    if ctx.message.author.id in players2matches.keys():
        await ctx.message.delete()
        await ctx.send("‼ You're currently in a match. ‼", delete_after=4)
        return

    matchType = ctx.message.content[8:12].upper()
    setType = ctx.message.content[13:16]
    if matchType != "NETP" and matchType != "WIFI":
        return
    if setType not in sets:
        return

    if ctx.message.author.id in searching[matchType][setType]:
        await ctx.send("‼ You're already searching for that. ‼", delete_after=4)
        await ctx.message.delete()
        return

    if matchType == "NETP":
        embedColor = netpColor
        icon = attributes["NETP"]['symbol']
    else:
        embedColor = wifiColor
        icon = attributes["WIFI"]['symbol']

    playerID = ctx.message.author.id

    # if the player isn't already in the ranking system, they get added
    if playerID not in rankings[matchType].keys():
        addPlayer(playerID, matchType)
    # print(rankings)

    showELO = displayELO(playerID, matchType)
    embed = discord.Embed(
        title=f"{ctx.message.author} [{showELO}] is searching for a match... \n"
              f"( {icon} {matchType} || {setType} )",
        description=f"({abort} = cancel search)\n(Search will end after 1 hour)\nClick on {challenge} to challenge them!\n"
                    f"Or unreact to withdraw your challenge.",
        color=discord.Colour(embedColor))
    embed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
    matchSearch = await ctx.send(embed=embed)
    searching[matchType][setType].append(playerID)
    searchMessages[matchSearch.id] = {"player": playerID,
                                      "matchType": matchType,
                                      "setType": setType,
                                      "challenges": [],
                                      "challengers": [],
                                      "color": embedColor,
                                      "messageObj": matchSearch,
                                      "queue": ctx}
    # Keeps track of the player who sent the search, type of match, and type of set. and distinguishes search messages

    # print("searching: ", searching)
    # print("searchMessages:", searchMessages)
    for icon in searchIcons:
        await matchSearch.add_reaction(icon)

    searchDuration = 3600
    await asyncio.sleep(searchDuration)
    if matchSearch.id in searchMessages:
        searchClose = discord.Embed(
            title=f"{ctx.message.author} [{showELO}] was searching for a match.",
            description=f"Search queue ended",
            color=discord.Colour(embedColor))
        searchClose.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        await matchSearch.edit(embed=searchClose)
        await matchSearch.clear_reactions()
        forgetMessage(matchSearch.id)


@client.event
async def on_message_delete(message):
    messageID = message.id

    if messageID in sdgames.keys():
        forgetSD(messageID)
        # print("sdgames: ", sdgames)
        # print("sdplayers: ", sdplayers)
        return

    if messageID not in searchMessages.keys():
        return
    commandmessage = searchMessages[messageID]["queue"]
    forgetMessage(messageID)
    await commandmessage.message.delete()
    # print("searchMessages should be empty: ", searchMessages)
    # print("challengeMessages should be empty: ", challengeMessages)
    # print("searching should be empty: ", searching)


@client.event
async def on_reaction_add(reaction, user):
    # print("emote:", reaction.emoji)

    if banCheck(user.id) == True:
        return

    messageID = reaction.message.id
    challengerID = user.id
    botID = client.user.id

    if challengerID == botID:  # client.user.id is the bot's ID. This prevents the bot from triggering any of the events when it sets up the emotes
        return

    if reaction.message.author.id != botID:  # Checks if reaction to message is not Brawlbot's
        return

    if messageID in searchMessages.keys() or messageID in matches.keys():  # Checks if this message is one that expects reactions on

        if messageID in searchMessages.keys():
            playerID = searchMessages[messageID]["player"]

        # event the player wants to cancel the search
        if reaction.emoji == abort and challengerID == playerID:  # only the person that queues up can cancel the search
            showELO = displayELO(playerID, searchMessages[messageID]["matchType"])
            embedColor = searchMessages[messageID]["color"]
            searchEnd = discord.Embed(
                title=f"{user} [{showELO}] was searching for a match.",
                description=f"Search queue ended",
                color=discord.Colour(embedColor))
            searchEnd.set_thumbnail(url=f"{user.avatar_url}")
            searchObj = searchMessages[messageID]["messageObj"]
            await searchObj.edit(embed=searchEnd)
            await searchObj.clear_reactions()
            forgetMessage(messageID)
            #commandmessage = searchMessages[messageID]["queue"]
            #await reaction.message.delete()
            #await commandmessage.message.delete()
            # print("searching should be gone: ", searching)
            # print("searchMessages should have deleted", searchMessages)
            # print("should have deleted challenges", challengeMessages)
        # event when someone clicks on challenge
        elif reaction.emoji == challenge:
            if challengerID == playerID:  # prevents you from challenging yourself
                return
            if user.id in players2matches.keys():
                await reaction.remove(user)
                channel = client.get_channel(searchChannel)
                await channel.send(f"<@{user.id}>You are currently in a match.", delete_after=4)
                return
            setType = searchMessages[messageID]["setType"]
            matchType = searchMessages[messageID]["matchType"]
            embedColor = searchMessages[messageID]["color"]
            icon = attributes[matchType]['symbol']
            if challengerID not in rankings[matchType].keys():
                addPlayer(challengerID, matchType)
                # print(rankings)
            showELO = displayELO(challengerID, matchType)
            embed = discord.Embed(
                title=f"{user} [{showELO}] would like to challenge you! \n"
                      f"( {icon} {matchType} || {setType} )",
                description=f"{accept} = accept challenge!",
                color=discord.Colour(embedColor))
            embed.set_thumbnail(url=user.avatar_url)  # shows the challenger's pfp
            # fetch change
            player = client.get_user(playerID)
            dm = await player.create_dm()

            dmChallenge = await dm.send(embed=embed)
            await dmChallenge.add_reaction(accept)

            challengeMessages[dmChallenge.id] = {"challenger": challengerID,
                                                 "searchMessage": reaction.message.id,
                                                 "messageObj": dmChallenge}
            searchMessages[messageID]["challenges"].append(dmChallenge.id)
            searchMessages[messageID]["challengers"].append(user.id)
            # print("challengers: ", searchMessages[messageID]["challengers"])
            # print("challengeMessages: ", challengeMessages)  # testing
            # print("searchMessages:", searchMessages)  # testing

        # event when players are in a match and want to cancel
        elif reaction.emoji == cancel and user.id in matches[messageID]["players"].keys():
            matches[messageID]["cancel"][user.id] = True
            # print("matches:", matches)
            if len(matches[messageID]["cancel"].keys()) == 2:
                matchType = matches[messageID]["matchType"]
                opponent = opponents[user.id]
                rankings[matchType][user.id] = matches[messageID]['players'][user.id]['elo']
                rankings[matchType][opponent] = matches[messageID]['players'][opponent]['elo']
                saveRankings(rankings)

                for plyrs in matches[messageID]["players"].keys():
                    players2matches.pop(plyrs)
                    opponents.pop(plyrs)
                # print("opponents should be empty: ", opponents)
                # print("players should be empty: ", players2matches)
                await matches[messageID]["messageObj"].delete()
                await matches[messageID]["pings"].delete()
                matches.pop(messageID)
                # print("matches should now be gone: ", matches)

        # event when players click on a reaction of a stage
        elif (str(reaction.emoji) in matches[messageID]["stages"]) or (str(reaction.emoji) == noBan):

            # game 1 procedures
            if matches[messageID]["gameCount"] == 1:
                if user.id == matches[messageID]["banning"]:
                    # print(f"ban is found{user.id}")
                    if len(matches[messageID]["stages"]) == 5:
                        matches[messageID]["banning"] = opponents[user.id]
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        # print("remaining stages: ", matches[messageID]["stages"])  # testing
                        # print("banning: ", matches[messageID]["banning"])  # testing
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = opponents[user.id]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                                value=f"{matches[messageID]['heading']}"
                                                    f"\n"
                                                    f"Waiting for <@{nextStrike}> to strike 2. (click on the reactions):\n"
                                                    f"{showstagelist(matches[messageID]['stages'])}",
                                                inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 4:
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        # print("remaining stages: ", matches[messageID]["stages"])  # testing
                        # print("banning: ", matches[messageID]["banning"])  # testing
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = user.id
                        newEmbed.set_field_at(0, name=f"Game 1",
                                                  value=f"{matches[messageID]['heading']}"
                                                        f"\n"
                                                        f"Waiting for <@{nextStrike}> to strike 1. (click on the reactions):\n"
                                                        f"{showstagelist(matches[messageID]['stages'])}",
                                                  inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 3:
                        matches[messageID]["banning"] = opponents[user.id]
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        #print("remaining stages: ", matches[messageID]["stages"])  # testing
                        #print("banning: ", matches[messageID]["banning"])  # testing

                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        nextStrike = opponents[user.id]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                              value=f"{matches[messageID]['heading']}"
                                                    f"\n"
                                                    f"Waiting for <@{nextStrike}> to strike. (click on the reactions):\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"{matches[messageID]['stages'][1]} {emotes2stage[matches[messageID]['stages'][1]]} \n",
                                              inline=False)
                        await reaction.clear()
                        await matchWindowObj.edit(embed=newEmbed)

                    elif len(matches[messageID]["stages"]) == 2:
                        matches[messageID]["banning"] = "N/A"
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                        #print("remaining stages: ", matches[messageID]["stages"])  # testing
                        #print("banning: ", matches[messageID]["banning"])  # testing
                        matchWindowObj = matches[messageID]['messageObj']
                        newEmbed = matchWindowObj.embeds[0]
                        newEmbed.set_field_at(0, name=f"Game 1",
                                              value=f"{matches[messageID]['heading']}"
                                                    f"Stage:\n"
                                                    f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n"
                                                    f"\n"
                                                    f"(winner reports by clicking <:win:844045482237886465> / "
                                                    f"loser reports by clicking <:loss:844045492798750761>)",
                                              inline=False)
                        newEmbed.set_thumbnail(url=stageTNs[matches[messageID]['stages'][0]])
                        await reaction.clear()
                        await matchWindowObj.clear_reaction(matches[messageID]['stages'][0].strip("<:>"))
                        await matchWindowObj.edit(embed=newEmbed)
                        for icon in winloss:
                            await matchWindowObj.add_reaction(icon.strip("<:>"))

            # game 2 and onwards procedures
            elif matches[messageID]["gameCount"] >= 2:
                #print("made it to game 2+")
                matchWindowObj = matches[messageID]['messageObj']
                newEmbed = matchWindowObj.embeds[0]
                gameCount = matches[messageID]["gameCount"]
                selecting = opponents[user.id]
                if user.id == matches[messageID]["banning"]:
                    matches[messageID]["banning"] = "N/A"
                    #print("made it to bans")
                    matches[messageID]["stagesel"] = opponents[user.id]
                    if str(reaction.emoji) in matches[messageID]["stages"]:
                        #print("stage recognized")
                        matches[messageID]["stages"].remove(str(reaction.emoji))
                    elif str(reaction.emoji) == noBan:
                        pass
                    #print("remaining stages", matches[messageID]["stages"])
                    newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                            value=f""
                                                f"\n"
                                                f"Waiting for <@{selecting}> to select their counterpick. (click on the reactions):\n"
                                                f"{showstagelist(matches[messageID]['stages'])}",
                                            inline=False)
                    await reaction.clear()
                    try:
                        await matchWindowObj.clear_reaction(noBan)
                    except:
                        pass

                    await matchWindowObj.edit(embed=newEmbed)

                elif matches[messageID]["stagesel"] == user.id:
                    #print("made it to stage selection")
                    matches[messageID]["banning"] = "N/A"
                    matches[messageID]["stagesel"] = "N/A"
                    stage = f"<:{reaction.emoji.name}:{reaction.emoji.id}>"
                    newEmbed.set_field_at(gameCount - 1, name=f"Game {gameCount}",
                                              value=f"(Waiting for character selections...)\n"
                                                    f"Stage:\n"
                                                    f"{stage} {emotes2stage[stage]} \n"
                                                    f"\n",
                                              inline=False)
                    newEmbed.set_thumbnail(url=stageTNs[stage])
                    matches[messageID]["heading"] = "N/A"
                    for icon in matches[messageID]['stages']:
                        await matchWindowObj.clear_reaction(icon.strip("<:>"))
                    try:
                        await matchWindowObj.clear_reaction(noBan)
                    except:
                        pass
                    await matchWindowObj.clear_reaction(noBan)
                    matches[messageID]["stages"] = [f"{stage}"]
                    await matchWindowObj.edit(embed=newEmbed)

                    dm = await (client.get_user(selecting)).create_dm()
                    charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {emotes2stage[stage]}]",
                                                description=f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                            f"If you're staying on the same character, click {stay}\n"
                                                            f"\n"
                                                                f"If you're having trouble selecting a character, type ``-characters``"
                                                                " to see a list of all character inputs I can recognize.",
                                                    color=defaultColor)
                    charaSelect.set_thumbnail(
                        url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
                    charaSelMessage = await dm.send(embed=charaSelect)
                    await charaSelMessage.add_reaction(stay)

        # event when win or loss is clicked
        elif str(reaction.emoji) in winloss and user.id in matches[reaction.message.id]["players"]:
            messageID = reaction.message.id
            if str(reaction.emoji) == win:
                matches[messageID]["winner"] = user.id
                # print("checking for winner: ", matches[messageID]["winner"])  # testing
            elif str(reaction.emoji) == loss:
                matches[messageID]["loser"] = user.id
                # print("checking for loser: ", matches[messageID]["loser"])  # testing

            # checks if opponent reported, otherwise it returns
            if str(reaction.emoji) == win and opponents[user.id] != matches[messageID]["loser"]:
                return

            elif str(reaction.emoji) == loss and opponents[user.id] != matches[messageID]["winner"]:
                return

            #calculateELO(matches[messageID]["winner"], matches[messageID]["loser"], matches[messageID]["matchType"],
             #            endCheck=False, modCheck=False, wNeeded=2)

            matches[messageID]["selections"][matches[messageID]["winner"]] = True
            matches[messageID]["selections"][matches[messageID]["loser"]] = False
            # print("both win and loss were selected")
            # print("winner should be selecting ", matches[messageID]["selections"][matches[messageID]["winner"]])
            # print("loser should not be selecting ", matches[messageID]["selections"][matches[messageID]["loser"]])
            winner = matches[messageID]['winner']
            loser = matches[messageID]['loser']
            winnerName = str(client.get_user(winner))[:-5]
            matches[messageID]["players"][winner]["wins"] += 1
            winnerChara = matches[messageID]['players'][winner]['character']
            if dsl == True:
                dslstage = matches[messageID]['stages']
                if dslstage[0] not in matches[messageID]['players'][winner]['dsl']:
                    matches[messageID]['players'][winner]['dsl'].append(dslstage[0])
            # print("dsl check: ", matches[messageID]['players'][winner])
            matchWindowObj = matches[messageID]["messageObj"]
            embedCount = matches[messageID]["gameCount"] - 1
            newEmbed = matchWindowObj.embeds[0]
            newEmbed.set_field_at(embedCount,
                                  name=f"Game {matches[messageID]['gameCount']} (Winner: {winnerChara} {winnerName})",
                                  value=f"{matches[messageID]['heading']}"
                                        f"Stage:\n"
                                        f"{matches[messageID]['stages'][0]} {emotes2stage[matches[messageID]['stages'][0]]} \n",
                                  inline=False
                                  )
            newEmbed.set_thumbnail(url='')
            await matchWindowObj.edit(embed=newEmbed)
            matches[messageID]["gameCount"] += 1
            if dsl == True:
                #print("dsl enabled")
                #print("fullstagelist: ", fullstagelist)
                matches[messageID]["stages"] = remainingstagelist(fullstagelist[:], matches[messageID]['players'][loser]['dsl'])
                #print("remaining stages after winloss: ", matches[messageID]["stages"])
            else:
                #print("stagelist not greater than 3")
                matches[messageID]["stages"] = fullstagelist[:]
                #print("fullstagelist: ", fullstagelist)
                #print("remaining stages after winloss: ", matches[messageID]["stages"])
            matches[messageID]["banning"] = matches[messageID]["winner"]
            matches[messageID]["winner"] = "N/A"
            matches[messageID]["loser"] = "N/A"
            # print("winner should be blank: ", matches[messageID]["winner"])
            # print("loser should be blank: ", matches[messageID]["loser"])
            matches[messageID]["heading"] = "N/A"
            # print("checking for updated game count: ", matches[messageID]["gameCount"])

            # if set is over
            if matches[messageID]["players"][user.id]["wins"] == matches[messageID]["winsNeeded"] or \
                    matches[messageID]["players"][opponents[user.id]]["wins"] == matches[messageID]["winsNeeded"]:
                winsNeed = matches[messageID]["winsNeeded"]
                calculateELO(winner, loser, matches[messageID]["matchType"], endCheck=False, modCheck=False,
                             wNeeded=winsNeed)
                matchType = matches[messageID]['matchType']
                newWinnerELO = rankings[matchType][winner]
                newLoserELO = rankings[matchType][loser]
                global noDecayListNetp
                global noDecayListWifi
                if matchType == "NETP":
                    if winner not in noDecayListNetp:
                        noDecayListNetp.append(winner)
                    if loser not in noDecayListNetp:
                        noDecayListNetp.append(loser)
                elif matchType == "WIFI":
                    if winner not in noDecayListWifi:
                        noDecayListWifi.append(winner)
                    if loser not in noDecayListWifi:
                        noDecayListWifi.append(loser)
                #print(f"ids should be added: {noDecayListNetp} {noDecayListWifi}")
                oldWinnerELO = matches[messageID]['players'][winner]['elo']
                oldLoserELO = matches[messageID]['players'][loser]['elo']
                winnerChange = showELOChange(newWinnerELO, oldWinnerELO)
                loserChange = showELOChange(newLoserELO, oldLoserELO)
                editPreranked(winner, matchType)
                editPreranked(loser, matchType)
                showWinnerELO = displayELO(winner, matchType)
                showLoserELO = displayELO(loser, matchType)
                # print("players2matches should be empty: ", players2matches)
                # print("opponents should be empty: ", opponents)
                # print("matches should be forgotten: ", matches)
                embed = matchWindowObj.embeds[0]
                embed.add_field(name=f"Results",
                                value=f"{win} {str(client.get_user(winner))[:-5]} [{showWinnerELO}] {winnerChange}\n"
                                      f"{loss} {str(client.get_user(loser))[:-5]} [{showLoserELO}] {loserChange}",
                                inline=False)
                rmWindow = 30
                embed.set_footer(text= f"Both players can click {rm} to initiate a rematch")
                winnerAvatar = client.get_user(winner).avatar_url
                embed.set_thumbnail(url=winnerAvatar)
                await matchWindowObj.unpin()
                await matchWindowObj.edit(embed=embed)
                await matchWindowObj.clear_reactions()
                await matchWindowObj.add_reaction(rm)
                await asyncio.sleep(rmWindow)
                await matchWindowObj.clear_reactions()
                embed.set_footer(text="")
                await matchWindowObj.edit(embed=embed)
                if messageID in matches.keys():
                    # print("rematch window closed")
                    forgetMessage(messageID)

            #otherwise
            else:
                banning = matches[messageID]["banning"]
                embed = matchWindowObj.embeds[0]
                embed.add_field(name=f"Game {matches[messageID]['gameCount']}",
                                value=f""
                                      f"\n"
                                      f"Waiting for <@{banning}> to ban. (click on the reactions):\n"
                                      f"{showstagelist(matches[messageID]['stages'])}",
                                inline=False)
                await matchWindowObj.edit(embed=embed)
                for icon in winloss:
                    await matchWindowObj.clear_reaction(icon.strip("<:>"))
                newstages = []
                for stageicon in matches[messageID]['stages']:
                    newstages.append(stage2emotes[stageicon])
                # print("newstages", newstages)
                for icon in newstages:
                    await matchWindowObj.add_reaction(icon)
                await matchWindowObj.add_reaction(noBan)

        # if rematch is clicked
        elif reaction.emoji == rm and user.id in matches[messageID]["players"].keys():
            # print("rematch was clicked")
            matches[messageID]["rematch"][user.id] = True
            if len(matches[messageID]["rematch"].keys()) == 2:
                messageObj = matches[messageID]["messageObj"]
                messageEmbed = messageObj.embeds[0]
                messageEmbed.set_footer(text="")
                await messageObj.edit(embed=messageEmbed)
                await messageObj.clear_reactions()

                playerID = matches[messageID]["playerList"][0]
                challengerID = matches[messageID]["playerList"][1]
                channel = client.get_channel(matchChannel)
                pings = await channel.send(f"<@{playerID}> <@{challengerID}>")

                matchType = matches[messageID]["matchType"]
                playerELO = displayELO(playerID, matchType)
                challengerELO = displayELO(challengerID, matchType)
                playerName = client.get_user(playerID)
                challengerName = client.get_user(challengerID)
                icon = matches[messageID]["icon"]
                setType = matches[messageID]["setType"]
                embedColor = matches[messageID]["embedColor"]
                winsNeeded = matches[messageID]["winsNeeded"]
                forgetMessage(messageID)
                # print("checking for empty matches list: ", matches)
                embed = discord.Embed(
                    title=f"{str(playerName)[:-5]} [{playerELO}] vs {str(challengerName)[:-5]} [{challengerELO}] \n"
                          f"( {icon} {matchType} || {setType} )",
                    description=f"(Both players can agree to cancel the set by clicking: {cancel}.)",
                    color=discord.Colour(embedColor))
                embed.add_field(name="Game 1", value="(double blind in progress...)\n")
                rematchWindow = await channel.send(embed=embed)
                await rematchWindow.pin()
                matches[rematchWindow.id] = {
                    "players": {
                        playerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][playerID], "dsl": []},
                        challengerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][challengerID],
                                       "dsl": []}
                        },
                    "winsNeeded": winsNeeded,
                    "cancel": {},
                    "rematch": {},
                    "heading": "N/A",
                    "gameCount": 1,
                    "stages": starters[:],
                    "banning": "N/A",
                    "stagesel": "N/A",
                    "selections": {playerID: True, challengerID: True},
                    "winner": "N/A",
                    "loser": "N/A",
                    "pings": pings,
                    "messageObj": rematchWindow,
                    "matchType": matchType,
                    "setType": setType,
                    "icon": icon,
                    "embedColor": embedColor,
                    "playerList": [playerID, challengerID]
                }

                players2matches[playerID] = rematchWindow.id
                players2matches[challengerID] = rematchWindow.id
                opponents[playerID] = challengerID
                opponents[challengerID] = playerID
                # print("opponents", opponents)
                # print("players: ", players2matches)

                await rematchWindow.add_reaction(cancel)
                dm1 = await playerName.create_dm()
                dm2 = await challengerName.create_dm()
                charaSelect = discord.Embed(title="[Game 1] (double blind)",
                                            description="Choose your character! \n Type out what character you will use.\n"
                                                        "\n"
                                                        "If you're having trouble selecting a character, type ``-characters``"
                                                        " to see a list of all character inputs I can recognize.",
                                            color=defaultColor)
                charaSelect.set_thumbnail(
                    url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
                await dm1.send(embed=charaSelect)
                await dm2.send(embed=charaSelect)
                # print("checking for new matches list: ", matches)


        # if the reaction is coming from a mod
        elif reaction.emoji == modkey:
            messageID = reaction.message.id

            # checks if key emote is on a match
            if messageID not in matches.keys():
                return

            matchWindowObj = matches[messageID]["messageObj"]
            embed = matchWindowObj.embeds[0]
            embed.add_field(name="Match was ended by mod.", value="🔨", inline=False)
            forgetMessage(messageID)
            await matchWindowObj.edit(embed=embed)
            await matchWindowObj.clear_reactions()

        # smashdown related reactions
        elif reaction.message.id in sdgames.keys():
            if reaction.emoji == join:
                print("join was clicked")

            # checks if same person is joining their own game
            if user.id in sdplayers.keys():
                # print("user already in match tried to join")
                return

            if sdgames[reaction.message.id]["closed"] == True:
                return

            sdgames[reaction.message.id]["closed"] = True

            messageID = reaction.message.id
            opponent = sdgames[messageID]["playerlist"][0]
            sdgames[messageID]["playerlist"].append(user.id)
            opponentName = client.get_user(opponent)
            username = client.get_user(user.id)

            sdplayers[user.id] = {"sdgameID": messageID, "messageObj": sdgames[messageID]["messageObj"],
                                  "opponent": opponent}
            sdplayers[opponent]["opponent"] = user.id
            sdgames[messageID]["players"][user.id] = {"character": "n/a", "wins": 0, "selecting": False,
                                                      "usedCharacters": [],
                                                      "field": 1}

            firstpick = random.choice(sdgames[messageID]["playerlist"])

            sdgames[messageID]["players"][firstpick]["selecting"] = True

            # print("sdplayers: ", sdplayers)
            # print("sdgames: ", sdgames)

            if sdgames[messageID]["players"][opponent]["selecting"] == True:
                selectmessageOpp = f"waiting for <@{opponent}>\nto pick their character...\n(type it in this chat)"
                selectmessageUsr = ""
            else:
                selectmessageOpp = f""
                selectmessageUsr = f"waiting for <@{user.id}>\nto pick their character...\n(type it in this chat)"

            newEmbed = discord.Embed(title="Smashdown!",
                                     description=showroster(sdgames[messageID]["remaining"], characterlist),
                                     color=defaultColor)

            newEmbed.add_field(name=opponentName, value=f"Wins: 0 🏆\n\n{selectmessageOpp}", inline=True)
            newEmbed.add_field(name=username, value=f"Wins: 0 🏆\n\n{selectmessageUsr}", inline=True)
            newEmbed.set_footer(text=f"Click on {leave} to end game.")

            sdgameMesObj = sdgames[messageID]["messageObj"]

            await sdgameMesObj.clear_reaction(join)
            await sdgameMesObj.edit(embed=newEmbed)

        # if player is trying to leave a game
        elif reaction.emoji == leave:
            if user.id not in sdgames[reaction.message.id]["playerlist"]:
                return
            # print("leave clicked")

            sdgameObj = sdgames[reaction.message.id]["messageObj"]

            if len(sdgames[reaction.message.id]["playerlist"]) == 1:
                await sdgameObj.delete()

            elif len(sdgames[reaction.message.id]["playerlist"]) == 2:
                await sdgameObj.clear_reactions()
                sdgameID = reaction.message.id
                opponent = sdplayers[user.id]["opponent"]

                rosterResults = sdgameObj.embeds[0]
                rosterResults.description = f"{showused(client.get_user(user.id), sdgames[sdgameID]['players'][user.id]['usedCharacters'])}\n" \
                                            f"{showused(client.get_user(opponent), sdgames[sdgameID]['players'][opponent]['usedCharacters'])}"

                updating = sdgameObj.embeds[0]
                updating2 = sdgameObj.embeds[0]
                footer = sdgameObj.embeds[0]

                userfield = sdgames[sdgameID]["players"][user.id]["field"]
                oppfield = sdgames[sdgameID]["players"][opponent]["field"]

                updating.set_field_at(index=userfield, name=f"{client.get_user(user.id)}",
                                      value=f"Wins: {sdgames[sdgameID]['players'][user.id]['wins']} 🏆\n\n")

                updating2.set_field_at(index=oppfield, name=f"{client.get_user(opponent)}",
                                       value=f"Wins: {sdgames[sdgameID]['players'][opponent]['wins']} 🏆\n\n")

                footer.set_footer(text="")

                await sdgameObj.edit(embed=rosterResults)
                await sdgameObj.edit(embed=updating)
                await sdgameObj.edit(embed=updating2)
                await sdgameObj.edit(embed=footer)

            forgetMessage(messageID)
            # print("sdgames should be deleted: ", sdgames)
            # print("sdplayers should be deleted: ", sdplayers)


        # if win or loss is reported on smashdown
        elif str(reaction.emoji) in winloss and user.id in sdplayers:
            # print("win loss recognized")
            sdgameID = sdplayers[user.id]["sdgameID"]
            nextgame = False
            if str(reaction.emoji) == win:
                sdgames[sdgameID]["winner"] = user.id
                # print("checking for winner: ", sdgames[sdgameID])
                if sdgames[sdgameID]["loser"] == sdplayers[user.id]["opponent"]:
                    nextgame = True
            elif str(reaction.emoji) == loss:
                sdgames[sdgameID]["loser"] = user.id
                # print("checking for loser: ", sdgames[sdgameID])
                if sdgames[sdgameID]["winner"] == sdplayers[user.id]["opponent"]:
                    nextgame = True

            if nextgame == True and sdgames[sdgameID]["remaining"] != 0:
                # print("moving on to the next game")

                sdgameObj = sdplayers[user.id]["messageObj"]

                for icon in winloss:
                    await sdgameObj.clear_reaction(icon)

                loser = sdgames[reaction.message.id]["loser"]
                winner = sdplayers[loser]["opponent"]
                loserfield = sdgames[reaction.message.id]["players"][loser]["field"]
                winnerfield = sdgames[reaction.message.id]["players"][winner]["field"]

                sdgames[sdgameID]["players"][winner]["wins"] += 1
                sdgames[sdgameID]["winner"] = "n/a"
                sdgames[sdgameID]["loser"] = "n/a"
                updating = sdgameObj.embeds[0]
                updating2 = sdgameObj.embeds[0]

                if len(sdgames[sdgameID]["remaining"]) > 1:
                    sdgames[reaction.message.id]["players"][loser]["selecting"] = True
                    sdgames[reaction.message.id]["players"][loser]["character"] = "n/a"
                    sdgames[reaction.message.id]["players"][winner]["character"] = "n/a"

                    updating.set_field_at(index=loserfield, name=f"{client.get_user(loser)}",
                                          value=f"Wins: {sdgames[sdgameID]['players'][loser]['wins']} 🏆\n\n"
                                                f"waiting for <@{loser}>\nto pick their character...\n(type it in this chat)")

                    updating2.set_field_at(index=winnerfield, name=f"{client.get_user(winner)}",
                                           value=f"Wins: {sdgames[sdgameID]['players'][winner]['wins']} 🏆\n\n")
                # if the roster is down to 1 character
                elif len(sdgames[sdgameID]["remaining"]) == 1:
                    # print("final character detected")
                    finalchara = sdgames[sdgameID]["remaining"][0]
                    sdgames[sdgameID]["remaining"].remove(finalchara)
                    # print("remaining should be empty: ", sdgames[sdgameID]["remaining"])
                    sdgames[reaction.message.id]["players"][loser]["character"] = finalchara
                    sdgames[reaction.message.id]["players"][winner]["character"] = finalchara

                    sdgames[sdgameID]['players'][winner]['usedCharacters'].append(finalchara)
                    sdgames[sdgameID]['players'][loser]['usedCharacters'].append(finalchara)

                    updating.set_field_at(index=loserfield, name=f"{client.get_user(loser)} {finalchara}",
                                          value=f"Wins: {sdgames[sdgameID]['players'][loser]['wins']} 🏆\n\n")

                    updating2.set_field_at(index=winnerfield, name=f"{client.get_user(winner)} {finalchara}",
                                           value=f"Wins: {sdgames[sdgameID]['players'][winner]['wins']} 🏆\n\n")

                    updatedRoster = sdgameObj.embeds[0]
                    updatedRoster.description = showroster(sdgames[sdgameID]["remaining"], characterlist)
                    await sdgameObj.edit(embed=updatedRoster)
                    for icon in winloss:
                        await sdgameObj.add_reaction(icon)

                # if there are no more characters
                elif len(sdgames[sdgameID]["remaining"]) == 0:
                    winnermark = ""
                    losermark = ""

                    if sdgames[sdgameID]['players'][winner]['wins'] > sdgames[sdgameID]['players'][loser]['wins']:
                        winnermark = "👑"

                    elif sdgames[sdgameID]['players'][winner]['wins'] < sdgames[sdgameID]['players'][loser]['wins']:
                        losermark = "👑"

                    # elif sdgames[sdgameID]['players'][winner]['wins'] == sdgames[sdgameID]['players'][loser]['wins']:
                    # drawmsg = sdgameObj.embeds[0]
                    # drawmsg.add_field(name="Draw Game", value='🎌', inline=False)
                    # await sdgameObj.edit(embed=drawmsg)

                    updating.set_field_at(index=loserfield, name=f"{losermark} {client.get_user(loser)} {losermark}",
                                          value=f"Wins: {sdgames[sdgameID]['players'][loser]['wins']} 🏆\n\n")

                    updating2.set_field_at(index=winnerfield, name=f"{winnermark} {client.get_user(winner)} {winnermark}",
                                           value=f"Wins: {sdgames[sdgameID]['players'][winner]['wins']} 🏆\n\n")

                    rosterResults = sdgameObj.embeds[0]
                    rosterResults.description = f"{showused(client.get_user(winner), sdgames[sdgameID]['players'][winner]['usedCharacters'])}\n" \
                                                f"{showused(client.get_user(loser), sdgames[sdgameID]['players'][loser]['usedCharacters'])}"

                    await sdgameObj.edit(embed=rosterResults)
                    await sdgameObj.clear_reactions()
                    forgetMessage(sdgameID)
                    # print("sdgames should be empty", sdgames)
                    # print("sdplayers should be empty", sdplayers)

                await sdgameObj.edit(embed=updating)
                await sdgameObj.edit(embed=updating2)


@client.event
async def on_reaction_remove(reaction, user):
    if banCheck(user.id) == True:
        return

    messageID = reaction.message.id
    userID = user.id
    # print("messageID: ", messageID)
    # print("reaction revoker id: ", userID)
    botID = client.user.id

    # client.user.id is the bot's ID. This prevents the bot from triggering any of the events when it sets up the emotes
    if userID == botID:
        return

    if reaction.emoji == challenge:
        if messageID not in searchMessages.keys():
            return
        if userID in searchMessages[messageID]["challengers"]:
            searchMessages[messageID]["challengers"].remove(userID)
        # print("user should be removed: ", searchMessages[messageID]["challengers"])
        # print("challenger successfully removed")


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(matchChannel)
    playerID = payload.user_id
    botID = client.user.id
    # print("payload: ", payload)

    if banCheck(playerID) == True:
        return

    # checks if reaction is on a challenge message
    if payload.message_id not in challengeMessages.keys() and playerID not in players2matches.keys():
        # print("not in there")
        return

    # event for when accept is clicked on
    elif payload.emoji.name == accept and playerID != botID:
        challengerID = challengeMessages[payload.message_id]['challenger']
        # print("payload: ", payload)
        challengemes = payload.message_id
        searchmes = challengeMessages[challengemes]["searchMessage"]
        # fetch change
        playerName = client.get_user(playerID)
        # fetch change
        challengerName = client.get_user(challengerID)

        # if the challenger withdrew their challenge, the bot deletes the challenge message and notifies the user
        if challengerID not in searchMessages[searchmes]["challengers"]:
            challengeObj = challengeMessages[challengemes]["messageObj"]
            await challengeObj.delete()
            withdrewDM = await playerName.create_dm()
            await withdrewDM.send(f"{challengerName} has withdrawn their challenge.")
            return

        # the the challenger is playing someone else, the bot deletes the challenge message and notifies the user
        if challengerID in players2matches.keys():
            challengeObj = challengeMessages[challengemes]["messageObj"]
            await challengeObj.delete()
            inMatchDM = await playerName.create_dm()
            await inMatchDM.send(f"{challengerName} is currently in a match.")
            return

        matchType = searchMessages[searchmes]["matchType"]
        setType = searchMessages[searchmes]["setType"]
        icon = attributes[matchType]['symbol']
        embedColor = searchMessages[searchmes]["color"]

        winsNeeded = int(setType[2:])//2 + 1
        # print(winsNeeded)

        # bot now stops keeping track of the search and corresponding challenge messages
        #await searchMessages[searchmes]["queue"].message.delete()
        #await searchMessages[searchmes]["messageObj"].delete()

        searchQueue = searchMessages[searchmes]["messageObj"]
        showELO = displayELO(playerID, matchType)
        searchFound = discord.Embed(
            title=f"{playerName} [{showELO}] found a match.",
            description=f"versus <@{challengerID}>",
            color=discord.Colour(embedColor))
        searchFound.set_thumbnail(url=playerName.avatar_url)
        await searchQueue.edit(embed=searchFound)
        await searchQueue.clear_reactions()
        forgetMessage(searchmes)


        pings = await channel.send(f"<@{playerID}> <@{challengerID}>")

        playerELO = displayELO(playerID, matchType)
        challengerELO = displayELO(challengerID, matchType)
        embed = discord.Embed(
            title=f"{str(playerName)[:-5]} [{playerELO}] vs {str(challengerName)[:-5]} [{challengerELO}] \n"
                  f"( {icon} {matchType} || {setType} )",
            description=f"(Both players can agree to cancel the set by clicking: {cancel}.)",
            color=discord.Colour(embedColor))
        embed.add_field(name="Game 1", value="(double blind in progress...)\n")
        matchWindow = await channel.send(embed=embed)
        await matchWindow.pin()
        matches[matchWindow.id] = {
            "players": {playerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][playerID], "dsl": []},
                        challengerID: {"character": "N/A", "wins": 0, "elo": rankings[matchType][challengerID], "dsl": []}
                        },
            "winsNeeded": winsNeeded,
            "cancel": {},
            "rematch": {},
            "heading": "N/A",
            "gameCount": 1,
            "stages": starters[:],
            "banning": "N/A",
            "stagesel": "N/A",
            "selections": {playerID: True, challengerID: True},
            "winner": "N/A",
            "loser": "N/A",
            "pings": pings,
            "messageObj": matchWindow,
            "matchType": matchType,
            "setType": setType,
            "icon": icon,
            "embedColor": embedColor,
            "playerList": [playerID, challengerID]
        }
        #print("matches: ", matches)  # testing

        players2matches[playerID] = matchWindow.id
        players2matches[challengerID] = matchWindow.id
        opponents[playerID] = challengerID
        opponents[challengerID] = playerID
        # print("opponents", opponents)
        # print("players: ", players2matches)

        await matchWindow.add_reaction(cancel)
        dm1 = await playerName.create_dm()
        dm2 = await challengerName.create_dm()
        charaSelect = discord.Embed(title="[Game 1] (double blind)",
                                    description="Choose your character! \n Type out what character you will use.\n"
                                                "\n"
                                                "If you're having trouble selecting a character, type ``-characters``"
                                                " to see a list of all character inputs I can recognize.",
                                    color=defaultColor)
        charaSelect.set_thumbnail(
            url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
        await dm1.send(embed=charaSelect)
        await dm2.send(embed=charaSelect)

        # print("searches should be deleted: ", searchMessages)  # testing
        # print("challenges should be deleted: ", challengeMessages)

    elif payload.emoji.name == stay and playerID != botID:
        playerDM = client.get_user(playerID)
        opponentDM = client.get_user(opponents[playerID])
        matchchannel = f"<#{matchChannel}>"
        matchWindowID = players2matches[playerID]
        selectedDM = await playerDM.create_dm()
        selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][playerID]['character']} selected!",
                                      description=f"Return to matchmaking: Click here -> {matchchannel}",
                                      color=defaultColor)
        selectedChara.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/845292400440377374/845292550889406494/R2F_smaller.png"
        )
        await selectedDM.send(embed=selectedChara)

        # if the winner is selecting their character
        if matches[matchWindowID]["heading"] == "N/A":
            matches[matchWindowID]["selections"][playerID] = False
            matches[matchWindowID]["selections"][opponents[playerID]] = True
            p1name = str(client.get_user(playerID))
            chara1 = matches[matchWindowID]['players'][playerID]['character']
            matches[matchWindowID]["heading"] = f"({p1name[:-5]}) {chara1} {versus} "
            # print(matches[matchWindowID]["heading"])  # testing
            stage = matches[matchWindowID]["stages"][0]
            stageName = emotes2stage[stage]

            playerCharacter = matches[matchWindowID]['players'][playerID]['character']
            gameCount = matches[matchWindowID]['gameCount']
            selectDM = await opponentDM.create_dm()
            charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {stageName}]",
                                        description=f"{playerDM} is going {playerCharacter}.\n"
                                                    f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                    f"If you're staying on the same character, click {stay}.\n"
                                                    f"\n"
                                                    f"If you're having trouble selecting a character, type ``-characters``"
                                                    " to see a list of all character inputs I can recognize.",
                                        color=defaultColor)
            charaSelect.set_thumbnail(
                url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
            opponentSel = await selectDM.send(embed=charaSelect)
            await opponentSel.add_reaction(stay)

        # if the loser is selecting their character
        elif matches[matchWindowID]["heading"] != "N/A":
            matches[matchWindowID]["selections"][playerID] = False
            p2name = str(client.get_user(playerID))
            chara2 = matches[matchWindowID]['players'][playerID]['character']
            matches[matchWindowID]["heading"] += f"{chara2} ({p2name[:-5]})\n"
            # print(matches[matchWindowID]["heading"])  # testing

            matchWindowObj = matches[matchWindowID]["messageObj"]
            embedCount = matches[matchWindowID]["gameCount"] - 1
            newEmbed = matchWindowObj.embeds[0]
            newEmbed.set_field_at(embedCount,
                                  name=f"Game {matches[matchWindowID]['gameCount']}",
                                  value=f"{matches[matchWindowID]['heading']}"
                                        f"Stage:\n"
                                        f"{matches[matchWindowID]['stages'][0]} {emotes2stage[matches[matchWindowID]['stages'][0]]} \n",
                                  inline=False
                                  )
            await matchWindowObj.edit(embed=newEmbed)
            for icon in winloss:
                await matchWindowObj.add_reaction(icon.strip("<:>"))



@client.event
async def on_message(message):
    await client.process_commands(message)
    authorID = message.author.id
    botID = 837093793722662942
    content = str(message.content.lower().strip())

    if banCheck(authorID) == True:
        return

    # bot ignores it's own messages
    if authorID == botID:
        return
    # bot ignores non-command based messages if it's not in a DM
    if message.guild in client.guilds and authorID in sdplayers.keys():
        # print("message recieved")
        sdgameID = sdplayers[authorID]["sdgameID"]
        if sdgames[sdgameID]["players"][authorID]["selecting"] == True:
            if content in brawlChara.keys():
                # print("Valid input recognized")
                await message.delete()
                if brawlChara[content] not in sdgames[sdgameID]["remaining"]:
                    return

                sdgames[sdgameID]["players"][authorID]["selecting"] = False
                sdgameObject = sdgames[sdgameID]["messageObj"]
                charaIcon = brawlChara[content]

                sdgames[sdgameID]["remaining"].remove(charaIcon)
                sdgames[sdgameID]["players"][authorID]["usedCharacters"].append(charaIcon)
                sdgames[sdgameID]["players"][authorID]["character"] = charaIcon

                fieldnum = sdgames[sdgameID]["players"][authorID]["field"]

                opponentID = sdplayers[authorID]["opponent"]

                selectEmbed = sdgameObject.embeds[0]
                selectEmbed.set_field_at(index=fieldnum, name=f"{client.get_user(authorID)} {charaIcon}",
                                         value=f"Wins: {sdgames[sdgameID]['players'][authorID]['wins']} 🏆")
                updatedRoster = sdgameObject.embeds[0]
                updatedRoster.description = showroster(sdgames[sdgameID]["remaining"], characterlist)

                await sdgameObject.edit(embed=selectEmbed)
                await sdgameObject.edit(embed=updatedRoster)

                if sdgames[sdgameID]["players"][opponentID]["character"] == "n/a":
                    sdgames[sdgameID]["players"][opponentID]["selecting"] = True
                    opponentField = sdgames[sdgameID]["players"][opponentID]["field"]

                    opponentEmbed = sdgameObject.embeds[0]

                    opponentEmbed.set_field_at(index=opponentField, name=f"{client.get_user(opponentID)}",
                                               value=f"Wins: {sdgames[sdgameID]['players'][opponentID]['wins']} 🏆\n\n"
                                                     f"waiting for <@{opponentID}>\nto pick their character...\n(type it in this chat)")
                    await sdgameObject.edit(embed=opponentEmbed)
                else:
                    sdFooter = sdgameObject.embeds[0]
                    sdFooter.set_footer(
                        text=f"Click on {leave} to end game.\nReport wins and losses by reacting below.")
                    await sdgameObject.edit(embed=sdFooter)
                    for icon in winloss:
                        await sdgameObject.add_reaction(icon)
                    # print("sdgames: ", sdgames)
        return

    # checks if the message author is in a match
    if authorID in players2matches.keys():

        matchWindowID = players2matches[authorID]

        if matches[matchWindowID]["selections"][authorID] == False:
            return

        if content != "stay" and content not in brawlChara.keys():
            return

        opponent = opponents[authorID]
        matchchannel = f"<#{matchChannel}>"

        # character selection event for game 1
        if matches[matchWindowID]['gameCount'] == 1:
            character = str(message.content.lower().strip())
            if character not in brawlChara.keys():
                return

            matches[matchWindowID]["players"][authorID]["character"] = brawlChara[character]
            selectedDM = await message.author.create_dm()
            selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                          description=f"Return to matchmaking: Click here -> {matchchannel}",
                                          color=defaultColor)
            selectedChara.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/845292400440377374/845292550889406494/R2F_smaller.png")
            await selectedDM.send(embed=selectedChara)
            # print("matches for double blinds:", matches)

            # checks if opponent has their character locked in
            if matches[matchWindowID]["players"][opponent]["character"] != "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                matches[matchWindowID]["selections"][opponents[authorID]] = False
                matchWindowObj = matches[matchWindowID]["messageObj"]
                p1ID = authorID
                p1name = str(client.get_user(authorID))
                p2ID = opponents[authorID]
                p2name = str(client.get_user(p2ID))
                chara1 = matches[matchWindowID]["players"][p1ID]["character"]
                chara2 = matches[matchWindowID]["players"][p2ID]["character"]
                firstStrike = random.choice([p1ID, p2ID])
                matches[matchWindowID]["banning"] = firstStrike
                stagelist = matches[matchWindowID]["stages"]
                newEmbed = matchWindowObj.embeds[0]
                heading = f"({p1name[:-5]}) {chara1} {versus} {chara2} ({p2name[:-5]})\n"
                matches[matchWindowID]["heading"] = heading
                newEmbed.set_field_at(0, name=f"Game 1",
                                      value=f"{heading}"
                                            f"\n"
                                            f"Waiting for <@{firstStrike}> to strike. (click on the reactions):\n"
                                            f"{showstagelist(stagelist)}",
                                      inline=False)
                await matchWindowObj.edit(embed=newEmbed)
                for icon in stages:
                    await matchWindowObj.add_reaction(icon.strip("<:>"))

                #print("checking for who's banning: ", matches[matchWindowID])

        # event for character selections game 2 and onwards
        elif matches[matchWindowID]['gameCount'] >= 2:
            selection = str(message.content.lower().strip())

            if selection in brawlChara.keys():
                matches[matchWindowID]['players'][authorID]['character'] = brawlChara[selection]

            # elif selection == "stay":
            # print("nothing changes")

            playerDM = client.get_user(authorID)
            opponentDM = client.get_user(opponents[authorID])
            selectedDM = await playerDM.create_dm()
            selectedChara = discord.Embed(title=f"{matches[matchWindowID]['players'][authorID]['character']} selected!",
                                          description=f"Return to matchmaking: Click here -> {matchchannel}",
                                          color=defaultColor)
            selectedChara.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/845292400440377374/845292550889406494/R2F_smaller.png"
            )
            await selectedDM.send(embed=selectedChara)

            # if the winner is selecting their character
            if matches[matchWindowID]["heading"] == "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                matches[matchWindowID]["selections"][opponents[authorID]] = True
                p1name = str(client.get_user(authorID))
                chara1 = matches[matchWindowID]['players'][authorID]['character']
                matches[matchWindowID]["heading"] = f"({p1name[:-5]}) {chara1} {versus} "
                # print(matches[matchWindowID]["heading"])  # testing
                stage = matches[matchWindowID]["stages"][0]
                stageName = emotes2stage[stage]

                playerCharacter = matches[matchWindowID]['players'][authorID]['character']
                gameCount = matches[matchWindowID]['gameCount']
                selectDM = await opponentDM.create_dm()
                charaSelect = discord.Embed(title=f"[Game {gameCount} | {stage} {stageName}]",
                                            description=f"{playerDM} is going {playerCharacter}.\n"
                                                        f"Choose your character for Game {gameCount}! \n Type out what character you will use.\n"
                                                        f"If you're staying on the same character, click {stay}.\n"
                                                        f"\n"
                                                        f"If you're having trouble selecting a character, type ``-characters``"
                                                        " to see a list of all character inputs I can recognize.",
                                            color=defaultColor)
                charaSelect.set_thumbnail(
                    url="https://media.discordapp.net/attachments/405387786036707329/843029286961414144/coinhand2.png")
                opponentSel = await selectDM.send(embed=charaSelect)
                await opponentSel.add_reaction(stay)
            # if the loser is selecting their character
            elif matches[matchWindowID]["heading"] != "N/A":
                matches[matchWindowID]["selections"][authorID] = False
                p2name = str(client.get_user(authorID))
                chara2 = matches[matchWindowID]['players'][authorID]['character']
                matches[matchWindowID]["heading"] += f"{chara2} ({p2name[:-5]})\n"
                # print(matches[matchWindowID]["heading"])  # testing

                matchWindowObj = matches[matchWindowID]["messageObj"]
                embedCount = matches[matchWindowID]["gameCount"] - 1
                newEmbed = matchWindowObj.embeds[0]
                newEmbed.set_field_at(embedCount,
                                      name=f"Game {matches[matchWindowID]['gameCount']}",
                                      value=f"{matches[matchWindowID]['heading']}"
                                            f"Stage:\n"
                                            f"{matches[matchWindowID]['stages'][0]} {emotes2stage[matches[matchWindowID]['stages'][0]]} \n",
                                      inline=False
                                      )
                await matchWindowObj.edit(embed=newEmbed)
                for icon in winloss:
                    await matchWindowObj.add_reaction(icon)


# last worked on 1/1/2023


if clonebot == True:
    botkey = " "
elif clonebot == False:
    botkey = " "

client.run(botkey)
