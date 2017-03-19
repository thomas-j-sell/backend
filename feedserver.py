from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

port_number = 8080

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/rss':
                self.path = "/rss.xml"
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type','application/rss+xml')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()

            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def startServer():
    try:
        server = HTTPServer(('', port_number), myHandler)
        print('Started httpserver on port ', str(port_number))
        server.serve_forever()

    except KeyboardInterrupt:
        server.socket.close()

