# -*- coding: utf-8 -*-
from controller.html_functions import generateNews
from controller.ctrl_cache import verifyLoggedIn, savePageToSession


def controllerIndex():
    page_name = 'index'
    verify_logged = verifyLoggedIn('username', False)
    if verify_logged != 'UNVERIFIED':
        savePageToSession(page_name, True)  # Save the current page to the visitor's session store

    news=generateNews(7)

    result=news

    return result





