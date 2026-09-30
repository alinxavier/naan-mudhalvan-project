import streamlit as st
import requests

st.set_page_config(page_title="LegalEase", layout="wide")

st.title("LegalEase: AI-Powered Legal Document Generator")

# Inputs
document_type = st.text_input("Document Type (e.g. Freelance Work Contract)")
parties = st.text_area("Parties Involved (e.g. Jane Doe (Provider), TechNova Inc. (Client))")
terms = st.text_area("Terms & Conditions (separate with semicolons)")
dates = st.text_input("Effective Date")

if st.button("Generate Document"):
    payload = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "dates": dates
    }
    
    # FastAPI Backend-ലേക്ക് POST റിക്വസ്റ്റ് അയക്കുന്നു
    response = requests.post("http://127.0.0.1:8000/generate", json=payload)
    
    if response.status_code == 200:
        generated_text = response.json().get("generated_text")
        st.session_state["generated_text"] = generated_text
        st.success("Document Generated Successfully!")

if "generated_text" in st.session_state:
    edited_text = st.text_area("Edit Document", st.session_state["generated_text"], height=300)
    st.session_state["generated_text"] = edited_text
    
    # ഡൗൺലോഡ് ബട്ടൺ
    st.download_button("Download as TXT", data=edited_text, file_name="legal_doc.txt", mime="text/plain")