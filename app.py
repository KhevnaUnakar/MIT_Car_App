import streamlit as st
import pickle

d1={'Comprehensive': 0,'Third Party insurance': 1,'Zero Dep': 2,'Not Available': 3,'Third Party': 1}
d2={'Petrol': 0, 'Diesel': 1, 'CNG': 2}
d3={'Manual': 0, 'Automatic': 1}
d4={'First Owner': 1,'Second Owner': 2,'Third Owner': 3,'Fifth Owner': 5,'Fourth Owner': 4}

final_model = pickle.load(open('final_model.pkl', 'rb'))

insurance_validity = st.text_input('Insurance validity: ')
fuel_type = st.text_input('Fuel Type: ')
kms_driven = st.text_input('KMs Driven: ')
ownsership = st.text_input('Ownership: ')
transmission = st.text_input('Transmission Type: ')

if st.button('Predict'):
    insurance_validity = d1[insurance_validity]
    fuel_type = d2[fuel_type]
    transmission = d3[transmission]
    ownsership = d4[ownsership]
    test = [[insurance_validity, fuel_type, kms_driven, ownsership, transmission]]
    yp = int(final_model.predict(test)[0])
    st.write(f'Predicted Car Price is {yp} Rs.'.format(yp))