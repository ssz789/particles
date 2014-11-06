from ROOT import TFile, TTree

f = TFile("events.root")
t = f.Get("events")
