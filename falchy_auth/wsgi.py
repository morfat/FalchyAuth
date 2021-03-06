import falcon


from falchemy_rest import middlewares , media_handlers
from .common.middlewares import CustomAuthMiddleWare

from .settings import DB_ENGINE #, OAUTH_SECRET_KEY


from .urls import routes

def create_application():
    application = falcon.API(media_type='application/json',
                             middleware = [ middlewares.CORSMiddleWare(), 
                                            middlewares.CoreMiddleWare( DB_ENGINE ), 
                                            CustomAuthMiddleWare()
                                           ]
                            )


    #have our custom json handler here
    handlers = falcon.media.Handlers({
    'application/json': media_handlers.CustomJSONHandler(),
    })

    #register the custom handler here
    #app.req_options.media_handlers=handlers
    application.resp_options.media_handlers = handlers

    #add routes
    for route in routes:
        #print (route)
        application.add_route(*route)

    return application



application = create_application()

