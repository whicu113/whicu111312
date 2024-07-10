from flask import Flask, request, jsonify, send_from_directory # type: ignore
import os

app = Flask(__name__)

# Stelle sicher, dass das Verzeichnis für geheime Dateien existiert
secret_dir = 'secret_data'
if not os.path.exists(secret_dir):
    os.makedirs(secret_dir)

# Definiere den Pfad zur Datei, in der die IP-Adressen gespeichert werden
ip_log_file = os.path.join(secret_dir, 'ip_log.txt')

@app.route('/log_ip', methods=['POST'])
def log_ip():
    visitor_ip = request.remote_addr
    with open(ip_log_file, 'a') as file:
        file.write(f'{visitor_ip}\n')
    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)