import json
from stackapi import StackAPI
SITE = StackAPI('stackoverflow' )
SITE.page_size = 100
SITE.max_pages = 8
# get all the questions
questions = SITE.fetch('questions', tagged = 'python;python-3.x;pandas')
jsobj = json.dumps(questions)
f = open("data/OtherData/question_data_2.json", "w")
f.write(jsobj)
f.close()

# filter data which tagged with python;python-3.x;pandas only!
question_data = json.load(open("data/OtherData/question_data_2.json.json"))
i = 0
while len(question_data["items"]) != 2428:
    if question_data["items"][i]["tags"] != ['python', 'python-3.x', 'pandas']:
        question_data["items"].pop(i)
        i = 0
    else:
        i = i + 1

f = open("data/OtherData/question_data_filtered.json", "r")
questions = json.load(f)
list2 = []
for i in questions['items']:
    x = i.get('question_id')
    list2.append(x)

# get all the answers
a1 = SITE.fetch('questions/{ids}/answers', ids = list2[0:100] )
a2 = SITE.fetch('questions/{ids}/answers', ids = list2[100:200] )
a3 = SITE.fetch('questions/{ids}/answers', ids = list2[200:300] )
a4 = SITE.fetch('questions/{ids}/answers', ids = list2[300:400] )
a5 = SITE.fetch('questions/{ids}/answers', ids = list2[400:500] )
a6 = SITE.fetch('questions/{ids}/answers', ids = list2[500:600] )
a7 = SITE.fetch('questions/{ids}/answers', ids = list2[600:700] )
a8 = SITE.fetch('questions/{ids}/answers', ids = list2[700:800] )
a9 = SITE.fetch('questions/{ids}/answers', ids = list2[800:900] )
a10 = SITE.fetch('questions/{ids}/answers', ids = list2[900:1000] )
a11 = SITE.fetch('questions/{ids}/answers', ids = list2[1000:1100] )
a12 = SITE.fetch('questions/{ids}/answers', ids = list2[1100:1200] )
a13 = SITE.fetch('questions/{ids}/answers', ids = list2[1200:1300] )
a14 = SITE.fetch('questions/{ids}/answers', ids = list2[1300:1400] )
a15 = SITE.fetch('questions/{ids}/answers', ids = list2[1400:1500] )
a16 = SITE.fetch('questions/{ids}/answers', ids = list2[1500:1600] )
a17 = SITE.fetch('questions/{ids}/answers', ids = list2[1600:1700] )
a18 = SITE.fetch('questions/{ids}/answers', ids = list2[1700:1800] )
a19 = SITE.fetch('questions/{ids}/answers', ids = list2[1800:1900] )
a20 = SITE.fetch('questions/{ids}/answers', ids = list2[1900:2000] )
a21 = SITE.fetch('questions/{ids}/answers', ids = list2[2000:2100] )
a22 = SITE.fetch('questions/{ids}/answers', ids = list2[2100:2200] )
a23 = SITE.fetch('questions/{ids}/answers', ids = list2[2200:2300] )
a24 = SITE.fetch('questions/{ids}/answers', ids = list2[2300:2400] )
a25 = SITE.fetch('questions/{ids}/answers', ids = list2[2400:2429] )

items = a1['items']+a2['items']+a3['items']+a4['items']+a5['items']+a6['items']+a7['items']+a8['items']\
        +a9['items']+a10['items']+a11['items']+a12['items']+a13['items']+a14['items']+a15['items']+a16['items']\
        +a17['items']+a18['items']+a19['items']+a20['items']+a21['items']+a22['items']+a23['items']+a24['items']+a25['items']

jsobj = json.dumps(items)
f = open("data/OtherData/answers_data_filtered.json", "w")
f.write(jsobj)
f.close()



