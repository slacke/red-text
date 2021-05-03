import pythonbox
import discord

# setup
webhook_url = r"https://discord.com/api/webhooks/829949930167599146/Tqo4bnNYEPUpLkHQAtgEJHLQM1BBaRl03ZLLj2YxDf6gQNXGuU7PEg9_QmKPru4GW7lM"


# process
webhook_url = webhook_url.split(r"/")
webhook = discord.Webhook.partial(webhook_url[-2], webhook_url[-1], adapter= discord.RequestsWebhookAdapter())

webhook_message = webhook.send('xddd', wait = True)
#webhook_message.delete()