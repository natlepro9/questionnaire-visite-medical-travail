import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- 1. Formulaire (Défini avant le bouton) ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")

motif = st.text_area("2. Motif de la consultation")

with st.expander("3. Antécédents médicaux"):
    maladies = st.text_input("Maladies chroniques")
    allergies = st.text_input("Allergies")
    trait_en_cours = st.text_input("Traitements en cours")
    diabete = st.text_input("Diabète")
    ht = st.text_input("Hypertension")

obs_clinique = st.text_area("4. Observations cliniques")
diagnostic = st.text_area("5. Diagnostic")
traitement = st.text_area("6. Traitement")
suivi = st.text_area("7. Suivi médical")

# --- 2. Génération PDF (Déclenchée par le bouton) ---
if st.button("Générer le Dossier Médical"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    largeur = 180 
    
    # En-tête
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)
    
    pdf.ln(25)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(5)
    
    # Infos Patient
    pdf.set_font("Arial", '', 12)
    info = f"Date : {date.today()} | Patient : {nom} {prenom}"
    pdf.multi_cell(largeur, 8, info.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)
    
    # Sections fusionnées (Titre + Contenu dans le même bloc)
    sections = [
        f"MOTIF :\n{motif}",
        f"ANTECEDENTS :\nChroniques: {maladies}, Allergies: {allergies}, Diabete: {diabete}, Hypertension: {ht}",
        f"EXAMEN CLINIQUE :\n{obs_clinique}",
        f"DIAGNOSTIC :\n{diagnostic}",
        f"TRAITEMENT :\n{traitement}",
        f"SUIVI :\n{suivi}"
    ]
    
    for bloc in sections:
        pdf.set_font("Arial", 'B', 12)
        # On utilise une bordure (1) pour vérifier que le texte reste bien dans les 180mm
        pdf.multi_cell(largeur, 8, bloc.encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.ln(2)
    
    # Signature
    pdf.ln(10)
    pdf.multi_cell(largeur, 8, "Signature du medecin : ____________________", 0, 'R')
    
    # Téléchargement
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")