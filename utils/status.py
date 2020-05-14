
class Status():
    def __init__(self,code,message,data,count):
        self.code = code
        self.message = message
        self.data = data
        self.count = count

    def success(self):

        return {'code':self.code,'message':self.message,'count':self.count,'data':self.data}

