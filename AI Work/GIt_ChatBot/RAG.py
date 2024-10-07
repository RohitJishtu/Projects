import spacy
from annoy import AnnoyIndex
import os
import subprocess

class RAGSystemWithSpacy:
    def __init__(self, repo_path=None, model_name="en_core_web_md"):
        self.repo_path = repo_path
        self.nlp = spacy.load(model_name)
        self.index = AnnoyIndex(300, 'angular')  # 300-dimensional vectors
        self.document_embeddings = []
        self.file_list = []

    def _read_code_file(self, file_path):
        """Reads content from a code file (e.g., .py, .js)."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def index_documents(self):
        """Walk through the Git repo files and index them for retrieval."""
        file_counter = 0
        for root, _, files in os.walk(self.repo_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    try:
                        # Check if the file is a code file (e.g., .py, .js, .html, .css)
                        if file.endswith(('.py', '.js', '.html', '.css','.md')):
                            content = self._read_code_file(file_path)
                        else:
                            continue  # Skip non-code files and image files

                        doc = self.nlp(content)
                        embedding = doc.vector
                        if embedding.any():
                            self.document_embeddings.append(embedding)
                            self.index.add_item(file_counter, embedding)
                            self.file_list.append(file_path)
                            file_counter += 1
                    except Exception as e:
                        print(f"Could not read {file_path}: {e}")
        self.index.build(10)

    def retrieve_document(self, query, top_k=1):
        """Embed the query and retrieve the most similar document."""
        query_embedding = self.nlp(query).vector
        closest_document_ids = self.index.get_nns_by_vector(query_embedding, top_k)
        closest_files = [self.file_list[doc_id] for doc_id in closest_document_ids]
        return closest_files

    def generate_answer_with_spacy(self, document_path, query):
        """Generate a simple answer based on the retrieved document."""
        with open(document_path, 'r', encoding='utf-8') as f:
            document_content = f.read()
        return f"Found in document: {document_content[:500]}..."

    def ask_question(self, query):
        """Complete workflow: retrieve the document and generate an answer."""
        closest_documents = self.retrieve_document(query)
        if closest_documents:
            document_path = closest_documents[0]
            answer = self.generate_answer_with_spacy(document_path, query)
            return answer
        else:
            return "No relevant document found."

# # Example usage
# if __name__ == "__main__":
#     repo_url = "https://github.com/RohitJishtu/demo_azure_streamlit"
#     repo_path = "demo_azure_streamlit"

#     if not os.path.exists(repo_path):
#         subprocess.run(["git", "clone", repo_url])

#     rag_system = RAGSystemWithSpacy(repo_path=repo_path)
#     rag_system.index_documents()

#     query = "Summarise the repo?"
#     answer = rag_system.ask_question(query)
#     print(answer)
