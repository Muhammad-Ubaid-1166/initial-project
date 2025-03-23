import streamlit as st
import re

st.title("Password Generator")

st.markdown("## enter you password to check its strength")

password = st.text_input("enter you password" , type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        feedback.append("password is long enough")
        score += 1
    else:
        feedback.append("password is too short")
    
    if re.search(r'[A-Z]', password):
        score += 0.5
    else:
        feedback.append("password should have at least one uppercase letter")
    if re.search(r'[a-z]', password):
        score += 0.5
    else:
        feedback.append("password should have at least one lowercase letter")
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("password should have at least one number")
    if re.search(r'[!@#$]', password):
        score += 1
    else:
        feedback.append("password should have at least one special character")

    if score == 4:
        feedback.append("password is strong")
    elif score == 3:
        feedback.append("password is medium")
    elif score == 2:
        feedback.append("password is weak")
    else:
        st.write("password is too weak")
    
    for i in feedback:
        st.markdown(f"### {i}")

    
else:
    st.write("please enter a password")
        
        
        
     
        
    


