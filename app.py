import streamlit as st
from pptx import Presentation
import os
from io import BytesIO
from PIL import Image
from pdf2image import convert_from_path


def display_pdf_slide(pdf_path):
    images = convert_from_path(pdf_path)

    for image in images:
        st.image(image, use_column_width=True)

def topic_1():
    st.title("Introduction to Hepatitis B")
    st.write("Add your introduction content here.")

    # Interactive Quiz
    st.header("Quiz: What is the primary mode of hepatitis B transmission?")
    options = ["A. Sexual contact", "B. Sharing needles", "C. Mother to child during childbirth", "D. All of the above"]
    correct_answer = "D. All of the above"

     # Display the radio button for user choice and set default value to an empty string
    user_choice = st.radio("Select your answer:", ["None"] + options)

    # Check if the user has made a selection
    if user_choice != "None":
        if user_choice == correct_answer:
            st.success("Correct! All of the above are primary modes of hepatitis B transmission.")
        else:
            st.error(f"Wrong! The correct answer is: {correct_answer}")
            
    # Embed YouTube video
    st.header("Watch the Introduction Video")
    video_url = "https://www.youtube.com/embed/Uos0zzzQ_Bw"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)




def topic_2():
    st.title("Modes of Transmission of HBV")
    st.write("Add your content about modes of transmission here.")
    
def topic_3():
    st.title("Prevention of HBV")
    st.write("Add prevention contents here.")
    
def topic_4():
    st.title("Prevention of Mother to Child Transmission of HBV")
    st.write("Add pmtct content here.")
    
def topic_5():
    st.title("Symptoms, Signs & Outcomes of HBV Infection")
    st.write("Add your signs and symptoms content here.")
    
def topic_6():
    st.title("Understanding Laboratory Tests for HBV")
    st.write("Add your serology content here.")
    
def topic_7():
    st.title("Outcome & Treatment of Acute HBV Infection")
    st.write("Add treatment of acute hbv content here.")

def topic_8():
    st.title("Criteria for Treatment of Chronic HBV Infection")
    st.write("Add treatment criteria for chronic hbv content here.")
    
    # Add any interactive elements, quizzes, or additional resources for Topic 2

# Define functions for the other topics (topic_3 to topic_8)

def main():
    st.title("🦠 Hepatitis B Course")
    st.write("Welcome to this Intermediate level Hepatitis B Course!")

    # List of bundled slide PDFs
    bundled_slides = {
        "Introduction": "slides/slide1.pdf",
        "Modes of Transmission of HBV": "slides/slide2.pdf",
        "Prevention of HBV": "slides/slide3.pdf",
        "Prevention of Mother to Child Transmission of HBV": "slides/slide4.pdf",
        "Symptoms, Signs & Outcomes of HBV Infection": "slides/slide5.pdf",
        "Understanding Laboratory Tests for HBV": "slides/slide6.pdf",
        "Outcome & Treatment of Acute HBV Infection": "slides/slide7.pdf",
        "Criteria for Treatment of Chronic HBV Infection": "slides/slide8.pdf",
        # Add more bundled slides as needed
    }

    selected_topic = st.selectbox("Select a Topic", list(bundled_slides.keys()))

    if st.button("🔍Display Topic Contents"):
        slide_path = bundled_slides[selected_topic]
        display_pdf_slide(slide_path)

    # Call the corresponding topic function based on user selection
    if selected_topic == "Introduction":
        topic_1()
    elif selected_topic == "Modes of Transmission of HBV":
        topic_2()
    elif selected_topic == "Prevention of HBV":
        topic_3()
    elif selected_topic == "Prevention of Mother to Child Transmission of HBV":
        topic_4()
    elif selected_topic == "Symptoms, Signs & Outcomes of HBV Infection":
        topic_5()
    elif selected_topic == "Understanding Laboratory Tests for HBV":
        topic_6()
    elif selected_topic == "Outcome & Treatment of Acute HBV Infection":
        topic_7()
    elif selected_topic == "Criteria for Treatment of Chronic HBV Infection":
        topic_8()
    # Call functions for the other topics (topic_3 to topic_8) here

if __name__ == "__main__":
    main()
