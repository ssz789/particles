from dimuon import find_pairs, FourMomentum
from nose.tools import assert_equal 


def test_zero_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs)==0

def test_one_particle():
    partciles = [None]
    pairs = find_pairs(particles)
    assert len(pairs)==0

def test_two_particle():
    partciles = [None,None]
    pairs = find_pairs(particles)
    assert len(pairs)==1

def test_three_particle():
    partciles = [None,None,None]
    pairs = find_pairs(particles)
    assert_equal(len(pairs)),3

def test_two_same_charge():
    pos1 = DummyParticle(+1)
    pos2 = DummyParticle(+1)
    particles = [pos1,pos2]
    pairs = find_pairs(particles)
    asssert_equal(len(pairs),0)

def test_can_create_fourmomentum():
    p=FourMomentum(0,0,0,0)

def test_zero_fourmomentum_has_zero_mass():
    p=FourMomentum(0,0,0,0)
    assert_equal(p.mass(),0.0)
