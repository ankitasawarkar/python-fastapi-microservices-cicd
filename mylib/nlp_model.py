import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A lazy dog is sleeping under a tree.",
    "The fox is very quick and agile.",
    "A quick brown rabbit jumps over the fence."
]

# Preprocessing function: Lemmatizes text and removes stopwords/punctuation
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    
    if not tokens:  # If the processed document is empty
        print(f"Warning: Processed document is empty after preprocessing.")
        return None  # Or you can return the original text if needed
    
    return " ".join(tokens)




# Function to find similar documents
def find_similar_documents(query, tfidf_matrix, documents, vectorizer, n=2):
    """
    Finds the top-n similar documents to the query using cosine similarity.

    Args:
        query (str): The search query.
        tfidf_matrix: The TF-IDF matrix of the documents.
        documents (list): List of original documents.
        vectorizer: The TF-IDF vectorizer.
        n (int): Number of similar documents to retrieve.

    Returns:
        list: List of tuples with similar documents and their similarity scores.
    """
    # Filter out any documents that became empty after preprocessing
    processed_documents = [preprocess_text(doc) for doc in documents]
    processed_documents = [doc for doc in processed_documents if doc]  # Remove None or empty strings

    # Preprocess the query
    #query_processed = preprocess_text(query)

    # Transform the query into TF-IDF
    query_tfidf = vectorizer.transform([processed_documents])
    
    # Calculate similarity scores
    similarity_scores = cosine_similarity(query_tfidf, tfidf_matrix)[0]
    similar_indices = similarity_scores.argsort()[-n:][::-1]

    return [(documents[i], similarity_scores[i]) for i in similar_indices]

def find_similarity(documents, query):
    """
    Finds and returns the top similar documents for a given query.

    Args:
        documents (list): List of original documents.
        query (str): The search query.

    Returns:
        str: Formatted string with similar documents and their similarity scores.
    """
    # Preprocess all documents
    processed_documents = [preprocess_text(doc) for doc in documents]

    # Vectorize the documents
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_documents)

    # Find similar documents
    similar_docs = find_similar_documents(query, tfidf_matrix, documents, vectorizer)

    # Prepare the result string
    result = f"\n🔍 Similar documents to '{query}':\n"
    for doc, score in similar_docs:
        result += f"- {doc} (Similarity Score: {score:.2f})\n"
    
    return result


# Example usage
query = "convolutional neural networks"
documents= ("Most modern deep learning models are based on multi-layered neural networks "
    "such as convolutional neural networks and transformers, although they can "
    "also include propositional formulas or latent variables organized layer-wise "
    "in deep generative models such as the nodes in deep belief networks and deep "
    "Boltzmann machines.")
result = find_similarity(documents, query)
print(result)
