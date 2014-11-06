from ROOT import TFile, TTree

def find_pairs(particles):
    num_particles = len(particles)
    pairs = []
    for 1_first in xrange (num_particles):
        for 1_second in xrange(1_first + 1, num_particles):
            pairs.append(None)
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
