#!/usr/bin/env python


import time
import sys
import os
import json
import getCardsWeb
from flask import Flask, request, Response
application = app = Flask('wsgi')

@app.route('/', methods=['GET', 'POST'])
def welcome():
    form = 'Calculate your five cards:<br>' + \
            'Enter a binary sequence of 5 digits with 1 = red and 0 = black<br><br>' + \
            '<form action="" method="POST"><input type="text" name="userSeq"/></form>'

    if request.method == 'POST':
        userSeq = request.form.get('userSeq')
        return form + getCardsWeb.doAll(userSeq) 

    return form

@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")

@app.route('/mongo')
def mongotest():
    from pymongo import Connection
    uri = mongodb_uri()
    conn = Connection(uri)
    coll = conn.db['ts']
    coll.insert(dict(now=int(time.time())))
    last_few = [str(x['now']) for x in coll.find(sort=[("_id", -1)], limit=10)]
    body = "\n".join(last_few)
    return Response(body, content_type="text/plain;charset=UTF-8")

def mongodb_uri():
    local = os.environ.get("MONGODB", None)
    if local:
        return local
    services = json.loads(os.environ.get("VCAP_SERVICES", "{}"))
    if services:
        creds = services['mongodb-1.8'][0]['credentials']
        uri = "mongodb://%s:%s@%s:%d/%s" % (
            creds['username'],
            creds['password'],
            creds['hostname'],
            creds['port'],
            creds['db'])
        print >> sys.stderr, uri
        return uri
    else:
        raise Exception, "No services configured"
    

if __name__ == '__main__':
    app.run(debug=True)
