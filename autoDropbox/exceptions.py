class InputError(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg)

