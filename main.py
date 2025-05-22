import time
import os
from colorama import Fore
import random
import string
import ctypes
import requests

os.system("pip install requests")
os.system("pip install colorama")
os.system("pip install ctypes")
os.system("pip install random")
os.system("pip install time")

def main(): 
    os.system("title nitro gen")
    os.system("cls")
    print(".    صحف عم طبار هعانص ديرت مك  ")
    num = int(input(""" [2] طبار هعانص ديرت مك: """))
    print(f"\n  رتنا طغضا ديرت ال اذاو طبارلا طح كوه بيو هلسري ديرت اذا")
    url = input(f" كوه بيو: ")
    webhook = url if url != "" else None
    valid = [] 
    invalid = 0 
    os.system("cls")
    time.sleep(1)
    

    for i in range(num): 
        try:
            code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16))
            url = f"https://discord.gift/{code}"
            response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if response.status_code == 200:
                print(f" ورتين لاغش: {url}")
                try:
                    requests.post(webhook, json={'content': url})
                except:
                    pass
                valid.append(url)
                with open("output/NitroCodes.txt", "w") as file:
                    file.write(url)
            elif response.status_code == 429:
                print(f"ForeRate limited, please wait {response.json()['retry_after']/1000} s")
                time.sleep(int(response.json()['retry_after'])/1000)
            else:
                print(f"INVALID NITRO: {url}")
                invalid += 1
        except Exception as e:
            print(f" Error : {url} {e}")
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Astraa")
    print(f"""\nResults:
       Valid: {len(valid)}
      Invalid: {invalid}
      Valid Codes: {', '.join(valid )}""")
    input(f"""\nرتنا طح جورخلا ديرت اذا """)
    main()

main()
