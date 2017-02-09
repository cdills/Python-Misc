from __future__ import print_function
import praw
import webbrowser
outputFile=open("Python/results.htm", 'w', errors='ignore')

reddit = praw.Reddit(client_id='', client_secret="",
                     password='', user_agent='Python:RL_Exchange_Search',
                     username='')

subreddit = reddit.subreddit('RocketLeagueExchange')

uQuery=input("Enter desired item. e.g. Hypernova:  ")
uLimit=input("How many results? e.g. 10:  ")
uSort=input("New, Top, or Hot:  ")
uTime=input("Seach post from the last hour, day, week, month, or year?:  ")
uTitle="Searching for: " + uSort + " post(s) containing " + uQuery + " posted in the last " + uTime + "."

sTags='''<html>
<head>'''+ uTitle.upper() +'''</head>
<body><p>'''

eTags='''</p></body>
</html>'''

print (sTags, file=outputFile)

for submission in subreddit.search(uQuery, sort=uSort, limit=int(uLimit), time_filter=uTime.lower()):

	print("<a href=" + submission.url + ">" + submission.title + "</a>", sep='', end='<br>', file=outputFile)
	
print (eTags, file=outputFile)

webbrowser.open(outputFile)