import csv
import re

def main():
	csv = filter(lambda x: x[1] == "com" , open_file()) # get all .com's
	words = open("words.txt", "r").readlines()
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
		lst = []
		for word in words:
			wordz = word.strip()
			if domain.find(wordz) != -1:
				lst.append(wordz)
		if len(lst) == 0:
			continue
		char_count = 0
		for word in lst:
			char_count += len(word)
		if (char_count >= len(domain)):
			check.append(domain)
			print domain
	for domain in check:
		comp.write(domain + "\n")
	print "Compilation complete"

def reduction(x, y):
	return len(x) + len(y)

def open_file():
	return csv.reader(open("dldoms.csv", "rb"), delimiter = ',')

main()