from discord_webhook import DiscordWebhook, DiscordEmbed

class Webhook:

	url_webhook = 'https://discordapp.com/api/webhooks/626625411295739904/c2tST5AbhPPon07yfPCW7e9gYJE-7CgqS-d1Cm5EgaQSl7hiNcc86zR0ebOvDHlKlE_z'
	# url_webhook = 'https://discordapp.com/api/webhooks/601232887219748874/tu1D8PBWC7STcVZ0nPArrvKiFoSVApLroINAOHC54a9SUA0XKKrE-DVj5TKw3JEF4_-P'

	def __init__(self, title, store, link, price, qty, src, color, size):
		webhook = DiscordWebhook(self.url_webhook)
		embed = DiscordEmbed(title='{}'.format(title), color=0x3cd13a)
		embed.set_author(name='Success! The Gecko App just cooked:')
		embed.add_embed_field(name='Store', value='{}'.format(store))
		embed.add_embed_field(name='Price', value='${0:.2f}'.format(price))
		embed.add_embed_field(name='Qty', value='{}'.format(qty))
		embed.add_embed_field(name='Link', value='{}'.format(link))
		embed.add_embed_field(name='Color', value='{}'.format(color))
		embed.add_embed_field(name='Size', value='{}'.format(size))
		embed.set_thumbnail(url=src)
		embed.set_footer(text='Powered by The Gecko App | @jayimshan', icon_url='https://i.imgur.com/E6zcSEY.png')
		embed.set_timestamp()
		webhook.add_embed(embed)
		webhook.execute()