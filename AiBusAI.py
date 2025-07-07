import streamlit as st
from google import genai
from PIL import Image
mybot =genai.Client(api_key="YOUR API KEY")
st.markdown(
    """
    <style>
    .st-emotion-cache-13k62yr {
        background: #3944BC;
    }
    </style>
    """,unsafe_allow_html=True)
spacer1, btn1_col, btn2_col, btn3_col = st.columns([5, 1, 1, 1])

with btn1_col:
    if st.button("Home"):
        st.write("you click Button Home")

with btn2_col:
    if st.button("login"):
        st.write("you click Button 2")

with btn3_col:
    if st.button("sign in"):
        st.write("you click Button 3")


col1,col2=st.columns(2)
with col1:
    st.title("Describer your business ideas here")
    business_name = st.text_input("1. What is your business's name?")
    business_description = st.text_area("2. Describe your business briefly..")
    target_audience = st.text_area("3. Who is your target audience?")
    current_capital = st.text_area("4. What is your current capital?")
    location = st.text_input("5. Which country and city are you starting your business in?")
    if st.button("generate"):
        if business_description and business_name and target_audience and current_capital and location:
            question = (
                f"My business is called {business_name}. "
                f"It is described as: {business_description}. "
                f"My target audience is {target_audience}. "
                f"Our current capital is {current_capital}. "
                f"We are starting in {location}. "
            )
            question+= "Can you provide suggestions to improve and grow my business?"
            response= mybot.models.generate_content(model="gemini-1.5-flash",
                                                    contents=question
                                                    )
        else:
            st.error("please fill the required fields.")
with col2:
    img_path = "robo.webp"
    mypick = Image.open(img_path)
    mypick = mypick.resize((700,900))
    st.image(mypick,caption=" ")

st.subheader("AI Suggestions:")
if response.text:
    st.write(response.text)



