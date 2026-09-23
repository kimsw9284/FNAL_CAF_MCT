import ROOT
from array import array

voltage = array('d', [1140,1240,1340,1440,1540,1580,1620,1660,1700]) #write the different voltages here

efficiency = array('d', [0.8849,0.8725,0.8904,0.8988,0.8869,0.9203,0.9341,0.9000,0.9030]) #write efficiency values

efficiency_error = array('d', [0.0142,0.0149,0.0139,0.0134,0.0141,0.0121,0.0111,0.0134,0.0132]) #Write the efficiency errors

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
canvas.SaveAs("beforeAug24_efficiency_vs_PMT4Voltage.png")
