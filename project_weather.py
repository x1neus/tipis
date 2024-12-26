import pandas as pd
import numpy as np
import streamlit as st
import joblib

model = joblib.load('weather.pkl')

all_columns = ['precipitation', 'temp_max', 'temp_min', 'wind']

st.title('Прогноз погоды')

precipitation = st.number_input('Осадки', min_value = 0.0, max_value = 55.9, value = 0.0, step = 0.1)
temp_max = st.number_input('Максимальная температура', min_value = -1.6, max_value = 35.6, value = 15.0, step = 0.1)
temp_min = st.number_input('Минимальная температура', min_value = -7.1, max_value = 18.3, value = 5.0, step = 0.1)
wind = st.number_input('Ветер', min_value = 0.4, max_value = 9.5, value = 2.0, step = 0.1)

input_data = {
  'precipitation': precipitation,
  'temp_max': temp_max,
  'temp_min': temp_min,
  'wind': wind
}

input_df = pd.DataFrame([input_data], columns = all_columns).fillna(0)

if st.button('Предсказать погоду'):
  prediction = model.predict(input_df)
  st.success(f'Предположительная погода: ${prediction[0]:}')
