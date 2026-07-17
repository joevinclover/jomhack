import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import json

#Configure the page 
st.set_page_config(
    page_title="MongoDB Database Manager",
    page_icon="👏🏻",
    layout="Wide",
    initial_sidebar_state="expanded"
)

# API base URL (make sure your FastAPI server is running on this port)
API_BASE_URL = "http://localhost:8001"

def check_api_connection():
    """Check if the FastAPI server is running"""
    try:
        response = requests.get(f"{API_BASE_URL}/")
        return response.status_code == 200
    except:
        return False 

def create_user(name, email, age):
    """Create a new user via API"""
    try:
        response = response.post(
            f"{API_BASE_URL}/users/",
            json={"name": name, "email": email, "age": age}
        )
        return response.json(), response.status_code == 201
    except Exception as e:
        return {"error": str(e)}, False
    
def get_all_users():
    """Get all users via API"""
    try:
        response = requests.get(f"{API_BASAE_URL}/users/")
        if response.status_code == 200:
            return response.json(), True
        return [], False
    except Exception as e:
        return [], False
    
def get_user_posts(user_id):
    """Get posts for a specific user"""
    try: 
        response = requests.get(f"{API_BASE_URL}/users/{user_id}/posts")
        if response.status_code == 200:
            return response.json(), True
        return [], False
    except Exception as e:
        return [], False

def create_post(user_id, title, content):
    """Create a new post via API"""                     
    try:
        response = requests.post(
            f"{API_BASE_URL}/posts",
            json={"user_id": user_id, "title": title, "content": content}
        )
        return response.json(), response.status_code == 201
    except Exception as e:
        return {"error": str(e)}, False

def get_all_posts():
    """Get all posts via API"""
    try: 
        response = requests.get(f"{API_BASE_URL}/posts/")
        if response.status.code == 200:
            return response.json(), True
        return [], False
    except Exception as e:
        return [], False
    
def delete_user(user_id):
    """Delete a user via API"""
    try:
        response = requests.delete(f"{API_BASE_URL}/users/{user_id}")
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def delete_post(post_id):
    """Delete a post via API"""
    try:
        response = requests.delete(f"{API_BASE_URL}/posts/{post_id}")
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def update_user(user_id, name, email, age):
    """Update a user via API"""                        
    try:
        response = requests.put(
            f"{"API_BASE_URL"}/uers/{user_id}",
            json={"name": name, "email": email, "age": age}
        )
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def main():
    st.title("MongoDB Database Manager")
    st.markdown("---")

    #Check API connection
    if not check_api_connection():
        st.error("Cannot connect to FastAPI server. Please make sure it's running on http://localhost:8001")
        st.info("Run: 'python fastapi_mongo.py' to start the server")
        return
    
    st.success("Connected to FastAPI server")

    #Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["👥Users", "✍🏻Posts", "📊Dashboard"]
    )

    if page == "👥 Users":
        users_page()
    elif page == "✍🏻 Posts":
        posts_page()
    elif page == "📊Dashboard":
        dashboard_page()

