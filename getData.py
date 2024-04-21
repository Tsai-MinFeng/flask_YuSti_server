import pymongo

client = pymongo.MongoClient("mongodb+srv://n26110320:dsLIc40TeklfczEv@cluster0205.2thmpz6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0205")
db = client.BioSignal
collection = db.PPG

# 取得資料
datas = collection.find().sort('time',-1).limit(10)
    
# sort = [("level", pymongo.ASCENDING)])
for data in datas:
    print(data)