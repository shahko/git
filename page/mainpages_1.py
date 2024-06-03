import streamlit as st

# 사용자 데이터 (예제에서는 간단하게 딕셔너리로 저장)
# 실제로는 데이터베이스에 저장된 데이터를 불러와야 합니다.
users = {
    "user1": "password1",
    "user2": "password2"
}

def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

def main():
    st.title("로그인 시스템")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        st.success("성공적으로 로그인하였습니다!")
        st.write("여기서 애플리케이션의 메인 내용을 보여줄 수 있습니다.")
        if st.button("로그아웃"):
            st.session_state["logged_in"] = False
    else:
        username = st.text_input("사용자 이름")
        password = st.text_input("비밀번호", type="password")

        if st.button("로그인"):
            if login(username, password):
                st.session_state["logged_in"] = True
                st.success("성공적으로 로그인하였습니다!")
            else:
                st.error("사용자 이름 또는 비밀번호가 잘못되었습니다.")

if __name__ == "__main__":
    main()
