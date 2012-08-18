import csv
import re
import datetime
import urllib2

# URL to download domain dump
domain_file_url = "http://www.odditysoftware.com/download/dldoms.php?domdate="

def main():
	csv = parse_raw_file(get_raw_domain_file())
	words = [w.lower().replace("\n","") for w in open("common.txt", "r").readlines()]
	comp = open(today() + ".txt", "w")
	digits = re.compile("\d")
	count = 0
	for domain_row in csv:
		domain = domain_row[0].replace(".com", "")
		if (digits.search(domain) != None or len(domain) > 12 or domain.find("-") != -1):
			continue
		if (is_all_words(domain, words) == True):
			count += 1
			comp.write(domain + "\n")
	print "Completed. Total domains: {}, Parsed domains: {}".format(len(csv), count)

def today():
	return str(datetime.date.today())

def get_raw_domain_file():
	return urllib2.urlopen(domain_file_url + today()).read()

def parse_raw_file(rfile):
	sfile = rfile.split("\n")
	if sfile[-1] == '':
		sfile.pop()
	return filter(lambda x: x[1] == "com", csv.reader(sfile, delimiter = ','))

def is_all_words(string, dct):
	str_len = len(string)
	S = [False] * (str_len)
	S[0] = (string[0] in dct)
	for i in range(1, str_len):
		check = string[0:i+1] in dct
		if (check):
			S[i] = check
		else:
			for j in range(0,i+1):
				if (S[j-1] and (string[j:i+1] in dct)):
					S[i] = True
					break
	return S[str_len-1]

#chyeah!
main()