#       ___                                                     ___
#     //   ) )                                                //   ) )
#    //___/ /         __  ___ / __      ___       __         //___/ /  __      ___
#   / ____ / //   / /  / /   //   ) ) //   ) ) //   ) )     / ____ / //  ) ) //   ) ) \\ / / //   / /
#  //       ((___/ /  / /   //   / / //   / / //   / /     //       //      //   / /   \/ / ((___/ /
# //            / /  / /   //   / / ((___/ / //   / /     //       //      ((___/ /    / /\     / /
#          ____/ /                                                                         ____/ /
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ A simple Python based web proxy created for CS33032.
#
# Author: Lydia MacBride 💫
#
# Note to self: Be careful when messing with your proxy settings so you don't spend an hour
#               troubleshooting *mysterious* network issues when done working on this.
#
# ✨ Requirements ✨
# TODO: 1.  Respond to HTTP & HTTPS requests and should display each request on a management console.
#        ↪  It should forward the request to the Web server and relay the response to the browser.
# TODO: 2.  Handle Websocket connections.
# TODO: 3.  Dynamically block selected URLs via the management console.
# TODO: 4.  Efficiently cache HTTP requests locally and thus save bandwidth.
#        ↪  You must gather timing and bandwidth data to prove the efficiency of your proxy.
# TODO: 5.  Handle multiple requests simultaneously by implementing a threaded server.
#
# 🌱 Stuff To Do 🌱
# TODO: Management Console
# TODO: Handle requests from web browser
# TODO: PROXY SERVER??????
# TODO: Move server to its own script
#

# Imports
import time
import threading
import requests as req
from http.server import BaseHTTPRequestHandler, HTTPServer

# Globals
url = "https://sharpfourth.net"
hostname = "localhost"
port = 8080


# Webserver Class
class Server(BaseHTTPRequestHandler):
    # TODO: Establish tunnel with server
    def do_CONNECT(self):
        print("CONNECT" + self.path)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Python Proxy</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<img src=\"https://c.tenor.com/ftslutYNByMAAAAC/orin-touhou.gif\">", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        print("GET " + self.path)


# Main
if __name__ == "__main__":
    print("Starting Python Proxy ✨")
    # r = req.get(url)
    # print(r.text)

    # Start webServer
    webServer = HTTPServer((hostname, port), Server)
    print("Server started http://%s:%s" % (hostname, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
