from ROOT import TFile, TTree

def find_pairs(particles):
    num_particles = len(particles)
    #print(num_particles)
    pairs = []
    print(range(4,4))
    for first in range(0, num_particles):
        for second in range(first + 1, num_particles):
            print("im here")
            pairs.append(None)
    print("pair size" + str(len(pairs)))
    return pairs

if __name__ == "__main__":
    find_pairs([])
    f = TFile("events.root")
    t = f.Get("events")
    nEvents = t.GetEntries()
    print "Number of events = " + str(nEvents)
    nBytes = t.GetEntry(0)
    assert nBytes>0, "read zero bytes from TTree"
    nParticles = t .nPart
    print "Number of particles = " + str(nParticles)
