import streamlit as st
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

st.title("📊 Diagram Builder")

code = st.text_area("Write Python diagram code below:", height=250, value="""
with Diagram("Simple Web Service", show=False, outformat="png", filename="diagram"):
    ELB("lb") >> EC2("web") >> RDS("db")
""")

if st.button("Generate Diagram"):
    try:
        exec(code)
        st.image("diagram.png")
    except Exception as e:
        st.error(f"Error: {e}")
