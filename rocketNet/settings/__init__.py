from .production import *
try:
    from local.settings import *
    
except ImportError:
    pass