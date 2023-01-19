import streamlit as st
import spacy
from spacy import displacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Create a main function
def main():
  # Add a text area for the user to input text
  text = st.text_area("Enter some text")

  # Add a button to trigger the named entity recognition
  if st.button("Recognize entities"):
    # Process the text using the SpaCy model
    doc = nlp(text)

    # Extract the named entities from the document
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    # Create an HTML representation of the named entities using displaCy
    html = displacy.render(doc, style="ent")

    # Display the HTML in the app using Streamlit's markdown function
    st.markdown(html, unsafe_allow_html=True)

# Run the main function
if __name__ == "__main__":
  main()
