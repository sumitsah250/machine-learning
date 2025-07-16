from flask import Flask , request, jsonify
import pickle
import numpy as np

model=pickle.load(open(r'C:\Users\sumit\OneDrive\Desktop\machine learning\projects\gold price prediction\model1.pkl','rb'))

app= Flask(__name__)

@app.route('/')
def home():
    return "Hello sumit"

@app.route('/predicate',methods=['POST'])
def predict():
    SPX=request.form.get('SPX')
    USO=request.form.get('USO')
    SLV=request.form.get('SLV')
    EUR=request.form.get('EUR')
    
    input_query=np.array([[SPX,USO,SLV,EUR]])
    result=model.predict(input_query)[0]
    
    result={"Gold Price":result}
    
    
    return jsonify(result)
if __name__=='__main__':
    app.run(debug=True)