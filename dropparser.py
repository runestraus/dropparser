import csv
import re
import datetime
import urllib

# http://www.odditysoftware.com/download/dldoms.php?domdate=2012-08-15
# urllib.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")

def main():
	csv = filter(lambda x: x[1] == "com" , csv.reader(open("dldoms.csv", "rb"), delimiter = ','))
	words = [w.lower().replace("\n","") for w in open("common.txt", "r").readlines()]
	comp = open(str(datetime.date.today()) + ".txt", "w")
	digits = re.compile("\d")
	for domain_row in csv:
		domain = domain_row[0].replace(".com", "")
		if (digits.search(domain) != None):
			continue
		if (len(domain) > 12):
			continue
		if (domain.find("-") != -1):
			continue
		if (is_all_words(domain, words) == True):
			comp.write(domain + "\n")
	print "Compilation complete"

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

main()