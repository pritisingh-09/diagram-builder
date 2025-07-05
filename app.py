import streamlit as st
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
import os
import uuid
from graphviz import ExecutableNotFound

# Configure Streamlit
st.set_page_config(page_title="Diagram Builder", layout="wide")
st.title("📊 Diagram Builder - Live Generator")
st.markdown("Write Python diagram code below and click **Run** to generate a diagram.")

# Default diagram code
default_code = """
with Diagram("Simple Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("db")
"""

code = st.text_area("Diagram Code", height=300, value=default_code)

if st.button("Run"):
    filename = f"diagram_{uuid.uuid4().hex[:8]}"
    try:
        # Write the user's code to a temporary file
        with open(f"{filename}.py", "w") as f:
            f.write(code)

        # Execute the code to generate the diagram
        exec(code, globals())

        # Display and download the diagram
        image_file = f"{filename}.png"
        if os.path.exists(image_file):
            st.image(image_file, caption="Your Generated Diagram", use_column_width=True)
            with open(image_file, "rb") as img:
                st.download_button("📥 Download Diagram", img, file_name=image_file)
            # Clean up
            os.remove(image_file)
            os.remove(f"{filename}.py")
        else:
            st.error("Diagram generation failed. Check your code syntax.")
    except ExecutableNotFound:
        st.error("Graphviz not found. Ensure 'dot' is installed on the system.")
    except Exception as e:
        st.error(f"Error: {e}")
