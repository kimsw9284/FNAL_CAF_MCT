import ROOT
from array import array

threshold = array('d', [-0.993,-0.906,-0.854,-0.798,-0.759,-0.699,-0.646,-0.595,-0.552,-0.502,-0.451,-0.402,-0.352,-0.303,-0.297]) #write the different thresholds here

efficiency = array('d', [0.7134,0.7860,0.7869,0.7856,0.8127,0.8164,0.8224,0.8563,0.8606,0.8787,0.8566,0.8924,0.8586,0.8964,0.8750]) #write efficiency values

efficiency_error = array('d', [0.0202,0.0183,0.0183,0.0184,0.0174,0.0173,0.0171,0.0157,0.0155,0.0146,0.0156,0.0138,0.0156,0.0136,0.0147]) #Write the efficiency errors

threshold_error = array('d', [0.0] * len(threshold))
ROOT.gStyle.SetOptStat(0)

canvas = ROOT.TCanvas("canvas","Efficiency vs Threshold", 800,700)

canvas.SetTicks(1,1)
canvas.SetFrameLineWidth(2)

canvas.SetTicks(1, 1)
graph = ROOT.TGraphErrors(len(threshold),threshold,efficiency,threshold_error,efficiency_error)

graph.SetTitle("")

graph.SetMarkerStyle(20)
graph.SetMarkerSize(1.3)
graph.SetMarkerColor(ROOT.kBlue + 1)

graph.SetLineColor(ROOT.kBlack)
graph.SetLineWidth(2)

graph.GetXaxis().SetTitle("Threshold")
graph.GetYaxis().SetTitle("Efficiency")

graph.GetXaxis().SetTitleSize(0.04)
graph.GetYaxis().SetTitleSize(0.04)
graph.GetYaxis().SetTitleOffset(1.2)

graph.GetYaxis().SetRangeUser(0.6, 1.0)

graph.Draw("AP")
canvas.SaveAs("beforeAug24_efficiency_vs_threshold.png")
