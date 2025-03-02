#Project 02: Unit Convertor
#Build a Unit Convertor Using Python and Streamlit

import streamlit as st
# Custom CSS for enhanced UI (UI ko behtar bnane k liye custom styling)
st.markdown(
     """
     <style>
     body {
          background-color: #1e1e2f;
          color: white;
     }
     .stApp{
          background-color: linear-gradient(135deg, #bcbcbc, #cfe2f3);
          padding: 30px;
          border-radius: 15px;
          box-shadow: 0px 10px 30px rgba(0,0,0, 0.3);
     }
     h1 {
          text-align: center;
          font-size: 36px;
          color: white;
     }
     .stButton>button {
         background: linear-gradient(45deg, #0b5394, #351c75);
         color: white;
         font-size: 18px;
         padding: 10px 20px;
         border-radius: 10px;
         transition: 0.3s;
         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
     }   
     .stButton>button:hover {
     transform: scale(1.05);
     background: linear-gradient(45deg, #92fe9d, #00c9ff);
     color: black;

     }
     .result-box {
          font-size: 20px;
          font-weight: bold;
          text-align: center;
          background: rgba(255, 255, 255, 0.1);
          padding: 15px;
          border-radius: 10px;
          color: #00c9ff
          margin-top: 20px;
          box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3)
     }
     .footer {
          text-align: center;
          marging-top: 50px;
          font-size: 14px;
          color: white
     }
     </style>
     """,
     unsafe_allow_html=True
)

#title and description:
st.markdown("<h1> 🌍 Universal Unit Converter 🚀 </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of 📏 Length, ⚖️ Weight, and 🌡️ Temperature.")

#sidebar menu(conversion type select krne ka option)
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])

# Inpit value (User se value lene ke liye)
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

# Layout for unit selection (From ar To units select kerne ka setup )
col1, col2 = st.columns(2)



if conversion_type == "Length":
     with col1:
          from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])
     with col2:
          to_unit = st.selectbox("To",["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
     with col1:
          from_unit = st.selectbox("From", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
     with col2:
          to_unit = st.selectbox("To", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
     with col1:
          from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
     with col2:
          to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])



#Converter functions (alag alg coversions k liye functions)
def length_converter(value, from_unit, to_unit):
     #Length units ko conversion factor k zarye convert krna
     length_units = {
          'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milimeters': 1000,
          'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
     }
     return (value / length_units[from_unit]) * length_units[to_unit]
                  
def weight_converter(value, from_unit, to_unit):
     #Weight units ko conversion factor k zarye convert krna
     weight_units = {
          'Kilograms': 1, 'Grams': 1000, 'Miligrams' : 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
     }
     return (value / weight_units[from_unit]) * weight_units[to_unit] 



def temp_converter(value, from_unit, to_unit):
     
     # Temperature conversion logic
     if from_unit == "Celsius":
          return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
     elif from_unit == "Fahrenheit":
          return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
     elif from_unit == "Kelvin":
          return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
     return value

# Convert button (conversion krne ka button)
if st.button("🤖Convert"):
     if conversion_type == "Length":
          result = length_converter(value, from_unit, to_unit)
     elif conversion_type == "Weight":
          result = weight_converter(value, from_unit, to_unit)
     elif conversion_type == "Temperature":
          result = temp_converter(value, from_unit, to_unit)

     # Result dikhana(Conversion resilt show krna)
     st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
     
# Footer message
st.markdown(
    """
    <div style="
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        background: linear-gradient(135deg, #0b5394, #351c75);
        color: white;
        border-radius: 15px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
        font-size: 16px;
    ">
        <p>Created with 💕 by <b>Muniza Nabeel</b></p>
        <p>🚀 Empowering users to explore the world of conversions!</p>
        <p>Follow me on 
            <a href="https://github.com/Muniza-NAbeel" style="color: #92fe9d; text-decoration: none;" target="_blank">GitHub</a> | 
            <a href="https://www.linkedin.com/in/muniza-malik-59826930a/" style="color: #00c9ff; text-decoration: none;" target="_blank">LinkedIn</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


