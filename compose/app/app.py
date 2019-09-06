import os

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
bind_port = int(os.environ['BIND_PORT'])


@app.route('/')
def hello():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return f'Hola desde Redis:Almacen de datos en memoria, han visitado un total de {total_hits} veces esta pagina web </b> <h2>"hola mundo"</h2>  .'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=bind_port)
