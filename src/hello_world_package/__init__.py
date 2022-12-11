# __init__.py
# This is executed upon running "import hello_world_package"

# define behavior for "from hello_world_package import *":
__all__ = ['hello', 'calculate']

# directly import submodules when using "import hello_world_package":
from hello_world_package import hello  # this can be called as "hello_world_package.hello"
from hello_world_package import calculate
