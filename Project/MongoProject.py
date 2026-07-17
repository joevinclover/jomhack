
from pymongo import MongoClient
from datetime import datetime, date
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from  .env file 

mongo_uri = os.getenv('MONGODB_ATLAS_CLUSTER_URI')

class DatabaseManager:
    def __init__(self, db_name='example_db', connection_string=mongo_uri):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.diary_collection = self.db.diary
        self.init_database()

    def init_database(self):
        """Initializa database with collections and indexes"""
        
        self.diary_collection.create_index("date", unique=True)
 
    def create_diary(self, title, content, weather, mood, tag):
        """Create a new daily diary entry"""
        try:
            today_date = str(date.today())

            diary_doc = {
                "date": today_date,
                "title": title,
                "content": content,
                "weather": weather,
                "mood": mood,
                "tag": tag,
                "created_at": datetime.now()
            }
            result = self.diary_collection.insert_one(diary_doc)
            return str(result.inserted_id)
        
        except Exception as e:
            print(f"Error creating diary post: {e}")
            return None
            
    def get_all_diary_posts(self):
        """Get diary post, sort from newest to oldest"""

        try:
            posts = list(self.diary_collection.find(
            {}
            ).sort("created_at", -1))

            # Convert MongoDB's special _id into a clean Python string
            for post in posts:
                post['_id'] = str(post['_id'])

            return posts
        except Exception as e:
            print(f"Error retrieving posts: {e}")
            return []

    def edit_diary_posts(self, target_date, title=None, content=None, weather=None, mood=None, tag=None):
        """Edit diary posts of any day"""

        try:
            update_fields = {}
            if title is not None: 
                update_fields["title"] = title
            if content is not None: 
                update_fields["content"] = content
            if weather is not None: 
                update_fields["weather"] = weather
            if mood is not None: 
                update_fields["mood"] = mood
            if tag is not None: 
                update_fields["tag"] = tag
        
            if not update_fields:
                return False

            # 2. Tell MongoDB to update the document matching that specific date
            result = self.diary_collection.update_one(
                {"date": target_date},           # Finds the specific day you asked for
                {"$set": update_fields}          # Applies your changes
            )
            return result.matched_count > 0
        
        except Exception as e:
            print(f"Error editing diary post: {e}")
        return False

    def delete_diary_post(self, target_date):
        """Delete a specific day's diary posts"""
        try:
            # Delete the post
            result = self.diary_collection.delete_one({"date": target_date})
            
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting diary post: {e}")
            return False
    
    def close_connection(self):
        """Close the MongoDB connection"""
        self.client.close()
        
def display_menu():
    """Personal Diary App"""
    print("\n" + "="*40)
    print("       DATABASE MANAGER")
    print("="*40)
    print("1. Create Diary Entry")
    print("2. View All Diary Posts")
    print("3. Edit Entry")
    print("4. Delete Entry")
    print("5. Exit")
    print("-"*40)

def main():
    """Main interactive CLI function"""
    try:
        db = DatabaseManager()
        print("Connected to MongoDb successfully!")
    except Exception as e:  
        print(f" Failed to connect to MongoDB: {e}")
        print("Make sure MongoDB is running on localhost:27017")
        return
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            print("\n--- Personal Diary App ---")
            Title = input("Enter Title: ").strip()
            Content = input("Enter Content: ").strip()
            Weather = input("Enter weather (Sunny/Windy/Rainy): ").strip()
            Mood = input("Enter mood (Happy/Sad/OK/Excited/Stressed): ").strip()
            Tag = input("Tag: ").strip()

            inserted_diary = db.create_diary(Title, Content, Weather, Mood, Tag)
            
            if inserted_diary:
                    print(f"Post created successfully! New post: {inserted_diary}")
            else:
                    print("Failed to create post")
        
        elif choice == '2':
            print("\n--- View All Diary Posts ---")
            posts = db.get_all_diary_posts()
            if posts:
                for post in posts:
                    print(f"Date: {post['date']} | Title: {post['title']} | Content: {post['content']} | Weather: {post['weather']} | Mood: {post['mood']} | Tag: {post['tag']} | Created At: {post['created_at']}")
                    print("-" * 30)
            else:
                print("No posts found for this user.")
        
        elif choice == '3':
            print("\n--- Edit Entry ---")
            target_date = input("Enter the date of the post to edit (YYYY-MM-DD): ").strip()
            print("Leave input blank and press Enter to keep the original value.")
            
            new_title = input("Enter new Title: ").strip() or None
            new_content = input("Enter new Content: ").strip() or None
            new_weather = input("Enter new Weather: ").strip() or None
            new_mood = input("Enter new Mood: ").strip() or None
            new_tag = input("Enter new Tag: ").strip() or None
            
            success = db.edit_diary_posts(    
                target_date, 
                new_title, 
                new_content, 
                new_weather, 
                new_mood, 
                new_tag
            )
            if not success:
                print("❌ Edit failed.")

        elif choice == '4':
            print("\n--- Delete Entry ---")
            target_date = input("Enter the date of the post to delete (YYYY-MM-DD): ").strip()
            confirm = input(f"Are you sure you want to delete post with title {target_date}? y/N: ").strip().lower()
            if confirm == 'y':
                if db.delete_diary_post(target_date):
                    print("Post deleted successfully!")
                else:
                    print("Post not found or deletion failed.")
            else:
                print("Deletion cancelled.")
        
        elif choice == '5':
            print("\nClosing database connection...")
            db.close_connection()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
