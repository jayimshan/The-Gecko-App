from discord_webhook import DiscordWebhook, DiscordEmbed

url = 'https://discordapp.com/api/webhooks/601232887219748874/tu1D8PBWC7STcVZ0nPArrvKiFoSVApLroINAOHC54a9SUA0XKKrE-DVj5TKw3JEF4_-P'
webhook = DiscordWebhook(url=url)
embed = DiscordEmbed(title='Success! You just cooked!', color=0x3cd13a)
embed.set_author(name='The Gecko App just cooked: Title')
embed.add_embed_field(name='Store', value='Store')
embed.add_embed_field(name='Price', value='Price')
embed.add_embed_field(name='Color', value='Color')
embed.add_embed_field(name='Size', value='Size')
# embed.set_thumbnail(url=self.src)
embed.set_footer(text='Powered by The Gecko App | @jayimshan', icon_url='https://i.imgur.com/E6zcSEY.png')
embed.set_timestamp()
webhook.add_embed(embed)
webhook.execute()
