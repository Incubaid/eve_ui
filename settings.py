MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'apitest'

DOMAIN = {
    'people': {
        'item_title': 'people',
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'name'
        },
        'schema': {
            'name': {
                'type': 'string',
                'maxlength': 50,
                'unique': True
            },
            'email': {
                'type': 'string',
                'regex': '^\S+@\S+$'
            },
            'location': {
                'type': 'dict',
                'schema': {
                    'address': {'type': 'string'},
                    'city': {'type': 'string'}
                }
            },
            'born': {'type': 'datetime'}
        }
    },
}

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
X_DOMAINS = '*'
MONGO_QUERY_BLACKLIST = []
