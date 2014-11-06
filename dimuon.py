from ROOT import TFile
from ROOT import TTree

class particle:
    def __init__(self, charge, qpt, E):
        self.charge = charge
        self.qpt = qpt
        self.E = E
    def charge(self):
        return self.charge

class p4momentum:
    def __init__(self, e, px, py, pz):
        self.e = e
        self.px = px
        self.py = py
        self.pz = pz

    def mass(self):
        e = self.e
        px = self.px
        py = self.py
        pz = self.pz
        return (e*e - px*px - py*py - pz*pz)**(0.5)
 
    def invmass(self, other):
        e = self.e   + other.e
        px = self.px + other.px
        py = self.py + other.py
        pz = self.pz + other.pz
        return (e*e - px*px - py*py - pz*pz)**(0.5)

def find_pairs(particles):
    num_particles = len(particles)
    #print(num_particles)
    pairs = []
    #print(range(4,4))
    for first in range(0, num_particles):
        for second in range(first + 1, num_particles):
            #print("im here")
            if particles[first].charge() == -particles[second].charge():
                pairs.append([first, second])
    #print("pair size" + str(len(pairs)))
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
