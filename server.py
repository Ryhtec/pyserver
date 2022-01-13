#import inbuilt module from http library
from http.server import  HTTPServer, BaseHTTPRequestHandler

#class to hold the server

class WebServer(BaseHTTPRequestHandler):
    #inbuilt method do_get inherited from the class
    #method runs when get request is received

    def do_GET(self):

        #check path if is a forward slash i.e index page
        if self.path == '/':

            #select path to index.html file
            self.path = '/index.html'

        #try to read the file requested    
        try:
            #read requested file
            file_to_open = open(self.path[1:]).read()



            #200 response is successful
            self.send_response(200)


         #for error if file cant be read   
        except:
            file_to_open = "File not found"

            #404 for file not found
            self.send_response(404)


        self.end_headers()

        #write content of files to screen
        #convert text file to byte
        self.wfile.write(bytes(file_to_open,'utf-8'))

#httpd httpdameion program that runs on background contains the localhost and port

httpd = HTTPServer(('localhost',8000),WebServer)

#the server to run unless closed by user
httpd.serve_forever()
  