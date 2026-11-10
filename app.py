import http.server
import json
import os

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {"status": "healthy", "version": "1.0"}
            self.send_response(200)
        else:
            response = {"message": "Trading Support Lab"}
            self.send_response(200)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = http.server.HTTPServer(("0.0.0.0", port), Handler)
    print(f"Application running on port {port}", flush=True)
    server.serve_forever()
