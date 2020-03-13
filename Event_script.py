def get_event_date(event):
    # parse the event log
    return event.date


def current_users(events):
    # sort the event log by the return  of  the event date
    events.sort(key=get_event_date)
    # create a dictionary with the computers
    machines = {}
    # iterate over  the list of  events and check and see if  the computer  is  in the dictionary
    for event in events:
        # if the  computer is not in the dictionary add it as a set??
        if event.machine not in machines:
            machines[event.machine] = set()
        # if event type = login  add the user  to the machine  set
        # the tutorial  uses  single = signs instead of  double Oo

        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)

    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [Event("101", "login", "jeffserverspc", "bob"),
          Event("102", "login", "jeffmailspc", "suzy"),
          Event("103", "login", "jeffspc", "jeff"),
          Event("104", "logout", "jeffspc", "jeff"),
          Event("105", "logout", "jeffmailspc", "suzy"),
          Event("107", "login", "server6", "james")
          ]

users = current_users(events)
print(users)
generate_report(users)
