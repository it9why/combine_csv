#!/usr/bin/env python3
"""
Simple HTTP server for CSV Combiner offline tool.
Run this script to serve the HTML file locally.
"""

import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Custom log format
        sys.stderr.write(f"[HTTP] {self.address_string()} - {format % args}\n")

def main():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server starting on http://localhost:{PORT}")
        print(f"Serving files from: {DIRECTORY}")
        print("Press Ctrl+C to stop the server")
        print("\nAccess the CSV Combiner at: http://localhost:8080/index.html")
        print("The tool works completely offline - no internet required.")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()