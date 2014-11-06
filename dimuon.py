from ROOT import TFile, TTree

class FourMomentum:
    def __init__(self, e,px,py,pz):
        pass
    def mass(self):
        return 0.0

def find_pairs(particles):
    num_particles = len(particles)
    pairs = []
    for i_first in xrange (num_particles):
        particle_a = particles[i_first]
        for i_second in xrange(i_first + 1, num_particles):
            particle_b = particles[i_second]
            if particle_a.q + particle_b.q == 0:
                pairs.append(particle_a, particle_b)
    return pairs

if __name__ == "__main__":

    f = TFile("events.root")
    t = f.Get("events")
    nEvents = t.GetEntries()
    print "Number of events = " + str(nEvents)
    nBytes = t.GetEntry(0)
    assert nBytes>0, "read zero bytes from TTree"
    nParticles = t .nPart
    print "Number of particles = " + str(nParticles)
