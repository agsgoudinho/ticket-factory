import Pyro4

uri = input("URI Object? ").strip()
resp = "S"

ticket_factory = Pyro4.Proxy(uri)

while resp == "S":
    print(ticket_factory.tickets())
    resp = input("Quer outro ticket? Digite S ou N: ").strip()
    if resp == 'N':
        print("Volte sempre")
    elif resp != 'S':
        print("Resposta invalida, execucao encerrada!")