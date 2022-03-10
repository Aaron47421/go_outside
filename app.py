from rich.console import Console
from os import system as sys
import time

def c(cmd):
    try:
        sys(cmd)
    except:
        print("ERROR")

def main():
    console = Console()
    console.print("[red bold]GO OUTSIDE JEEZ[/]")
    time.sleep(2)
    try:
        c("taskkill /f /im discord.exe")
    except:
        console.print("[green]At least you are not a discord nerd[/green]")

if __name__ == '__main__':
    main()
