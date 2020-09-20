import discord
from discord.ext import commands
import pickle

PICKLE_FILE = "rooms.pkl"


async def openResult(ctx):
    try:
        with open(PICKLE_FILE, "rb") as data:
            rooms = pickle.load(data)
    except FileNotFoundError:
        await ctx.send("Not result found")

    return rooms


async def sendRoomResult(ctx, room):
    msg = "{:-^37}\n".format(room["name"])
    for pc in room["online_pcs"]:
        msg += "``" + pc["host_name"] + "``    "
        if len(pc["protocols"]) == 1:
            if pc["protocols"] == "rdp":
                msg += "ssh:x:    rdp:white_check_mark: \n"
            else:
                msg += "ssh:white_check_mark:    rdp:x: \n"
        else:
            for protocol in pc["protocols"]:
                msg += protocol + ":white_check_mark:    "
            msg += "\n"

    await ctx.send(msg)


class ScanRoomCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.limit = 1999

    @commands.command(aliases=["CheckAll", "checkall"])
    async def up(self, ctx):
        rooms_result = await openResult(ctx)

        for room in rooms_result:
            await sendRoomResult(ctx, room)

    @commands.command(aliases=["Check", ])
    async def check(self, ctx, *room_name):
        room_name = "".join(room_name).lower()
        letters = ["a", "b", "c", "d", "e"]
        format1 = ["tp" + letter for letter in letters]
        format2 = ["tpinfo" + letter for letter in letters]
        rooms_name = letters + format1 + format2
        rooms_name.append("radiocom")
        rooms_result = await openResult(ctx)

        if room_name in rooms_name:
            for room in rooms_result:
                if room_name == "radiocom":
                    if room["name"] == "Radiocom":
                        await sendRoomResult(ctx, room)
                        break
                elif room["name"][-1].lower() == room_name[-1]:
                    await sendRoomResult(ctx, room)
                    break
                elif room == rooms_result[-1]:
                    await ctx.send("Not result found")

        else:
            await ctx.send("Invalid room")
