from ftplib import FTP
from flask import Flask, redirect, url_for, request, render_template, send_file

app = Flask(__name__)

ftp = FTP('')


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    host = request.form['host']
    port = request.form['port']
    user = request.form['user']
    pw = request.form['pw']

    ftp.connect(host, port)
    ftp.login(user, pw)
    return ftp
@app.route('/logout', methods=['POST'])
def logout():
    ftp.quit()
    return ftp

@app.route('get-directory', methods=['GET'])
def get_directory():
    dir = request.args.get('dir')
    return ftp.cwd(dir)
@app.route('/images')
def get_image():
    filename = request.args.get('filename')
    print(filename)
    file_path = 'out/' + filename
    return send_file(file_path, mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=True)
