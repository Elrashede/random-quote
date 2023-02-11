from flask import Flask
import json
from random import randint

app=Flask(__name__)

# f = open("quotes.json", "r")
#open file quotes and get random quote.
def random_qoute():
    with open('quotes.json') as rq:
        data = json.load(rq)
        qoute = data["quotes"]
        #list of dictionary
        my_list =[]
        for i in range(len(qoute)):
            id=data["quotes"][i]["id"]
            my_list.append({"id":id,"count":0})
        
        random_index = randint(0, len(qoute)-1)
        randomQuote=data["quotes"][random_index]
        quoteId=randomQuote["id"]
        
        for i in range(len(qoute)):
            if quoteId == my_list[i]["id"]:
                my_list[i]["count"]+=1
        print(my_list)
        return randomQuote

#find quote if i have the id;
def search_quote(id):
    with open('quotes.json') as rq:
        # get all content of a file
        data = json.load(rq)
        quoteLen=len(data["quotes"])
        for i in range(quoteLen):
            if(id==data["quotes"][i]["id"]):
                qouteVal=data["quotes"][i]["quote"]
                return qouteVal
        
#open file authors and get author of the quote.
def quote_details():
    with open('authors.json') as sa:
        data = json.load(sa)
        authLen=len(data["authors"])
        authors = data["authors"]
        quoteID=random_qoute()["id"] 
        print(quoteID)
        result={
            "quoteId": 0,
            "quote": "",
            "author": ""
        }
        for i in range(authLen):
            if quoteID in authors[i]["quoteIds"]:
                result["quoteId"]=quoteID
                result["quote"]=search_quote(quoteID)
                result["author"]=authors[i]["author"]
                return result
                
                       
@app.route('/quote/random')
def index():
    return quote_details()

if __name__=="__main__":
    app.run(debug=True)

