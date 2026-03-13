# Enterprise UPI Behavioral Analytics Framework v6.0

## Project Overview
This repository hosts an advanced machine learning pipeline designed to perform granular behavioral modeling on raw UPI transaction logs. The system utilizes a hybrid approach, combining unsupervised clustering for discovery and supervised classification for statistical validation.

## Key Technical Features
- **Multi-Algorithm Pipeline:** Integration of K-Means and optimized scaling for robust persona identification.
- **Automated Cluster Optimization:** Uses Silhouette Coefficient analysis to determine the ideal number of behavioral segments.
- **Supervised Validation:** Implements a Random Forest Classifier with **GridSearchCV Hyperparameter Tuning** to verify cluster stability.
- **Feature Engineering:** Calculation of Rolling Averages, Withdrawal Volatility, and Liquidity Ratios to capture temporal spending trends.

## Methodology & Architecture
1. **Data Ingestion Layer:** Robust CSV parsing with automated metadata cleaning and type enforcement.
2. **Feature Engineering Layer:** Transformation of raw currency logs into behavioral metrics (e.g., Spend Intensity).
3. **Clustering Layer:** Unsupervised segmentation into three core personas:
   - **Conservative Savers:** High liquidity maintenance with infrequent withdrawals.
   - **High-Velocity Transactors:** Regular, moderate-to-high volume transaction patterns.
   - **High-Net-Worth Entities:** Statistical outliers with significant balance reserves.
4. **Validation Layer:** Cross-validation achieving near 100% accuracy in mapping behavior to identified personas.

## Repository Artifacts
- `analysis.py`: Modular, enterprise-grade Python framework (220+ lines).
- `persona_clusters.png`: High-resolution behavior segmentation map.
- `correlation_heatmap.png`: Statistical feature interaction matrix.
- `Project_Summary_Report.txt`: Automatically generated executive summary.
- `MyTransaction_Processed.csv`: Dataset with categorized behavioral labels.

## Execution
To run the full analytics suite:
```bash
python analysis.py
```
