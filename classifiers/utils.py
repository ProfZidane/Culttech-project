from langchain.schema import OutputParser

class CategoryParser(OutputParser):
    def parse(self, text: str) -> str:
        text = text.strip().lower()
        
        if 'technology' in text:
            return 'technology'
        elif 'culture' in text:
            return 'culture'
        else:
            return 'other'
