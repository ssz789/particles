from dimuon import find_pairs

def test_zero_particles():
    particles = []
    pairs = find_pairs(particles)
    assert len(pairs)==0

def test_one_particle():
    particles = [None]
    pairs = find_pairs(particles)
    assert len(pairs)==0

def test_two_particle():
    particles = [None,None]
    pairs = find_pairs(particles)
    assert len(pairs)==1


def test_5_particle():
    particles = [None,None,None,None,None]
    pairs = find_pairs(particles)
    assert len(pairs)==10


