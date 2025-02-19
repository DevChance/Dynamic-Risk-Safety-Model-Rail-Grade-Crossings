import datetime
import math

# Define visibility timespans for each month
visibility_timespans = {
    1: {"Dawn": ("5:54 am", "6:50 am"), "Day": ("6:50 am", "5:05 pm"), "Dusk": ("5:05 pm", "6:02 pm"), "Dark": ("6:02 pm", "5:54 am")},
    2: {"Dawn": ("5:37 am", "6:31 am"), "Day": ("6:31 am", "5:34 pm"), "Dusk": ("5:34 pm", "6:28 pm"), "Dark": ("6:28 pm", "5:37 am")},
    3: {"Dawn": ("6:05 am", "6:59 am"), "Day": ("6:59 am", "6:56 pm"), "Dusk": ("6:56 pm", "7:49 pm"), "Dark": ("7:49 pm", "6:05 am")},
    4: {"Dawn": ("5:23 am", "6:19 am"), "Day": ("6:19 am", "7:18 pm"), "Dusk": ("7:18 pm", "8:14 pm"), "Dark": ("8:14 pm", "5:23 am")},
    5: {"Dawn": ("4:50 am", "5:49 am"), "Day": ("5:49 am", "7:40 pm"), "Dusk": ("7:40 pm", "8:40 pm"), "Dark": ("8:40 pm", "4:50 am")},
    6: {"Dawn": ("4:36 am", "5:40 am"), "Day": ("5:40 am", "7:58 pm"), "Dusk": ("7:58 pm", "9:01 pm"), "Dark": ("9:01 pm", "4:36 am")},
    7: {"Dawn": ("4:49 am", "5:51 am"), "Day": ("5:51 am", "7:57 pm"), "Dusk": ("7:57 pm", "8:59 pm"), "Dark": ("8:59 pm", "4:49 am")},
    8: {"Dawn": ("5:15 am", "6:12 am"), "Day": ("6:12 am", "7:33 pm"), "Dusk": ("7:33 pm", "8:30 pm"), "Dark": ("8:30 pm", "5:15 am")},
    9: {"Dawn": ("5:38 am", "6:32 am"), "Day": ("6:32 am", "6:54 pm"), "Dusk": ("6:54 pm", "7:48 pm"), "Dark": ("7:48 pm", "5:38 am")},
    10: {"Dawn": ("5:59 am", "6:52 am"), "Day": ("6:52 am", "6:15 pm"), "Dusk": ("6:15 pm", "7:09 pm"), "Dark": ("7:09 pm", "5:59 am")},
    11: {"Dawn": ("5:22 am", "6:18 am"), "Day": ("6:18 am", "4:47 pm"), "Dusk": ("4:47 pm", "5:43 pm"), "Dark": ("5:43 pm", "5:22 am")},
    12: {"Dawn": ("5:45 am", "6:43 am"), "Day": ("6:43 am", "4:44 pm"), "Dusk": ("4:44 pm", "5:42 pm"), "Dark": ("5:42 pm", "5:45 am")}
}

# Define MIS codes
mis_codes = {
    "MISC": 0.0,
    "MISCL": 0.10,
    "MISR": 0.25,
    "MISD": 0.90,
    "MISDD": 1.00,
    "MIST": 1.25,
}

# Mapping from warning type to effectiveness scores
warning_type_effectiveness = {
    "Highly Effective": 0.5,
    "Moderate Effect": 0.25,
    "Minimal Effect": 0.10,
    "No Effect": 0.0,
}

def get_visibility_rating(date_time):
    month = date_time.month
    time = date_time.strftime("%I:%M %p")
    for period, times in visibility_timespans[month].items():
        start, end = times
        if start <= time <= end:
            return {"Dawn": 1, "Day": 2, "Dusk": 3, "Dark": 4}.get(period, 0)
    return 0

def calculate_mis(Vrating, I, W):
    Villuminated = 0 if I == 1 and Vrating in [1, 3, 4] else Vrating
    return Villuminated + W

def calculate_baseline_score(a, b, c, d, R, M, L, D, T, W_type, MIS):
    MaxSpeed = M
    NumLanes = L
    AADT = D
    TDT = T
    Baseline = 30  # Adjust as necessary
    score = (a*R) + (math.log(math.exp(b * (1 + MIS) * (MaxSpeed - Baseline)) + 1)) + (c*NumLanes) + (d*math.log(AADT * (1 - MIS/2) * TDT)) - (W_type * (1 - MIS/3))
    return score

# User inputs MIS code
mis_code_input = input("Do you have an MIS code? If yes, enter it (MISC, MISCL, MISR, MISD, MISDD, MIST). If no, type 'no': ").strip().upper()
if mis_code_input in mis_codes:
    MIS = mis_codes[mis_code_input]
    print(f"Meteorological Impact Score (MIS) set to: {MIS}")
    # Skip inputs related to date, time, weather, and illumination
    tracks_input = int(input("Number of Railroad Tracks: "))
    max_speed_input = int(input("Maximum Speed for Trains: "))
    lanes_input = int(input("Number of Highway Traffic Lanes: "))
    aadt_input = int(input("Average Annual Daily Traffic Count: "))
    tdt_input = int(input("Total Daily Trains: "))
    warning_type_input = input("Type of Cross Warning (Highly Effective, Moderate Effect, Minimal Effect, No Effect): ")

    # Set default values for skipped inputs
    Vrating = 0
    W = 0
    I = 0
    W_type = warning_type_effectiveness.get(warning_type_input, 0)  # Fetch the effectiveness based on user input
else:
    # Proceed with inputs
    date_input = input("Enter date (YYYY-MM-DD): ")
    time_input = input("Enter time (HH:MM AM/PM): ")
    datetime_input = datetime.datetime.strptime(f"{date_input} {time_input}", "%Y-%m-%d %I:%M %p")

    weather_input = int(input("Weather (1=Clear, 2=Cloudy, 3=Rain): "))
    illuminated_input = int(input("Crossing Illuminated (1=Yes, 0=No): "))
    tracks_input = int(input("Number of Railroad Tracks: "))
    max_speed_input = int(input("Maximum Speed for Trains: "))
    lanes_input = int(input("Number of Highway Traffic Lanes: "))
    aadt_input = int(input("Average Annual Daily Traffic Count: "))
    tdt_input = int(input("Total Daily Trains: "))
    warning_type_input = input("Type of Cross Warning (Highly Effective, Moderate Effect, Minimal Effect, No Effect): ")

    # Convert inputs
    Vrating = get_visibility_rating(datetime_input)
    W = {1: 0.00, 2: 0.10, 3: 0.25}.get(weather_input, 0)
    I = illuminated_input
    W_type = warning_type_effectiveness.get(warning_type_input, 0)  # Fetch the effectiveness based on user input
    # Calculate MIS
    MIS = calculate_mis(Vrating, I, W)

# Calculate scores
Baseline_Score = calculate_baseline_score(0.5, 0.021, 0.5, 1.0, tracks_input, max_speed_input, lanes_input, aadt_input, tdt_input, W_type, MIS)

print(f"Meteorological Impact Score (MIS): {MIS}")
print(f"Baseline Score: {Baseline_Score}")
