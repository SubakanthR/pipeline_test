import http.server
import socketserver
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Force the server to look for index.html if the main page is requested
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

print(f"Starting server natively on port {PORT}...")
# This setting avoids the 'address already in use' crash if you restart quickly
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Server is actively running. Open http://localhost:{PORT} in your browser.")
    print("Press Ctrl+C inside this terminal window to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped cleanly.")
