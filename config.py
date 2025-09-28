#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Ankush

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8492404811:AAGe-Ts1FeefAq0g0h4cZNMXUC1PHb0YCJA")
    API_ID = int(os.environ.get("API_ID", "27397664"))
    API_HASH = os.environ.get("API_HASH", "527b9c1f6495ba3be54ce0a2658ae463")
    AUTH_USERS = "8217117312"


