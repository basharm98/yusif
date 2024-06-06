from pyrogram import Client
from pyrogram import filters

from mody.Redis import db
from mody.get_info import token, sudo_info, get_bot

Bot = Client(
    'MainBot',
    25829176,
    '160b2bf653ee7dd974bd6d09a7968cd1',
    bot_token=token,
    plugins=dict(root='plugins/bot')
)


sudo_client = Client(
    'MainUser',
    25829176,
    '160b2bf653ee7dd974bd6d09a7968cd1',
    session_string=db.get(f'{get_bot.id}:{sudo_info.id}:session'),
    plugins=dict(root='plugins/user')
)
sudo_client.login = False


def Bfilter(text):
    return filters.msg(text) & filters.private & filters.user(sudo_info.id)

