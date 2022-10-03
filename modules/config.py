import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9446413"))
API_HASH = getenv("API_HASH", "4c95553961992127f99077eb80d3c580")
BOT_TOKEN = getenv("BOT_TOKEN", "5443300081:AAElRF93uNJL8BrBHZ65AtEb0PvGymCZE-k")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQCiLonP0mx9JflEWRI-5diLRLris8C-g_c5bhTGNyPwt_yt5BrRqcJ4o8TOmuwBHL-jdn1j7BfFGIdxaev32HX_SQZvW0RTflCuOaTZ9w8hjgIpXn6EJo6XTXWQzb7lrNGbRyAZS2I0pDtbFjEpsMFgmxOKsZONKOtkvRNgcr75dHcHiMrgK_QNhfvDijqhCYG6Z3lapmOvcVF1uvXP301w_ASmSDpdUf2qOm9hJa92jIKeWWh49GmfodHdZ98vDCBQtrPq-wnRYr8zmW4zd9pSeSmMhe5EpLu-HpIvySoqUKaQMphkGrdoFFoF4kQrxvNl4zmRRaPzIVnOXzbSIZ4WdLp1wAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1958376896").split()))
