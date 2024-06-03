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
        st.error("사용자 이름 또는 비밀번호가 잘못되었습니다")

def logout():
    st.session_state.login_status = False
    st.session_state.username = ''

def main():
    st.title("로그인 페이지")

    if st.session_state.login_status:
        st.write(f"{st.session_state.username}님, 환영합니다!")
        if st.button("로그아웃"):
            logout()
    else:
        st.subheader("로그인 해주세요")
        username = st.text_input("사용자 이름")
        password = st.text_input("비밀번호", type='password')
        if st.button("로그인"):
            login(username, password)

if __name__ == "__main__":
    main()
