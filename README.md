# CAC 2024 Analysis — PR Package

**Contact / Verification Email:** 23f1001029@ds.study.iitm.ac.in

This pull request contains reproducible code, figures, and a data story analyzing 2024 Customer Acquisition Cost (CAC) versus the industry target.

## Dataset
- **Quarterly CAC (2024):**
  - Q1: 230.79
  - Q2: 231.33
  - Q3: 228.33
  - Q4: 236.45
- **Average (must be exact):** **231.73**
- **Industry Target:** **150**

## Reproducibility
```bash
pip install -r requirements.txt
python analysis.py
```

Outputs will be saved under `figures/`:
- `figures/cac_trend_2024.png`
- `figures/cac_vs_target_2024.png`

## Key Findings
1. **Sustained Elevation Above Target:** The 2024 **average CAC is 231.73**, which is **81.73** above the industry target of 150 (≈ **54% higher**).
2. **Mild Quarter-to-Quarter Variability:** CAC ranges from **228.33 (Q3)** to **236.45 (Q4)**—a narrow band (≈ **3.1% spread**), indicating stability but at an elevated level.
3. **Upward Finish:** **Q4 is the highest** quarter, suggesting end-of-year pressures (auction CPMs, seasonal competition) or diminishing channel efficiency.
4. **No Structural Improvement Yet:** Despite stability, there is **no downward trend** toward the benchmark, implying strategy and channel mix haven’t materially changed.

## Business Implications
- **Margin Compression:** Elevated CAC compresses contribution margins and payback periods, requiring higher LTV or pricing to maintain unit economics.
- **Budget Allocation Risk:** Continuing to fund the current mix will **lock in inefficiency**; even a 10% reduction only reaches ~208, still far from 150.
- **Forecasting & Cash:** At 231.73, growth at constant CAC increases burn; scaling without efficiency gains could **overstretch working capital**.

## Recommendations to Reach CAC 150
**Primary Strategy: Optimize Digital Marketing Channels.** Focus areas:

1. **Channel Mix Rebalancing**
   - Shift spend from underperforming paid channels to **high-intent search** and **retargeting** where conversion efficiency is measurably higher.
   - Cap CPA on broad social prospecting; expand **SEO and content** to increase low-cost inbound volume.
2. **Creative & Funnel Optimization**
   - Systematically A/B test **ad creatives**, **audiences**, and **landing pages**; set a **weekly testing cadence** with pre-registered hypotheses.
   - Improve on-site **conversion rate (CRO)**: speed, above-the-fold value props, social proof, simplified checkout.
3. **Bidding & Audience Controls**
   - Tighten **geo/device dayparting**, exclude low-converting segments, and apply **target CPA/ROAS bidding** with clean conversion signals.
   - Deploy **retention and referral loops** (email, SMS, loyalty) to lift LTV, allowing higher CAC where justified.
4. **Attribution & Measurement**
   - Implement **server-side tracking** and MMM-lite experiments (geo holdouts) to validate causal lift; reduce waste from misattributed channels.
5. **Governance & Targets**
   - Set a staged target path: **Q2 next year: ≤205**, **Q3: ≤180**, **Q4: ≤150** with monthly reviews and corrective actions.

## Files Included
- `data/cac_2024.csv` — source data
- `analysis.py` — analysis & plot generation (pure matplotlib, no seaborn)
- `figures/cac_trend_2024.png` — quarterly trend
- `figures/cac_vs_target_2024.png` — average vs target
- `requirements.txt` — Python dependencies

## How to Create the Pull Request
1. Fork or create a repo on GitHub (e.g., `cac-2024-analysis`).
2. Clone it locally and copy this folder’s contents.
3. Commit on a new branch:
   ```bash
   git checkout -b feat/cac-2024-analysis
   git add .
   git commit -m "CAC 2024 analysis: code, figures, and data story (contains 23f1001029@ds.study.iitm.ac.in)"
   git push -u origin feat/cac-2024-analysis
   ```
4. Open a PR with title **"CAC 2024: analysis, visualizations, and data story"** and paste this README as the PR body.
   - Ensure the PR text includes the email: **23f1001029@ds.study.iitm.ac.in**

---

_Prepared via LLM-assisted code generation. All computations are reproducible._