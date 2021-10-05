import tornado.web
import tornado.websocket
import tornado.ioloop


class basicRequestHandler(tornado.websocket.WebSocketHandler):  # Class to create a server to handle the request
    def get(self):
        self.write('Hello, world, this is a Python on the backend')  # printing out the message to webpage

class queryParamRequestHandler(tornado.websocket.WebSocketHandler):  # Class to create a server to handle the request
    def get(self):
        num = self.get_argument('num')
        if (num.isdigit()):
            r = "odd" if int(num)%2 != 0 else "even"
            self.write(f"{num} is {r}")
        else:
            self.write(f"{num} is not a valid integer")


class listRequestHandler(tornado.websocket.WebSocketHandler):  # Class to create a server to handle the request
    def get(self):
        self.render('index.html')


class resourceParamRequestHandler(tornado.websocket.WebSocketHandler):  # Class to create a server to handle the request
    def get(self, studentName, courseId):
        self.write(f'Welcome {studentName} with course id {courseId}')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/', basicRequestHandler),  # Calling out the class with the / request
        (r'/animal', listRequestHandler),
        (r'/isEven', queryParamRequestHandler),
        (r'/students/([a-z]+)/([0-9]+)', resourceParamRequestHandler)
    ])
 
    port = 8888
    app.listen(port)  # assigning the app to listen to port 8888
    print(f"Application is ready and listening on port {port}")  # printing put the message to the console

    tornado.ioloop.IOLoop.current().start()  # Keeps this app running