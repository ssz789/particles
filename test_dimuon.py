from dimuon import find_pairs

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
