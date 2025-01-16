from datetime import time

class MyTime(time):
    def __sub__(self, other):
        if not isinstance(other, time):
            raise TypeError("Cannot subtract time from " + type(other))
        return (self.hour - other.hour) * 60 + self.minute - other.minute

    def __str__(self):
        h = self.hour
        m = self.minute
        return (str(h) if h > 9 else ("0" + str(h))) + ":" + (str(m) if m > 9 else ("0" + str(m)))
