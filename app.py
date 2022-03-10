import socket

from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def show_index():
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
              sock = socket.create_connection((ip_arr[i], port_arr[j]), timeout=0.5)
              condition="OPEN"
            except socket.timeout as err:
              condition="CLOSED (Timeout)"
            except socket.error as err:
              condition="CLOSED (Refused)"
            temp_var = f"Port {port_arr[j]} is {condition} to {ip_arr[i]}" + "<br>"
            info_array+= temp_var
        return json.dumps({'data': info_array})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

