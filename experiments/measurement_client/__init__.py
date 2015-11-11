import gce_interface.interface
import gce_interface.server_codes

import client

from gce_interface.interface import GCEInterface
from gce_interface.server_codes import *
from client import MeasurementClient

def argparsers():
    return [
        #gce_interface.parser,
        client.parser
    ]
