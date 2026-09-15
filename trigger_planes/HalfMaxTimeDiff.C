// ********************************************************************************
// * HalfMaxTimeDiff.C
// *
// * Computes, event by event, the half-maximum crossing time (interpolated,
// * on the leading/falling edge of the negative-going pulse, BEFORE the peak)
// * for channel 2 and channel 3, then plots and saves the distribution of
// * (t3_half - t2_half).
// *
// * Reads directly from the .root file produced by Dat2Root.cc, using the
// * raw waveform branches c2/c3 (voltage vs. sample index). Does NOT rely on
// * the "peaktime" branch, which only marks the sample-index of the minimum,
// * not a real leading-edge arrival time.
// *
// * NOTE: dt_per_bin below assumes uniform sample spacing. Dat2Root.cc
// * currently discards the real per-bin DRS4 time calibration array
// * (tmpEventTime), so this is an approximation. Update dt_per_bin to match
// * your actual DRS4 sampling rate, or patch Dat2Root.cc to save the real
// * per-bin calibration if you need higher precision.
// *
// * Usage (from a ROOT prompt or command line):
// *   root -l -q 'HalfMaxTimeDiff.C("yourfile.root")'
// *
// * Optional arguments let you adjust the sampling interval, baseline window,
// * and histogram range without editing the code:
// *   root -l -q 'HalfMaxTimeDiff.C("yourfile.root", 0.2, 100, 200, -20, 20)'
// *
// ********************************************************************************

#include <iostream>
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TCanvas.h"
#include "TStyle.h"

// Finds the interpolated half-maximum crossing time (in ns) on the leading
// edge of a negative-going pulse, scanning from the start of the waveform
// up to the sample of minimum voltage. Returns -999 if no crossing is found.
double FindHalfMaxTime(const Float_t *wave, int nsamples, int baseline_samples,
                        double dt_per_bin)
{
    if (baseline_samples < 1 || baseline_samples >= nsamples) baseline_samples = 100;

    // Baseline estimate from the first N samples
    double baseline = 0;
    for (int i = 0; i < baseline_samples; i++) baseline += wave[i];
    baseline /= (double)baseline_samples;

    // Find the peak (minimum voltage) location
    int idx_min = 0;
    double vmin = wave[0];
    for (int i = 0; i < nsamples; i++)
    {
        if (wave[i] < vmin)
        {
            vmin = wave[i];
            idx_min = i;
        }
    }

    // Reject flat/noisy traces with no real pulse
    if (baseline - vmin < 1e-6) return -999;

    double threshold = baseline - 0.5 * (baseline - vmin);

    // Scan from just after the baseline window up to the peak for the
    // first downward crossing of the threshold, then linearly interpolate
    for (int i = 1; i <= idx_min; i++)
    {
        if (wave[i - 1] >= threshold && wave[i] < threshold)
        {
            double frac = (threshold - wave[i - 1]) / (wave[i] - wave[i - 1]);
            double bin_crossing = (i - 1) + frac;
            return bin_crossing * dt_per_bin;
        }
    }

    return -999; // no valid crossing found for this event
}

void HalfMaxTimeDiff(const char *rootfile = "yourfile.root",
                      double dt_per_bin = 0.2,      // ns per sample - CHECK against your DRS4 settings
                      int baseline_samples = 100,   // number of leading samples used for baseline
                      int nbins = 200,
                      double xmin = -20,
                      double xmax = 20)
{
    TFile *f = TFile::Open(rootfile, "read");
    if (!f || f->IsZombie())
    {
        std::cerr << "!! Could not open file: " << rootfile << std::endl;
        return;
    }

    TTree *T = (TTree *)f->Get("T");
    if (!T)
    {
        std::cerr << "!! Could not find tree 'T' in file: " << rootfile << std::endl;
        return;
    }

    Float_t c2[1024], c3[1024];
    T->SetBranchAddress("c2", c2);
    T->SetBranchAddress("c3", c3);

    TH1F *hdt = new TH1F("hdt",
                          "Arrival time difference (ch3 - ch2);#Delta t [ns];Events",
                          nbins, xmin, xmax);

    Long64_t nentries = T->GetEntries();
    Long64_t nfilled = 0;

    for (Long64_t i = 0; i < nentries; i++)
    {
        T->GetEntry(i);

        double t2_half = FindHalfMaxTime(c2, 1024, baseline_samples, dt_per_bin);
        double t3_half = FindHalfMaxTime(c3, 1024, baseline_samples, dt_per_bin);

        if (t2_half > -999 && t3_half > -999)
        {
            hdt->Fill(t3_half - t2_half);
            nfilled++;
        }
    }

    std::cout << ">> Processed " << nentries << " events, "
              << nfilled << " had valid crossings on both channels." << std::endl;

    gStyle->SetOptStat(1111);

    TCanvas *c = new TCanvas("c_halfmaxdiff", "Half-max arrival time difference", 800, 600);
    hdt->Draw();
    c->Update();

    // Save both a PNG image and a ROOT file containing the histogram
    c->SaveAs("HalfMaxTimeDiff.png");
    TFile *fout = new TFile("HalfMaxTimeDiff_hist.root", "recreate");
    hdt->Write();
    fout->Close();

    std::cout << ">> Saved plot to HalfMaxTimeDiff.png" << std::endl;
    std::cout << ">> Saved histogram to HalfMaxTimeDiff_hist.root" << std::endl;
}
