# flake8: noqa
from pypi_mobans._version import __version__
from pypi_mobans._version import __author__
from lml.plugin import PluginInfo


@PluginInfo('pypi', tags=['setupmobans', 'pypi', 'pypimobans'])
class Pypkg():
    def __init__(self):
        __package_path__ = os.path.dirname(__file__)
        self.resources_path = os.path.join(
            __package_path__, "resources")