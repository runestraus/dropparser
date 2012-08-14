import csv
import re

def main():
	words = open("words.txt", "r").readlines()
	new = open("new.txt", "w")
	for word in words:
		if (len(word) > 3 and len(word) <= 10):
			new.write(word)

main()