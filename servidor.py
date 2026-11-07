#!/usr/bin/env python3
# Servidor local de la Mesa de cartas.
# Agrega los encabezados de aislamiento (COOP/COEP) para que la voz neuronal use varios núcleos del procesador.
import http.server, socketserver, os, sys, webbrowser, threading

PUERTO = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Manejador(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.wasm': 'application/wasm', '.onnx': 'application/octet-stream', '.json': 'application/json', '.js': 'text/javascript'}
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'credentialless')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    def log_message(self, *a): pass

class Servidor(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

url = f'http://localhost:{PUERTO}/'
print(f'Mesa de cartas en {url}  (cerrá esta ventana para apagarla)')
if '--sin-navegador' not in sys.argv:
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
Servidor(('localhost', PUERTO), Manejador).serve_forever()
