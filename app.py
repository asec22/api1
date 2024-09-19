import csv
from csv import DictReader
from flask import Flask, request,render_template,redirect,url_for

app = Flask(__name__)

def readFile(file):
    file_dict={}
    file_path="./static/"+file
    x=0
    with open(file_path, 'r') as f:
        dict_reader = DictReader(f)
        data_dict= list(dict_reader)
    for items in data_dict:
        x_string="PT{:05d}".format(x+1)
        a=x_string
        file_dict[a]=items 
        x+=1
    return [file_dict,data_dict,file_path,file]

def writeFile(dnary,file):
    new_dict=dnary
    headers=list(new_dict[0].keys())
    dpath=file
    with open(dpath,'w',newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()
        writer.writerows(new_dict)
    return dpath
    
@app.route('/')
def index(): 
    mypatients=readFile("fakepatient.csv")
    return mypatients[0]

if __name__=="__main__":
    app.run(debug=True)