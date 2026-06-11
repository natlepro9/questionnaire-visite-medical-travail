import streamlit as st
from fpdf import FPDF
import os
from datetime import date

st.title("Dossier de Visite Médicale")

# --- Formulaire ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance")
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")
    urgence = st.text_input("Personne à contacter en cas d’urgence")
    tel_urgence = st.text_input("Téléphone d'urgence")

motif = st.text_area("2. Motif de la consultation")

with st.expander("3. Antécédents médicaux"):
    st.subheader("Personnels")
    maladies = st.text_input("Maladies chroniques")
    chir = st.text_input("Chirurgies / hospitalisations")
    allergies = st.text_input("Allergies")
    traitements = st.text_input("Traitements en cours")
    vaccins = st.checkbox("Vaccinations à jour")
    st.subheader("Familiaux")
    diabete = st.text_input("Diabète")
    ht = st.text_input("Hypertension")
    cardio = st.text_input("Maladies cardiaques")
    cancer = st.text_input("Cancer")
    autres_fam = st.text_input("Autres")

habitudes = st.text_area("4. Habitudes de vie (Tabac, Alcool, Activité, etc.)")

with st.expander("5. Examen clinique"):
    col1, col2 = st.columns(2)
    taille = col1.number_input("Taille (cm)")
    poids = col2.number_input("Poids (kg)")
    tension = st.text_input("Tension artérielle")
    frequence = st.text_input("Fréquence cardiaque")
    obs_clinique = st.text_area("Observations médicales")

examens = st.text_area("6. Examens complémentaires")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations médicales")
suivi = st.text_area("10. Suivi médical")

# --- Génération PDF ---
if st.button("Générer le Dossier Médical"):
    pdf = FPDF()
    pdf.add_page()
    
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=10, y=10, w=30)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "DOSSIER DE VISITE MEDICALE", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Date : {date.today()}", ln=True)
    pdf.cell(0, 10, f"Patient : {nom} {prenom}", ln=True)
    pdf.ln(5)
    
    sections = [
        ("Motif", motif), ("Antécédents", f"Chroniques: {maladies}, Allergies: {allergies}"),
        ("Examen Clinique", obs_clinique), ("Diagnostic", diagnostic),
        ("Traitement", traitement), ("Suivi", suivi)
    ]
    
    for titre, contenu in sections:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, titre, ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 10, contenu)
        pdf.ln(2)
    
    pdf.ln(10)
    pdf.cell(0, 10, "Signature du medecin : ____________________", ln=True, align='R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")