import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9194842"))
API_HASH = getenv("API_HASH", "73a311feefa9a6dd437d3ae9bd4f8cbb")
BOT_USERNAME = getenv("BOT_USERNAME", "arnav_officialbot")
BOT_TOKEN = getenv("BOT_TOKEN", "5515309267:AAH3O_AnzyEgY5DPKa3COReNML3d2I8sezY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQDEMbP_9Xz8djkUmD3eijhi6tMRMxbKgFgQAQ3vjO6fN-6nPAs3f_Qr4RvXlTbi7QEl6HOBRlcxKxNyVttMKWTWOzb88qrBE-wI-pk70Q1PBAi7UJ5Md_XItAILzpAIVsSgF20oO8fXkoyepwgs2X-mXssBbfWCZoldByKqMTgHQAdv-PZHOlbKVKXsr2T7TBRy_pB2oxnuXKbV5oieqjC_-60jW0LuAC4QZ9Pn9HvSjjE2tRgWbpecKngvS55YSzpF6UzlykLIvlv0709nAqKhqQh9FOXYGaGID3WogRKniMidcsStvscZ_TRlwtEv4caMV9VjKLA7xTWNr4t2rss6AAAAASwVnR4A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5516833572").split()))
aiohttpsession = aiohttp.ClientSession()
