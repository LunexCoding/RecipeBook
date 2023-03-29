import uuid


class IDGenerator:
    def getID(self):
        return str(uuid.uuid4())


g_IDGenerator = IDGenerator()
