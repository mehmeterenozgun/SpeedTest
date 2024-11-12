from flask import Flask, request, jsonify, send_file
import time
app = Flask(__name__)


@app.route('/')
def index():
    return send_file('index.html')

@app.route('/ping-test') #empty function for ping test
def ping_test():
    return ""

@app.route('/download-test', methods=['GET'])
def download_test():
    file_url = "./test.txt"
    response = send_file(file_url, as_attachment=True)
    response.headers["Content-Disposition"] = "attachment; filename=test.txt"
    return response


@app.route('/upload-test', methods=['POST'])
def upload_test():

    start_time = time.time()
    request.data
    end_time = time.time()

    file_size_mb = len(request.data) / (1024 * 1024)
    upload_speed = file_size_mb / (end_time - start_time)

    return jsonify({'upload_speed': upload_speed * 8, 'file_size': file_size_mb})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)