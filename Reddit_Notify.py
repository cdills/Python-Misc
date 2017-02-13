"Watches Reddit submission stream for chosen subreddit and notifies based on user criteria"

import praw
import webbrowser
from local_modules import reddit_auth #imports sensitive reddit API information. accepts subredditname, returns subreddit object
import smtplib


def gmail_sms(body): #Semds SMS using google account. Accepts body as message to be sent. 
		
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	
	server.starttls()
	server.login( "gmail_user", 'gmail_pass' )
	
	# Destination number must use gateweay of cell provider
	server.sendmail( 'from', 'to@vtext.com ', body)

	print(body) #Prints to console to verify message sent

def watch_post(subreddit): #must be run with reddit_auth as argument
	for submission in subreddit.stream.submissions():
		scan_post(submission, criteria)

def ask_subreddit(): #Gets user input for desired subreddit. returns string
	subreddit_To_search=input("Enter subreddit name to monitor: ") or all
	return str(subreddit_To_search)

def get_criteria(): #gets user search criteria, sets as global, returns string
	global criteria
	criteria=input("Enter the text you would like to detect: ")
	return str(criteria)
	
def scan_post(submission,search): #searches each submission from watch_post for desired text and sends text with title. Saves post.
	search_str=str(search)
	normalized_title = submission.title.lower()
	if search_str in normalized_title:
		submission.save(category="Saved by R_Notifiy")
		gmail_sms(submission.title)

def main():
	get_criteria()
	watch_post(reddit_auth(ask_subreddit()))	

if __name__ == "__main__":
	main()
