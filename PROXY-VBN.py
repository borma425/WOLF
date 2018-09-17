#!/usr/bin/python

#	 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- WELCOME TO WOLF TOOL (^-^) -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


###############################################################[+>]: Cecking all tool need :[<+]#######################################################
try:
   import optparse,socket,os,time,sys,subprocess,cookielib,random,hashlib
   import datetime
   import threading
   from ftplib import FTP
   from urllib2 import urlopen, Request, URLError, HTTPError,install_opener,build_opener,ProxyHandler
except:
      print("\n[!]:Some Modules is Not Found In your Python\n[*]:Please Update your Python")
      exit()
try:
   from Core.banner import banner
   from Core.examples import examples
   from Core import mechanize
   from Core import pxssh
   from Core.proxys import proxy
except:
       print("\n[!]:The [Core] Tool Folder Is Missing!!")
       exit()

#######################################################################################################################################################

###################################################### Choice Random user agent #######################################################################
def useragent():
    useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
    return random.choice(useragents)

useuser = useragent()
useuser2 = useuser
useuser3 = useuser2
useuser4 = useuser3
#######################################################################################################################################################

############# show time #############
				    #
mytime = datetime.datetime.now()    #
hour = mytime.hour		    #
min = mytime.minute		    #
sec = mytime.second                 #######
timenow = "{}:{}:{}".format(hour,min,sec) #
###########################################

############################## Random color ################################
									   #
cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m'] #
colors = cor[random.randint(0,5)]					   #
									   #
############################################################################

#============== Checking internet connection! ===============#
							     #
server = "www.google.com"				     #
def check():						     #
  try:							     #
      s = socket.gethostbyname(server)			     #
      conn = socket.create_connection((s, 80), 2)	     #
      return True					     #
  except:						     #
	pass						     #
  return False						     #
check1 = check()					     #
check2 = check1						     #
check3 = check2						     #
check4 = check3						     #
check5 = check4						     #
check6 = check5						     #
check7 = check6						     #
check8 = check7						     #
##############################################################

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ERRORS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def msgerrorconnect():
  print(cor[3]+"\n[!]Ops:"+cor[5]+" Your Not Connected To The "+cor[4]+"[ Internet ]"+cor[2]+"\n[*]:"+cor[3]+"Please Connect To The Internet and try again ??")
  exit()

def passnotfound(x):
	       print(cor[3] + "\n[!]:"+cor[5]+"Password Not Found In [ "+cor[4]+x+cor[5]+" ] Wordlist!\n"+cor[2]+"[*]:"+cor[3]+"Try Other Wordlist ??")
	       exit()
def serverblock(x):
	  print(cor[3]+"\n[!]:"+cor[5]+"Your Blooked from "+cor[4]+x+cor[5]+" webserver!\n"+cor[2]+"[*]:"+cor[3]+"If Your "+cor[4]+"[ Internet ]"+cor[3]+ "Is Good try ["+cor[4]+" -p"+cor[3]+" ] For Use Random [Proxy] For Bypass Blooked :)\n[!]:If Your"+cor[4]+"[ Internet ]"+cor[3]+"Is Slow Please Wait 5-10 munites and try again ?? ")
	  try:
	      os.system("service network-manager restart")
	      exit()
	  except:
		pass
	  exit()

def servererror():
            print(cor[3]+"\n[!]:"+cor[5]+"Ops: Your Not Connected To The "+cor[4]+"[ Any Network ]"+cor[2]+"\n[*]:"+cor[3]+"Please Connect To Some Network and try again ??")
            exit()
def exceptkey():
  print(cor[4] + "\n[!]:"+cor[3]+"Stoping Attack.......")
  time.sleep(2)
  exit()

def errorfile(x):
	print(cor[3]+"\n[!]:Error The: [ "+cor[4]+x+cor[3]+" ] File Not Found!!")
	exit()
#####################################################################################################################################################
#-------------------------------------Tool version------------------------------------#
ver = cor[1]+"[*]:"+cor[5]+"BrtForTe Version:"+cor[4]+" ["+cor[3]+"1.2"+cor[4]+"]"    #
#-------------------------------------------------------------------------------------#
ve = "1.2"
proxy1 = proxy()
proxy2 = proxy1
proxy3 = proxy2
proxy4 = proxy3
proxy5 = proxy4
proxy6 = proxy5