import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model

# Downloading data for Continental
symbol = 'CON.DE'
data = yf.download(symbol, start='2005-01-01', end='2024-09-06')

# Calculating daily returns
data['Return'] = data['Close'].pct_change()
data = data.dropna()

# Fitting a GARCH(1, 1) model to the returns
model = arch_model(data['Return'] * 100, vol='Garch', p=1, q=1)
model_fit = model.fit()

# Model parameters
mu = model_fit.params['mu']
omega = model_fit.params['omega']
alpha = model_fit.params['alpha[1]']
beta = model_fit.params['beta[1]']

# Current stock price
last_price = data['Close'].iloc[-1]

# Number of simulations and prediction period
num_simulations = 100000
num_days = 252

# Initializing simulation paths
simulations = np.zeros((num_days, num_simulations))
simulations[0] = last_price

# Initial volatility
volatility = np.zeros(num_days)
volatility[0] = np.sqrt(model_fit.conditional_volatility.iloc[-1])

# Simulating volatility and stock prices
for t in range(1, num_days):
    random_shock = np.random.normal(loc=0, scale=volatility[t - 1], size=num_simulations)
    simulations[t] = simulations[t - 1] * (1 + random_shock / 100)
    volatility[t] = np.sqrt(omega + alpha * np.mean(random_shock ** 2) + beta * (volatility[t - 1] ** 2))

# Calculating the average trend
mean_trend = np.mean(simulations, axis=1)

# Extracting final simulated prices
final_prices = simulations[-1]

# 1. Extreme values of daily returns
extreme_min = data['Return'].min()
extreme_max = data['Return'].max()

# Dates of extreme returns
date_min = data['Return'].idxmin()
date_max = data['Return'].idxmax()

# 2. Estimating quantiles of final simulated prices
percentile_5 = np.percentile(final_prices, 5)
percentile_95 = np.percentile(final_prices, 95)

# 3. Calculating Value-at-Risk (VaR) at 95% confidence level
VaR_95_hist = np.percentile(data['Return'], 5)
VaR_95_mc = last_price - percentile_5

# Estimating the 0.1% extreme lower bound
percentile_0_1 = np.percentile(final_prices, 0.1)

# Ensuring VaR_95_mc is a float
if isinstance(VaR_95_mc, pd.Series):
    VaR_95_mc_value = VaR_95_mc.item()
else:
    VaR_95_mc_value = VaR_95_mc

# Results
print(f"Extreme daily returns: Min = {extreme_min:.6f} (Date: {date_min}), Max = {extreme_max:.6f} (Date: {date_max})")
print(f"Return quantiles:\n{data['Return'].quantile([0.01, 0.05, 0.10])}")
print(f"Value-at-Risk (VaR) at 95% confidence level (historical): {VaR_95_hist:.6f}")
print(f"Value-at-Risk (VaR) at 95% confidence level (Monte Carlo): {VaR_95_mc_value:.2f} EUR")
print(f"5% quantile of final prices: {percentile_5:.2f} EUR")
print(f"95% quantile of final prices: {percentile_95:.2f} EUR")
print(f"0.1% quantile of final prices: {percentile_0_1:.2f} EUR")

# Plotting the average trend and random sample paths
plt.figure(figsize=(12, 8))
plt.plot(mean_trend, color='blue', lw=2, label='Average Trend')
for i in np.random.choice(num_simulations, 15, replace=False):
    plt.plot(simulations[:, i], lw=1, alpha=0.5, color='grey')

# Annotating expected price at the end
expected_price = mean_trend[-1]
plt.text(num_days - 10, expected_price, f'{expected_price:.2f} EUR', color='blue', ha='center', va='bottom')

plt.title('Monte Carlo Simulation of Future Stock Prices for Continental')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)

# Plotting histogram of final prices
plt.figure(figsize=(12, 6))
plt.hist(final_prices, bins=50, alpha=0.75, color='blue', edgecolor='black')

# Adding vertical lines for quantiles
plt.axvline(x=percentile_5, color='red', linestyle='--', label='5% Quantile')
plt.axvline(x=percentile_95, color='green', linestyle='--', label='95% Quantile')
plt.axvline(x=percentile_0_1, color='purple', linestyle='--', label='0.1% Quantile')

# Annotating quantile values on the chart
def add_text_with_border(x, y, text, color):
    plt.text(x, y, text, color=color, ha='center', va='center', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

add_text_with_border(percentile_5, plt.gca().get_ylim()[1] * 0.9, f'5%: {percentile_5:.2f} EUR', 'red')
add_text_with_border(percentile_95, plt.gca().get_ylim()[1] * 0.9, f'95%: {percentile_95:.2f} EUR', 'green')
add_text_with_border(percentile_0_1, plt.gca().get_ylim()[1] * 0.8, f'0.1%: {percentile_0_1:.2f} EUR', 'purple')

plt.title('Distribution of Final Simulated Prices')
plt.xlabel('Stock Price')
plt.ylabel('Frequency')
plt.legend()
plt.grid(False)

plt.tight_layout()
plt.show()

# Plotting volatility over time
plt.figure(figsize=(10, 5))
plt.plot(model_fit.conditional_volatility, color='purple', label='Estimated Volatility (GARCH)')
plt.title('Estimated Volatility Over Time')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.grid(True)
plt.show()
