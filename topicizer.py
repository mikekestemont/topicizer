#!/usr/bin/env python
# -*- coding: utf-8 -*-

###### TOPICIZER #############################################################
## Copyright (c) 2015 University of Antwerp, Belgium                        ##
## Author: Mike Kestemont <mike.kestemont@gmail.com>                        ##
##############################################################################

import re
import os
import shutil
import sys

from collections import Counter

from lxml import etree
import pandas as pd

PUNCTUATION = re.compile(r"\.|\?|\!|\,|\:|\;")
WHITESPACE = re.compile(r"\s+")
QUOTES = re.compile(r'\"|\'|\“|\”|\‘|\’|\«|\»')
ES = re.compile(r'\é|\è|\ë')

def clean_text(text):
	text = text.lower()
	text = ES.sub("e", text)
	text = PUNCTUATION.sub(" ", text)
	text = WHITESPACE.sub(" ", text)
	text = QUOTES.sub("", text)
	return text

def main():
	print("Topicizer started...")
	# parse arguments:
	path_to_dict, path_to_corpus, output_folder = sys.argv[1:]
	# clean up / make the output folder
	output_folder = os.path.normpath(output_folder)
	if os.path.isdir(output_folder):
		shutil.rmtree(output_folder)
	os.mkdir(output_folder)
	# parse topics:
	tree = etree.parse(open(path_to_dict))
	topics = {}
	vocab_counter = Counter()
	for node in tree.iterfind("//cnode"):
		t = node.attrib["name"].lower()
		if not t.startswith("t"):
			t += "t"
		topics[t] = set()
		for n in node.iterfind("pnode"):
			text = n.attrib["name"]
			text = clean_text(text)
			regex = re.compile(text)
			topics[t].add(regex)
	# initialize some containers:
	sorted_topics = sorted(list(topics.keys()))
	df_topic_counts = pd.DataFrame(columns=["ID", "word_count"]+sorted_topics)
	df_first_occurence = pd.DataFrame(columns=["ID", "word_count"]+sorted_topics)
	words_found_file = open(os.sep.join([output_folder, "words_found.tsv"]), "w+")
	vocab_count_file = open(os.sep.join([output_folder, "vocab_count.tsv"]), "w+")
	# loop over the documents:
	texts = open(path_to_corpus).readlines()
	for text in texts:
		text = clean_text(text)
		try:
			ID, text = text.split(" ", 1)
			if ID == "id" and text.strip() == "body":
				continue
		except ValueError:
			continue
		print("\t* parsing document #"+str(ID))
		matched_expressions = []
		# initalize dict for this text:
		local_topic_counts = {k:0 for k in sorted_topics}
		first_occurence = {k:"NA" for k in sorted_topics}
		for topic_name, topic_vocab in topics.items():
			for regex in topic_vocab:
				matches = list(regex.finditer(text))
				if matches:
					matched_expressions.append(regex.pattern)
					first_occurence[topic_name] = matches[0].span()[0]
					local_topic_counts[topic_name] += len(matches)
					vocab_counter[regex.pattern] += len(matches)
		word_count = len(text.split())
		df_topic_counts.loc[len(df_topic_counts.index)] = [ID, word_count]+[local_topic_counts[c] for c in sorted_topics]
		df_first_occurence.loc[len(df_first_occurence.index)] = [ID, word_count]+[first_occurence[c] for c in sorted_topics]
		if matched_expressions:
			words_found_file.write(ID+"\t"+','.join(matched_expressions)+"\n")
	for k, v in vocab_counter.items():
		vocab_count_file.write(k+"\t"+str(v)+"\n")
	df_topic_counts = df_topic_counts.set_index("ID")
	df_first_occurence = df_first_occurence.set_index("ID")
	words_found_file.close()
	vocab_count_file.close()
	# save to csv
	name = os.path.splitext(path_to_corpus)[0]+"-"+os.path.splitext(path_to_dict)[0]+"-"
	df_topic_counts.to_csv(os.sep.join([output_folder, "topic_cnts.csv"]))
	df_first_occurence.to_csv(os.sep.join([output_folder, "1st_occ.csv"]))
	#print(df_topic_counts.to_string())
	#print(df_first_occurence.to_string())
	print("Topicizer ended!")

if __name__ == "__main__":
	main()
