from os import system
from requests import post, Session
from json import loads , JSONDecodeError
from uuid import uuid4
from time import sleep
import sys
from itertools import cycle
from colorama import Fore, init
from hashlib import md5
import time
from random import shuffle

init(autoreset=True)  # initialize colorama

Creator = "t.me/NothingReal"
session = Session()
session.headers.update({'User-Agent' : 'Dalvik/2.1.0 (Linux; U; Android 13; 23049PCD8G Build/TKQ1.221114.001)',
                        'Accept-Encoding' : 'gzip',
                        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'})

cr = Creator
restore_key = input("Please enter your restore key: ")

def decode(data):
    final_string = ''
    for key in data.keys():
        final_string += f"{key}={data[key]}&"
    return final_string[:-1]


def load():
    data = {'game_version' : '1.7.10655' , 'device_name' : 'unknown' , 'os_version' : '10' , 'model' : 'SM-A750F' , 'udid' : str(uuid4().int) , 'store_type' : 'iraqapps' , 'restore_key' : restore_key , 'os_type' : 2}
    return loads(session.post('http://iran.fruitcraft.ir/player/load' , decode(data) , timeout = 5).text)

def collect_gold(data , headers):
    collect = post("http://iran.fruitcraft.ir/cards/collectgold",
        data = data,
        headers = headers,
    )

def start(sleep_time):
    done = 0
    lost = 0
    
    try:
        collect_gold(collect_data , headers)
        done += 1
    except Exception as e:
        print(e)
        lost += 1
    finally:
        sys.stdout.write(f"\r• Gold Mine Done: {Fore.GREEN}{str(done)}{Fore.RESET} --- • Gold Mine Lost: {Fore.RED}{str(lost)}{Fore.RESET}")
        sys.stdout.flush()
        sleep(sleep_time * 60)  # login once after starting
        
        while True:
            sleep(sleep_time * 60)  # sleep for the specified time in minutes
            try:
                collect_gold(collect_data , headers)
                done += 1
            except Exception as e:
                print(e)
                lost += 1
            finally:
                sys.stdout.write(f"\r• Gold Mine Done: {Fore.GREEN}{str(done)}{Fore.RESET} --- • Gold Mine Lost: {Fore.RED}{str(lost)}{Fore.RESET}")
                sys.stdout.flush()

def print_banner():
    colors = [Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.RED]
    shuffle(colors)  # shuffle the colors list randomly
    color = colors[0]  # select the first color from the shuffled list
    print(color + "_  ______      _  _____ ___  ____")
    print(color + "| |/ /  _ \    / \|_   _/ _ \/ ___|")
    print(color + "| ' /| |_) |  / _ \ | || | | \___ \\")
    print(color + "| . \|  _ <  / ___ \| || |_| |___) |")
    print(color + "|_|\_\_| \_\/_/   \_\_| \___/|____/")

def main():
    print_banner()
    sleep_time = int(input("Please enter the mine time (in minutes): "))
    print("\n\n\n\n", 'mine time is >> ', Fore.CYAN, str(sleep_time), Fore.RESET, ' min', "\n")
    start(sleep_time)

collect_data = {'udid' : str(uuid4().int) , 'restore_key' : restore_key}
headers = {
    'User-Agent' : 'Dalvik/2.1.0 (Linux; U; Android 13; 23049PCD8G Build/TKQ1.221114.001)',
    'Accept-Encoding' : 'gzip',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
}

main()
