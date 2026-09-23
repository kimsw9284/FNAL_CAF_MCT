import ROOT
from array import array

voltage = array('d', [1180,1220,1260,1300,1340,1380,1420,1460,1500,1540,1580,1620,1660,1700]) #write the different voltages here

efficiency = array('d', [0.9640,0.9639,0.9760,0.9702,0.9600,0.9779,0.9780,0.9740,0.9700,0.9641,0.9700,0.9701,0.9781,0.9740]) #write efficiency values

efficiency_error = array('d', [0.0083,0.0083,0.0069,0.0076,0.0088,0.0066,0.0066,0.0071,0.0076,0.0083,0.0076,0.0076,0.0065,0.0071]) #Write the efficiency errors

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

graph.GetYaxis().SetRangeUser(0.9, 1.0)

graph.Draw("AP")
canvas.SaveAs("beforeAug24_efficiency_vs_PMT1Voltage.png")
