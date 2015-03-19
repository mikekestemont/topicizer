# Topicizer
This repo provides a simple script to count words and topics in texts. It mimicks aspects of the behaviour of the [Lexicoder](http://www.lexicoder.com/) software package, but should also work for right-to-left languages like Hebrew.

## Dependencies
This script is meant to be used with the Python 3 Anaconda distribution. Please download and install the Anaconda distribution for Python 3 (not 2!) before running the script. Detailed instructions are available at [Continuum's website](http://continuum.io/downloads).

## Input files
The topicizer.py script requires two input files: a dictionary and a corpus. The dictionary takes the ".lcd" extension and should be written in valid XML. A short example in Dutch:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<dictionary style="Lexicoder" name="policy_agendas">
		<cnode name="t100">
			<pnode name="totaal aanbod"></pnode>
			<pnode name="conjunctuur"></pnode>
			<pnode name="vraagschok"></pnode>
			<pnode name=" NBB "></pnode>
		</cnode>
			<cnode name="t200">
			<pnode name="burgerrecht "></pnode>
			<pnode name="validisme"></pnode>
			<pnode name="recht op informatie"></pnode>
			<pnode name="bifobie"></pnode>
		</cnode>
	</dictionary>
```

Note that this script is highly aware of whitespace etc. in the vocabulary which you provide, so be vigilant. (Please don't use tab character in the word or topic name attributes.) Secondly, you need a corpus file which takes a .txt extension and which has one document per line (except for the header on the first line). A Dutch-language example:

```tsv
ID	body
1	De vergadering wordt geopend om 14.28 uur en voorgezeten door de heer André Flahaut.
2	Een reeks mededelingen en besluiten moeten ter kennis gebracht worden van de Kamer. Zij worden op de website van de Kamer en in de bijlage bij het integraal verslag van deze vergadering opgenomen. Aanwezig bij de opening van de vergadering zijn de ministers van de federale regering: Pieter De Crem, Didier Reynders, Koen Geens, Servais Verherstraeten, Hendrik Bogaert
3	Berichten van verhindering: Eva Brems, Minneke De Ridder, Guy D'haeseleer, Flor Van Noppen, wegens gezondheidsredenen Linda Musin, Karel Uyttersprot, wegens familiale redenen; Sabien Lahaye-Battheu
```

Each document should be preceded by a counter (ID), followed by a tab character ("\t"). Please make sure that all your input files have been properly encoded as "UTF-8" before saving them.

## Running the script

First, download this repository by clicking "Download ZIP" and unzipping the folder in a convenient location on your computer, such as your Desktop. In the unzipped folder, you can find topicizer.py as well as a number of example files. This script should be run from the command line: first open a command line window (e.g. via the "Terminal" in your Applications folder on Mac OS X). After opening this window, navigate to the directory using the cd command: 

```bash
>>> cd ~/Desktop/topicizer
```

From there, now can now run the script with the example data:

```
>>> python topicizer.py sample_data/dutch/dutch_dictionary.lcd sample_data/dutch/dutch_corpus.txt dutch_output
>>> python topicizer.py sample_data/hebrew/hebrew_dictionary.lcd sample_data/hebrew/dutch_corpus.txt hebrew_output
```

Note that the script takes three arguments that specify paths: the dictionary, the corpus and the output folder. The order in which you specify these matters! The paths you specify can be absolute or, like in our case, relative to the script itself. This should print something like the following to your prompt:

```
Topicizer started...
	* parsing document #1
	* parsing document #2
	* parsing document #3
	* parsing document #4
	* parsing document #5
	...
	* parsing document #47
	* parsing document #48
	* parsing document #49
	* parsing document #50
Topicizer ended!

```

Larger corpora might take a while to be processed. After running the script, a folder with the outputs will have been created in the same folder as topicizer.py. The following files should have created:
* 1st_occ.tsv: tells you where the first match for each topic was found per topic (if any, counted in characters). Also has a column with the word counts per documents.
* topic_cnts.tsv: tells you how many matches were found for each topic in each document (if any). Also has a column with the word counts per documents.
* vocab_count.tsv: gives you the global frequency (i.e. cumulative document frequency) for each word in the vocabulary you specified.
* words_found.tsv: gives you a comma-separated list of all the words found in a document.

These files are in a so-called tab-separated or comma-separated format, which you can easily open in most speadsheet applications for subsequent processing.

That's it folks, enjoy!







