from pymongo import MongoClient

client = MongoClient('localhost', 27017)

lista = client.list_database_names()

if 'teste' in lista:
    client.drop_database('teste')

db = client.get_database('teste')

collection = db.get_collection('pessoa')
data = {
    'nome': 'Artur',
    'idade': 34,
    'curso': 'ciência de dados'
}

collection.insert_one(data)

multi_data = [
    {
        'nome': 'Carlos',
        'idade': 25,
        'curso': 'ciência da computação'
    },
    {
        'nome': 'Judite',
        'idade': 21,
        'curso': 'Análise de sistemas'
    },
    {
        'nome': 'Andreia',
        'idade': 35,
        'curso': 'direito'
    }
]

collection.insert_many(multi_data)

collection.delete_one({'nome': 'Carlos'})

judite = collection.find_one({'nome': 'Judite'})