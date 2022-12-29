import streamlit as st
import pickle
from util import format

with open('../../flight_prices_model.pkl', 'rb') as f:
    model = pickle.load(f)

CITIES = ('Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai')
AIRLINES = ('Indigo', 'Air_India', 'GO_FIRST', 'SpiceJet', 'Vistara', 'AirAsia')
TIMES = ('Afternoon', 'Early_Morning', 'Evening', 'Late_Night', 'Morning', 'Night')
CLASS = ('Economy', 'Business')
STOPS = ('None', 'One', '2 or more')

st.title('Flight Price Prediction')

airline = st.selectbox(
    'Select an airline',
    AIRLINES
)

source_city = st.selectbox(
    'Select the departing city',
    CITIES
)

destination_city = st.selectbox(
    'Select the destination city (Cannot be same as departing city)',
    CITIES
)

departure_time = st.selectbox(
    'Select departure time',
    TIMES
)

arrival_time = st.selectbox(
    'Select arrival time',
    TIMES
)

stops = st.selectbox(
    'Select the number of stops',
    STOPS
)

seat_class = st.radio(
    'Select a class',
    CLASS
)

duration = st.number_input(
    'Select duration of flight (0.8 - 50 hours)',
    0.80, 50.0
)

days_left = st.slider(
    'Select days left until flight',
    min_value=1, max_value=49
)

submit = st.button('Predict')

if submit:
    X = format(airline, source_city, destination_city, departure_time, arrival_time, stops, seat_class, duration, days_left)
    pred = model.predict(X)
    st.subheader("Estimated price for flight is ₹" + str(int(pred)) + " (rupees)")
    