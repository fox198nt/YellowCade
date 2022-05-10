from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '''
    <!doctype html>
    <html>
    <head>
    <link href="/yellowcade.css" rel="stylesheet">
    <h1>YellowCade</h1>
    <p>a discord bot mamade by fox198</p>
    <p>something to help me develop the cat command</p>
    <iframe src="https://www.youtube.com/embed/Q5u6MDQAG7I"></iframe>
    </body>
    </html>
    '''

def run():
    app.run(host="0.0.0.0", port=9090)

def keep_alive():
    server = Thread(target=run)
    server.start()