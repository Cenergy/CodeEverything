# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '25/10/2018 4:42 PM'


import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
import serial
import sys
import os
import time
import re


from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/websocket", ChatSocketHandler),
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html", messages=ChatSocketHandler.cache)

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200

    def open(self):
        print ("new client opened")
        ChatSocketHandler.waiters.add(self)
        while True:
            ser = serial.Serial("com64", 9600, timeout=30)
            ser.write(('AT+CFUN=1\r').encode('utf-8'))
            while True:
                line = ser.readline()
                try:
                    ChatSocketHandler.send_infos(line.decode('utf-8'))
                except:
                    pass
                if (re.search(b'OK', line)):
                    break

    def on_close(self):
        ChatSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    @classmethod
    def send_infos(cls, chat):
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)

        ChatSocketHandler.send_updates(message)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()