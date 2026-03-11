import streamlit as st

st.set_page_config(page_title="Water Potability Checker", layout="centered")

st.title("💧 Water Potability Checker")
st.subheader("Enter Water Quality Parameters")

# Input parameters
ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, format="%.1f")

arsenic = st.number_input(
    "Arsenic (mg/L)", min_value=0.0, step=0.001, format="%.3f"
)

lead = st.number_input(
    "Lead (mg/L)", min_value=0.0, step=0.001, format="%.3f"
)

fluoride = st.number_input(
    "Fluoride (mg/L)", min_value=0.0, step=0.1, format="%.2f"
)

nitrate = st.number_input(
    "Nitrate (mg/L)", min_value=0.0, step=1.0
)

iron = st.number_input(
    "Iron (mg/L)", min_value=0.0, step=0.01, format="%.2f"
)

st.write("---")

if st.button("Check Water Quality"):

    score = 100
    unsafe = False

    st.subheader("Parameter Status")

    col1, col2 = st.columns(2)

    # pH
    if ph < 6.5 or ph > 8.5:
        col1.error("⚠️ pH Unsafe")
        score -= 20
        unsafe = True
    else:
        col1.success("✅ pH Safe")

    # Arsenic
    if arsenic > 0.01:
        col2.error("⚠️ Arsenic Unsafe")
        score -= 20
        unsafe = True
    else:
        col2.success("✅ Arsenic Safe")

    col3, col4 = st.columns(2)

    # Lead
    if lead > 0.01:
        col3.error("⚠️ Lead Unsafe")
        score -= 20
        unsafe = True
    else:
        col3.success("✅ Lead Safe")

    # Fluoride
    if fluoride > 1.0:
        col4.error("⚠️ Fluoride Unsafe")
        score -= 20
        unsafe = True
    else:
        col4.success("✅ Fluoride Safe")

    col5, col6 = st.columns(2)

    # Nitrate
    if nitrate > 45:
        col5.error("⚠️ Nitrate Unsafe")
        score -= 10
        unsafe = True
    else:
        col5.success("✅ Nitrate Safe")

    # Iron
    if iron > 0.3:
        col6.error("⚠️ Iron Unsafe")
        score -= 10
        unsafe = True
    else:
        col6.success("✅ Iron Safe")

    st.write("---")

    # Safety Score
    st.subheader("Water Safety Score")
    st.progress(score / 100)
    st.write(f"### Safety Score: {score}%")

    if unsafe:
        st.error("❌ Water is NOT Drinkable")
    else:
        st.success("✅ Water is Safe to Drink")