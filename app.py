import loader as ld
import classifiers.keywords as keywords
import classifiers.llm as llm
import database as db

# loading the news data
news = ld.load_news()

articles_to_save = []
# Classifying keywords in the news articles
""" 
for article in news:
    title = article['name']
    description = article.get('description', '')    
    category = keywords.classify_keywords(title, description)
    if category != 'other':
        print(article)
        articles_to_save.append(article)
        if db.find_document_by_name('news', article['name']) is None:
            print(f"Inserting article: {article['name']} with category: {category}")
            db.insert_document('news', {
                'name': article['name'],
                'type': article['type'],
                'url': article['url'],
                'category': category
            })
        else:
            print(f"Skipping article: {article['name']} with category: {category}") """



# Classifying using LLM
for article in news:
    title = article['name']
    description = article.get('description', '')    
    category = llm.classify_llm_gemini(title, description)
    print(f"Classified {title} as {category}")
    if category != 'other':
        print(article)
        articles_to_save.append(article)
        if db.find_document_by_name('news', article['name']) is None:
            print(f"Inserting article: {article['name']} with category: {category}")
            db.insert_document('news', {
                'name': article['name'],
                'type': article['type'],
                'url': article['url'],
                'category': category
            })
        else:
            print(f"Skipping article: {article['name']} with category: {category}")