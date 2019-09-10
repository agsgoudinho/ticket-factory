import Pyro4


@Pyro4.expose
class TicketFactory(object):
    def __init__(self):
        global cont_server
        if cont_server > 0:
            self.cont_instance = cont_server
        else:
            self.cont_instance = 0

    def tickets(self):
        global cont_server
        self.cont_instance = cont_server
        self.cont_instance += 1
        cont_server = self.cont_instance
        return "Your ticket: ", cont_server


cont_server = 0
daemon = Pyro4.Daemon()
uri = daemon.register(TicketFactory)

print("Ready. Object uri =", uri)
daemon.requestLoop()