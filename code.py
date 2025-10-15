 import pandas as pd
 import numpy as np
 import matplotlib.pyplot as plt
 # Simulated daily returns for 3 assets (A, B, C)
 np.random.seed(42)
 returns = pd.DataFrame({
    'Asset_A': np.random.normal(0.001, 0.02, 252),
    'Asset_B': np.random.normal(0.0008, 0.015, 252),
    'Asset_C': np.random.normal(0.0012, 0.018, 252)
 })
 # Calculate mean returns and covariance
 mean_returns = returns.mean() * 252
 cov_matrix = returns.cov() * 252
 # Random portfolio weights
 weights = np.array([0.4, 0.35, 0.25])
 portfolio_return = np.dot(weights, mean_returns)
 portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
 # Sharpe ratio (risk-free rate = 2%)
 sharpe_ratio = (portfolio_return - 0.02) / portfolio_volatility
 print(f"Expected Annual Return: {portfolio_return:.2%}")
 print(f"Annual Volatility: {portfolio_volatility:.2%}")
 print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
 # Visualization
 returns.plot(title='Simulated Asset Returns', figsize=(8,4))
 plt.xlabel('Days')
 plt.ylabel('Daily Return')
 plt.show()
