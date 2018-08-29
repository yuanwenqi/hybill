import DataLoaderService

a = DataLoaderService.DataLoaderService()
data = a.createDataSetsWithElements(100,"name","age")
for i in data:
    print(i)
