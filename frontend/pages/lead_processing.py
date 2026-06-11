import streamlit as st

from api.client import process_lead


def show_lead_processing_page():
    st.title("🚀 Lead Processing")

    st.write(
        "Enter a lead message and classify it as HOT, WARM, or COLD."
    )

    message = st.text_area(
        "Lead Message",
        height=160,
        placeholder="Example: We need AI automation urgently for our sales pipeline."
    )

    if st.button("Process Lead", type="primary"):

        if not message.strip():
            st.warning("Please enter a lead message.")
            return

        with st.spinner("Processing lead..."):
            try:
                response = process_lead(
                    message=message.strip()
                )
            except Exception as e:
                st.error(f"Backend connection failed: {str(e)}")
                return

        if response.status_code != 200:
            st.error("Failed to process lead.")
            return

        data = response.json()

        label = data.get("label", "UNKNOWN")
        confidence = float(data.get("confidence", 0))
        ai_response = data.get("response", "")

        st.divider()

        col1, col2 = st.columns(
            [
                1,
                2
            ]
        )

        with col1:
            if label == "HOT":
                st.error("🔥 HOT Lead")
            elif label == "WARM":
                st.warning("🟡 WARM Lead")
            else:
                st.info("❄️ COLD Lead")

            st.metric(
                "Confidence",
                f"{confidence * 100:.0f}%"
            )

            st.progress(
                min(
                    max(
                        confidence,
                        0
                    ),
                    1
                )
            )

        with col2:
            st.subheader("AI Response")
            st.write(ai_response)