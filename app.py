import loader as ld
import classifiers.keywords as keywords
import classifiers.llm as llm
import database as db

# loading the news data
news = ld.load_news()

articles_to_save = []
# Classifying keywords in the news articles

def classify_using_keywords():
    for article in news:
        title = article['name']
        description = article.get('description', '')    
        if db.find_document_by_name(article['name']) is not None:
            print(f"Skipping article: {article['name']} as it already exists in the database")
            continue
        category = keywords.classify_keywords(title, description)
        if category != 'other':
            print(article)
            articles_to_save.append(article)
            print(f"Inserting article: {article['name']} with category: {category}")
            db.insert_document({
                'name': article['name'],
                'type': article['type'],
                'url': article['url'],
                'description': article.get('description', ''),
                'category': category,
                'created_at': article.get('created_at'),
                'source_feed': article.get('source_feed')
            })




# Classifying using LLM
def classify_using_llm():
    for article in news:
        title = article['name']
        description = article.get('description', '')    
        if db.find_document_by_name(article['name']) is not None:
            print(f"Skipping article: {article['name']} as it already exists in the database")
            continue
        category = llm.classify_llm_ollama(title, description)
        print(f"Classified {title} as {category}")
        if category != 'other':
            print(article)
            articles_to_save.append(article)
            print(f"Inserting article: {article['name']} with category: {category}")
            db.insert_document({
                'name': article['name'],
                'type': article['type'],
                'url': article['url'],
                'description': article.get('description', ''),
                'category': category,
                'created_at': article.get('created_at'),
                'source_feed': article.get('source_feed')
            })



# Main execution
if __name__ == "__main__":
    pass
    #classify_using_keywords()
    #classify_using_llm()