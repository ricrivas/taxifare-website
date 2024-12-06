import streamlit as st
import requests
import datetime

# Título de la página
st.title('Taxi Fare app')


# Controladores para los parámetros del viaje
pickup_datetime = st.text_input("Enter the date and time of the pickup (YYYY-MM-DD HH:MM:SS)", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Enter the pickup longitude", -73.950655)
pickup_latitude = st.number_input("Enter the pickup latitude", 40.783282)
dropoff_longitude = st.number_input("Enter the dropoff longitude", -73.984365)
dropoff_latitude = st.number_input("Enter the dropoff latitude", 40.769802)
passenger_count = st.number_input("Enter the passenger count", 1, step=1)

# URL de la API
url = 'https://taxifare.lewagon.ai/predict'

if st.button('Get Fare Prediction'):
    
    # Construir un diccionario con los parámetros de la API
    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    # Llamar a la API usando el paquete `requests`
    response = requests.get(url, params=params)
    prediction = response.json()

    # Mostrar la predicción al usuario
    st.write(f"Fare prediction: ${prediction['fare']:.2f}")

