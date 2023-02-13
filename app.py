from flask import Flask
import json
import xlsxwriter
import xlwt
import xlrd
from xlutils.copy import copy
import openpyxl
from openpyxl import load_workbook
from random import randint
import pandas as pd


app=Flask(__name__)

# f = open("quotes.json", "r")
#open file quotes and get random quote.
def random_qoute():
    with open('quotes.json') as rq:
        data = json.load(rq)
        qoute = data["quotes"]
        quoteLen=len(data["quotes"])
       
        random_index = randint(0, len(qoute)-1)
        randomQuote=data["quotes"][random_index]
        quoteId=randomQuote["id"]

         #open excel file and update count value
        # reading excel file 
        
        workbook = xlrd.open_workbook('Quotes Report.xlsx')
        sheet = workbook.sheet_by_index(0) 
        cell_value = sheet.cell_value(1, 2)
        for i in range(quoteLen):
           if quoteId == cell_value:
            sheet.write(2, 2,2 )
            print("done")
            workbook.save(filename="Quotes Report.xlsx")
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

# create Excel File and add column , run once       
# def create_Excel():
#     workbook2 = xlwt.Workbook() 
#     sheet = workbook2.add_sheet('Quotes Report') 
#     sheet.write(0,0, 'Quote ID')
#     sheet.write(0,1, 'Count')
#     with open('quotes.json') as rq:
#         data = json.load(rq)
#         qoute = data["quotes"]
#         my_list =[]
#         for i in range(len(qoute)):
#             id=data["quotes"][i]["id"]
#             my_list.append({"id":id,"count":0})
#     for i in range(len(my_list)):                                          
#         sheet.write(i+1, 0, my_list[i]["id"])                                 
#         sheet.write(i+1, 1, my_list[i]["count"])       
#         workbook2.save('Quotes Report.xlsx')
    
    

@app.route('/quote/random',methods=['GET'])
def index():
    return quote_details()

if __name__=="__main__":
    # create_Excel()
    app.run(debug=True)

