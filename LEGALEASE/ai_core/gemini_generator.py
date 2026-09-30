import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self, model_name="gemini-3.8-flash"):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model_name)

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = f"""
        Generate a professional legal {document_type}.
        Parties involved: {parties}
        Effective Date: {dates}
        Key Terms & Conditions: {terms}
        
        Ensure legal-grade formatting and clear headings.
        """
        response = self.model.generate_content(prompt)
        return response.text