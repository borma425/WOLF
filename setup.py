#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# setup.py
# yehia1hacker
#I-love-python


import os, time, sys

GREEN = '\033[1m' + '\033[32m'
WHITE = '\033[1m' + '\33[97m'
END = '\033[0m'

uname=input("enter user name=-💬-  ")
passwd=""
attempt=0
flag=0
while(attempt!=10000000000):
    passwd=input("enter password- 👁  🔰-🔰-☢️  ")
    if(passwd=="yehia1hacker"):
        flag=1
        break
    else:
        attempt=attempt+1
        if(attempt==10000000000):
            print("you have tried maximum number of time")
if(flag==1):
    print("welcome ✅ ",uname)

print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyo+:--.``      ``.--/+oyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNds+-.`                          `.:+ydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMNho:`                                     `.:ohNMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMmy/.                                             `./yNMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMNy:`                    ---Yehia--                      `/hNMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMdo.                                                          .omMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMd/`                                                              `+dMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMd/`                                                                  `/mMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMm+`        .:.             ```..------------..```            `-:.        .oNMMMMMMMMMMMM')
print('MMMMMMMMMMMy.      `/sdy:`         `.....--.``-.`-.`.-``.--.....`         `/hds:`      -hMMMMMMMMMMM')
print('MMMMMMMMMN+`   ...omMNs.       ``...```..`   -.  ..  .-   `..```...`        .sNMd+...   `+NMMMMMMMMM')
print('MMMMMMMMd:  `:yo:hMMm/       `.-.`   .-`    ..   ..   ..    `-.   `--.`       +mMMh:os:   /mMMMMMMMM')
print('MMMMMMMd.  `sNy.hMms//     `..``....--`    `-    ..   `-`    `--....``..`     +/smMy.hNs`  -dMMMMMMM')
print('MMMMMMd. ``sMN-odo/sd-   `..`     .-.......--``-:+o+/-`--.......-`     `..`   -ds/od+:NMo`` -dMMMMMM')
print('MMMMMd. :+:NMh`/ohNd-  `..`      `-`     `.-``oNh:/dMNo.-.`     `-`      `-.   :mNh+/.dMm-o- -mMMMMM')
print('MMMMN- /N//MN+omNmo.  `-.       `-`       ..  :ho-.yMNo -.       .-`       .-`  .omNmo+MN:om: :NMMMM')
print('MMMM+ .mM/:NdmNy+:   `-`        -.        -`     .omh/` .-        .-        .-`   :+hNmdN:+Mm` sMMMM')
print('MMMh` +MMo:Nms:+h:  `--..``    .-        `-`     :y-    `-`        -.    ``..--`  :h//yNm-sMM/ `dMMM')
print('MMM:  sMMh-y/omMo  `-` ``......-.``      .-      ::      -.     ```.-......`` .-`  sMdo/y-dMMo  /M.M')
print('MMd` `oMMd.+mMMo`  -.         .-`........--...``+dd/``...--........`-.         ..  `oMMm+`mMM+` `dMM')
print('MMo ./-NMhoNMm+   `-          -.        `-.`````/dh:`````.-         .-         `-`   omMN+dMN.+` sMM')
print('MN- ss`sMyMMy.o   -.         `-`         -.      --      .-         `-          .-  `o.yMNhMo`yo :NM')
print('MN``hm-`mNN/`sd  `-`         `-`        `-`  ``-+oo+-``  .-         `-`         `-   ms`+NNd`:Ny .NM')
print('Mm `hMh`/N:.hMo  `-`         .-`        `-./y--smMMds--y:.-`        `-`         `-`  sMh./N:`dMy `mM')
print('Mm  oMMy./-mMm-  `--.........---......--/smMN   /NN:  `NMms/-.......---.........--`  :NMd.+.hMM/  mM')
print('Mm  `NMMs hMMs   `-`         .-`:+osydmNMMMM+  -/hy/.  oMMMMNmhyso+:`-`         `-`   yMMy`yMMN` `mM')
print('MN` `+NMN:MMd./  `-`         `-oMMMMMMMMMMMN-   .md`   :NMMMMMMMMMMM+-`         `-   /.mMN:NMN/. .NM')
print('MN:`s`/mMsMM/.d:  -.         `:dMMMMMMMMMMMN:   +MM/   /NMMMMMMMMMMMh:          .-  +d`+MNyMm:.s`/NM')
print('MMo yd-.ymNm`:Mh` `-          /NMMMMMMMMMMMMy   yMMs   hMMMMMMMMMMMMm:         `-` `hN:`NmNy.:ds sMM')
print('MMd`:MNo./mh yMm.  -.         oNMMMMMMMMMMMMM/  hMMy  /MMMMMMMMMMMMMN+         ..  -NMs mm:.oNN-`mMM')
print('MMM: oNMm+-o`mMM:` `-. ``.....hMMMMMMMMMMMMMMN/ dMMy +NMMMMMMMMMMMMMMy.....`` .-  `:MMm o-omMN+ /MMM')
print('MMMh` /mMMd/`mMM::o``--.```   dMMMMMMMMMMMMMMMNomMMdsNMMMMMMMMMMMMMMMh   ```.--``o-+MMd +dMMm: .dMMM')
print('MMMMo  -yNMNssMM+`dd.`-`     .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`     .-`.dd sMMoyNMNy-  sMMMM')
print('MMMMN- :::ymNddMd sMd.`-.    /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:    .-`-dM+`dMddNms-/: :MMMMM')
print('MMMMMd-`yy-./ydNN::NMh` .-`  sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo  `-. .dMN-/NNdy:.:ys`-mMMMMM')
print('MMMMMMd..sNh+--/ys.hMMs`.....hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy`....`yMMy.ys/-:odNs`-mMMMMMM')
print('MMMMMMMd-`/dMNdy+/--mMN//y/.:mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd-./y:+MMm--/oymNMh/ -mMMMMMMM')
print('MMMMMMMMm/ `/ymMMNmsodMm-oNhomMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmodm+:mMhoymNMMmy:` /mMMMMMMMM')
print('MMMMMMMMMN+` `:oymNNNmmNd-oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN+-mNmmNNNmy+-` `oNMMMMMMMMM')
print('MMMMMMMMMMMh- .++:::/osydh//dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd//hdys+/:::++` -hMMMMMMMMMMM')
print('MMMMMMMMMMMMNo.`/yhhyssoooo+/ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmho/+oooossyhhy:`.oNMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMm/` -/ydNNMMMMMMNmmdhsyMMMMMMMMMMMMMMMMMMMMMMMMMMyyhdmmNMMMMMMNmdy/. .+mMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMd+.  `://++++/:---/sdMMMMMMMMMMMMMMMMMMMMMMMMMMho:---:/++++//:`  .+dMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMmo.`.+sssoooshdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhsooosss/.`-smMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMNh/``:+ydmNNNmdymMMMMMMMMMMMMMMMMMMMMMMMMMMdydmNNNmdy+:`./hNMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMNy/.`        hMMMMMMMMMMMMMMMMMMMMMMMMMMy        `./hNMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMNds:.`   `dMMMMMMMMMMMMMMMMMMMMMMMMMMd    `./sdNMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+::mMMMMMMMMMMMMMMMMMMMMMMMMMMm::oydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
if __name__ == '__main__':

            print('header + """          v2.0 """ + Black hat + """by yehia1hacker (yehia1hacker)    """ + "\n" + END')

            print('header + """                         v2.0 """ + Black hat + """yehia1hacker    """ + "\n" + END')


            print('[+] Installing requirements in 10 seconds... Press CTRL + C to skip.')
            time.sleep(5)
            print("[+] Installing requirements...")
            os.system("apt update  ")
            os.system("apt upgrade  ")
            os.system("apt install python")
            os.system("apt install python2")
            os.system("pip3 install requests bs4")
            os.system("pip2 install mechanize")
            os.system("pip install -r requirements.txt")
            os.system("clear")
            os.system("chmod +x WOLF.py")
            os.system("chmod +x dnsServer.py")
            os.system("chmod +x proxyScript.py")
            os.system("chmod +x requirements.txt")
            os.system("python3 WOLF.py")
            os.system("clear")
            print(" Script installed successfully  ")
            print("Greetings to all")
print("[+] Setup done.")

print("🤩------------------------------------------🤩")
print("Thanks for installing the script ✅ ",uname)
print("😎------------------------------------------😎")
