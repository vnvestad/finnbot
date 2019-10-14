import pymongo
import os

class DatabasePipeline(object):

    collection_name = 'items'

    def __init__(self, mongo_server, mongo_port, mongo_db):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server = os.getenv('MONGODB_SERVER'),
            mongo_port = int(os.getenv('MONGODB_PORT')),
            mongo_db = os.getenv('MONGODB_DB')
        )

    def open_spider(self, spider):
        if self.mongo_server:
            self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
            self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        if self.mongo_server:
            self.client.close()

    def process_item(self, item, spider):
        if self.mongo_server:
            self.db[self.collection_name].insert_one(dict(item))
        return item