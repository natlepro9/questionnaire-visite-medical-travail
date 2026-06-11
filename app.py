import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- 1. Formulaire ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1))
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")

motif = st.text_area("2. Motif de la consultation")

with st.expander("3. Antécédents médicaux"):
    maladies = st.text_input("Maladies chroniques")
    allergies = st.text_input("Allergies")
    fam = st.text_input("Antécédents familiaux")

habitudes = st.text_area("4. Habitudes de vie")

with st.expander("5. Examen clinique"):
    obs_clinique = st.text_area("Observations médicales")

# Nouvelles sections ajoutées
examens_compl = st.text_area("6. Examens complémentaires")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations médicales")
suivi = st.text_area("10. Suivi médical")

# --- 2. Génération PDF ---
if st.button("Générer le Dossier Médical"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    largeur = 180 
    
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)
    
    pdf.ln(25)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(5)
    
    # Infos Patient
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(largeur, 8, f"Date : {date.today()} | Patient : {nom} {prenom}")
    pdf.ln(5)
    
    # Liste complète des 10 sections
    sections = [
        f"2. MOTIF :\n{motif}",
        f"3. ANTECEDENTS :\n{maladies}, {allergies}, {fam}",
        f"4. HABITUDES DE VIE :\n{habitudes}",
        f"5. EXAMEN CLINIQUE :\n{obs_clinique}",
        f"6. EXAMENS COMPLEMENTAIRES :\n{examens_compl}",
        f"7. DIAGNOSTIC :\n{diagnostic}",
        f"8. TRAITEMENT :\n{traitement}",
        f"9. RECOMMANDATIONS :\n{recommandations}",
        f"10. SUIVI MEDICAL :\n{suivi}"
    ]
    
    for bloc in sections:
        pdf.set_font("Arial", 'B', 12)
        # On utilise une largeur fixe de 180mm pour forcer le retour à la ligne
        pdf.multi_cell(largeur, 8, bloc.encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.ln(2)
    
    pdf.ln(5)
    pdf.multi_cell(largeur, 8, "Signature du medecin : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")