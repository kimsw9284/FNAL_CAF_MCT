import ROOT
from array import array

width = array('d', [20,30,40,50,60,70,80]) #write the different widths here

efficiency = array('d', [0.2386,0.7100,0.8529,0.8849,0.8628,0.8802,0.8900]) #write efficiency values

efficiency_error = array('d', [0.0190,0.0203,0.0158,0.0142,0.0153,0.0145,0.0140]) #Write the efficiency errors

width_error = array('d', [0.0] * len(width))
ROOT.gStyle.SetOptStat(0)

canvas = ROOT.TCanvas("canvas","Efficiency vs Width", 800,700)

canvas.SetTicks(1,1)
canvas.SetFrameLineWidth(2)

canvas.SetTicks(1, 1)
graph = ROOT.TGraphErrors(len(width),width,efficiency,width_error,efficiency_error)

graph.SetTitle("")

graph.SetMarkerStyle(20)
graph.SetMarkerSize(1.3)
graph.SetMarkerColor(ROOT.kBlue + 1)

graph.SetLineColor(ROOT.kBlack)
graph.SetLineWidth(2)

graph.GetXaxis().SetTitle("Width [ns]")
graph.GetYaxis().SetTitle("Efficiency")

graph.GetXaxis().SetTitleSize(0.04)
graph.GetYaxis().SetTitleSize(0.04)
graph.GetYaxis().SetTitleOffset(1.2)

graph.GetYaxis().SetRangeUser(0.0, 1.0)

graph.Draw("AP")
canvas.SaveAs("beforeAug24_efficiency_vs_width.png")
