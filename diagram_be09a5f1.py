
with Diagram("Simple Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("db")
