#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    lookup = {}
    for i in range(length):
        # print(f"tickets[i].destination: {tickets[i].destination}")
        lookup[tickets[i].source] = tickets[i].destination
    
    # lookup['NONE'] represents our final destination
    # create a while loop and append to route until the destination is reached
    route = [lookup['NONE']]
    while route[len(route) - 1] is not 'NONE':
        route.append(lookup[route[len(route)-1]])

    return route


# # Reconstruct long test to debug
# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#             "SLC", "PIT", "ORD", "NONE"]
# result = reconstruct_trip(tickets, 10)
# print(f"Expected: {expected}\n")
# print(f"My result: {result}")