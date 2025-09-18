from flask import Flask, request, jsonify
import ephem
from datetime import datetime, timezone

app = Flask(__name__)

def classify_phase(illumination):
    """
    Classify the moon into one of the 8 main phases
    based on illumination percentage (0–100).
    """
    if illumination == 0:
        return {"phase": "New Moon", "icon": "🌑", "phase_id": "0"}
    elif 0 < illumination < 25:
        return {"phase": "Waxing Crescent", "icon": "🌒", "phase_id": "1"}
    elif illumination == 25:
        return {"phase": "First Quarter", "icon": "🌓", "phase_id": "2"}
    elif 25 < illumination < 50:
        return {"phase": "Waxing Gibbous", "icon": "🌔", "phase_id": "3"}
    elif illumination == 50:
        return {"phase": "Full Moon",  "icon": "🌕", "phase_id": "4"}
    elif 50 < illumination < 75:
        return {"phase": "Waning Gibbous", "icon": "🌖", "phase_id": "5"}
    elif illumination == 75:
        return {"phase": "Last Quarter", "icon": "🌗", "phase_id": "6"}
    elif 75 < illumination < 100:
        return {"phase": "Waning Crescent", "icon": "🌘", "phase_id": "7"}
    else:
        return {"phase": "New Moon", "icon": "🌑", "phase_id": "0"}

@app.route("/api/moonphase", methods=["GET"])
def moonphase():
    # Read the date from query string, e.g. /api/moonphase?date=2025-09-13 or /api/moonphase?date=today
    date_str = request.args.get("date", None)
    if not date_str:
        return jsonify({"error": "Missing 'date' parameter (YYYY-MM-DD)"}), 400
    
    if date_str.lower() == "today":
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format, expected YYYY-MM-DD"}), 400

    # Calculate with ephem
    moon = ephem.Moon(date)
    phase_percentage = moon.phase  # illumination percentage (0 = new, 100 = full)
    phase_name = classify_phase(round(phase_percentage))

    # Next main phases
    next_new = ephem.next_new_moon(date)
    next_first_quarter = ephem.next_first_quarter_moon(date)
    next_full = ephem.next_full_moon(date)
    next_last_quarter = ephem.next_last_quarter_moon(date)

    return jsonify({
        "date": date_str,
        "illumination_percent": round(phase_percentage, 2),
        "phase": phase_name["phase"],
        "phase_icon": phase_name["icon"],
        "phase_id": phase_name["phase_id"],
        "next_phases": {
            "new_moon": {"date": str(next_new.datetime().date()), "phase_id": "0"},
            "first_quarter": {"date":str(next_first_quarter.datetime().date()), "phase_id": "2"},
            "full_moon": {"date": str(next_full.datetime().date()), "phase_id": "4"},
            "last_quarter": {"date":str(next_last_quarter.datetime().date()), "phase_id": "6"}
        }
    })

if __name__ == "__main__":
    app.run(debug=True, port=5050)