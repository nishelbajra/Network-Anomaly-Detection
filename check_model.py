import joblib

# Load the pipeline
pipeline = joblib.load('pipeline.pkl')

# Get the model
model = pipeline.named_steps['model']

print("Model type:", type(model).__name__)
print("\nFull model info:")
print(model)

# For unsupervised models, -1 typically means outlier/anomaly
# and 1 means normal/inlier
print("\n" + "="*60)
print("PREDICTION INTERPRETATION:")
print("="*60)
print("  -1 = Anomaly/Outlier (Suspicious/Attack)")
print("   1 = Normal/Inlier (Legitimate Traffic)")
print("="*60)
