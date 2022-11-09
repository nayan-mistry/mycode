import http.server
import socketserver

def main():
    PORT = 9021

    handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("",PORT), handler)

    print(("serving at port", PORT))

    httpd.serve_forever()

if __name__ == "__main__":
    main()