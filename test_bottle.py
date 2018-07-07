import json
from bottle import run, request, response, Bottle

# import pymysql.cursors
# from datetime import datetime

# connection = pymysql.connect(host='localhost',
#                              user='administrador',
#                              password='y2kalce04',
#                              db='snomed',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)


config_file = open('config.json')
config_data = json.load(config_file)
pth_xml = config_data["paths"]["xml"]

app = Bottle()


@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route('/examples', method=['OPTIONS', 'GET'])
def examples():
    if request.method == 'OPTIONS':
        return {'aaaa'}
    else:
        return {'examples': [{
            'id': 1,
            'name': 'Foo'}, {
            'id': 2,
            'name': 'Bar'}
        ]}


@app.route('/snomed', method='GET')
def recipe_show():
    term = request.query.term
    criterio = request.query.criterio
    if "" != term:
        print(term)
        data = [
            {
                'id': 1,
                'name': 'Leoncio Prado'
            }, {
                'id': 2,
                'name': 'Manuel Prado'
            }
        ]
        result = {'status': True, 'data': data}
        return result
    else:
        return {"status": False, "error": "show called without a filename"}


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=8080,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))
