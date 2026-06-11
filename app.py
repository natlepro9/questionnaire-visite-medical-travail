import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- Formulaire ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
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
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    
    # Largeur utile de la page (210 - 15 - 15 = 180mm)
    largeur = 180
    
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)

    pdf.ln(25)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(largeur, 8, f"Date : {date.today()} | Patient : {nom} {prenom}")
    pdf.ln(5)
    
    sections = [
        ("Motif", motif), 
        ("Antécédents", f"Chroniques: {maladies}, Allergies: {allergies}, Familiaux: {diabete}, {ht}, {cardio}, {cancer}, {autres_fam}"),
        ("Examen Clinique", f"Taille: {taille}cm, Poids: {poids}kg, Tension: {tension}, Obs: {obs_clinique}"), 
        ("Diagnostic", diagnostic),
        ("Traitement", traitement), 
        ("Suivi", suivi)
    ]
    
    for titre, contenu in sections:
        pdf.set_font("Arial", 'B', 12)
        # Encodage sécurisé pour éviter l'erreur Unicode
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'))
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur, 8, contenu.encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(2)
    
    pdf.ln(10)
    pdf.cell(largeur, 10, "Signature du medecin : ____________________", ln=True, align='R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")