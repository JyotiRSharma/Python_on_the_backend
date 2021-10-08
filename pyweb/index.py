import tornado.web
import tornado.websocket
import tornado.ioloop
import json


# Root handler to redirect it to index.html
class mainRequestHandler(tornado.websocket.WebSocketHandler):
    def get(self):
        self.render('index.html')


class listRequestHandler(tornado.websocket.WebSocketHandler):
    # http://govinda:8888/fruits
    # That's how a get request will look like
    def get(self):
        fh = open('D:/Studies/Hussein Nasser/Python on the Backend/pyweb/list.txt', 'r')
        fruits = fh.read().splitlines()
        for f in fruits:
            print(f)
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        # http://govinda:8888/fruits?fruit=Mango 
        # This is how a POST request will look
        fruit = self.get_argument('fruit')
        fh = open('D:/Studies/Hussein Nasser/Python on the Backend/pyweb/list.txt', 'a')
        fh.write(f'\n{fruit}')
        fh.close()
        self.write(json.dumps({'message':'Your fruit has been added successfully!'}))


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', mainRequestHandler),  # Root handler
        (r'/fruits', listRequestHandler),
    ])
 
    port = 8888
    app.listen(port)  # assigning the app to listen to port 8888
    print(f"Application is ready and listening on port {port}")  # printing put the message to the console

    tornado.ioloop.IOLoop.current().start()  # Keeps this app running
