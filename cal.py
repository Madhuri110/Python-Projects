
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/result', methods=['POST' , 'GET'])
def result():
    num1=float(request.form["num1"])
    num2=float(request.form["num2"])
    
    if request.method=="POST":
        if request.form["process"]=="add":
            return str(num1+num2)
        if request.form["process"]=="substract":
            return str(num1-num2)
        if request.form["process"]=="multiply":
            return str(num1*num2)
        if request.form["process"]=="divide":
            return str(num1/num2)
        
        
        
        
if __name__=='__main__':
    app.run()
