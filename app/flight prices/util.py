import pandas as pd

CITIES = {'Delhi': 2, 'Mumbai': 5, 'Bangalore': 0, 'Kolkata': 4, 'Hyderabad': 3, 'Chennai': 1}
AIRLINES = {'Indigo': 3, 'Air_India': 1, 'GO_FIRST': 2, 'SpiceJet': 4, 'Vistara': 5, 'AirAsia': 0}
TIMES = {'Afternoon': 0, 'Early_Morning': 1, 'Evening': 2, 'Late_Night': 3, 'Morning': 4, 'Night': 5}
CLASS = {'Economy': 1, 'Business': 0}
STOPS = {'None': 2, 'One': 0, '2 or more': 1}

def format(airline, source, destination, departure, arrival, stops, seat, duration, days):

    airline = AIRLINES[airline]
    source = CITIES[source]
    destination = CITIES[destination]
    departure = TIMES[departure]
    arrival = TIMES[arrival]
    stops = STOPS[stops]
    seat = CLASS[seat]

    data = [(airline, source, departure, stops, arrival, destination, seat, duration, days)]
    X = pd.DataFrame(data, columns=["airline", "source city", "departure time", "stops", "arrival time", "destination city", "seat class", "duration", "days left"])

    return X