from flask import Flask
import pandas as pd
from regex import D
app = Flask(__name__)

@app.route('/')

def dummy():
    return 'Hello world'


@app.route('/loc/<int:a>/<int:b>')
def loc(a,b):
    df = pd.read_csv("TESTY.csv")
    d= df.loc[(df['WIDTH'] == a) & (df['HEIGHT'] == b)]
    e = d.to_dict()
    return e
if __name__ =="__main__":
    app.run(debug=True)