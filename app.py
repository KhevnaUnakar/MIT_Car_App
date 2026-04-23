import streamlit as st
import pickle

# --- Page Config ---
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# --- Mappings ---
d1 = {'Comprehensive': 0, 'Third Party Insurance': 1, 'Zero Dep': 2, 'Not Available': 3, 'Third Party': 1}
d2 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
d3 = {'Manual': 0, 'Automatic': 1}
d4 = {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth Owner': 4, 'Fifth Owner': 5}

# --- Load Model ---
@st.cache_resource
def load_model():
    return pickle.load(open('final_model.pkl', 'rb'))

final_model = load_model()

# --- Header ---
st.title("🚗 Car Price Predictor")
st.markdown("Fill in the details below to get an estimated resale price for your car.")
st.divider()

# --- Input Form ---
col1, col2 = st.columns(2)

with col1:
    insurance_validity = st.selectbox(
        "Insurance Type",
        options=list(d1.keys()),
        help="Select the type of insurance coverage"
    )
    fuel_type = st.selectbox(
        "Fuel Type",
        options=list(d2.keys()),
        help="Select the fuel type of the car"
    )

with col2:
    transmission = st.selectbox(
        "Transmission",
        options=list(d3.keys()),
        help="Select the transmission type"
    )
    ownership = st.selectbox(
        "Ownership",
        options=list(d4.keys()),
        help="Select the ownership history"
    )

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=1_000_000,
    step=500,
    value=30000,
    help="Total kilometers the car has been driven"
)

st.divider()

# --- Predict Button ---
if st.button("Predict Price", type="primary", use_container_width=True):
    ins = d1[insurance_validity]
    fuel = d2[fuel_type]
    trans = d3[transmission]
    own = d4[ownership]

    test = [[ins, fuel, kms_driven, own, trans]]
    yp = int(final_model.predict(test)[0])

    st.success(f"### Estimated Resale Price: ₹ {yp:,}")
    st.caption("This is a model-based estimate and may vary from actual market prices.")
