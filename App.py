from flask import Flask, jsonify,request
import pickle
import sklearn
import numpy as np
import pandas as pd 
import os
app=Flask(__name__)

@app.route('/Hello/<parameter>')
def intyaz (parameter):
    return "welcome to avani infosoft" +parameter

@app.route('/cropInput',methods = ['POST'])
def cropIn():
    a = request.form['nitrogen']
    b = request.form['phosphorus']
    c = request.form['potassium']
    d = request.form['temperature']
    e = request.form['humidity']
    f = request.form['ph']
    g = request.form['rainfall']
    file = open("pickle/crop_model.pickle",'rb')
    new_dict = pickle.load(file)
    model = new_dict.predict([[int(a),int(b),int(c),float(d),float(e),float(f),float(g)]])
    file.close()
    rlist=np.array(model)
    return jsonify(rlist.tolist())

  
    
if __name__ == '__main__':
    app.run(debug=True)    