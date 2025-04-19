from datetime import datetime  

# Get the current time in seconds to start  
start_time = datetime.now()  

# Prompt the user to enter something  
input_text = input("Enter something to check your typing speed: ")  

 
end_time = datetime.now()  

 
time_taken = (end_time - start_time).total_seconds()  



print(f"\nTime taken to type: {time_taken:.1f} seconds")  


num_characters = len(input_text)  


typing_speed_cpm = (num_characters / time_taken) * 60 if time_taken > 0 else 0  

print(f"Typing speed: {typing_speed_cpm:.2f} characters per minute")  