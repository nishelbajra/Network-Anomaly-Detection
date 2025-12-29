import joblib
import json

# Load the pipeline
pipeline = joblib.load('pipeline.pkl')
model = pipeline.named_steps['model']

# Get basic info
info = {
    "model_type": type(model).__name__,
    "model_module": type(model).__module__
}

# Write to JSON for easy reading
with open('model_type.json', 'w') as f:
    json.dump(info, f, indent=2)

print(json.dumps(info, indent=2))
