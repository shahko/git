import streamlit as st

# 사용자 데이터베이스 예제 (간단한 딕셔너리)
user_db = {
    "user1": "password1",
    "user2": "password2"
}

# 세션 상태를 초기화합니다.
if 'login_status' not in st.session_state:
    st.session_state.login_status = False
if 'username' not in st.session_state:
    st.session_state.username = ''

def login(username, password):
    if username in user_db and user_db[username] == password:
        st.session_state.login_status = True
        st.session_state.username = username
    else:
        st.error("Invalid username or password")

def logout():
    st.session_state.login_status = False
    st.session_state.username = ''

def main():
    st.title("Login Page")

    if st.session_state.login_status:
        st.write(f"Welcome, {st.session_state.username}!")
        if st.button("Logout"):
            logout()
    else:
        st.subheader("Please log in")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            login(username, password)

if __name__ == "__main__":
    main()
