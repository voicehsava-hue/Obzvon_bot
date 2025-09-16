    import http.server
    import ssl
    import socketserver

    # Задайте порт и пути к файлам сертификата и ключа
    PORT = 4000  # HTTPS по умолчанию использует порт 443
    CERT_FILE = 'cert.pem'
    KEY_FILE = 'key.pem'

    class MyHandler(http.server.SimpleHTTPRequestHandler):
        pass

    # Настройка SSL/TLS контекста
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    # Создание сервера с SSL-контекстом
    # Можно использовать SocketServer.TCPServer и добавить обработчик контекста в обертку SSLEngine
    # Или использовать http.server.HTTPServer, который сам поддерживает SSL контекст
    # В данном примере используем HTTPServer
    httpd = http.server.HTTPServer(("", PORT), MyHandler)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"HTTPS сервер запущен на порту {PORT}")

    # Запуск сервера
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
