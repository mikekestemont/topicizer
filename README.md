# Topicizer
This repo provides a simple script to count words and topics in texts. It partially mimicks the behaviour of the [Lexicoder](http://www.lexicoder.com/) software package, but should also work for right-to-left languages like Hebrew.

# Dependencies
This script is meant to be used with the Python 3 Anaconda distribution. Please download and install the Anaconda distribution for Python 3 (not 2!) before running the script. Detailed instructions are available at [Continuum's website](http://continuum.io/downloads).

# Input 
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

Note that the script is highly aware of whitespace etc. in the vocabulary which you provide. Secondly, you need a corpus:



Please make sure that all your input files have been properly encoded as "UTF-8" before saving them.

