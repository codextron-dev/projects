from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from socket import gethostbyname, gethostname

ip = gethostbyname(gethostname())

server = ThreadingHTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)

print(f"Open http://{ip}:8000 on this device or another device on your Wi-Fi")

server.serve_forever()
