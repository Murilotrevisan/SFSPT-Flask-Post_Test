from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/jsonpack', methods=['GET', 'POST'])
def postHandler():
    content = request.get_json()
    print(content)
    return 'JSON RECEIVED VIA POST'