import plotly.express as px
import csv
import numpy as np


def getData(path, column1, column2):
    col1=[]
    col2=[]
    with open(path) as f:
      data=csv.DictReader(f)
      for row in data:
          col1.append(float(row[column1]))
          col2.append(float(row[column2]))
    return{"x": col1, "y": col2}


def findCorrelation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("The correlation for your data set is", correlation[0,1], ".")
    num=correlation[0,1]
    if num > 0:
      print("It is a positive number, which means your data is related in some way.")
    elif num == 0:
     print("It is zero, so your data isn't related at all.")
    else:
      print("It is a negative number, so the things you were comparing don't make sense.")
def main():
    path = input("Hey! Enter the path of the file.")
    if(path):
        with open(path, "r") as file:
            first_line = file.readline()
        print("Here are the choices for x and y:", first_line, ". Copy and paste these into the sections below.")
        column1 = input("Enter the column name for x.")
        column2 = input("Enter the column name for y.")
        data= getData(path, column1, column2)
        findCorrelation(data)
  
main()
 