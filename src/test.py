import random
import string

from rich.console import Console
from rich import print as printc

console = Console()


s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
print(s)
