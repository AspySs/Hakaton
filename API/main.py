from flask import Flask
from flask import request
import sqlite3
import json

conn = sqlite3.connect('../data.sqlite', check_same_thread=False)
cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_tags/', methods=['GET'])
def get_tgs():
    res = cur.execute("""SELECT DISTINCT * FROM tags""")
    result = res.fetchall()
    return json.dumps(result)

@app.route('/get_text/', methods=['GET'])
def get_txts():
    tag = request.args.get('tag')
    res = cur.execute("SELECT post_id FROM tags WHERE tag = ? ORDER BY date DESC", (tag, ))
    result_id = res.fetchall()
    lst = []
    for i in result_id:
        res = cur.execute("SELECT text FROM posts WHERE id = ?", (i[0], )).fetchone()
        lst.append(res)
    return json.dumps(lst)


if __name__ == '__main__':
    app.run()
