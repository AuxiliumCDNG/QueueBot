import discord

from globals import change_setting, get_setting


async def execute(client, message, args):
    # check permission of user
    roles = []
    for role in message.author.roles:
        roles.append(role.name)
    if not "Queue Admin" in roles:
        if message.author.id == message.guild.owner_id:
            await message.channel.send("Notice: You are allowed to use this command, because you are the owner of this server. Would you mind giving yourself the **Queue Admin** role for redundance? You can also give it to other people for administrating QueueBot.")
        else:
            await message.channel.send("You don't have permission to do that.\nAsk for the **Queue Admin** role.")
            return

    if change_setting(message.guild.id, "supportchannel", args[0]) == True:
        await message.channel.send("Support Channel changed.")
    else:
        await message.channel.send("There was an error changing the Support Channel. It's probably not your fault. Please consult the bot hoster!")

    return
