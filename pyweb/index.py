import tornado.web
import tornado.websocket
import tornado.ioloop
import json


class listRequestHandler(tornado.websocket.WebSocketHandler):
    def get(self):
        fh = open('D:/Studies/Hussein Nasser/Python on the Backend/pyweb/list.txt', 'r')
        fruits = fh.read().splitlines()
        for f in fruits:
            print(f)
        fh.close()
        self.write(json.dumps(fruits))


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/fruits', listRequestHandler),
    ])
 
    port = 8888
    app.listen(port)  # assigning the app to listen to port 8888
    print(f"Application is ready and listening on port {port}")  # printing put the message to the console

    tornado.ioloop.IOLoop.current().start()  # Keeps this app running
