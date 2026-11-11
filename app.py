import http.server
import json
import os

VERSION = os.environ.get("APP_VERSION", "1.0.0")
HEALTH_STATUS = os.environ.get("HEALTH_STATUS", "healthy")


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": HEALTH_STATUS,
                "version": VERSION
            }
            self.send_response(200 if HEALTH_STATUS == "healthy" else 503)
        else:
            response = {
                "message": "Trading Support Lab",
                "version": VERSION
            }
            self.send_response(200)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = http.server.HTTPServer(("127.0.0.1", port), Handler)
    print(f"Application version {VERSION} running on port {port}", flush=True)
    server.serve_forever()
