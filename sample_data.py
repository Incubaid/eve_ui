from gevent import monkey
monkey.patch_all()
import gevent

import requests, time
before = time.time()

data = [
    {'name': 'Jo De Boek', 'email': 'jo@codescalers.com'},
    {'name': 'Reem', 'email': 'reem@codescalers.com'},
    {'name': 'Sherif', 'email': 'sherif@codescalers.com'},
    {'name': 'Hendrik', 'email': 'hendrik@codescalers.com', 'born': 1982},
    {'name': 'KDS', 'email': 'kds@codescalers.com'},
    {'name': 'Jan', 'email': 'jan@codescalers.com'},
    {'name': 'Rob', 'email': 'rob@codescalers.com'},
    {'name': 'Jonas', 'email': 'Jonas@codescalers.com'},
    {'name': 'Sarah', 'email': 'Sarah@codescalers.com'},
    {'name': 'Mohab', 'email': 'mohab@codescalers.com'},
    {'name': 'Majik', 'email': 'majid@codescalers.com'},
    {'name': 'Mahmoud Ali', 'email': 'mahmoudali@codescalers.com'},
    {'name': 'Omnia', 'email': 'omnia@codescalers.com'},
    {'name': 'Tamer', 'email': 'tamer@codescalers.com'},
    {'name': 'Karim Sayed', 'email': 'ksayed@codescalers.com'},
    {'name': 'Youssef', 'email': 'Youssef@codescalers.com'},
    {'name': 'Hazem', 'email': 'Hazem@codescalers.com'},
    {'name': 'Nabil', 'email': 'nabil@codescalers.com'},
    {'name': 'Nayer', 'email': 'nayer@codescalers.com'},
    {'name': 'Heba', 'email': 'heba@codescalers.com'},
    {'name': 'Mogon', 'email': 'mogon@codescalers.com'},
    {'name': 'Sameh', 'email': 'sameh@codescalers.com'},
    {'name': 'Other mahmoud', 'email': 'other-mahmoud@codescalers.com'},
    {'name': 'Galal', 'email': 'galal@codescalers.com'},
    {'name': 'bishoy', 'email': 'bishoy@codescalers.com'},
    {'name': 'david', 'email': 'david@codescalers.com'},
]

gevent.joinall([gevent.spawn(requests.post, 'http://localhost:5000/people', data=d) for d in data])

print time.time() - before