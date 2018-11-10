

from falchy.core import middlewares

from ..tenants.models import Tenant
from ..sites.models import Site

from ..applications.models import Application

import falcon

class CustomAuthMiddleWare(middlewares.AuthMiddleWare):
    def __init__(self):
        pass

    def get_secret_key(self,req):
        host_name = req.get_header('Origin')  #req.forwarded_host
        db =  self.get_db(req)

        site = self.get_site(db, host_name)

        if not site:
            raise falcon.HTTPForbidden(description=" Requests from: {origin} not configured.".format( origin = host_name ) )

        tenant = self.get_authenticated_tenant(db, site.get("tenant_id") )
        application = self.get_authenticated_app(db, tenant.get("application_id") )

        #add the tenant and application to context
        req.context["authenticated_application"] = application
        req.context["authenticated_tenant"] = tenant
        return application.get("signing_secret")
    
    def get_site(self,db, host_name):
        return db.objects( Site.all() ).filter(host_name__eq=host_name).fetch_one()
    
    def get_authenticated_tenant(self,db, tenant_id):
        return db.objects( Tenant.get(tenant_id) ).fetch_one()

    def get_authenticated_app(self,db,application_id):
        return db.objects( Application.get(application_id ) ).fetch_one()




