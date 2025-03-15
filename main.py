from news_retriever import NewsRetriever
from embedding_engine import EmbeddingEngine
from summarizer import Summarizer
from user_manager import UserManager

def main():
    retriever = NewsRetriever()
    embedder = EmbeddingEngine()
    summarizer = Summarizer()
    user_manager = UserManager()

    print("📢 Welcome to News Summarizer!")
    
    while True:
        print("\nOptions: 1. Search News  2. View Preferences  3. View History  4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            topic = input("Enter topic to search: ")
            articles = retriever.fetch_articles(topic)
            user_manager.add_preference(topic)
            user_manager.add_history(topic)

            for article in articles:
                print(f"\nTitle: {article['title']}")
                summary_mode = input("Brief (b) or Detailed (d) summary? ").strip().lower()
                mode = "brief" if summary_mode == "b" else "detailed"

                embedder.store_article(article)
                summary = summarizer.summarize(article["content"], mode=mode)
                print(f"Summary: {summary}")

        elif choice == "2":
            print("\nYour Saved Preferences:")
            print(user_manager.get_preferences())

        elif choice == "3":
            print("\nSearch History:")
            print(user_manager.get_history())

        elif choice == "4":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
