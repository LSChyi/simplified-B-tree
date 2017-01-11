class LeafNode:
    def __init__(self, value, pid, sid):
        self.value = value
        self.pid = pid
        self.sid = sid

    def rid(self):
        return "{}{}".format(self.pid, self.sid)

    def __str__(self):
        return "{}:{}".format(self.value, self.rid())
