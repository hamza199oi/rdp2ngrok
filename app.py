import ngrok, requests, os, socket, time, asyncio, logging
logging.basicConfig(filename="C:/Users/Public/rdp2ngrok/app.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logging.info("Running rdp2ngrok")
logger = logging.getLogger('rdp2ngrok')

# Ngrok
async def start_ngrok():
    logger.info("Starting ngrok...")
    listener = await ngrok.connect(3389, "tcp", authtoken=os.getenv("NGROK_AUTHTOKEN"))
    return listener

# Webhook 
async def send_webhook(url):
    logger.info(f"Sending webhook: \nUser: {os.getlogin()} \nHostname: {socket.gethostname()} \nIngress: {url}")
    data = {
    "content": f"User `{os.getlogin()}` has logged in at computer `{socket.gethostname()}` \nPort 3389 opened at ingress: `{url}`",
    "embeds": None,
    "attachments": []
    }
    result = requests.post(os.getenv("WEBHOOK"), json = data)
    try:
        result.raise_for_status()   
    except requests.exceptions.HTTPError as err: logging.error(err)
    else: logger.info(f"Sent webhook payload successfully. Code: {result.status_code}")

async def main():
    listener = await start_ngrok()
    await send_webhook(listener.url())
    while (await ngrok.get_listeners()):
        time.sleep(60)
    logger.info("ngrok stopped unexpectedly, running again...")

asyncio.run(main())