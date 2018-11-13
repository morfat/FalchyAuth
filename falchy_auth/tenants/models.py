

from falchy.db.models import Base
from sqlalchemy import Column, String, Boolean, ForeignKey


class Tenant(Base):
    name = Column(String(100), nullable = False,unique = True) #change to per application
    is_super_tenant = Column(Boolean, default = False)
    application_id = Column(String(50), ForeignKey('applications.id') , nullable = False)
    business_mode = Column(String(10), nullable = False,default = 'B2C') #B2B or B2C
    auth_username_field =  Column(String(100), nullable = True) #if not give, the one from app is preferred
    

  



    