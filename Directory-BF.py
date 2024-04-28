#!/bin/python

import requests
print('============================================')
target = input('[+] Please, specify target url: ')
print('============================================')
file = input('[+] Enter name of the file that contains wordlist of directories: ')
print('============================================')
print('[+] Searching... ')
print('============================================')
def request(url):
	try:
		return requests.get('http://' + url)
	except requests.exception.ConnectionError:
		pass
		
f = open(file, 'r')

for line in f:
	directory = line.strip()
	full_path = target + '/'+ directory 
	response = request(full_path)
	if response:
		print('[*] Discovered path: ' + full_path)
print('[+] Finished!')
