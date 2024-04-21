# initialize the app and connect to the database
import pymongo
client = pymongo.MongoClient("mongodb+srv://n26110320:dsLIc40TeklfczEv@cluster0205.2thmpz6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0205")
db = client.BioSignal
collection = db.PPG
print("Database connected")

# results = collection.insert_many([
  {
    "name": "Liam",
    "gender": "male",
    "data": [5, 7, 9, 6, 8, 10, 12, 11, 13, 14],
    "sampling_rate": 60,
    "time": "2024-03-24T08:15:30+08:00"
  },
  {
    "name": "Olivia",
    "gender": "female",
    "data": [12, 14, 11, 15, 13, 16, 18, 17, 19, 20],
    "sampling_rate": 60,
    "time": "2024-03-24T09:45:22+08:00"
  },
  {
    "name": "Noah",
    "gender": "male",
    "data": [18, 16, 19, 17, 20, 22, 24, 21, 23, 25],
    "sampling_rate": 60,
    "time": "2024-03-24T10:05:10+08:00"
  },
  {
    "name": "Emma",
    "gender": "female",
    "data": [22, 24, 21, 23, 25, 26, 28, 27, 29, 30],
    "sampling_rate": 60,
    "time": "2024-03-24T11:30:45+08:00"
  },
  {
    "name": "Oliver",
    "gender": "male",
    "data": [27, 29, 26, 28, 30, 31, 33, 32, 34, 35],
    "sampling_rate": 60,
    "time": "2024-03-24T12:50:05+08:00"
  },
  {
    "name": "Mia",
    "gender": "female",
    "data": [32, 34, 31, 33, 35, 36, 38, 37, 39, 40],
    "sampling_rate": 60,
    "time": "2024-03-24T13:15:55+08:00"
  },
  {
    "name": "Jackson",
    "gender": "male",
    "data": [37, 39, 36, 38, 40, 41, 43, 42, 44, 45],
    "sampling_rate": 60,
    "time": "2024-03-24T14:25:30+08:00"
  },
  {
    "name": "Sophia",
    "gender": "female",
    "data": [42, 44, 41, 43, 45, 46, 48, 47, 49, 50],
    "sampling_rate": 60,
    "time": "2024-03-24T15:40:20+08:00"
  },
  {
    "name": "Aiden",
    "gender": "male",
    "data": [47, 49, 46, 48, 50, 51, 53, 52, 54, 55],
    "sampling_rate": 60,
    "time": "2024-03-24T16:55:35+08:00"
  },
  {
    "name": "Isabella",
    "gender": "female",
    "data": [52, 54, 51, 53, 55, 56, 58, 57, 59, 60],
    "sampling_rate": 60,
    "time": "2024-03-24T17:05:50+08:00"
  },
  {
    "name": "Lucas",
    "gender": "male",
    "data": [57, 59, 56, 58, 60, 61, 63, 62, 64, 65],
    "sampling_rate": 60,
    "time": "2024-03-24T18:20:15+08:00"
  },
  {
    "name": "Charlotte",
    "gender": "female",
    "data": [62, 64, 61, 63, 65, 66, 68, 67, 69, 70],
    "sampling_rate": 60,
    "time": "2024-03-24T19:35:05+08:00"
  },
  {
    "name": "Ethan",
    "gender": "male",
    "data": [67, 69, 66, 68, 70, 71, 73, 72, 74, 75],
    "sampling_rate": 60,
    "time": "2024-03-24T20:45:22+08:00"
  },
  {
    "name": "Amelia",
    "gender": "female",
    "data": [72, 74, 71, 73, 75, 76, 78, 77, 79, 80],
    "sampling_rate": 60,
    "time": "2024-03-24T21:50:40+08:00"
  },
  {
    "name": "Logan",
    "gender": "male",
    "data": [77, 79, 76, 78, 80, 81, 83, 82, 84, 85],
    "sampling_rate": 60,
    "time": "2024-03-24T22:55:30+08:00"
  },
  {
    "name": "Harper",
    "gender": "female",
    "data": [82, 84, 81, 83, 85, 86, 88, 87, 89, 90],
    "sampling_rate": 60,
    "time": "2024-03-24T23:15:45+08:00"
  },
  {
    "name": "James",
    "gender": "male",
    "data": [87, 89, 86, 88, 90, 91, 93, 92, 94, 95],
    "sampling_rate": 60,
    "time": "2024-03-25T00:25:10+08:00"
  },
  {
    "name": "Evelyn",
    "gender": "female",
    "data": [92, 94, 91, 93, 95, 96, 98, 97, 99, 100],
    "sampling_rate": 60,
    "time": "2024-03-25T01:30:20+08:00"
  },
  {
    "name": "Benjamin",
    "gender": "male",
    "data": [97, 99, 96, 98, 100, 101, 103, 102, 104, 105],
    "sampling_rate": 60,
    "time": "2024-03-25T02:40:05+08:00"
  },
  {
    "name": "Lily",
    "gender": "female",
    "data": [102, 104, 101, 103, 105, 106, 108, 107, 109, 110],
    "sampling_rate": 60,
    "time": "2024-03-25T03:50:30+08:00"
  }
])

# result = collection.insert_one({
#     "name": "May",
#     "email": "byebye@gmail.com",
#     "password": "seeyou",
#     "level": 1
# })

print(results.inserted_ids)