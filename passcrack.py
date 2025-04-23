import itertools
import sys
import time
from tqdm import tqdm
import random

banner = """
██╗  ██╗ █████╗ ███████╗██╗
██║ ██╔╝██╔══██╗╚══███╔╝██║
█████╔╝ ███████║  ███╔╝ ██║
██╔═██╗ ██╔══██║ ███╔╝  ██║
██║  ██╗██║  ██║███████╗██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
+-----------------------------------------+
| Name      : Kazi Ashrafuzzaman          |
| Github.   : @SilentVirtualCriminalGang  |
| Facebook  : WHO.AM.I.X0                 |
| What's app: +8801873561165              |
+-----------------------------------------+"""


def print_colored(text):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sys.stdout.write(f"\033[38;2;{r};{g};{b}m{text}\033[0m")
    sys.stdout.flush()


print(banner)


print("Choose password type:")
print("1. Numbers only")
print("2. Numbers and Letters")
print("3. Numbers, Letters, and Symbols")
choice = input("Enter choice (1/2/3): ")


numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"


if choice == '1':
    keys = numbers
elif choice == '2':
    keys = numbers + letters
elif choice == '3':
    keys = numbers + letters + symbols
else:
    print("Invalid choice, defaulting to numbers and letters.")
    keys = numbers + letters


pas = input("Enter the password to crack: ")
length = len(pas)


start_time = time.time()
total_combinations = len(keys) ** length


for idx, guess in enumerate(tqdm(itertools.product(keys, repeat=length), total=total_combinations, desc="Cracking", ncols=100, unit="guess")):
    guess = ''.join(guess)
    
    
    print(f"\rChecking: {guess}", end="")

    if guess == pas:
        end_time = time.time()
        print(f"\nPassword cracked successfully!\nPassword: {guess}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        break


fucker = """
Developed by: Kazi Ashrafuzzaman
"""


print(fucker)
