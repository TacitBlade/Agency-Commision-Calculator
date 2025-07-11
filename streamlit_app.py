import streamlit as st

custom_name = st.text_input("Enter Your App Name", value="🎯 Agent Bean Calculator")

# Display custom title
st.title("Agent Beans Dashboard")
st.subheader("📊 Agent Totals Summary")

# Form input
with st.form("bean_calc_form"):
    num_agents = st.number_input("How many agents?", min_value=1, step=1)
    agents_input = []
    for i in range(int(num_agents)):
        st.markdown(f"#### Agent {i+1}")
        name = st.text_input(f"Name", key=f"name_{i}")
        beans_earned = st.number_input("Beans Earned by Host", key=f"beans_{i}")

        salary_usd = get_salary_from_target(target_hit)

        agents_input.append({
            "name": name,
            "beans_earned": beans_earned,
            "salary_usd": salary_usd
        })
    submitted = st.form_submit_button("Calculate")

# Process form data
if submitted:
    if any(agent["name"] == "" for agent in agents_input):
        st.error("🚫 Please enter a name for every agent.")
    else:
        results = []
        for agent in agents_input:
            salary_beans, commission, total = calculate_total_beans(agent["beans_earned"], agent["salary_usd"])
            diamonds, breakdown = convert_beans_to_diamonds(total)

            results.append({
                "Agent": agent["name"],
                "Beans Earned": int(agent["beans_earned"]) if agent["beans_earned"].is_integer() else round(agent["beans_earned"], 2),
                "Salary (USD)": int(agent["salary_usd"]) if agent["salary_usd"].is_integer() else round(agent["salary_usd"], 2),
                "Salary in Beans": int(salary_beans) if salary_beans.is_integer() else round(salary_beans, 2),
                "5% Commission": int(commission) if commission.is_integer() else round(commission, 2),
                "Total Beans": int(total) if total.is_integer() else round(total, 2),
                "Diamonds": int(diamonds),
                "Diamond Breakdown": breakdown
            })
