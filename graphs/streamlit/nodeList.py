import streamlit as st
from neo4j import GraphDatabase

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def get_nodes():
    with driver.session() as session:
        # Execute a query to retrieve all the nodes
        result = session.run("MATCH (n) RETURN n")
        # Extract the nodes from the result
        nodes = [record["n"] for record in result]
        return nodes

def main():
    st.title("Neo4j Node Retriever")
    # Add a button to the app
    if st.button("Retrieve nodes"):
        # When the button is pressed, retrieve the nodes and display them in the app
        nodes = get_nodes()
        st.write(nodes)

if __name__ == "__main__":
    main()
