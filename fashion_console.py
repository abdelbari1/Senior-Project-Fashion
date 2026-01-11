from fashion.io.data_loader import XLDataLoader
from fashion.persistance.repository import Repository
from fashion.persistance.cnt.default_conn_provider import DefaultConnectionProvider
from fashion.tools.descriptor.model_descriptor_serializer import ModelDescriptorSerializer
from fashion.cache import acache
import time

def init_persistance_layer() -> Repository:
    pooler = DefaultConnectionProvider(usr='fashion', pwd='fashion', schema='fashion')
    mds = ModelDescriptorSerializer()
    md = mds.load_descriptor('fashion/tools/fashion_mapping.json')
    md.compute_inverted_relations()
    rep = Repository(md, pooler)
    return rep

def loading_model_and_data_in_pdb():
    rep = init_persistance_layer()
    xl = XLDataLoader()
    acache.set_repository(rep)
    st = time.time()
    xl.load_default_model(acache, 'fashion/data/tmp/fashion_template.xlsx')
    et = time.time()
    print(f'loading data took: {(et - st)} seconds')
    print('--- -- - D O N E - -- ---')

loading_model_and_data_in_pdb()
