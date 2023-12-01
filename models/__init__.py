from models.RCMF_Model import RCMF
from models.RCMF_Model import RCMF_Base
from models.RCMF_Model import RCMF_Base_22K

__factory = {
    'RCMF': RCMF,
    'RCMF_Base': RCMF_Base,
    'RCMF_Base_22K': RCMF_Base_22K
}

def names():
    return sorted(__factory.keys())

def create(name, *args, **kwargs):
    if name not in __factory:
        raise KeyError("Unknown caption model:", name)
    return __factory[name](*args, **kwargs)