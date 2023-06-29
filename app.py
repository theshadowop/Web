import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://theshadowop: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@github.com/theshadowop/File-Sharing-Bot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
