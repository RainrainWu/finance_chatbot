import os

from linebot import LineBotApi
from linebot.models import (
    TextSendMessage,
    ImageSendMessage
)


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(img_url, img_url))
    return "OK"


"""
def send_button_message(id, text, buttons):
    pass
"""