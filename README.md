# Usage

	usage: haveibeenpwned [-h] [-e <email>] [-f </path/to/file>] [-p] [-s <seconds>]

	Check if an email or list of emails has been pwned at haveibeenpwned.com

	optional arguments:
	  -h, --help            show this help message and exit
	  -e <email>, --email <email>
				email to check
	  -f </path/to/file>, --file </path/to/file>
				file with one email per line
	  -p, --pwned           print only pwned emails
	  -s <seconds>, --sleep-time <seconds>
				sleep time between queries in seconds, to avoid being blocked (default 2)

# Install 
	git clone https://github.com/diegovargasj/HaveIBeenPwned.git
	cd HaveIBeenPwned/
	pip3 install -r requirements.txt

