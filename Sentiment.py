from textblob import TextBlob
with open("demo.txt") as file:
    for line in file:
        text=line
        obj=TextBlob(text)
        sentiment=obj.sentiment.polarity
        print (line," ",sentiment)
        

