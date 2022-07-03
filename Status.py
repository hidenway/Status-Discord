from pypresence import Presence
from time import time

RPC = Presence("Id Bots")
btns = [
    {
        "label": "Discord Server",
        "url": "https://discord.gg/h74uYT9ewD"
    }
]

RPC.connect()
RPC.update(
    state="sweeter than your life",
    details="Vinki Discord Bot Dev",
    start=time(),
    buttons=btns,
    large_image="yuki",
    small_image="python",
    large_text="Vinki | Dev",
    small_text="Python Dev"
)
