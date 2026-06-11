import streamlit as st
import pandas as pd

from api.client import (
    get_analytics,
    get_recent_leads
)


def show_admin_dashboard():

    if st.session_state.role != "ADMIN":
        st.error("Access denied. Admin users only.")
        return

    st.title("📊 Admin Dashboard")

    token = st.session_state.token

    if not token:
        st.warning("Please login first.")
        return

    st.subheader("Lead Analytics")

    analytics_response = get_analytics(
        token=token
    )

    if analytics_response.status_code == 200:

        analytics = analytics_response.json()

        # Temporary debug. Remove after confirming.
        st.write("DEBUG ANALYTICS:", analytics)

        total = analytics.get("total", 0)
        hot = analytics.get("hot", 0)
        warm = analytics.get("warm", 0)
        cold = analytics.get("cold", 0)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Leads", total)
        col2.metric("🔥 HOT", hot)
        col3.metric("🟡 WARM", warm)
        col4.metric("❄️ COLD", cold)

        chart_data = pd.DataFrame(
            {
                "Label": ["HOT", "WARM", "COLD"],
                "Count": [hot, warm, cold]
            }
        )

        st.bar_chart(
            chart_data,
            x="Label",
            y="Count"
        )

    else:
        st.warning("Analytics available only for admin users.")

    st.divider()

    st.subheader("Recent Leads")

    recent_response = get_recent_leads(
        token=token
    )

    if recent_response.status_code != 200:
        st.warning("Recent leads available only for admin users.")
        return

    leads = recent_response.json()

    if not leads:
        st.info("No recent leads found.")
        return

    table_data = []

    for lead in leads:
        table_data.append(
            {
                "Message": lead.get("message"),
                "Label": lead.get("label"),
                "Confidence": lead.get("confidence"),
                "Response": lead.get("response")
            }
        )

    df = pd.DataFrame(table_data)

    st.dataframe(
        df,
        width="stretch"
    )

    st.divider()

    st.subheader("Lead Details")

    for lead in leads:
        label = lead.get("label", "UNKNOWN")
        message = lead.get("message", "")
        confidence = lead.get("confidence", 0)
        response = lead.get("response", "")

        with st.expander(f"{label} | {message[:80]}"):
            st.write(f"**Message:** {message}")
            st.write(f"**Confidence:** {confidence}")
            st.write(f"**AI Response:** {response}")