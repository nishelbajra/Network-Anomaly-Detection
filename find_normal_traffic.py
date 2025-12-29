import joblib
import pandas as pd
import json

# Load the pipeline
pipeline = joblib.load('pipeline.pkl')

# Test various network traffic patterns
test_cases = [
    # Case 1: Minimal traffic
    {str(i): 0 for i in range(41)},
    
    # Case 2: Small HTTP request
    {
        "0": 0, "1": "tcp", "2": "http", "3": "SF",
        "4": 181, "5": 5450, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 1, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
        "18": 0, "19": 0, "20": 0, "21": 0, "22": 1, "23": 1,
        "24": 0.0, "25": 0.0, "26": 0.0, "27": 0.0, "28": 1.0,
        "29": 0.0, "30": 0.0, "31": 9, "32": 9, "33": 1.0,
        "34": 0.0, "35": 0.11, "36": 0.0, "37": 0.0, "38": 0.0,
        "39": 0.0, "40": 0.0
    },
    
    # Case 3: FTP connection
    {
        "0": 0, "1": "tcp", "2": "ftp_data", "3": "SF",
        "4": 491, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
        "18": 0, "19": 0, "20": 0, "21": 0, "22": 2, "23": 2,
        "24": 0.0, "25": 0.0, "26": 0.0, "27": 0.0, "28": 1.0,
        "29": 0.0, "30": 0.0, "31": 1, "32": 1, "33": 1.0,
        "34": 0.0, "35": 1.0, "36": 0.0, "37": 0.0, "38": 0.0,
        "39": 0.0, "40": 0.0
    },
    
    # Case 4: SMTP email
    {
        "0": 0, "1": "tcp", "2": "smtp", "3": "SF",
        "4": 1032, "5": 1424, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 1, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
        "18": 0, "19": 0, "20": 0, "21": 0, "22": 1, "23": 1,
        "24": 0.0, "25": 0.0, "26": 0.0, "27": 0.0, "28": 1.0,
        "29": 0.0, "30": 0.0, "31": 1, "32": 1, "33": 1.0,
        "34": 0.0, "35": 1.0, "36": 0.0, "37": 0.0, "38": 0.0,
        "39": 0.0, "40": 0.0
    },
    
    # Case 5: Private network traffic
    {
        "0": 0, "1": "tcp", "2": "private", "3": "S0",
        "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0,
        "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, "17": 0,
        "18": 0, "19": 0, "20": 0, "21": 0, "22": 123, "23": 1,
        "24": 0.0, "25": 1.0, "26": 0.0, "27": 0.01, "28": 0.0,
        "29": 0.0, "30": 1.0, "31": 255, "32": 1, "33": 0.0,
        "34": 1.0, "35": 0.0, "36": 0.0, "37": 1.0, "38": 1.0,
        "39": 0.0, "40": 0.0
    }
]

case_names = [
    "Minimal Traffic (all zeros)",
    "Small HTTP Request",
    "FTP Data Connection",
    "SMTP Email",
    "Private Network Traffic"
]

print("Testing different network traffic patterns...\n")
print("="*70)

normal_traffic_found = []

for i, (test_data, name) in enumerate(zip(test_cases, case_names)):
    df = pd.DataFrame([test_data])
    df.columns = df.columns.astype(str)
    
    # Ensure all expected columns exist
    expected_columns = [str(j) for j in range(41)]
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0
    
    df = df[expected_columns]
    
    # Define categorical and numeric columns
    categorical_columns = ['1', '2', '3']
    numeric_columns = [col for col in df.columns if col not in categorical_columns]
    
    df[categorical_columns] = df[categorical_columns].astype(str).fillna('missing')
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)
    
    try:
        prediction = pipeline.predict(df)
        result = "✅ NORMAL (1)" if prediction[0] == 1 else "⚠️  ANOMALY (-1)"
        
        print(f"Case {i+1}: {name}")
        print(f"Result: {result}")
        print("-"*70)
        
        if prediction[0] == 1:
            normal_traffic_found.append({
                "name": name,
                "data": test_data
            })
    except Exception as e:
        print(f"Case {i+1}: {name}")
        print(f"Error: {str(e)}")
        print("-"*70)

print("\n" + "="*70)
if normal_traffic_found:
    print(f"\n✅ Found {len(normal_traffic_found)} NORMAL traffic pattern(s)!\n")
    for item in normal_traffic_found:
        print(f"Pattern: {item['name']}")
        print(f"JSON Data:\n{json.dumps([item['data']], indent=2)}\n")
else:
    print("\n⚠️  No normal traffic patterns found in test cases.")
    print("The model may be very strict or trained on limited normal data.")
    print("\nTip: Try data with these characteristics:")
    print("  - Protocol: tcp, udp, icmp")
    print("  - Service: http, ftp, smtp, telnet, etc.")
    print("  - Flag: SF (normal connection)")
    print("  - Moderate packet sizes and counts")
