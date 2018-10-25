#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid
import json
import tornado.ioloop
import tornado.web
import tornado.websocket


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

waiters = set()
class ChatHandler(tornado.websocket.WebSocketHandler):
    # 用户存储当前聊天室用户

    # 用于存储历时消息
    messages = []

    def check_origin(self, origin):
        return True

    def open(self):
        """
        客户端连接成功时，自动执行
        :return:
        """
        # ChatHandler.waiters.add(self)
        # uid = str(uuid.uuid4())
        # self.write_message(uid)
        #
        # for msg in ChatHandler.messages:
        #     content = self.render_string('message.html', **msg)
        #     self.write_message(content)
        waiters.add(self)
        print("来人了")

    def on_message(self, message):
        """
        客户端连发送消息时，自动执行
        :param message:
        :return:
        """
        content=self.render_string("message.html",msg=message)
        for client in waiters:
            client.write_message(content)


    def on_close(self):
        """
        客户端关闭连接时，，自动执行
        :return:
        """
        waiters.remove(self)


def run():
    settings = {
        'template_path': 'templates',
        'static_path': 'static',
    }
    application = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/chat", ChatHandler),
    ], **settings)
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()




