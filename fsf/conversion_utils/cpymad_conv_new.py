"""
Module conversion_utils.cpymad_conv
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a Python3 module with functions for importing and exporting elements from and to cpymad
"""

DIFF_ATTRIBUTE_MAP_CPYMAD = {
                        'length': 'l', 
                        'location': 'at', 
                        'reference_element': 'from', 
                        'voltage': 'volt', 
                        'frequency': 'freq', 
                        'calibration': 'calib',
                        'aperture_size':'aperture',
                        'aperture_type':'apertype',
                        }

INVERT_DIFF_ATTRIBUTE_MAP_CPYMAD = {v: k for k, v in DIFF_ATTRIBUTE_MAP_CPYMAD.items()}


def attr_mapping_from_cpymad(cpymad_element):
    for key in DIFF_ATTRIBUTE_MAP_CPYMAD:
        try: cpymad_element[key] = cpymad_element.pop(DIFF_ATTRIBUTE_MAP_CPYMAD[key]) 
        except: KeyError 
    if 'frequency' in cpymad_element:
        cpymad_element['frequency'] *= 1e6
        cpymad_element['voltage'] *= 1e6
    return cpymad_element


def from_cpymad(xs_cls, cpymad_element, name=None, aperture=False):
    if not isinstance(cpymad_element, dict):
        name = cpymad_element.name
        elemdata={'base_type':cpymad_element.base_type.name}
        for parname, par in cpymad_element.cmdpar.items():
            elemdata[parname]=par.value
        cpymad_element = elemdata
    mapped_attr = attr_mapping_from_cpymad(cpymad_element)
    return xs_cls(name, **mapped_attr)


def attr_mapping_to_cpymad(element_dict):
    for key in DIFF_ATTRIBUTE_MAP_CPYMAD:
        try: element_dict[DIFF_ATTRIBUTE_MAP_CPYMAD[key]] = element_dict.pop(key) 
        except: KeyError 
    if 'freq' in element_dict:
        element_dict['freq'] /= 1e6
        element_dict['volt'] /= 1e6
    return element_dict


def to_cpymad(element, madx):
    mapped_attr = attr_mapping_to_cpymad(element.get_dict())
    base_type = element.__class__.__name__
    madx_base_type = base_type.lower()
    if base_type == 'RectangularBend':
        mapped_attr['l'] = element._chord_length
        mapped_attr['e1'] = element._rbend_e1
        mapped_attr['e2'] = element._rbend_e2
        madx_base_type = 'rbend'
    if 'reference' in mapped_attr:
        mapped_attr.pop('reference')
    return madx.command[madx_base_type].clone(element.name, **mapped_attr)
