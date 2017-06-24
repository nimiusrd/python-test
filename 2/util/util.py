import re
from typing import Match


def is_url(src: str) -> Match[str]:
    return re.fullmatch(r'^https://[0-9a-zA-Z/:%$&()~.=+\-_]+$', src)
