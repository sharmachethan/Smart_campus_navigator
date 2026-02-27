import requests, time

# Make sure Flask server (app.py) is running on http://127.0.0.1:5000
url = 'http://127.0.0.1:5000/nearest'

coords = [
    (13.3538, 74.7915),  # Main Gate
    (13.3551, 74.7926),  # Innovation Center
    (13.3562, 74.7934),  # Food Court
]

rtts = []
print("Starting 50 simulated location updates...\n")

for i in range(50):
    lat, lon = coords[i % len(coords)]
    t0 = time.time()
    resp = requests.post(url, json={'lat': lat, 'lon': lon, 'radius_m': 150})
    rtts.append((time.time() - t0) * 1000)
    if i % 10 == 0:
        print(f"Update {i+1}: {resp.json()['notification']}")

print("\n----------------------------------")
print(f"Mean RTT (ms): {sum(rtts)/len(rtts):.2f}")
print(f"Min RTT (ms): {min(rtts):.2f}")
print(f"Max RTT (ms): {max(rtts):.2f}")
print(f"Total samples: {len(rtts)}")
print("----------------------------------")
