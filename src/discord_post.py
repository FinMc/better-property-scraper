import discord


def post_on_discord(new_props, TOKEN, channel_id):
    if len(new_props) > 0:
        message_strings = []

        for prop in new_props:
            message_strings.append(
                " Found:\n{0}\n{1}\nPrice: {2}\n{3}".format(
                    *[
                        prop["name"],
                        prop["address"],
                        prop["price"],
                        prop["link"],
                    ]
                )
            )

        client = discord.Client(intents=discord.Intents.default())

        @client.event
        async def on_ready():
            channel = client.get_channel(channel_id)
            for j in message_strings:
                await channel.send(j)
            await client.close()

        client.run(TOKEN)
