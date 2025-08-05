KEYWORDS = {
    'technology': ['AI', 'tech', 'software', 'digital', 'app', 'coding', 'robot', 'machine learning'],
    'culture': ['art', 'music', 'cinema', 'museum', 'culture', 'artist', 'book', 'exhibition']
}

def classify_keywords(title, description):
    text = (title + ' ' + description).lower()    
    scores = {}
    for category, words in KEYWORDS.items():
        scores[category] = sum(1 for word in words if word.lower() in text)
    
    if max(scores.values()) == 0:
        return 'other'
    print(f"Scores: {scores}")  # Debugging line to see scores  
    return max(scores, key=scores.get)

