# -*- coding: utf-8 -*-
from linebot import (LineBotApi, WebhookHandler)
import sys , os
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
 SourceUser, SourceGroup, SourceRoom,
 TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
 ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
 CarouselTemplate, CarouselColumn, PostbackEvent,
 StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
 ImageMessage, VideoMessage, AudioMessage,
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent)
line_bot_api = LineBotApi('eMsgLuZ6rYOhWPhAL4Z+9BtjZHKs96MX8FeWPBPbppQxmjSLXWzn61QhB3bYjO2hlRZiAZrArRikvcHlw0ZSgPK+JTklzYRhAVKIPr/3Zy5/K9ADlpnjfBcnCTfoAxsilFeWzSdzUyFpW/Y9E7REkgdB04t89/1O/w1cDnyilFU=')
try:
	line_bot_api.push_message('Ufac7aa7413fd9c7696de1ccfd2062270', TextSendMessage(text="OK"))
except Exception as e:
	line_bot_api.push_message('Ufac7aa7413fd9c7696de1ccfd2062270', TextSendMessage(text="error"))

