import asyncio
from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorClient




class MongoModel():
    def __init__(self) -> None:
        self.client = AsyncIOMotorClient(host='localhost', port=27017)
        self.db = self.client['my_mongo_db'] # змінити на своє 
        self.time = datetime.now().strftime("%Y-%M-%D %H:%M:%S")


    async def create_db(self, name_db: str, table_name: str):
       await self.db[name_db].insert_one({
           "table_name": table_name,
           "create_time": self.time,
           "items": []      
       })
    
    async def add_item(self, name_db: str, table_name: str, items_data: dict):
       await self.db[name_db].update_one(
           {"table_name": table_name},
           {
               "$push": {
                   "items": items_data
               }
           }, upsert=True
       )
       print('Create')
       
my_dict = {
    "name": 'mac_book',
    "count": 5,
    "description": 'new'
}       


async def main():
    a = MongoModel()
    # await a.create_db(name_db='testmongoclass', table_name='table001')
    await a.add_item(name_db='test', table_name='table001', items_data=my_dict)

    


asyncio.run(main())