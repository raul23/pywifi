import os
import pywifi

__version__ = '0.1.0a1'
__test_version__ = '0.1.0a1'  # For debugging purposes
__package_name__ = __package__
__project_name__ = pywifi.__name__.split('.')[-1]
__project_dir__ = os.path.expanduser(f'~/.{__project_name__}')
