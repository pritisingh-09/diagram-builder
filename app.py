import streamlit as st
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
import os
import uuid

st.set_page_config(page_title="Diagram Builder", layout="wide")

st.title("📊 Diagram Builder - Live Generator")
st.markdown("Write Python diagram code below and click **Run** to generate a diagram.")

code = st.text_area("Diagram Code", height=300, value="""
with Diagram("Simple Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("db")
""")

if st.button("Run"):
    filename = f"diagram_{uuid.uuid4().hex[:8]}"
    try:
        with open(f"{filename}.py", "w") as f:
            f.write(code)

        exec(code, globals())

        image_file = f"{filename}.png"
        st.image(image_file, caption="Your Generated Diagram", use_column_width=True)
        with open(image_file, "rb") as img:
            st.download_button("📥 Download Diagram", img, file_name=image_file)
        os.remove(image_file)
        os.remove(f"{filename}.py")
    except Exception as e:
        st.error(f"Error: {e}")
