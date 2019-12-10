import os
import sys

from flask import Flask, request, abort
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

import fsm
import handler

load_dotenv()

machine = fsm.InvestMachine("IM")
hall = handler.HallHandler(machine)
news = handler.NewsHandler(machine)
voladility = handler.VoladilityHandler(machine)

app = Flask(__name__, static_url_path="")

channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        text = str(event.message.text.lower())
        if (machine.state == "hall"):
            hall.handle(event, text)
            continue
        if (machine.state == "news"):
            news.handle(event, text)
            continue
        if (machine.state == "volatility"):
            voladility.handle(event, text)
            continue

    return "OK"


if __name__ == "__main__":

    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
