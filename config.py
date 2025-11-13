"""
Configuration file for FloodSafe ML Pipeline
Store your API credentials here (add to .gitignore!)
"""

# NASA Earthdata credentials
NASA_USERNAME = "samprity"  # Replace with your NASA Earthdata username
NASA_PASSWORD = "Shampoo2015!"  # Replace with your NASA Earthdata password

# Google Earth Engine
GEE_SERVICE_ACCOUNT_JSON = r"C:\Users\utech\Downloads\testing-477914-273b428b8bc2.json"  # Path to your GEE JSON key file

# OpenRouteService (already have)
ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6Ijg2MmVmMzA4NmVhNDQ3MThiNmU0NGQwODQ1MjU5NzNiIiwiaCI6Im11cm11cjY0In0="

# Data storage paths
DATA_DIR = "data"
RAW_DATA_DIR = f"{DATA_DIR}/raw"
PROCESSED_DATA_DIR = f"{DATA_DIR}/processed"
MODEL_DIR = "models"

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Routing parameters
LAMBDA_SAFEST = 10.0  # High weight on flood risk
LAMBDA_BALANCED = 3.0  # Medium weight
LAMBDA_FASTEST = 0.5  # Low weight (prioritize speed)