"Watches Reddit submission stream and notifies based on user criteria"

import tkinter
from tkinter import *
import threading
import praw
import os
from local_modules import reddit_auth #imports  reddit API information. accepts subredditname, returns subreddit object
from twilio.rest import TwilioRestClient
import smtplib

def notify(): #Sloppy way of running main functions without using classes 
	watch_post(reddit_auth(ssub))

thread_one=threading.Thread(target=notify) #Runs notify as threaded object
stopped="false" #Set initial state for stop variable



def gui(): #Draws GUI window and defines interaactive functions
	global printer

	def stopper(): #Sets stopped variable to break look, outputs to text window
		global stopped
		stopped = "true"
		t.insert(END, " Stopping please restart Reddit_Notify to search again ")

	def callback(): #Captures text in entry fields and starts notify thread
		global query, ssub
		query=e_q1.get()
		ssub=e_q2.get()
		t.insert(END, f"Searching r/{ssub} for \"{query}\":\n")
		thread_one.daemon="true" #This allows the thread to stop when the window is closed
		thread_one.start()

	def printer(submission): #Writes title of search results to text window
		urlline = submission.url + "\n"
		title = submission.title + "\n"
		link = f"<a href={urlline}>{title}</a>"
		t.insert(END, title)



	window=tkinter.Tk() #creates window object
	window.configure(background="#a1dbcd")
	window.title("Reddit Notify") #Sets window title
	#window.wm_iconbitmap("none") #sets window icon



	l_intro= Label(window, text="       Welcome to Reddit Notify       ", fg="#a1dbcd", bg="#383a39", font=("Helvitica",24))
	l_intro.pack() #pack places object in window sequentially

	l_q1= Label(window, text="Text to search for:", bg="#a1dbcd", fg="#383a39", font=(14))
	l_q1.pack(padx=10)

	e_q1 = Entry(window)
	e_q1.pack()

	l_q2 = Label(window, text="Subreddit to monitor:", bg="#a1dbcd", fg="#383a39", font=(14))
	l_q2.pack()

	e_q2 = Entry(window)
	e_q2.pack()

	s = Button(text="Stop", command=stopper, fg="#a1dbcd", bg="#383a39", font=(14))
	s.pack(side=BOTTOM,pady=5)

	b = Button(text="Begin", command=callback, fg="#a1dbcd", bg="#383a39", font=(14))
	b.pack(pady=5)



	t = Text(window,height=5, width=43, font="Helvitica", fg="#383a39")
	t.pack(pady=5, padx=5)


	window.mainloop()  # Draws window on screen



def gmail_sms(body): #Sends SMS using google account. Accepts body as message to be sent. 
		
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	
	server.starttls()
	server.login( "@gmail.com", '' )
	
	# Destination number must use gateweay of provider
	server.sendmail( '', '@vtext.com ', body)

	print(body) #Prints to console to verify message sent

def twilio_auth(results):	#Sends SMS using Twilio acct. 
	account_sid = ""
	auth_token = ""
	client = TwilioRestClient(account_sid, auth_token)
	
	message = client.messages.create(to="+", from_="", body=results)
	print(message.body)
	
def watch_post(subreddit): #must be run with reddit_auth as argument
	for submission in subreddit.stream.submissions():
		scan_post(submission, query)
		if stopped=="true": #breaks look when stopped variable is set by stop button
			break


def ask_subreddit(): #Gets user input for desired subreddit. returns string
	subreddit_To_search=input("Enter subreddit name to monitor: ") or all
	return str(subreddit_To_search)

def get_criteria():  #gets user search criteria, sets as global, returns string
	global criteria
	criteria=input("Enter the text you would like to detect: ")
	return str(criteria)
	
def scan_post(submission,search): #searches submission from watch_post for desired text
	search_str=str(search)
	normalized_title = submission.title.lower()
	if search_str in normalized_title:
		submission.save(category="Saved by R_Notify")
		gmail_sms(submission.title)
		printer(submission)


def main():

	gui()

if __name__ == "__main__":
	main()
