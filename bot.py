from pyrogram import Client
from config import *
import os
from flask import Flask

# Create a Flask app
app = Flask(__name__)

class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()      
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")

    async def stop(self, *args):
        await super().stop()      
        print("Bot Restarting........")

bot = Bot()

# Define a simple route for the Flask app
@app.route('/')
def home():
    return "Bot is running!", 200

if __name__ == "__main__":
    from threading import Thread

    # Run the bot in a separate thread
    bot_thread = Thread(target=bot.run)
    bot_thread.start()

    # Run the Flask web server
    port = int(os.environ.get('PORT', 8443))  # Default to 8443 if PORT is not set
    app.run(host='0.0.0.0', port=port)
