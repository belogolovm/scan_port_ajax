import socket

from flask import Flask, render_template, request, jsonify, json
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index():
    return render_template('index.html')

output=[]
@app.route('/', methods = ['POST'])
def get_data_from_html():
        return render_template('index.html')

@app.route('/check', methods=['GET', 'POST'])
def check():
        ip = request.form['ip'];
        port =  request.form['port']
        ip_arr = ip.split()
        port_arr = port.split()
        info_array = ""
        for i in range(0,len(ip_arr)):
          for j in range(0,len(port_arr)):
            try:
              sock = socket.create_connection((ip_arr[i], port_arr[j]), timeout=2)
#              print("Port", port_arr[j],"is OPEN to", ip_arr[i])
              condition="OPEN"
            except socket.timeout as err:
#              print("Port", port_arr[j],"is CLOSED TIMEOUT to", ip_arr[i])
              condition="CLOSED (Timeout)"
            except socket.error as err:
#              print("Port", port_arr[j],"is CLOSED REFUSED to", ip_arr[i])
              condition="CLOSED (Refused)"
            temp_var = f"Port {port_arr[j]} is {condition} to {ip_arr[i]}" + "<br>"
            info_array+= temp_var
#        return info_array
        return json.dumps({'data': info_array})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

