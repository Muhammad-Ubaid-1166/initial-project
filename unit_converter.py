import streamlit as st
st.title("Unit Converter")



catogory = st.selectbox("select the catagory of unit",("meter","centimeter","kilogram","gram","tonne","pounds to kilogram","kilogram to pounds"))
if catogory == "meter":
    input_unit = st.number_input("enter the number")
elif catogory == "centimeter":
    input_unit = st.number_input("enter the number")
elif catogory == "kilogram":
    input_unit = st.number_input("enter the number")
elif catogory == "gram":
    input_unit = st.number_input("enter the number")
elif catogory == "tonne":
    input_unit = st.number_input("enter the number")
elif catogory == "pounds to kilogram":
    input_unit = st.number_input("enter the number")
elif catogory == "kilogram to pounds":
    input_unit = st.number_input("enter the number")


if catogory:
    option = st.selectbox("select the option to convert",("centimeter","meter","gram","kilogram","tonne to kilogram","pounds to kilogram","kilogram to pounds"))
    if option == "centimeter":
        result = input_unit * 100
        if st.button("convert it in to centimeter"):
            st.write(f"the result is {result}")

    elif option == "meter":
        result = input_unit / 100
        if st.button("convert it in to meter"):
            st.write(f"the result is {result}")
    elif option == "gram":
        result = input_unit * 1000
        if st.button("convert it in to gram"):
            st.write(f"the result is {result}")
    elif option == "kilogram":
        result = input_unit / 1000
        if st.button("convert it in to gram"):
            st.write(f"the result is {result}")
    elif option == "tonne to kilogram":
        result = input_unit * 1000
        if st.button("convert it in to kilogram"):
            st.write(f"the result is {result}")
    elif option == "pounds to kilogram":
        result = input_unit * 2.25
        if st.button("convert it in to kilogram"):
            st.write(f"the result is {result}")
            
        
            
    






