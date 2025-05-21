# Monte Carlo Simulation and Value-at-Risk (VaR) Analysis for Continental AG Stock

This project performs a financial risk analysis of Continental AG's stock using a GARCH(1,1) model and Monte Carlo simulation. The analysis includes:

- Estimating volatility using a GARCH(1,1) model  
- Simulating future stock price paths over a one-year horizon  
- Calculating Value-at-Risk (VaR) at the 95% confidence level (both historical and Monte Carlo)  
- Visualizing simulated trajectories, final price distributions, and volatility over time  

## Files Included

- `ADA_VaR_Stojkovic.py` — Python script for data loading, modeling, simulation, and visualization  
- `monte_carlo_paths.png` — Simulated stock price paths with average trend line  
- `final_price_distribution.png` — Histogram of simulated final prices with quantile markers  
- `volatility_over_time.png` — Time series of GARCH-estimated volatility  

## Key Results

- **Extreme daily returns**: Minimum and maximum return values with dates  
- **VaR at 95% confidence level**:
  - Historical: Based on historical returns distribution  
  - Monte Carlo: Based on simulated price paths  
- **Final price quantiles**: 5%, 95%, and 0.1%  
- **Expected future price**: Based on the average of all simulations  

## Requirements

Install the required Python packages using pip:

pip install yfinance pandas numpy matplotlib arch


## How to Run

1. Download or clone the repository.  
2. Make sure all files are in the same folder.  
3. Run the Python script by opening a terminal/command prompt and typing:

python ADA_VaR_Stojkovic.py


The script will display charts and print key metrics in the console.

## Notes

- The simulation uses 100,000 future price paths over 252 trading days (approx. 1 year).  
- Data is sourced from Yahoo Finance for Continental AG (ticker: `CON.DE`).  
- Volatility is modeled using a GARCH(1,1) model fitted to daily returns (in %).  
- You can modify the `symbol` variable in the script to analyze another stock.  

## Author

**Jovan Stojković**  
Master's student in Advanced Data Analytics in Business  

_This project was developed for educational and demonstration purposes._
