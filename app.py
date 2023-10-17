import ngrok, requests, os, socket, time, asyncio
# Ngrok
async def start_ngrok():
    listener = await ngrok.connect(3389, "tcp", authtoken=os.getenv("NGROK_AUTHTOKEN"))
    return listener

# Webhook 
async def send_webhook(url):
    data = {
    "content": f"User `{os.getlogin()}` has logged in at computer `{socket.gethostname()}` \nPort 3389 opened at ingress: `{url}`",
    "embeds": None,
    "attachments": []
    }
    result = requests.post(os.getenv("WEBHOOK"), json = data)
    try:
        result.raise_for_status()   
    except requests.exceptions.HTTPError as err: print(err)
    else: continue

async def main():
    listener = await start_ngrok()
    await send_webhook(listener.url())
    while (await ngrok.get_listeners()):
        time.sleep(60)

asyncio.run(main())