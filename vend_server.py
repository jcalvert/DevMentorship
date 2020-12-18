import cherrypy
import json

class VendServer(object):

    #Bonus, make this respect content types!
    @cherrypy.expose
    def inventory(self):
        return json.dumps({'coke': 0, 'sprite': 1, 'lacroix': 3})

    @cherrypy.expose
    def insert_coin(self, coin):
        return json.dumps({"coins": 0})

if __name__ == '__main__':
    cherrypy.quickstart(VendServer())
