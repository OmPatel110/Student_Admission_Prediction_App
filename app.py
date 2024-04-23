import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl', 'rb'))

def main():
    # Custom CSS for styling the title
    title_style = """
    <style>
        /* Custom CSS for the title */
        .title-text {
            color: #0874D1; /* Change text color to blue */
            font-size: 36px; /* Increase font size */
            font-weight: bold; /* Make text bold */
            text-align: left; /* Center-align text */
            margin-bottom: 20px; /* Add some bottom margin */
            margin-top: 0px;
        }
    </style>
    """
    # Display the styled title with emoji
    st.markdown(title_style, unsafe_allow_html=True)
    st.markdown("<h1 class='title-text'>Prediction of Student Admission 🎓 to University 🏛️</h1>", unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 400px;
    }
    </style>
    """, unsafe_allow_html=True)


# Set input field width
    st.markdown(
    """
    <style>
/* Input field width */
    div.stTextInput > div:first-child input[type="text"],
    div.stNumberInput > div:first-child input[type="number"],
    div.stSelectbox > div:first-child select {
        width: 300px;
        height: 40px;
        border-radius: 8px;
        border: 2px solid #1E88E5;
        padding: 5px 10px;
        font-size: 16px;
        color: #1E88E5;
        background-color: #F5F5F5;
    }

/* Increase spacing between input fields */
    .stTextInput, .stNumberInput, .stSelectbox {
        margin-bottom: 20px;
    }

/* Style the select box */
    div.stSelectbox > div:first-child::after {
        color: #1E88E5;
    }
    </style>
    """, unsafe_allow_html=True)

    # GRE score
    gre = st.number_input('GRE Score', min_value=0, max_value=340, value=0, step=1)

    # TOEFL score
    toefl = st.number_input('TOEFL Score', min_value=0, max_value=120, value=0, step=1)

    # University Rating
    university_rating = st.number_input('University Rating', min_value=1, max_value=5, value=1, step=1)

    # SOP
    sop = st.number_input('SOP (Statement of Puropse)', min_value=1.0, max_value=5.0, value=1.0, step=0.1)

    # LOR
    lor = st.number_input('LOR (Letter of Recommendation)', min_value=1.0, max_value=5.0, value=1.0, step=0.1)

    # CGPA
    cgpa = st.number_input('CGPA', min_value=1.0, max_value=10.0, value=1.0, step=0.1)

    # Research
    research = st.selectbox('Research', ['Yes', 'No'])

    if st.button('Predict'):
        research = 1 if research == 'Yes' else 0

        # Prepare input data as a DataFrame
        input_data = pd.DataFrame({
            'GRE Score': [gre],
            'TOEFL Score': [toefl],
            'University Rating': [university_rating],
            'SOP': [sop],
            'LOR ': [lor],
            'CGPA': [cgpa],
            'Research': [research]
        })

        # Make prediction using the pre-trained pipeline
        prediction = pipe.predict(input_data)[0]

       # Display the prediction result
        if prediction == 1:
            st.title('Prediction: Admitted')
            st.success("Congratulations! You've been admitted to the university. 🎉🎓")
            st.balloons()  # Show balloons animation
        else:
            st.title('Prediction: Not Admitted')
            st.error("Oops! It seems you were not admitted. Don't lose hope, try again harder! 💪📚")

if __name__ == "__main__":
    main()
