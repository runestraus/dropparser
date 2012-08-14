import csv
import re
import nltk

def main():
	csv = filter(lambda x: x[1] == "com" , open_file()) # get all .com's
	words = [w for w in nltk.corpus.words.words('en') if w.islower() and len(w) >= 2 and len(w) <= 10 or w == "i" or w == "a"]
	comp = open("comp.txt", "w")
	digits = re.compile("\d")
	check = []
	for domain_row in csv:
		domain = domain_row[0].replace(".com", "")
		if (digits.search(domain) != None):
			continue
		if (len(domain) > 10):
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

def open_file():
	return csv.reader(open("dldoms.csv", "rb"), delimiter = ',')

main()