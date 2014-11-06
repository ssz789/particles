from ROOT import TFile, TTree

f = TFile("events.root")
t = f.Get("events")
nEvents = t.GetEntries()
print "Number of events = " + str(nEvents)
nBytes = t.GetEntry(0)
assert nBytes>0, "read zero bytes from TTree"
