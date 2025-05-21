# Monte Carlo Simulation and Value-at-Risk (VaR) Analysis for Continental AG Stock

This project performs a financial risk analysis of Continental AG's stock using a GARCH(1,1) model and Monte Carlo simulation. The analysis includes:

- Estimating volatility with a GARCH model
- Simulating future stock price paths
- Value-at-Risk (VaR) calculation (both historical and Monte Carlo)
- Visualizing price trajectories and return distributions

## Files Included

- `ADA_VaR_Stojkovic.py` — Python script for modeling, simulation, and visualization
- `monte_carlo_paths.png` — Simulated stock price paths with average trend line
- `final_price_distribution.png` — Histogram of simulated final prices with quantile markers
- `volatility_over_time.png` — Time series plot of GARCH-estimated volatility

## Key Results

- **Extreme daily returns**: Minimum and maximum return values with their corresponding dates
- **VaR (95% confidence level)**:
  - Historical method: based on empirical return distribution
  - Monte Carlo method: based on simulated price paths
- **Final price quantiles**: 5%, 95%, and 0.1% of the final simulated prices
- **Expected future price**: Based on the average across all simulated paths

## Requirements

Install the required Python packages using pip:

```bash
pip install yfinance pandas numpy matplotlib arch
How to Run
Download or clone the repository.

Ensure all files are in the same folder.

Run the Python script:

bash
Copy
Edit
python ADA_VaR_Stojkovic.py
The script will output charts and key metrics in the console.

Notes
Simulates 100,000 future stock price paths over a 252-day (1-year) period

Uses historical data for Continental AG (CON.DE) from Yahoo Finance

GARCH(1,1) model fitted to daily returns (in %)

You can modify the symbol variable in the script to analyze a different stock

Author
Jovan Stojković
Master's student in Advanced Data Analytics in Business
This project was developed for learning and demonstration purposes.
