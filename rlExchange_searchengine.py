# Searches rocketleagueexchange for desired items, outputs to and opens html page.

from __future__ import print_function
import praw
import webbrowser


def reddit_auth():
	global reddit, subreddit
	reddit = praw.Reddit(client_id="", client_secret="",
	password='', user_agent='',
	username='')
	subreddit = reddit.subreddit('RocketLeagueExchange')
def get_input():
	global uFlair, fQuery, uLimit, uSort, uTime, uTitle
	gFlair=input("Enter PC, PS4, or Xbox: ") or "PC"
	uFlair="[" + gFlair + "]"
	uQuery=input("Enter desired item. e.g. Hypernova:  ") or "Photon"
	fQuery=(uFlair + " " + uQuery)
	uLimit=input("How many results? e.g. 10:  ") or 10
	uSort=input("Sort by relevance, hot, top, new, or comments?:  ") or "relevance"
	uTime=input("Seach post from the last hour, day, week, month, or year?:  ") or "hour"
	uTitle="Searching for post(s) containing: \"" + fQuery + "\" posted in the last " + uTime + " sorted by " + uSort
def create_htm():
	global	filepath, outputFile
	filepath="/Scripts/Python/out.html"
	outputFile=open(filepath, 'w', errors='ignore')
	sTags='''<html>
	<head>'''+ uTitle.upper() +'''</head>
	<body><p>'''
	print (sTags, file=outputFile)
def close_htm():
	eTags='''</p></body>
	</html>'''
	print (eTags, file=outputFile)
def add_urllist():
	print("<a href=" + submission.url + ">" + submission.title + "</a>", sep='', end='<br>', file=outputFile)
def do_search():
	for submission in subreddit.search(fQuery, sort=uSort, limit=int(uLimit), time_filter=uTime.lower()):
		print("<a href=" + submission.url + ">" + submission.title + "</a>", sep='', end='<br>', file=outputFile)
def open_htm():
	webbrowser.open(filepath)
def email_self(fFile): # Doesn't work, email is blank
	import	smtplib
	from email.mime.text import MIMEText
	gmail_user=""
	gmail_pwd=""
	fp = open(fFile, 'r')
	msg = MIMEText(fp.read(), _subtype="html")
	fp.close()
	
	msg['Subject'] = "RLE Trades"
	msg['From'] = ""
	msg['TO'] = ""
	
	s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	s.ehlo()
	s.starttls
	s.login(gmail_user, gmail_pwd)
	s.sendmail("to", "from", msg.as_string())
	s.close
	
reddit_auth()
get_input()
create_htm()
do_search()
close_htm()
# email_self(filepath)
open_htm()