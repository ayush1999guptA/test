from flask import Flask,jsonify


app=Flask(__name__)
stores=[
        {
         'name':'my wonderful store',
         'item': [
                   {'name':'bread',
                    'price':15.99}
                ]
         }
        ]
@app.route('/store',methods=['POST'])
def create_a_store():
	pass
@app.route('/store')
def get_store():
    return(jsonify({'stores':stores}))	

app.run(port=500)	