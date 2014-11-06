from dimuon import particle
from dimuon import p4momentum
from dimuon import find_pairs
from nose.tools import assert_equal

def test_zero_p4Momentum():
    t = p4momentum(0,0,0,0)
    assert t.mass() == 0

def test_stationary_p4Momentum():
    t = p4momentum(1,0,0,0)
    assert t.mass() == 1

def test_stationarytimesnothing_p4Momentum():
    t1 = p4momentum(9,1,1,1)
    t2 = p4momentum(0,0,0,0)
    assert_equal(t1.invmass(t2),2)

def test_stationarytimesphoton_p4Momentum():
    t1 = p4momentum(1,0,0,0)
    t2 = p4momentum(1,0,0,0)
    assert_equal(t1.invmass(t2),2)


def test_zero_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs)==0

def test_one_particle():
    particles = [None]
    pairs = find_pairs(particles)
    assert len(pairs)==0
"""
def test_two_particle():
    particles = [None,None]
    pairs = find_pairs(particles)
    assert len(pairs)==1

def test_5_particle():
    particles = [None,None,None,None,None]
    pairs = find_pairs(particles)
    assert len(pairs)==0

def test_3_real_particles():
    particle_list = []
    
    p1 = particle(+1,20,10)
    p2 = particle(-1,2,17)
    p3 = particle(+1,3,12)
    particle_list.append(p1)
    particle_list.append(p2)
    particle_list.append(p3)

    pair_list = find_pairs(particle_list)
    assert pair_list == ([0,1], [1,2])

"""
