import streamlit as st

st.set_page_config(page_title="BMI & Nutrition Calculator", layout="wide")
st.title("🏋️‍♂️ BMI & Nutrition Calculator")
st.write("Calculate your BMI and get personalized nutrition recommendations!")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📏 Body Measurements")
    # User inputs
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
    weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)
    age = st.number_input("Age", min_value=15, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    # Activity level
    activity_level = st.selectbox(
        "Activity Level",
        ["Sedentary (little or no exercise)",
         "Lightly active (light exercise 1-3 days/week)",
         "Moderately active (moderate exercise 3-5 days/week)",
         "Very active (hard exercise 6-7 days/week)",
         "Extremely active (very hard exercise, physical job)"]
    )

if st.button("Calculate BMI & Nutrition"):
    if height > 0 and weight > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        # Calculate BMR using Mifflin-St Jeor Equation
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        # Activity multipliers
        activity_multipliers = {
            "Sedentary (little or no exercise)": 1.2,
            "Lightly active (light exercise 1-3 days/week)": 1.375,
            "Moderately active (moderate exercise 3-5 days/week)": 1.55,
            "Very active (hard exercise 6-7 days/week)": 1.725,
            "Extremely active (very hard exercise, physical job)": 1.9
        }
        
        tdee = bmr * activity_multipliers[activity_level]
        
        # Health category
        if bmi < 18.5:
            category = "Underweight"
            protein_multiplier = 1.8  # Higher protein for muscle building
            carb_multiplier = 1.2
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            protein_multiplier = 1.6
            carb_multiplier = 1.0
        elif 25 <= bmi < 30:
            category = "Overweight"
            protein_multiplier = 1.4
            carb_multiplier = 0.8
        else:
            category = "Obese"
            protein_multiplier = 1.2
            carb_multiplier = 0.6
        
        # Calculate nutrition needs
        protein_grams = weight * protein_multiplier
        protein_calories = protein_grams * 4
        
        # Carbs: 45-65% of remaining calories
        remaining_calories = tdee - protein_calories
        carb_calories = remaining_calories * 0.55  # 55% of remaining calories
        carb_grams = carb_calories / 4
        
        # Fat: remaining calories
        fat_calories = remaining_calories - carb_calories
        fat_grams = fat_calories / 9
        
        with col1:
            st.subheader("📊 BMI Results")
            st.metric("BMI", f"{bmi:.1f}")
            st.metric("Category", category)
            st.metric("Daily Calories", f"{tdee:.0f} kcal")
        
        with col2:
            st.subheader("🍎 Nutrition Recommendations")
            st.metric("Protein", f"{protein_grams:.0f}g ({protein_calories:.0f} kcal)")
            st.metric("Carbohydrates", f"{carb_grams:.0f}g ({carb_calories:.0f} kcal)")
            st.metric("Fat", f"{fat_grams:.0f}g ({fat_calories:.0f} kcal)")
            
            # Additional recommendations
            st.markdown("---")
            st.markdown("**💡 Tips:**")
            if category == "Underweight":
                st.markdown("- Focus on nutrient-dense foods")
                st.markdown("- Include healthy fats (nuts, avocados)")
                st.markdown("- Eat 5-6 smaller meals per day")
            elif category == "Normal weight":
                st.markdown("- Maintain balanced nutrition")
                st.markdown("- Stay hydrated (8-10 glasses/day)")
                st.markdown("- Include regular exercise")
            elif category == "Overweight":
                st.markdown("- Create a moderate calorie deficit")
                st.markdown("- Focus on lean proteins")
                st.markdown("- Increase fiber intake")
            else:  # Obese
                st.markdown("- Consult a healthcare provider")
                st.markdown("- Start with gentle exercise")
                st.markdown("- Track food intake")
    else:
        st.error("Please enter valid height and weight values.")