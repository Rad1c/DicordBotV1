from dicord_bot import DiscordBot
from dotenv import load_dotenv
import os

load_dotenv()

_api_key = os.getenv("CHATGPT_API_KEY")
_token = os.getenv("DISCORD_TOKEN")

bot = DiscordBot(_token, _api_key)

bot.run()