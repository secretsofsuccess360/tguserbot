"""
Created By @Jisan7509
GF created by @KshitijGagan
"""
import asyncio
import random

from userbot import catub

from ..core.managers import edit_or_reply
from . import catmemes

plugin_category = "extra"


@catub.cat_cmd(
    pattern="abuse$",
    command=("abuse", plugin_category),
    info={
        "header": "shows you some abuse sentences",
        "usage": "{tr}abuse",
    },
)
async def abusing(abused):
    "random abuse string"
    reply_text = random.choice(catmemes.ABUSE_STRINGS)
    await edit_or_reply(abused, reply_text)


@catub.cat_cmd(
    pattern="abusehard$",
    command=("abusehard", plugin_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}abusehard",
    },
)
async def fuckedd(abusehard):
    "random gali string"
    reply_text = random.choice(catmemes.ABUSEHARD_STRING)
    await edit_or_reply(abusehard, reply_text)


@catub.cat_cmd(
    pattern="randi$",
    command=("randi", plugin_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}randi",
    },
)
async def metoo(e):
    "random gali string"
    txt = random.choice(catmemes.RENDISTR)
    await edit_or_reply(e, txt)


@catub.cat_cmd(
    pattern="rape$",
    command=("rape", plugin_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}rape",
    },
)
async def raping(raped):
    "random gali string"
    reply_text = random.choice(catmemes.RAPE_STRINGS)
    await edit_or_reply(raped, reply_text)


@catub.cat_cmd(
    pattern="fuck$",
    command=("fuck", plugin_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}fuck",
    },
)
async def chutiya(fuks):
    "random gali string"
    reply_text = random.choice(catmemes.CHU_STRINGS)
    await edit_or_reply(fuks, reply_text)


@catub.cat_cmd(
    pattern="thanos$",
    command=("thanos", plugin_category),
    info={
        "header": "shows you some gali sentences",
        "usage": "{tr}thanos",
    },
)
async def thanos(thanos):
    "random gali string"
    reply_text = random.choice(catmemes.THANOS_STRINGS)
    await edit_or_reply(thanos, reply_text)

