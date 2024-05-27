from app.project import app
import logging


if __name__ == '__main__':
    #ssl_cert='certificate.crt'
    #ssl_key='private_key.pem'
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=8080, debug=True)
    #app.run(ssl_context=(ssl_cert, ssl_key),host="0.0.0.0", port=8080)