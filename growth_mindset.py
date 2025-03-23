import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.title("Growth Mindset")
st.markdown("## Upload Your File")

# File uploader
file_upload = st.file_uploader("Upload your file", type=["csv", "xlsx"]) # it upload the file to the app

if file_upload: #  a condition
    # Extract file extension
    file_ext = os.path.splitext(file_upload.name)[-1].lower() # it split the file name and extension and then it will chose its outer part which is the extension

    # Read the file based on its extension
    if file_ext == ".csv": # it will read the file as a csv file
        df = pd.read_csv(file_upload) # it will read with the help of pd which is a library of pandas
    elif file_ext == ".xlsx": # it will read the file as a excel file
        df = pd.read_excel(file_upload) # it will read with the help of pd which is a library of pandas
    else:
        st.error("Invalid file type") # it will show an error if the file is not a csv or excel file

    # Display file details
    st.write(f"File Name: {file_upload.name}") # it will show the file name
    st.write(f"File Size: {file_upload.size} bytes") # it will show the file size in bytes

    # Display a preview of the file
    st.write("Preview of the file:") # it will show the preview of the file
    st.dataframe(df.head()) # it will show the first 5 rows of the file

    # Checkbox for cleaning data
    if st.checkbox(f"Clean data for {file_upload.name}"): # fist condition of checkbox
        col1, col2 = st.columns(2) # it will create 2 columns

        with col1:
            # Remove duplicate rows
            if st.button("Remove duplicate rows"): # second condition of button
                df.drop_duplicates(inplace=True)  # No need to reassign
                st.write("Duplicates removed") # it will show a message that the duplicates are removed
                st.dataframe(df)  # Display the updated DataFrame after removing duplicates

        with col2:
            # Fill missing values
            if st.button(f"Fill missing values for {file_upload.name}"): # third condition of button
                numerical_cols = df.select_dtypes(include=['number']).columns
                df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
                st.write("Missing values filled")
                st.dataframe(df)  # Display the updated DataFrame after filling missing values

    # Data analysis
    st.subheader(f"Data Analysis for {file_upload.name}") # it will show the data analysis for the file
    columns = st.multiselect( # it will create a multiselect for the columns
        f"Select columns for analysis for {file_upload.name}", # it will show the columns for the analysis
        df.columns, # it will show the columns of the file
        default=df.columns # it will show the default columns
    )
    df = df[columns] # now the df variable is convert in to df[columns]

    # Visualization
    st.subheader(f"Visualization for {file_upload.name}") # it will show the visualization for the file
    if st.checkbox(f"Show visualization for {file_upload.name}"): # fourth condition of checkbox
        st.bar_chart(df.select_dtypes(include=['number'])) # it will show the bar chart for the file like a map and the select_dtypes is a function of pandas that is used to select the columns that are of a certain data type

    # File conversion
    st.subheader("Conversion Data Type") # it will show the conversion data type
    conversion_type = st.radio( # it will create a radio for the conversion data type
        f"Convert {file_upload.name} to",
        ["csv", "xlsx"] # it will show the options for the conversion data type that what should be the output file or chose your option
    )

    if st.button(f"Convert {file_upload.name}"): # fifth condition of button
        buffer = BytesIO() # it will create a buffer , buffer is a function of io which is a library of python which is used to store the data in a temporary memory and the full form of buffer is binary input output,  and the full form of BytesIO is binary input output stream

        if conversion_type == "csv": # sixth condition of button
            df.to_csv(buffer, index=False)  # Save DataFrame as CSV in buffer
            file_name = file_upload.name.replace(file_ext + ".csv", "csv") # it will replace the file extension with the csv extension
            mime_type = "text/csv"  # MIME type for CSV files , mimme is a function of io which is a library of python which is used to store the data in a temporary memory and the full form of mime is multi-purpose internet mail extensions , text/csv is a type of mime type it's means that the file is a csv file.

        elif conversion_type == "xlsx": # seventh condition of button
            df.to_excel(buffer, index=False)  # Save DataFrame as Excel in buffer
            file_name = file_upload.name.replace(file_ext, "xlsx") # it will replace the file extension with the xlsx extension
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME type for Excel files , it is a extension of excel file

        # Move the buffer's cursor to the beginning
        buffer.seek(0) # it will move the buffer's cursor to the beginning

        # Download the file
        st.download_button(
            label=f"Download {file_name}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )
        if st.download_button:
                st.success("Data saved to database")

