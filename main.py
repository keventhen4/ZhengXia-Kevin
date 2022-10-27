import sys, time, random, os
from termcolor import colored


prg = open("Preview.txt", "r")
exec(prg.read())


#prg.close()
time.sleep(10)
os.system('clear')