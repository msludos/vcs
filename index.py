from flask import Flask, render_template, url_for, request
from bot.bot import *
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/vk', methods=['GET', 'POST', 'HEAD'])
def vkapi():
    return getCToken()
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'This page only for VK API requests'

    if data['type'] == 'confirmation':
        return getCToken()
    elif data['type'] == 'message_new':
        process_command(data["object"]["message"])
        return 'ok'
    
    return 'ok'

    
if __name__ == "__main__":
    app.run()