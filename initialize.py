
#create all db
import sys

from falchy.db.models import Base
from falchy_auth.settings import DB_ENGINE
from falchy.db.sql import Db 


def init_db():
    from falchy_auth.applications import models
    from falchy_auth.content_types import models
    from falchy_auth.permissions import models
    from falchy_auth.tenants import models
    from falchy_auth.sites import models
    from falchy_auth.organizations import models
    from falchy_auth.clients import models
    from falchy_auth.users import models
    from falchy_auth.apis import models
    from falchy_auth.emails import models
    from falchy_auth.roles import models
    from falchy_auth.teams import models


    Base.metadata.create_all(DB_ENGINE)



def init_app(db, app_name):
    import time
    from falchy_auth.applications.models import Application
    from falchy_auth.tenants.models import Tenant
    from falchy_auth.sites.models import Site
    from falchy_auth.apis.models import API
    from falchy_auth.organizations.models import Organization
    from falchy_auth.users.models import User, OrganizationUser


    auth_username_field = input("Enter App Username field ( email or phone_number ): ")

    is_multitenant_q = input("Is the Application Multitenant ? ( y , n): ")
    tenant_business_mode = input("Business Mode ? ( B2B, B2C): ")
    username = input("Enter Superuser %s: "%(auth_username_field))
    password = input("Enter Superuser Password: ")
    api_name = "Default API {random_time}".format( random_time = str(time.time()).split('.')[0] )
    tenant_name =  "Default Tenant {random_time}".format( random_time = str(time.time()).split('.')[0] )
    app_name =  "Default APP {random_time}".format( random_time = str(time.time()).split('.')[0] )
    organization_name = "Default Organization {random_time}".format( random_time = str(time.time()).split('.')[0] )

    api_uri = input("Default Resource Server URL: ")
    is_multitenant = True if is_multitenant_q == 'y' else False

    
    created_app = db.objects( Application.insert() ).create(**{"auth_username_field": auth_username_field,"name":app_name,"is_multitenant": is_multitenant })

    #create super tenant
    application_id = created_app.get("id")
    created_tenant = db.objects( Tenant.insert() ).create(**{"is_super_tenant": True,"name":tenant_name,"business_mode": tenant_business_mode,
                                            "application_id": application_id
                                            })
   
    
    #create default api
    tenant_id = created_tenant.get("id")
    created_api = db.objects( API.insert() ).create(**{"is_default": True,"name":api_name,"description": "Default Generated",
                                            "uri": api_uri,"tenant_id": tenant_id
                                            })

    #create default site with default domain name
    created_site = db.objects( Site.insert() ).create(**{ "tenant_id": tenant_id, "host_name":"admin.localhost" })

    #create user
    user_d = { "password": password , "is_staff": True, "is_super_user": True,
               "is_active": True, auth_username_field: username,"tenant_id": tenant_id
            }
    created_user = db.objects( User.insert() ).create(**user_d)
    user_id = created_user.get("id")

    User.set_password( db, user_id, password)
    

    #create organization
    if tenant_business_mode == 'B2B':
        created_organization = db.objects( Organization.insert() ).create(**{"name": organization_name,"tenant_id": tenant_id })
        db.objects( OrganizationUser.insert() ).create(**{"is_admin":True,"user_id": user_id, "organization_id": created_organization.get("id") })


#Db Tables

init_db()

# Create new app data

args = sys.argv

try:
    db = Db( DB_ENGINE.connect() )
    transaction = db._connection.begin()

    app_name = args[1]
    init_app(db, app_name)

    transaction.commit()

except IndexError:
    transaction.rollback()
finally:
    db._connection.close()



