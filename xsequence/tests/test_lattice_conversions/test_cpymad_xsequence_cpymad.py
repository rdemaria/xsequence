"""
Module tests.test_lattice_conversions.test_cpymad_xsequence_cpymad
------------------
:author: Felix Carlier (fcarlier@cern.ch)
This is a test module to test consistency for converting back and forth from cpymad.
"""

from xsequence.lattice import Lattice
import pytest
from xsequence.conversion_utils import conv_utils
from pathlib import Path

TEST_SEQ_DIR = Path(__file__).parent.parent / "test_sequences"

@pytest.fixture(scope="module")
def example_cpymad_xsequence_cpymad():
    """
    Create cpymad instance from import and export through xsequence
    
    Returns:
        Old and new twiss tables from cpymad
    """
    madx_lattice = conv_utils.create_cpymad_from_file(str(TEST_SEQ_DIR / "lattice.seq"), 120)
    madx_lattice.command.beam(particle='electron', energy=120)
    madx_lattice.use('l000013')
    xsequence_lattice = Lattice.from_cpymad(madx_lattice, 'l000013')
    madx_lattice_new = xsequence_lattice.to_cpymad()
    madx_lattice_new.command.beam(particle='electron', energy=120)
    madx_lattice_new.use('l000013')
    twiss = madx_lattice.twiss(sequence='l000013')
    twiss_new = madx_lattice_new.twiss(sequence='l000013')
    return twiss, twiss_new

def test_cpymad_xsequence_cpymad_s(example_cpymad_xsequence_cpymad):
    twiss, twiss_new = example_cpymad_xsequence_cpymad
    assert sum(abs(twiss.s - twiss_new.s)) == 0

def test_cpymad_xsequence_cpymad_orbit(example_cpymad_xsequence_cpymad):
    twiss, twiss_new = example_cpymad_xsequence_cpymad
    assert sum(abs(twiss.x - twiss_new.x)) == 0 and\
           sum(abs(twiss.y - twiss_new.y)) == 0

def test_cpymad_xsequence_cpymad_beta(example_cpymad_xsequence_cpymad):
    twiss, twiss_new = example_cpymad_xsequence_cpymad
    assert sum(abs(twiss.betx - twiss_new.betx)) == 0 and\
           sum(abs(twiss.bety - twiss_new.bety)) == 0

def test_cpymad_xsequence_cpymad_disp(example_cpymad_xsequence_cpymad):
    twiss, twiss_new = example_cpymad_xsequence_cpymad
    assert sum(abs(twiss.dx - twiss_new.dx)) == 0 and\
           sum(abs(twiss.dy - twiss_new.dy)) == 0

def test_cpymad_xsequence_cpymad_alfa(example_cpymad_xsequence_cpymad):
    twiss, twiss_new = example_cpymad_xsequence_cpymad
    assert sum(abs(twiss.alfx - twiss_new.alfx)) == 0 and\
           sum(abs(twiss.alfy - twiss_new.alfy)) == 0

def test_cpymad_xsequence_cpymad_phase(example_cpymad_xsequence_cpymad):
    twiss, twiss_new = example_cpymad_xsequence_cpymad
    assert sum(abs(twiss.mux - twiss_new.mux)) == 0 and\
           sum(abs(twiss.muy - twiss_new.muy)) == 0


@pytest.fixture(scope="module")
def example_cpymad_xsequence_cpymad_coll():
    """
    Create cpymad instance from import and export through xsequence from lattice
    with collimators
    
    Returns:
        Old and new twiss tables from cpymad
    """
    madx_lattice = conv_utils.create_cpymad_from_file(str(TEST_SEQ_DIR / "collimators.seq"), 180)
    madx_lattice.command.beam(particle='electron', energy=180)
    madx_lattice.use('ring')
    xsequence_lattice = Lattice.from_cpymad(madx_lattice, 'ring')
    madx_lattice_new = xsequence_lattice.to_cpymad()
    madx_lattice_new.command.beam(particle='electron', energy=180)
    madx_lattice_new.use('ring')
    twiss = madx_lattice.twiss(sequence='ring')
    twiss_new = madx_lattice_new.twiss(sequence='ring')
    return twiss, twiss_new

def test_cpymad_xsequence_cpymad_coll_s(example_cpymad_xsequence_cpymad_coll):
    twiss, twiss_new = example_cpymad_xsequence_cpymad_coll
    assert sum(abs(twiss.s - twiss_new.s)) == 0

def test_cpymad_xsequence_cpymad_coll_orbit(example_cpymad_xsequence_cpymad_coll):
    twiss, twiss_new = example_cpymad_xsequence_cpymad_coll
    assert sum(abs(twiss.x - twiss_new.x)) == 0 and\
           sum(abs(twiss.y - twiss_new.y)) == 0

def test_cpymad_xsequence_cpymad_coll_beta(example_cpymad_xsequence_cpymad_coll):
    twiss, twiss_new = example_cpymad_xsequence_cpymad_coll
    assert sum(abs(twiss.betx - twiss_new.betx)) == 0 and\
           sum(abs(twiss.bety - twiss_new.bety)) == 0

def test_cpymad_xsequence_cpymad_coll_disp(example_cpymad_xsequence_cpymad_coll):
    twiss, twiss_new = example_cpymad_xsequence_cpymad_coll
    assert sum(abs(twiss.dx - twiss_new.dx)) == 0 and\
           sum(abs(twiss.dy - twiss_new.dy)) == 0

def test_cpymad_xsequence_cpymad_coll_alfa(example_cpymad_xsequence_cpymad_coll):
    twiss, twiss_new = example_cpymad_xsequence_cpymad_coll
    assert sum(abs(twiss.alfx - twiss_new.alfx)) == 0 and\
           sum(abs(twiss.alfy - twiss_new.alfy)) == 0

def test_cpymad_xsequence_cpymad_coll_phase(example_cpymad_xsequence_cpymad_coll):
    twiss, twiss_new = example_cpymad_xsequence_cpymad_coll
    assert sum(abs(twiss.mux - twiss_new.mux)) == 0 and\
           sum(abs(twiss.muy - twiss_new.muy)) == 0