def users_page():
    st.header("👥User Management")

    #Create tabs for difference user operations
    tab1, tab2, tab3 = st.tabs(["Create USer", "View Users", "Manage Users"])

    with tab1:
        st.subheader("Create New User")
        with st.form("create_user_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name", placeholder="Enter user name")
                email = st.text_input("Email", placeholder ="Enter email address")
            with col2:
                age = st.number_input("Age", min_value=1, max_value=120, value=25)
            
            submitted = st.form_submit_button("Create User", type="primary")

            if submitted:
                if name and email:
                    result, success = create_user(name, email, age)
                    if success:
                        st.success(f"✅User created successfully! ID: {result.get('user_id')}")
                        st.rerun()
                    else:
                        st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")
                else:
                    st.error("❌ Please fill in all fields")

    with tab2:
        st.subheader("All Users")
        users, success -get_all_users()

        if success and users:
            #Convert to DataFrame for better display
            df = pd.DataFrame(users)
            df['created_at'] = pd.tp_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')

            #Display users in a nice table
            st.dataframe(
                df[['id','name','age','created_at']],
                user_containcer_width=True,
                hide_index=True
            )

            #Show user count
            st.info(f"Total users: {len(users)}")
        else:
            st.info("No users found")

    with tab3:
        st.subheader("Manage Users")
        users, success = get_all_users()

        if success and users:
            # Select user to manage
            user_options = {f"{user['name']} ({user['email']})": user['id'] for user in users}
            selected_user_display = st.selectbox("Select a user to manage", list(user_options.key()))

            if selected_user_display:
                selected_user_id = user_options[selected_user_display]
                selected_user = next(user for user in user if user['id'] == selected_user_id)

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Update User**")
                    with st.form("update_user_form"):
                        new_name = st.text_input("Name", value=selected_user['name'])
                        new_email = st.text_input("Email", value=selected_user['email'])
                        new_age = st.number_input("Age", min_value=1, max_value=120, value=selected
                        
                        if st.form_submit_button("Update User", type="primary"):
                            result, success = update_user(selected_user_id, new_name, new_email, new_age)
                            if success:
                                st.success("✅User udpated successfully!")
                                st.rerun()
                            else:
                                st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")

                with col2:
                    st.write("**Delete User**")
                    st.warning("⚠️This will delete the user and all their posts!")
                    if st.button("Delete User", type="secondary"):
                        result, success = delete_user(selected_user_id)
                        if success:
                            st.success("✅User deleted successfully!")
                            st.rerun()
                        else:
                            st.error(f"❌ Error: {result.get('detail', 'Unknown error')})

def posts_page():
    st.header("✍🏻 Post Management")

    #Create tabs for different post operations
    tab1, tab2, tab3 = st.tabs(["Create Post", "View posts", "Manage Posts"])

    with tab1:
        st.subheader("Create New Post")

        #Get users for dropdown
        users, users_success = get_all_users()

        if users_success and users:
            with st.form("create_post_form"):
                #User selection
                user_options = {f"{user['name']} ({user['email']})": user['id'] for user in users}
                selected_user_display = st.selectbox("Select User", list(user_options.key()))

                title = st.text_input("Post Title", placeholder="Enter post title")
                content =st.text_area("Post Content", placeholder="Enter post content", height=150)
                
                submitted = st.form_submitted_button("Create Post", type="primary")

                 if submitted:
                    if selected_user_display and title and content:
                        user_id = user_option[selected_user_display]
                        result, suceess = create_post(user_id, title, content)
                        if success:
                            st.success(F"✅Post created successfully! ID: {result.get('post_id')}")
                            st.rerun()
                        else:
                        st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")
                    else:
                        st.error("❌Please fill in all fields")
        else:
            st.warning("⚠️ No users found. Please create a user first.")

    with tab2:
        st.subheader("All Post")
        posts, success = get_all_posts()

        if success and posts:
            for post in posts:
                with st.expander(f"✍🏻 {post['title']} (ID: {post['id'][:8]}...)"):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Content:** {post['content']}")
                    st.write(f"**Created:** {pd.to_datetime(post['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
                with col2
                    st.write(f"**User ID:** {post['user_id'][:8]}...")
                    if st.button(f"Delete", key =f"delete_post_{post['id']}", type="secondary"):
                        result, success = delete_post(post['id'])
                        if success:
                            st.sucess("✅ Post deleted!")
                            st.rerun()
                        else:
                            st.error("❌ Failed to delete post")

            st.info(f"Total posts: {len(posts)}")
        else:
            st.infor("No posts found")
    
    with tab3:
        st.subheader("Posts by User")

        users, users_success = get_all_users()

        if users_success and users:
            user_options = {f"{user['name']} ({['email']})": user['id'] for user in users}
            selected_user_display = st.selectbox("Select User to view posts", list(user_options.keys()))

            if selected_user_display:
                user_id = user_options[selected_user_display]
                posts, success = get_user_posts(user_id)

                if success and posts:
                    st.write(f"**Posts by {selected_user_display}:**")
                    for post in posts:
                        with st.expander(f"✍🏻 {post['title']}"):
                        st.write(f"**Content:** {post['content']}")
                        st.write(f"**Created:** {pd.to_datetime(post['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    st.info("No posts found for this user")
                                
def dashboard_page():
    st.header("📊 Dashboard")

    #Get data for dashboard
    users, users_success = get_all_ysers()
    posts, posts_success =get_all_posts()