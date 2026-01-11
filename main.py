from fashion.api.fastapi.services import app
from fashion.api.fastapi.services import *
from fashion.persistance.cnt.default_conn_provider import DefaultConnectionProvider
from fashion.persistance.repository import Repository
from fashion.tools.descriptor.model_descriptor_serializer import ModelDescriptorSerializer
from fashion.cache import acache

def init_persistance_layer():
    pooler = DefaultConnectionProvider(usr='fashion', pwd='fashion', schema='FASHION')
    mds = ModelDescriptorSerializer()
    md = mds.load_descriptor('fashion/tools/fashion_mapping.json')
    md.compute_inverted_relations()
    rep = Repository(md, pooler)
    return rep


@app.on_event("startup")
def startup_worker():
    rep = init_persistance_layer()
    acache.set_repository(rep)
    print('Welcome to fashion backend')


@app.on_event("shutdown")
def shutdown_worker():
    print('Thank you for using fashion backend')