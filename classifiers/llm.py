import config as cfg
from openai import OpenAI
import google.generativeai as genai

config = cfg.Config()
genai.configure(api_key=config.GOOGLE_API_KEY)

openai_client = OpenAI(api_key=config.OPEN_AI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')




def classify_llm_openai(title, description):
    try:
        prompt = f"""
        You are a news classifier. 
        Given a title and description of a news article, classify it into one of the following categories: technology, culture, or other.
        Description can be empty.
        Title: {title}
        Description: {description}
        """
        
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5
        )
        
        result = response.choices[0].message.content.strip().lower()
        return result if result in ['technology', 'culture'] else 'other'
        
    except Exception as e:
        print(f"LLM Error: {e}")
        return 'other'
    

def classify_llm_gemini(title, description):
    try:
        text = f"Title: {title}\nDescription: {description[:300] if description else ''}"        
        prompt = f"""
        Classify this news article into exactly one category: technology, culture, or other.
        
        Categories:
        - technology: AI, software, gadgets, programming, tech companies, digital innovation and all around technology.
        - culture: arts, music, cinema, literature, museums, entertainment, creative works and all around culture.
        - other: politics, sports, economics, health, etc.
        
        Article:
        {text}
        
        Answer with only one word: technology, culture, or other
        """
        
        response = model.generate_content(prompt)
        result = response.text.strip().lower()
        
        # Validation
        valid_categories = ['technology', 'culture', 'other']
        if result in valid_categories:
            return result
        else:
            print(f"Invalid Gemini response: {result}")
            return 'other'
            
    except Exception as e:
        print(f"Gemini Error: {e}")
        return 'other'