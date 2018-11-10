

from falchy.db.models import Base,HasTenantMixin ,utc_pk

from sqlalchemy import Column, String, Boolean, ForeignKey, UniqueConstraint

                       
class Client(HasTenantMixin,Base):
    name = Column(String(100), nullable = False)
    #is_first_party = Column(Boolean, default = False)
    organization_id = Column(String(50), ForeignKey('organizations.id'), nullable = True)
    description = Column(String(150), nullable = True)
    client_id = Column(String(50), nullable = False,  unique = True, default = utc_pk)
    client_secret = Column(String(100), nullable = True)
    web_origins = Column(String(100), nullable = True)
    #auth_call_back_urls = Column(String(100), nullable = True)
    is_active = Column(Boolean, default = True)
    #is_confidential = Column(Boolean, default = False) #means cient can handle passwords for users
    client_type = Column(String(100)) 

    __table_args__ =  ( UniqueConstraint('tenant_id','organization_id', 'name', name='_organization_client'),
                       )

    @classmethod
    def get(cls,pk):
        return cls.all().where(cls.client_id == pk)
        







    