# -*- coding: utf-8 -*-
from controller.html_functions import generateNews


def controllerIndex():

    news=generateNews(7).encode('utf-8')

    result=news

    return result





