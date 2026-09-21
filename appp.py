if st.session_state.page == "home":

    st.title("🧠 QuizCraft")
    st.subheader("Smart Quiz Generator")
    st.write("Turn your study material into an interactive quiz.")
    st.divider()

    st.subheader("Why QuizCraft?")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.subheader("📄 PDF & Text")
            st.write(
                "Enter your notes or upload a PDF as study material."
            )

    with col2:
        with st.container(border=True):
            st.subheader("🎯 Smart Quiz")
            st.write(
                "Generate questions according to topic and difficulty."
            )

    with col3:
        with st.container(border=True):
            st.subheader("📊 Results")
            st.write(
                "Complete the quiz and check your performance."
            )

    st.divider()
    st.subheader("Get Started")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Login"):
            go_to("login")

    with col2:
        if st.button("✨ Sign Up"):
            go_to("signup")


elif st.session_state.page == "login":

    st.title("🔐 Login")

    col1, col2, col3 = st.columns([1, 1.4, 1])

    with col2:

        with st.container(border=True):

            st.subheader("Welcome Back")

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            if st.button("Login →"):

                if not username or not password:

                    st.error(
                        "Please enter username and password."
                    )

                elif check_login(username, password):

                    st.session_state.username = username
                    st.session_state.logged_in = True

                    reset_quiz()

                    go_to("dashboard")

                else:

                    st.error(
                        "Invalid username or password."
                    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back to Home"):
            go_to("home")

    with col2:
        if st.button("Create Account"):
            go_to("signup")


elif st.session_state.page == "signup":

    st.title("✨ Create Account")

    col1, col2, col3 = st.columns([1, 1.4, 1])

    with col2:

        with st.container(border=True):

            st.subheader("Join QuizCraft")

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            username = st.text_input(
                "Username",
                placeholder="Choose a username"
            )

            email = st.text_input(
                "Email",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Create a password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Confirm your password"
            )

            if st.button("Create Account →"):

                if not all([
                    name,
                    username,
                    email,
                    password
                ]):

                    st.error(
                        "Please fill all fields."
                    )

                elif password != confirm_password:

                    st.error(
                        "Passwords do not match."
                    )

                elif add_user(
                    name,
                    username,
                    email,
                    password
                ):

                    st.success(
                        "Account created successfully! 🎉"
                    )

                    st.session_state.username = username
                    st.session_state.logged_in = True

                    reset_quiz()

                    go_to("dashboard")

                else:

                    st.error(
                        "Username or email already exists."
                    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back to Home"):
            go_to("home")

    with col2:
        if st.button(
            "Already have an account? Login"
        ):
            go_to("login")
