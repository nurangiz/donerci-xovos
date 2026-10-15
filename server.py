# Donerci Xovos - Python Mahalliy Server
import http.server
import socketserver
import webbrowser

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.html': 'text/html',
})

print(f"Server ishga tushdi: http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer to'xtatildi.")
