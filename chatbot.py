import pandas as pd

# Load the dataset
df = pd.read_csv('tamil_nadu_schemes.csv')  # Change this to your dataset path

df.columns.tolist()

# Function to get scheme information
def get_scheme_info(scheme_name):
    try:
        # Search for the scheme in the dataset (case insensitive)
        scheme_info = df[df['Scheme Name'].str.lower() == scheme_name.lower()]

        if not scheme_info.empty:
            description = scheme_info.iloc[0]['Description']
            eligibility = scheme_info.iloc[0]['Eligibility']
            benefits = scheme_info.iloc[0]['Benefits']
            application_process = scheme_info.iloc[0]['Application Process']
            
            response = (
                f"*Scheme Name*: {scheme_info.iloc[0]['Scheme Name']}\n\n"
                f"*Description*: {description}\n\n"
                f"*Eligibility*: {eligibility}\n\n"
                f"*Benefits*: {benefits}\n\n"
                f"*Application Process*: {application_process}\n\n"
                "For further inquiries, feel free to ask about other schemes!"
            )
            
            return response
        else:
            return "I'm sorry, but I couldn't find any information regarding that scheme. Please check the name and try again."
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"

# Main chatbot loop
print("Welcome to the Tamil Nadu Schemes Chatbot!")
print("You can inquire about any government scheme or type 'exit' to stop.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Thank you for using the Tamil Nadu Schemes Chatbot. Have a great day!")
        break
    
    response = get_scheme_info(user_input)
    print("Schemegenie Bot:\n", response)