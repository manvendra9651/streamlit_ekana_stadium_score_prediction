import streamlit as st

st.title("🏏 T20 Score Predictor - Ekana Stadium")

st.write("Enter match details to predict final score")

# input fields
current_score = st.number_input("Current Score", min_value=0)
overs_completed = st.number_input("Overs Completed", min_value=0.0, max_value=20.0)
wickets = st.number_input("Wickets Lost", min_value=0, max_value=10)

pitch = st.selectbox(
    "Pitch Type",
    ["Slow Pitch", "Normal Pitch", "Batting Pitch"]
)

# prediction logic
if st.button("Predict Score"):

    remaining_overs = 20 - overs_completed

    if pitch == "Slow Pitch":
        run_rate = 7
    elif pitch == "Normal Pitch":
        run_rate = 8
    else:
        run_rate = 9

    predicted_runs = current_score + (remaining_overs * run_rate)

    st.subheader("Predicted Final Score")
    st.success(int(predicted_runs))