import streamlit as st
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
import os
import uuid
from graphviz import ExecutableNotFound

# Streamlit config
st.set_page_config(page_title="Diagram Builder", layout="wide")
st.title("📊 Diagram Builder - Live Generator")
st.markdown("Write Python diagram code below and click **Run** to generate a diagram.")

DEFAULT_CODE = """
with Diagram("Simple Web Service", show=False, filename="diagram"):
    ELB("lb") >> EC2("web") >> RDS("db")
"""

code = st.text_area("Diagram Code", height=300, value=DEFAULT_CODE)

if st.button("Run"):
    try:
        exec(code)  # Generate diagram.png
        if os.path.exists("diagram.png"):
            st.image("diagram.png", use_column_width=True)
            with open("diagram.png", "rb") as img:
                st.download_button("📥 Download", img, file_name="diagram.png")
            os.remove("diagram.png")  # Clean up
        else:
            st.error("No diagram generated. Check your code syntax.")
    except ExecutableNotFound:
        st.error("Graphviz not installed! Ensure 'dot' is in PATH.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
