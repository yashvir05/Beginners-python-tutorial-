
#print('hello')
#os.chdir('/Users/yash/PycharmProjects/')
#print(os.getcwd())    # to get pwd in python in your OS
#print(dir(os))
#print(os.listdir())

import sys, re
import argparse
import os, configparser
from math import factorial

user_config_dir = os.path.expanduser("~") + "/.meraki_tools"
user_config = user_config_dir + "/default_config.ini"
print(user_config_dir)
print(user_config)
print(os.stat('/Users/yash/.meraki_tools/default_config.ini'))
key = os.chdir('/Users/yash/.meraki_tools/')
print(key)


if not os.path.isfile(user_config):
    print("No preferences found. Exiting…")
    sys.exit()
os.chdir('/Users/yash/.meraki_tools/')
print(os.listdir())
print(os.getcwd())
path = os.path.join(os.environ.get('HOME'), '.meraki_tools','default_config.ini')
with open('default_config.ini', 'r') as f:
    for line in f:
        print(line, end='')
    #content = f.read()
    #print(content)
config = configparser.ConfigParser()
e = config.read('/default_config.ini')
print(e)

a = dict(boo='bharti' , booboo= 'yash')
for key in a:
    print(f'{key}  => {a[key]}')
f = [str(factorial(x)) for x in range(1,20)]  # comprehension
print(f)
f = [len(str(factorial(x))) for x in range(1,20)]
print(f)

for i in range(2,3):
   # print(i)