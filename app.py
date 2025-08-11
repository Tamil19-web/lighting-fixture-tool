import streamlit as st
import pandas as pd

# Load demo dataset (replace path if needed)
@st.cache_data
def load_data():
    return pd.read_csv('lighting_fixture_demo_dataset.csv')

df = load_data()

st.title("Lighting Fixture Equivalent Search Tool")

uploaded_file = st.file_uploader("Upload Site Image", type=["jpg", "jpeg", "png"])

brand_list = df["Brand"].unique().tolist()
selected_brand = st.selectbox("Select Brand", brand_list)

if uploaded_file and selected_brand:
    st.image(uploaded_file, caption="Uploaded Site Image", use_column_width=True)

    st.write(f"Showing top 3 equivalent fixtures for brand: {selected_brand}")

    filtered = df[df["Brand"] == selected_brand].head(3)

    for _, row in filtered.iterrows():
        st.write(f"**Model:** {row['Model']}")
        st.write(f"Lumen Output: {row['Lumen Output']} lm")
        st.write(f"Color Temperature: {row['Color Temperature (K)']} K")
        st.write(f"Wattage: {row['Wattage (W)']} W")
        st.write(f"IP Rating: {row['IP Rating']}")
        st.write(f"Cost: ${row['Cost (USD)']}")
        st.write(f"Lead Time: {row['Lead Time (Days)']} days")
        st.image(row['Image URL'], width=200)
        st.markdown("---")
else:
    st.info("Please upload an image and select a brand.")
