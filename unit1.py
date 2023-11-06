import streamlit as st
import plotly.express as px
import pandas as pd

# Create a Streamlit app
st.set_page_config(layout="wide")
st.title("Supply Chain Insights")

# Navigation
menu = st.sidebar.selectbox("Select a Topic", [
    "Introduction",
    "Fundamentals of Supply Chain",
    "Evolution of Supply Chain",
    "Role in the Economy",
    "Decision Phases in Supply Chain",
    "Enablers and Drivers of Supply Chain Performance",
    "Supply Chain Strategy",
    "Supply Chain Performance Measures",
])

# Content for each section
if menu == "Introduction":
    st.header("Introduction")
    st.write("Supply chains are the backbone of global commerce. They involve the flow of goods, information, and services from suppliers to manufacturers to customers. This application will explore various aspects of supply chains and their critical role in the global economy.")

elif menu == "Fundamentals of Supply Chain":
    st.header("Fundamentals of Supply Chain")
    st.write("A supply chain is a network of organizations, people, activities, information, and resources involved in the creation and delivery of products and services. The key components of a supply chain include suppliers, manufacturers, distributors, retailers, and customers.")

    # Sample Supply Chain Diagram
    st.image("supply_chain_diagram.png", use_column_width=True)

    # Supply Chain Process
    st.subheader("Supply Chain Process")
    st.write("The supply chain process involves procurement, production, distribution, and customer delivery. Each phase is interconnected and impacts the overall supply chain performance.")
    
    # Sample Flowchart Image
    st.image("supply_chain_process.png", use_column_width=True)

elif menu == "Evolution of Supply Chain":
    st.header("Evolution of Supply Chain")
    st.write("Supply chains have evolved significantly over the years. From local and linear chains, they have become global, complex, and interconnected networks. This evolution has been driven by advancements in transportation, communication, and information technology.")
    
    # Sample Evolution Chart
    evolution_data = pd.DataFrame({
        'Year': [2000, 2010, 2020, 2030],
        'Complexity': [1, 2, 3, 4],
    })
    fig = px.line(evolution_data, x='Year', y='Complexity', title="Supply Chain Complexity Over Time")
    st.plotly_chart(fig)

    # Major Technological Advancements
    st.subheader("Major Technological Advancements")
    st.write("Advancements in technology, such as RFID, IoT, and blockchain, have significantly impacted supply chain operations. These technologies improve visibility, traceability, and decision-making.")
    
    # Sample Technological Advancements Image
    st.image("technological_advancements.png", use_column_width=True)

elif menu == "Role in the Economy":
    st.header("Role in the Economy")
    st.write("Supply chains play a pivotal role in the economy. They impact economic growth, employment, and consumer welfare. Inefficiencies or disruptions in the supply chain can have far-reaching consequences.")

    # Economic Impact
    st.subheader("Economic Impact")
    st.write("A well-functioning supply chain contributes to GDP growth and job creation. It allows businesses to reach broader markets and consumers to access a variety of products.")
    
    # Sample Economic Impact Chart
    economic_data = pd.DataFrame({
        'Year': [2010, 2015, 2020, 2025],
        'GDP Contribution': [12, 15, 18, 21],
    })
    fig = px.line(economic_data, x='Year', y='GDP Contribution', title="GDP Contribution Over Time")
    st.plotly_chart(fig)

elif menu == "Decision Phases in Supply Chain":
    st.header("Decision Phases in Supply Chain")
    st.write("Supply chain decisions occur at various phases, including procurement, production, distribution, and customer service. Effective decision-making is crucial for optimizing supply chain performance.")

    # Sample Decision Phases Matrix
    decision_phases_data = pd.DataFrame({
        'Phase': ['Procurement', 'Production', 'Distribution', 'Customer Service'],
        'Importance': [5, 4, 3, 4],
    })
    st.table(decision_phases_data)

    # Decision Support Systems
    st.subheader("Decision Support Systems")
    st.write("Advanced decision support systems leverage data and analytics to make informed decisions at each supply chain phase.")
    
    # Sample Decision Support System Image
    st.image("decision_support_system.png", use_column_width=True)

elif menu == "Enablers and Drivers of Supply Chain Performance":
    st.header("Enablers and Drivers of Supply Chain Performance")
    st.write("Several factors enable and drive supply chain performance. These include technology adoption, collaboration with partners, risk management strategies, and more.")

    # Sample Enablers and Drivers Chart
    enablers_data = pd.DataFrame({
        'Factor': ['Technology', 'Collaboration', 'Risk Management', 'Inventory Optimization'],
        'Importance': [4, 4, 5, 3],
    })
    fig = px.bar(enablers_data, x='Factor', y='Importance', title="Factors Driving Supply Chain Performance")
    st.plotly_chart(fig)

    # Collaborative Partnerships
    st.subheader("Collaborative Partnerships")
    st.write("Collaboration with suppliers, manufacturers, and distributors is essential for streamlining the supply chain. It leads to better coordination and cost savings.")
    
    # Sample Collaboration Image
    st.image("collaborative_partnerships.png", use_column_width=True)

elif menu == "Supply Chain Strategy":
    st.header("Supply Chain Strategy")
    st.write("Developing a supply chain strategy is essential for aligning supply chain activities with overall business goals. Different strategies, such as lean, agile, and responsive supply chains, can be adopted based on the business's needs and objectives.")

    # Sample Supply Chain Strategy Comparison
    strategy_data = pd.DataFrame({
        'Strategy': ['Lean', 'Agile', 'Responsive'],
        'Key Features': ['Efficiency', 'Flexibility', 'Customer Responsiveness'],
    })
    st.table(strategy_data)

    # Strategy Alignment
    st.subheader("Strategy Alignment")
    st.write("The chosen supply chain strategy should align with the business's goals, customer expectations, and market conditions.")
    
    # Sample Strategy Alignment Image
    st.image("strategy_alignment.png", use_column_width=True)

elif menu == "Supply Chain Performance Measures":
    st.header("Supply Chain Performance Measures")
    st.write("To assess supply chain performance, various key performance indicators (KPIs) are used. Examples include on-time delivery, order accuracy, inventory turnover, and supply chain cost as a percentage of revenue.")

    # Sample KPIs Visualization
    kpi_data = pd.DataFrame({
        'KPI': ['On-time Delivery', 'Order Accuracy', 'Inventory Turnover', 'Cost as % of Revenue'],
        'Performance': [95, 98, 12, 8],
    })
    fig = px.bar(kpi_data, x='KPI', y='Performance', title="Supply Chain KPIs")
    st.plotly_chart(fig)

    # Continuous Improvement
    st.subheader("Continuous Improvement")
    st.write("Regularly monitoring KPIs and making data-driven decisions can lead to continuous supply chain performance improvement.")
    
    # Sample Continuous Improvement Image
    st.image("continuous_improvement.png", use_column_width=True)

# Footer or acknowledgment
st.sidebar.text("Created by Jashvanth S R")

# Run the app
if __name__ == "__main__":
    st.write(f"Welcome to the {menu} section!")
