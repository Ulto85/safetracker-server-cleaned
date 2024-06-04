webhook_url = 'https://discord.com/api/webhooks/'
from time import sleep
from discord import Webhook, RequestsWebhookAdapter

print("starting webhook")
while True:
    webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
    webhook.send(content="/check")
    sleep(3600)