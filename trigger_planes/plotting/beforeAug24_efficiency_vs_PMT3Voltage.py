import ROOT
from array import array

voltage = array('d', [1180,1220,1260,1300,1340,1380,1420,1460,1500,1540,1580,1620,1660,1700]) #write the different voltages here

efficiency = array('d', [0.8529,0.8574,0.8780,0.8958,0.8842,0.8563,0.8526,0.8782,0.8762,0.8924,0.9002,0.8845,0.9006,0.9008]) #write efficiency values

efficiency_error = array('d', [0.0158,0.0156,0.0146,0.0137,0.0143,0.0157,0.0158,0.0146,0.0147,0.0138,0.0134,0.0143,0.0133,0.0133]) #Write the efficiency errors

voltage_error = array('d', [0.0] * len(voltage))
ROOT.gStyle.SetOptStat(0)

canvas = ROOT.TCanvas("canvas","Efficiency vs Voltage", 800,700)

canvas.SetTicks(1,1)
canvas.SetFrameLineWidth(2)

canvas.SetTicks(1, 1)
graph = ROOT.TGraphErrors(len(voltage),voltage,efficiency,voltage_error,efficiency_error)

graph.SetTitle("")

graph.SetMarkerStyle(20)
graph.SetMarkerSize(1.3)
graph.SetMarkerColor(ROOT.kBlue + 1)

graph.SetLineColor(ROOT.kBlack)
graph.SetLineWidth(2)

graph.GetXaxis().SetTitle("Voltage [V]")
graph.GetYaxis().SetTitle("Efficiency")

graph.GetXaxis().SetTitleSize(0.04)
graph.GetYaxis().SetTitleSize(0.04)
graph.GetYaxis().SetTitleOffset(1.2)

graph.GetYaxis().SetRangeUser(0.75, 1.0)

graph.Draw("AP")
canvas.SaveAs("beforeAug24_efficiency_vs_PMT3Voltage.png")
