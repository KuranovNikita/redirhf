from .production import *
try:
    # from .local_settings import *
    from .production import *
    
except ImportError:
    pass