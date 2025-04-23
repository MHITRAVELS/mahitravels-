import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print("Open this URL in your web browser to view the website")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever() 