# -*- coding:utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler())
print("server port is: " + str(httpd.server_port))
httpd.serve_forever()