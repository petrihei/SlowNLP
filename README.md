# SlowNLP

Project work for course KIK-LG211, Building NLP Applications

The application takes the user's input (in English), searches for the closest match in Latin Wiktionary and compares the two, calculating the similarity percentage. In addition to the percentage, the application finds the English translation for the search word and prints it.

Installation

Prerequisities

• You must have Solr installed in your computer (the version used in the application was 7.1.0; earlier versions have not been tested). You can download it here:http://mirror.netinch.com/pub/apache/lucene/solr/7.1.0/
• You must have the Latin Wiktionary dump downloaded. You can find the latest dump here:https://dumps.wikimedia.org/lawiktionary/latest/
• You must have a working Internet connection for the application to search for the translations in an online dictionary.

Creating Solr index for the application

1. Create a Solr core in directory \solr-7.1.0\server\solr\ following Solr instructions.
2. Copy schema.xml and data-config.xml from the repository to the "conf" folder of the core.
3. In the "conf" folder, delete managed-schema.xml.
4. In the data-config.xml file, specify the path in the local computer in the URL.
5. Run Solr and index the dataset.

Installing

Clone the LatinAI repository, i.e. the following files:
• latinAI.py
• latinInspector.py
• logic.py
• crawler.py
• ui.py
• solrConnector.py

Running the application

1. Start Solr.
2. When Solr is up and running, run latinAi.py in a command prompt.
3. Follow the instructions on the screen and eithera) Be seriously impressedb) Wonder why anyone would create something like this (answer: it's for a school project, not meant to be a serious piece of software!)


