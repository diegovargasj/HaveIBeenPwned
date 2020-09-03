#!/usr/bin/python3
import requests
import argparse
from termcolor import colored
import time


URL = 'https://haveibeenpwned.com/unifiedsearch/'
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept-Language': 'en-US,en;q=0.5'
        }

def is_pwned(email):
    resp = requests.get(URL + email, headers=headers)
    if resp.content:
        return True

    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if an email or list of emails has been pwned at haveibeenpwned.com')
    parser.add_argument(
            '-e', 
            '--email', 
            metavar='<email>', 
            dest='email',
            type=str,
            help='email to check'
            )
    parser.add_argument(
            '-f', 
            '--file', 
            metavar='</path/to/file>',
            dest='file',
            type=str,
            help='file with one email per line'
            )
    parser.add_argument(
            '-p', 
            '--pwned', 
            action='store_true', 
            dest='pwned',
            help='print only pwned emails'
            )
    parser.add_argument(
            '-s', 
            '--sleep-time', 
            metavar='<seconds>',
            dest='sleep', 
            type=int,
            default=2,
            help='sleep time between queries in seconds, to avoid being blocked (default 2)'
            )

    args = parser.parse_args()
    email = args.email
    email_file = args.file
    pwned = args.pwned
    SLEEP = args.sleep

    emails = []
    if email:
        emails.append(email)

    if email_file:
        with open(email_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                emails.append(line.replace('\n', ''))

    for email in emails:
        if is_pwned(email):
            print(f'{email}: ' + colored('Pwned!', 'red'))

        elif not pwned:
            print(f'{email}: ' + colored('Safe', 'green'))

        time.sleep(SLEEP)

