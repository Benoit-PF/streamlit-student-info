import streamlit as st
# Title of the app
st.title("Student Information")

# Text input for student's name
studenttemp_name = st.text_input(
               label = "Entrez le nom de l'étudiant:",
               help="en majuscule de préference",
               placeholder="Ecriver vore nom ici")

# studen_name en upper
# Convertir le texte saisi en majuscules
student_name_input = studenttemp_name.upper()

# Slider for student's age
student_age = st.slider("Selectionne l'âge de l'étudiant :", 1, 80,30)

# Button to display the input text and age
if st.button("Affichage Information de l'étudiant",type="primary"):
    st.write("Nom de l'étudiant : ", student_name_input)
    st.write("Age de l'étudiant : ", student_age," ans")     