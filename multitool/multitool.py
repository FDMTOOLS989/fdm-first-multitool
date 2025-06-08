import requests
import os
import json

logo ="""

\033[38;2;146;255;12m ███████╗██████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
\033[38;2;146;255;12m ██╔════╝██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
\033[38;2;146;255;12m █████╗  ██║  ██║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     ███████╗
\033[38;2;146;255;12m ██╔══╝  ██║  ██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
\033[38;2;146;255;12m ██║     ██████╔╝██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
\033[38;2;146;255;12m ╚═╝     ╚═════╝ ╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝\033[38;2;0;128;255m



"""



while True:
    os.system("tittle FDM TOOL")
    os.system("cls")
    print(logo)
    print("[1] Iplockup")
    print("[2] webhook sender ")
    print("[3] Show HWID")
    print("")
    x = input("option: ")

    if x == "1":
        os.system("cls")
        print("IP LOOKUP\n")
        ip = input("Enter IP: ")
        os.system("cls")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        print("RESULTS\n\n")
        print(f"\033[38;2;0;128;255mcountry: \033[38;2;0;128;255m{data["country"]}")
        print(f"\033[38;2;0;128;255mcity: \033[38;2;0;128;255m{data["city"]}")  
        print(f"\033[38;2;0;128;255mregion:\033[38;2;0;128;255m{data["region"]}")
        print(f"\033[38;2;0;128;255mtimezone:\033[38;2;0;128;255m{data["timezone"]}")
        print("")
        pause = input("Press enter to return...")


    if x == "2":
        os.system("cls")
        print("WEEBHOOK SENDER\n \033[38;2;0;128;255m")
        url = input("\033[38;2;0;128;255mEnter webhook url: \033[38;2;0;128;255m")
        message = input("message: \033[38;2;0;128;255m")
        name =input("Webhook Name: \033[38;2;0;128;255m")
        
        data = {
            "content": message,
            "username": name
        }     

        try:
           r = requests.post(url, json=data)
           print("Webhook sending")
        except:
            print("ERROR SENDIN WEBHOOK")

        print()
        pause = input("Press enter to return...")

    if x == "3":

        os.system("cls")
        print("\n \033[38;2;0;128;255mHardware ID\n")

        print("\n \033[38;2;255;0,0mCPU SERIAL\n \033[38;2;255;255;255m")
        print(os.system("wimic cpu get ProcessorID"))  

        print("\n \033[38;2;255;0,0mCPU SERIAL\n \033[38;2;255;255;255m")
        print(os.system("wimic diskdrive get SerialNumber "))