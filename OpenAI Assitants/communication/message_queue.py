import queue

class MessageQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def send_message(self, message):
        self.queue.put(message)

    def receive_message(self):
        if not self.queue.empty():
            return self.queue.get()
        else:
            return None