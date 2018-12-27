

class Athlete:

    def __init__(self, value = 0):
        self.thing = value

    def how_big(self):
        return len(self.thing)

    def __init__(self, a_name, a_dob=None, a_time=[]):
        self.name = a_name
        self.dob = a_dob
        self.time = a_time

    def add_time(self, times):
        self.time.append(times)

    def add_times(self, list_of_times):
        self.time.extend(list_of_times)
