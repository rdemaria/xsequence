"""
Module conversion_utils.conv_utils
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module containing accelerator dependent utility functions.
"""

import xsequence.elements_dataclasses as xed
from cpymad.madx import Madx
import at


def create_cpymad_from_file(sequence_path, energy, particle_type='electron', logging=True):
    if logging:
        madx = Madx(command_log='log.madx')
    else:
        madx = Madx()

    madx.option(echo=False, info=False, debug=False)
    madx.call(file=sequence_path)
    madx.input('SET, FORMAT="25.20e";')
    madx.command.beam(particle=particle_type, energy=energy)
    return madx


def create_pyat_from_file(file_path):
    ring = at.load.matfile.load_mat(file_path, key='ring')
    ring = at.Lattice(ring)
    return ring

def get_id_data(id_class=xed.ElementID, **kwargs):
    return id_class(**{k:kwargs[k] for k in id_class.INIT_PROPERTIES if k in kwargs})
        
def get_parameter_data(parameter_class=xed.ElementParameterData, **kwargs):
    return parameter_class(**{k:kwargs[k] for k in parameter_class.INIT_PROPERTIES if k in kwargs})
        
def get_position_data(position_class=xed.ElementPosition, **kwargs):
    return position_class(**{k:kwargs[k] for k in position_class.INIT_PROPERTIES if k in kwargs})

def get_aperture_data(aperture_class=xed.ApertureData, **kwargs):
    return aperture_class(**{k:kwargs[k] for k in aperture_class.INIT_PROPERTIES if k in kwargs})

def get_pyat_data(pyat_class=xed.PyatData, **kwargs):
    return pyat_class(**{k:kwargs[k] for k in pyat_class.INIT_PROPERTIES if k in kwargs})
