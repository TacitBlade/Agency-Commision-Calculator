import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image

# Tier structure for salary calculation
tier_structure = {
    0: 0,
    5000: 23,
    10000: 23,
    20000: 45,
    30000: 67,
    40000: 89,
    50000: 112,
    60000: 134,
    70000: 156,
    80000: 178,
    90000: 200,
    100000: 221,
    110000: 243,
    120000: 263,
    130000: 281,
    170000: 361,
    250000: 525,
    350000: 735,
    450000: 945,
    600000: 1220,
    800000: 1613,
    1000000: 2000,
    1500000: 2950,
    2000000: 3925,
    3000000: 5900,
    4000000: 7650,
    5000000: 9200,
    6000000: 10200,
}

def get_salary_from_target(target_hit):
    salary = 0
    for target, s in sorted(tier_structure.items()):
        if target_hit >= target:
            salary = s
        else:
            break
    return salary

# Function to calculate salary in beans, commission, and total
def calculate_total_beans(beans_earned, salary_usd):
    salary_beans = salary_usd * 210
    commission = beans_earned * 0.05
    total = salary_beans + commission
    return salary_beans, commission, total

# Function to convert beans to diamonds
def convert_beans_to_diamonds(beans):
    conversions = [
        {"diamonds": 3045, "beans": 10999},
        {"diamonds": 1105, "beans": 3999},
        {"diamonds": 275,  "beans": 999},
        {"diamonds": 29,   "beans": 109},
        {"diamonds": 2,    "beans": 8}
    ]
    diamonds = 0
    breakdown = []

    for pack in conversions:
        count = beans // pack["beans"]
        if count > 0:
            diamonds += count * pack["diamonds"]
            beans -= count * pack["beans"]
            breakdown.append(f"{int(count)}×{pack['diamonds']}d")

    return diamonds, ", ".join(breakdown)

# Streamlit app configuration
st.set_page_config(page_title="Agent Bean Calculator", layout="centered")

# Enter custom app name
custom_name = st.text_input("Enter Your App Name", value="🎯 Agent Bean Calculator")

# Display custom title
st.title(custom_name)

# Form input
with st.form("bean_calc_form"):
    num_agents = st.number_input("How many agents?", min_value=1, step=1)
    agents_input = []
    for i in range(int(num_agents)):
        st.markdown(f"#### Agent {i+1}")
        name = st.text_input(f"Name", key=f"name_{i}")
        beans_earned = st.number_input("Beans Earned by Host", key=f"beans_{i}")
        target_hit = st.number_input("Target Hit", key=f"target_hit_{i}")

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

        # Remove breakdown from main table
        df = pd.DataFrame([{k: v for k, v in r.items() if k != "Diamond Breakdown"} for r in results])
        df = df.sort_values(by="Total Beans", ascending=False)

        st.success("✅ Calculations complete!")
        st.dataframe(df.style.set_properties(**{"text-align": "center"}), use_container_width=True)

        # Totals
        total_all = df["Total Beans"].sum()
        total_diamonds = df["Diamonds"].sum()
        st.info(f"💰 **Total Beans Across All Agents:** {int(total_all) if total_all.is_integer() else round(total_all, 2)}")
        st.success(f"💎 **Total Diamonds for All Agents:** {total_diamonds}")

        # Excel download
        output = BytesIO()
        df.to_excel(output, index=False, sheet_name="Agent Beans")
        st.download_button(
            "📥 Download Results as Excel",
            output.getvalue(),
            file_name="agent_bean_results.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # Per-agent breakdown
              st.subheader("📊 Agent Totals Summary")
        for row in results:
            bean_value = int(row['Total Beans']) if isinstance(row['Total Beans'], (int, float)) and row['Total Beans'] == int(row['Total Beans']) else round(row['Total Beans'], 2)
            st.metric(label=f"{row['Agent']}", value=f"{bean_value} Beans")