@catub.cat_cmd(
    pattern="gf$",
    command=("gf", plugin_category),
    info={
        "header": "fuck GF",
        "usage": "{tr}gf",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(21)
    kakashi = await edit_or_reply(event, "BSDK tera gf h na ek ...!")
    animation_chars = [
        "`Ruk jaa , Abhi teri GF ko Fuck karta hu`",
        "`Teri GF ka mood bana rha 🔥`",
        "`Teri GF ki gand pakad ke kiss kr rha 🤚😘`",
        "`Teri GF ki chut mai ungli daal rha🖕`",
        "`Teri GF ki chut ka test le rha 💧😍👅`",
        "`Teri GF muhh me lund lene ko keh rhi🍌`",
        "`Requested accepted😻💋, Teri GF lund ka test le rhi🍌`",
        "`Teri GF chudne ke liye ready hai 👀`",
        "`Your GF Is Ready To Fuck`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ki chut laal kardi\n\nTeri GF chut mai pura le rhi\n\nBs hone wala hai. 0%\n\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ki chut mese\n\nWhite paani\n\nNikal rha pura..\n\nBhot chud rhi... 4%\n\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ki gand aahh\n\nTeri GF ki gand pe\n\nThappad maar rha...\n\nBhot chuda rhi... 8%\n\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ke boobs\n\nTeri GF ke nipples\n\nMuhh me le rha....\n\nBhot tight ho gye boobs... 20%\n\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ki gand mai\n\nPura lund Ja rha\n\nGand ka hole.....\n\nPura laal kar diya... 36%\n\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ki chut ka\n\nBhot zor se chod rha\n\nPani ane lag......\n\nGya chut mese... 52%\n\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ki chut mai\n\nBhot zor se chod rha\n\nPani chhod rhi.......\n\nKash k chut... 84%\n\n███████████████████▒▒▒▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF blowjob de rhi\n\nLund uski chut mese ake\n\nMuhh me........\n\nJa rha... 89%\n\n██████████████████████▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF lund le rhi pura\n\nGale tak daal rhi\n\nLund ka.......\n\nTest le rhi... 90%\n\n██████████████████████▒▒▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF keh rhi fuck me aahhh\n\nAb teri GF ki chut mai bhot\n\nZor se.......\n\nChod rha... 96%\n\n████████████████████████▒`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ab muhh me cum le legi\n\nTeri GF k muh me\n\nLund diya.......\n\nCum in mouth... 100%\n\n█████████████████████████`",
        "`Teri GF ko chodte hue🖕🤤\n\nTeri GF ka mai sex partner\n\nTeri GF keh rhi mai\n\nPermanent sex partner\n\nOf your GF🤤🤤`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 21])

@catub.cat_cmd(
    pattern="fk (.*)$",
    command=("fk (.*)", plugin_category),
    info={
        "header": "chitiya gandu lodu",
        "usage": "{tr}fk (.*)",
    },
)
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    animation_interval = 3
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "👁👁")
    animation_chars = [
        f"👁👁\n  👄  =====> Abey {name} Chutiya",
        f"👁👁\n  👅  =====> Abey {name} Gay",
        f"👁👁\n  💋  =====> Abey {name} Lodu",
        f"👁👁\n  👄  =====> Abey {name} Gandu",
        f"👁👁\n  💋  =====> Abey {name} Randi",
        f"👁👁\n  👄  =====> Abey {name} Betichod",
        f"👁👁\n  👅  =====> Abey {name} Behenchod",
        f"👁👁\n  💋  =====> Abey {name} NaMard",
        f"👁👁\n  👄  =====> Abey {name} Lavde",
        f"👁👁\n  👅  =====> Abey {name} Bhosdk",
        f"👁👁\n  👄  =====> Hi {name} Mc, How Are You Bsdk...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])



@catub.cat_cmd(
    pattern="chod$",
    command=("chod", plugin_category),
    info={
        "header": "fuck mom",
        "usage": "{tr}chod",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "1 2 3..Searching Randi..")
    animation_chars = [
        "`Randi Founded`",
        "`Your Mom Is Going To Fuck`",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 84%\n█████████████████████▒▒▒▒ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 100%\n█████████████████████████ `",
        "`Fucking Your Mom\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nYour mom get Pregnant\n\nResult: Now You Have 1 More Younger Brother `",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])

@catub.cat_cmd(
    pattern="kiss$",
    command=("kiss", plugin_category),
    info={
        "header": "shows you fun kissing animation",
        "usage": "{tr}kiss",
    },
)
async def _(event):
    "fun animation"
    catevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@catub.cat_cmd(
    pattern="fuk$",
    command=("fuk", plugin_category),
    info={
        "header": "shows you fun fucking animation",
        "usage": "{tr}fuk",
    },
)
async def _(event):
    "fun animation"
    catevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@catub.cat_cmd(
    pattern="sex$",
    command=("sex", plugin_category),
    info={
        "header": "shows you fun sex animation",
        "usage": "{tr}sex",
    },
)
async def _(event):
    "fun animation"
    catevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])

@catub.cat_cmd(
    pattern="nikal$",
    command=("nikal", plugin_category),
    info={
        "header": "Nikal Laude",
        "usage": "{tr}nikal",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    kakashi = await edit_or_reply(event, "nakal")
    animation_chars = [
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Lavde   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pehli   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(P)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Fursat  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Meeee   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀lodu⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 6])

@catub.cat_cmd(
    pattern="gaali$",
    command=("gaali", plugin_category),
    info={
        "header": "Hindi Big Gaali 1",
        "usage": "{tr}gaali",
    },
)
async def cat(event):
    await edit_or_reply(
        event,
        "Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI !",
    )

@catub.cat_cmd(
    pattern="gali$",
    command=("gali", plugin_category),
    info={
        "header": "Hindi Big Gaali 2",
        "usage": "{tr}gali",
    },
)
async def cat(event):
    await edit_or_reply(
        event,
        "Behen ke lode madahrchod teri ma randi bhsdk tera pyra khandan randi teri kandan kai ma ka bhods lund katta madarchod tere lund pe road roller chale tere behen ki chut kate tura khandan ke gand me bomb phute teri ma ke bur me 100 log ke lund teri behen ke bur me 100 log ke lund madarchod behenchod mai ka loda behen ka loda randi teri behen ma ki chut behen ki chut teri chut ki chut harami phate hue condom ke nateeje tera baap ko paisa nahi tha to uses condom se teri maa ko chooda benchod lodo hai tu sabka chusta gay lund hai nahi be lund akuad me re hamare desh ki taraf bhi dekha to tatte ukhad ke kutto ko keladenge madharchod Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI loda leke muh me nachne wale ma ki jaat lund kate tera tiri bb ko chode duniya tiri gand me parmanu dhamaka teri ma ka buur me garam oil ki kadhai teri behen ki bane porn aur upload ho pornhub me teri ma ko 100 logo ne choda tab tu paida hua tra papa gay tu gay tera khandan gay bc mc maki chut belen ki lodi ma ki lodi behen teri randi ma teri randi loda undono ke muh me loda katgaya to muh me lele aur kuch hame bola to tera loda tere muh me deke tere gand se nikalenge madarchod beti teru chodaye beti teri rundi teri beti ki bur me 1000 logo ka lund teri beti ka gangbang tere papa be lund nund na hone ke karan teri ma rundi teri ma randi hone ke karan tu aur tera bhai behen teri behen radi kuki teri ma randi behen radi hone ke karan ro 1000 se choda ke uske 10000 bacche tere lund par hathi dore teri gand me chiti kate kera pura satyanash ho *Main roz teri* *behno ki banjar chut me* *apna lawda daalke andar* *haryali lata tha magar aaj* *unke ke baare me* *sunke mujhe bhut afsos* *huwa..ki unko ab bada loudha chahye..ab mera balatkaaari* *lawda lagataar 4 ghante tk* *apne muh me kon* *rakhega..vo teri* *behne hi thi jo apni kaali* *magar rasilli chut mere* *saamne khol deti aur* *zameen pe naagin ki tarah* *rengne lgti thi jaise ki* *kisine unki chut pe naariyal* *tod diya ho vo b bada wala* *mumbai ka naariyal.",
    )

@catub.cat_cmd(
    pattern="egali$",
    command=("egali", plugin_category),
    info={
        "header": "Big English Gaali",
        "usage": "{tr}egali",
    },
)
async def cat(event):
    await edit_or_reply(
        event,
        "This is for you your a fucking waste of sperm madfaka I   don't know why your parents give birth a worthless shit like you  you faggot ass with a fucking gay bi sextual laurstic slutty minded kid lemaric siliastic  crow  face and ass hahaha your like a pork shit 💩madfaka tell your father to fuck you everynight so that u can have your pussy more effective to everyone  who did fucked you till now  bullshit say to Infront of everyone eyes like I eat bunny's pees at the same time while am sucking his dick bleh 😂 haha 😂😂😂😂 madfaka what u thought maybe u thought like am from India bsdk am not and that's why am fucking isolated from you ya know what your a fucking black ass who is in form of an human you will get fucked again by this bunny wait for it didle doddoy kid with a fucking phony dick 😂😂😂😂😂😂😂😂😂 fuck you🖕i will come again and again  for fucking your black ass shit everytime you  will be in front of my eyes  i will be there for fucking your Lili crow as black face hahaha for you😂😂😂👉👌🖕maderchod who the fuck are u u fucking inferior shitty asshole u know what shit you are the shit who drink my pees instead of drinking water now I will fuck ur mom one-day I went to your house with a condom then literally I went up to your mom shitty asshole and fucked  it like a real hard coocky dicky sumty dick I know like your mom enjoyed it a lot much then your sis caz your mom was a mature shit tho u know what u fucking cow face porky poopypants I also know where do u live and how do u eat let me give a brief description about where do u live you live in a fucking slum where ur mom sell her pussy in a reatil price yo and that the shitty reason how u eat three times hahahaha😂😂😂😂We or I are gonna rape your whole ugly family even tho they are as much as ugly as my shitty poop but so what I will still fuck them and insist them by fucking harder to say it like Bunny Coney  is the best fucker in the  world he  even can defeat the most famous porn star Johnny sins hahaha 😂😂😂Well let me say some stories about your mom actually not your mom's only it's our strory tho Your mother name  is Mrs  Mia khalifa she comes of a fucking pornography hilometic whore family she can suck and lick and you know what she lick she lick my sweet heavy hunktik dick hehe she is so kind I meant  your mom caz she suck my dick too kindly wow  hehe 😍 🙄   your mother Love my coocky dick very much and in back I also  love her sexy sweet pussy  as well mm we love each other  in this way hehe now am gonna tell how I fucked your mom well I used to sleep with her in first place then I slowly used to unfasten your mom bra and 👙 hehe after that I began my part what is too good to go with for me I literally fucked her every night like if I calculate in hours full night huhu I enjoyed those night even tho I still fuck her  lot hmm maybe she also miss those days like I do who knows however   maybe her happiness was know no bounds  and yh in her face I did seen a beams of joy for my hard core fucking hmm  well in profound respect I really wanna fuck her again and again caz I am  indebted to her asshole you know why let me tell you why well I only did fucked her pussy not asshole that's why One-day your sis we're going to her collage and I and some ma friend were waiting for her caz as much as we were concerned about her is she is a fucking bitch who earn money through her pussy postitution  and that's what makes us horny and greedy then that's why we all give her proposal about fucking her  vagina  or u can say pussy in few bucks after that we get Alas!!! And said wait what she is gonna give her fucking Hippocratic pussy in that much money for few bucks then I asked her hey why are u selling your pussy in a retail price then she replied like listen we don't get 3 times food that's why I and my mom's do it at last but not least after that   u know what I said  and what she did  she did fucked me like a fucking horny bitch I swear I enjoyed this part.",
    )

@catub.cat_cmd(
    pattern="bsdk$",
    command=("bsdk", plugin_category),
    info={
        "header": "Bsdk Gaand Mardunga tab maanega ?",
        "usage": "{tr}bsdk",
    },
)
async def _(event):
    if event.fwd_from:
        return
    #name = event.pattern_match.group(1)
    animation_interval = 1.3
    animation_ttl = range(11)
    kakashi = await edit_or_reply(event, "Abe lawde apna kaam kr")
    animation_chars = [
            "Bhsdk gaand",
            "Maardunga",
            "Tab",
            "Maanega",
            "Kya",
            "Maiya",
            "Chodu",
            "Saala",
            "Nikal",
            "Lawde",
            "Bhsdk gaand Mardunga Tab Maanega Kya Maiya Chodu Saala Nikal Lawde"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await kakashi.edit(animation_chars[i % 11])
        