import Pyro4


@Pyro4.expose
class TicketFactory(object):

    def tickets(self):
        global cont
        cont += 1
        return "Your ticket: ", cont


cont = 0
daemon = Pyro4.Daemon()
uri = daemon.register(TicketFactory)

print("Ready. Object uri =", uri)
daemon.requestLoop()