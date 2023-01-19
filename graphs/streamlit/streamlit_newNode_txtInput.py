import streamlit as st
from neo4j import GraphDatabase
from py2neo import graph

# Add your Neo4j database credentials here
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"

# Create a driver instance to connect to the Neo4j database
driver = GraphDatabase.driver(uri, auth=(user, password))

# Create a function that will create a node in the database
def create_node(tx, label, properties):
    query = f"MERGE (n:{label} {properties})"
    tx.run(query)

# Create the main app
def main():
    st.title("Neo4j Node Creator")
    label = st.text_input("Enter node label:")
    properties = st.text_area("Enter node properties (in JSON format-e.g. {date: '1/1/11', notes: 'added new feature'}):")
    
    if st.button("Create node"):
        with driver.session() as session:
            session.write_transaction(create_node, label, properties)
            st.success("Node created successfully!")
    if st.button('Get all nodes'):
        cypher = "MATCH (n) RETURN n"
        result =graph.run(cypher)

        #Present nodes
        st.write("All nodes:")
        st.write(list(result))

if __name__ == '__main__':
    main()