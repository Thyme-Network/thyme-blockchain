import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("THYME_ROOT", "~/.thyme/mainnet"))).resolve()
