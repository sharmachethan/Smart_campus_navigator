from flask import Flask, render_template, request, jsonify
import time
import math

app = Flask(__name__)

# MIT Manipal campus coordinates (you can add more)
facilities = [
    {"name": "Main Gate", "lat": 13.3538, "lon": 74.7921},
    {"name": "NLH", "lat": 13.3546, "lon": 74.7929},
    {"name": "Food Court", "lat": 13.3553, "lon": 74.7934},
    {"name": "Innovation Center", "lat": 13.3560, "lon": 74.7939},
    {"name": "Hostel Block", "lat": 13.3565, "lon": 74.7945}
]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = (math.sin(dphi/2)**2 +
         math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2)
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))

@app.route('/')
def index():
    return render_template('index.html', campus_lat=13.355034, campus_lon=74.792821)

@app.route('/nearest', methods=['POST'])
def nearest():
    t0 = time.time()
    data = request.get_json()
    lat, lon, radius = float(data['lat']), float(data['lon']), float(data['radius_m'])
    nearby = []
    for f in facilities:
        dist = haversine(lat, lon, f['lat'], f['lon'])
        if dist <= radius:
            nearby.append({
                'name': f['name'],
                'lat': f['lat'],
                'lon': f['lon'],
                'distance': round(dist, 2)
            })
    processing_time = (time.time() - t0) * 1000
    return jsonify({
        'count': len(nearby),
        'nearby': nearby,
        'server_processing_ms': round(processing_time, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
