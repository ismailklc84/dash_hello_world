from dash import Dash, html
import redis
import datetime
import os


app = Dash()
application = app.server

redis_instance = redis.StrictRedis(host='redis', port=6379, password='redis-password')
REDIS_HASH_NAME = os.environ.get("DASH_APP_NAME", "app-data")
REDIS_KEYS = {"DATASET": "DATASET", "DATE_UPDATED": "DATE_UPDATED"}

redis_instance.hset(
                REDIS_HASH_NAME, REDIS_KEYS["DATE_UPDATED"], str(datetime.datetime.now())
    )

data_last_updated = redis_instance.hget(
        REDIS_HASH_NAME, REDIS_KEYS["DATE_UPDATED"]
    ).decode("utf-8")

app.layout = html.Div([
    html.Div(children='Hello World'),
    html.Div(children=data_last_updated)
])

@app.server.route("/ping")
def ping():
  return "{status: ok}"


if __name__ == '__main__':
    app.run_server(port=8080)
