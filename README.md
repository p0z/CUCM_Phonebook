# CUCM Phonebook Viewer

**CUCM Phonebook Viewer** - view phonebook from corporate directory :).

#### How it work?
The script parse XML from ccmcip directory.

Command line parameters:

	$ python cucm_phonebook.py -h
	
	optional arguments:
	-h, --help		show this help message and exit
	-t, --target		URL CUCM host (ex: https://target:8443/)
	-l, --lastname		Lastname search, default: none
	-f, --firstname		Firstname search, default: none
	-n, --number		Number, default: none
	-s, --start		Start records, default: 0
	-e, --end		End records, default: 30

Usage:

	$ python cucm_phonebook.py -t https://cucmsrv:8443/
