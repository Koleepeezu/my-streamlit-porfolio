import streamlit as st


# Page config
st.set_page_config(page_title="My Developer Portfolio", page_icon="💻", layout="wide")
st.markdown(
    """
<img src="https://img.freepik.com/free-vector/top-view-dark-laptop-background-template_52683-7081.jpg"  width="100%" alt="Custom Image" height="450">
    
    """,
    unsafe_allow_html=True
)




# --- Sidebar ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Contact"])

# --- Header ---
st.title("Hi, I'm Kolapo, am a Python Web & Web3 Developer")
st.subheader("Building scalable web applications and decentralized solutions")

# --- Home ---
if selection == "Home":
    #st.image("image.jpg", width=200)  # Optional
    st.markdown("""
        ## About Me
        I'm a Python developer with a focus on modern web apps and blockchain tech. I specialize in:
        - Building WEB APPLICATION using PYTHON.
        - Buiding Web App For Data Science Using Streamlit
        - Python Web3 Development.
    """)

# --- Projects ---
elif selection == "Projects":
    st.header("Projects")
    projects = [
        {
            "title": "Decentralized Voting App",
            "description": "A dApp using Solidity + web3.py + Streamlit frontend",
            "link": "https://github.com/Koleepeezu/Voting-app"
      
                            },
            {
            "title":"Web app for data science",
            "description":"A Data Science Web App Using Python, Streamlit, Pandas, Numpy and Matlotib",
            "link": "https://github.com/Koleepeezu/E-commerce"
                },

        {
            "title": "Personal portfolio",
            "description": "A personal portfolio website using streamlit",
            "link": "https://github.com/Koleepeezu/personal-port"
        }
    ]
    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])
        st.markdown(f"[GitHub]({project['link']})")

# --- Skills ---
elif selection == "Skills":
    st.header("Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Web Development")
        st.write("- Bulding Website App With Python(streamlit) ")
        st.write("- Building website app for data science using streamlit and python")
        

    with col2:
        st.markdown("### Web3 / Blockchain")
        st.write("- Solidity")
        st.write("- web3.py, React, python")
        

# --- Contact ---
elif selection == "Contact":
  st.header("📬 Contact Me")

  st.markdown(
    """
    <style>
        .contact-form {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            width: 100%;
            max-width: 500px;
            margin: auto;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }

        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }

        .contact-form button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .contact-form button:hover {
            background-color: #45a049;
            }
    </style>

    <form class="contact-form" action="https://formsubmit.co/koleepeezu.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """,
    unsafe_allow_html=True
)



 

  st.markdown("You can also find me at:")
  st.markdown("[GitHub](https://github.com/Koleepeezu)")
  st.markdown("[LinkedIn](https://www.linkedin.com/in/kolapo-ofobutu-006658366?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )")












 # Add a footer
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 15px;
            background-color:  #21376c;
            padding: 10px 0;
            z-index: 100;
        }
    </style>
    <div class="footer">
        &copy; 2024 @kolapo All rights reserved.
    </div>
""", unsafe_allow_html=True)




