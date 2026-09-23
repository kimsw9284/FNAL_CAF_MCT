import ROOT
from array import array

voltage = array('d', [1140,1240,1340,1440,1540,1640,1700]) #write the different voltages here

efficiency = array('d', [0.9720,0.9820,0.9760,0.9860,0.9821,0.9880,0.9801]) #write efficiency values

efficiency_error = array('d', [0.007378,0.005934,0.006858,0.005265,0.005922,0.004860,0.006236]) #Write the efficiency errors

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
canvas.SaveAs("beforeAug24_efficiency_vs_PMT1VoltageOnly.png")
