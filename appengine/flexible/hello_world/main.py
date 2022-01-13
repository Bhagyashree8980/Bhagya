
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    #return ['BHAGYASHREE - SMIT2122004',+,'\n',+, 'BHUSHAN - SMIT2122005',+,'\n',+, 'CHINMAY - SMIT2122006',+,'\n',+, 'DEMO FOR THE TOPIC GOOGLE APP ENGINE.']

return'BHAGYASHREE - SMIT2122004 
BHUSHAN - SMIT2122005 
CHINMAY - SMIT2122006 

DEMO FOR THE TOPIC GOOGLE APP ENGINE!'

if __name__ == '__main__':
  
    app.run(host='127.0.0.1', port=8080, debug=True)
