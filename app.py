from flask import Flask
from time import strftime
from socket import gethostname
from socket import gethostbyname
app = Flask(__name__)
@app.route('/')
def welcome():
    return 'Please go to the next direction => IP of your machine:9000/dockerEndpoint'
    
@app.route('/dockerEndpoint')
def docker():
    date = ' The current date is: ' + strftime('%d/%m/%y')
    time = ' The current time is: ' + strftime('%H:%M:%S')
    hostname = ' The hostname is: ' + gethostname()
    ipNumber = ' The IP number is: ' + gethostbyname(gethostname())
    message = date + time + hostname + ipNumber
    return message

if __name__ == '__main__':
    app.run(debug=True , port=9001 , host='0.0.0.0')