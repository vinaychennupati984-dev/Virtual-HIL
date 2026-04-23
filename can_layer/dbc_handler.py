import cantools

class DBCHandler:
    def __init__(self, dbc_file):
        self.db = cantools.database.load_file(dbc_file)

    def encode(self, message_name, signals):
        msg = self.db.get_message_by_name(message_name)
        return msg.encode(signals)

    def decode(self, message_name, data):
        msg = self.db.get_message_by_name(message_name)
        return msg.decode(data)