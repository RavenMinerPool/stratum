import weakref
from twisted.internet import reactor

class ConnectionRegistry(object):
    __connections = weakref.WeakKeyDictionary()
    
    @classmethod
    def add_connection(cls, conn):
        cls.__connections[conn] = True

    @classmethod
    def remove_connection(cls, conn):
        try:
            del cls.__connections[conn]
        except:
            print "Warning: Cannot remove connection from ConnectionRegistry"  
    
    @classmethod
    def iterate(cls):
        return cls.__connections.iterkeyrefs()
        
def dump_connections():
    for x in ConnectionRegistry.iterate():
        c = x()
        c.transport.write('cus')
        print '!!!', c
    reactor.callLater(5, dump_connections)
    
#reactor.callLater(0, dump_connections)        