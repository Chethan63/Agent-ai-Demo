
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# Section 1: Image Generator
st.header("Educosys Image Generator")
user_prompt = st.text_input("What do you want to generate image for?")

if st.button("Generate Image"):
    if not user_prompt:
        st.warning("Please enter the prompt!")
    else:
        try:
            with st.spinner("Generating image..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["Text", "Image"]
                    )
                )
            st.subheader("Generated Image")
            for part in response.candidates[0].content.parts:
                if getattr(part, "text", None) is not None:
                    st.write(part.text)
                elif getattr(part, "inline_data", None) is not None:
                    image = Image.open(BytesIO(part.inline_data.data))
                    st.image(image)
        except Exception as e:
            st.error(f"Error generating image: {e}")

# Section 2: Image Caption Generator
st.header("Educosys Image Caption Generator")
uploaded_image = st.file_uploader("Upload an image for caption generation", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image")

    if st.button("Generate Caption"):
        try:
            with st.spinner("Generating caption..."):
                # Convert image to bytes for Gemini API
                img_bytes = uploaded_image.read()
                gemini_image = types.Content(
                    parts=[
                        types.Part(text="What is this image?"),
                        types.Part(inline_data=types.Blob(mime_type=uploaded_image.type, data=img_bytes))
                    ]
                )
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=gemini_image
                )
                st.subheader("Generated Caption:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error generating caption: {e}")

# Section 3: YouTube Video Summarizer
st.header("Educosys YouTube Video Summarizer")
youtube_url = st.text_input("Enter YouTube Video URL")

if st.button("Summarize Video"):
    if not youtube_url:
        st.warning("No YouTube URL Present!")
    else:
        try:
            with st.spinner("Generating summary..."):
                # Gemini API does not natively support YouTube URLs; placeholder for future implementation
                st.error("YouTube summarization is not supported directly. Please extract transcript or use a supported API.")
        except Exception as e:
            st.error(f"Error generating summary: {e}")