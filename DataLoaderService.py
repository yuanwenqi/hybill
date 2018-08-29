import random
class DataLoaderService:
    def __init__(self):
        print("init DataLoaderService")

    def createDataSetsWithElements(self,length,*args):
        data = []
        title = ["id"]
        for i in args:
            title.append(i)
        data.append(title)
        for i in range(length):
            record = [i]
            for element in args:
                record.append(random.randint(0,100))
            data.append(record)
        return data




