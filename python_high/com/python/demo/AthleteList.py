from python_high.com.python.demo.AthleteTest import sanitize


class AthleteList(list):

    def __init__(self, a_name, a_dob = None, a_time = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_time)

    def top3(self):
        return sorted(set([sanitize(s) for s in self]))[0:3]
