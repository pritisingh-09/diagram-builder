import streamlit as st
import os
import uuid
import subprocess
import sys
import platform
from graphviz import ExecutableNotFound

# --- Graphviz Installation Check ---
def install_graphviz():
    """Attempt to install Graphviz based on the operating system"""
    try:
        if platform.system() == "Linux":
            st.warning("Installing Graphviz (this may take a minute)...")
            subprocess.run(["apt-get", "update"], check=True, capture_output=True)
            subprocess.run(["apt-get", "install", "-y", "graphviz"], check=True, capture_output=True)
        elif platform.system() == "Darwin":
            st.warning("Please install Graphviz manually with: brew install graphviz")
        elif platform.system() == "Windows":
            st.warning("Please download Graphviz from: https://graphviz.org/download/")
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to install Graphviz: {str(e)}")

# --- Verify Graphviz ---
try:
    # Test Graphviz installation
    subprocess.run(["dot", "-V"], check=True, capture_output=True)
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.network import ELB
    from diagrams.aws.database import RDS
except (ImportError, ExecutableNotFound, subprocess.CalledProcessError, FileNotFoundError):
    st.error("Graphviz not found! Attempting to install...")
    install_graphviz()
    st.experimental_rerun()  # Restart the app after installation attempt

# --- Streamlit App ---
st.set_page_config(page_title="Diagram Builder", layout="wide")
st.title("📊 Diagram Builder - Live Generator")
st.markdown("""
    Write Python diagram code below and click **Run** to generate a diagram.  
    Requires Graphviz installed on your system.
""")

DEFAULT_CODE = """
with Diagram("Simple Web Service", show=False, filename="diagram"):
    ELB("lb") >> EC2("web") >> RDS("db")
"""

code = st.text_area("Diagram Code", height=300, value=DEFAULT_CODE)

if st.button("Run"):
    try:
        # Generate unique filename
        filename = f"diagram_{uuid.uuid4().hex[:8]}"
        
        # Execute the diagram code
        exec(code)
        
        # Display and download
        if os.path.exists("diagram.png"):
            st.image("diagram.png", use_column_width=True)
            with open("diagram.png", "rb") as img:
                st.download_button(
                    "📥 Download Diagram",
                    img,
                    file_name=f"{filename}.png",
                    mime="image/png"
                )
            os.remove("diagram.png")  # Clean up
        else:
            st.error("No diagram generated. Check your code syntax.")
            
    except ExecutableNotFound:
        st.error("""
            Graphviz 'dot' command not found. Please ensure:
            1. Graphviz is installed (https://graphviz.org/download/)
            2. 'dot' is in your system PATH
        """)
    except Exception as e:
        st.error(f"Error generating diagram: {str(e)}")
        st.code(f"Full error:\n{str(e)}", language="text")

# --- Installation Instructions ---
with st.expander("Troubleshooting Guide"):
    st.markdown("""
    **Common Issues:**
    - 🚨 *Graphviz not found*: Install Graphviz first
      - Linux: `sudo apt-get install graphviz`
      - Mac: `brew install graphviz`
      - Windows: [Download installer](https://graphviz.org/download/)
    
    - 💡 *Diagram not generating*:
      1. Check your code follows the diagrams library syntax
      2. Ensure you're using valid component names
      3. Look for Python errors above
    """)
