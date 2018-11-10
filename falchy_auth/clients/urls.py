

from .resources import *

routes = [
    ('',ListCreateClients() ),
    ('/{pk}',RetrieveUpdateClient() ),
    ('/generateSecret',GenerateClientSecret() ),

]

