import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- 1. Formulaire ---
with st.expander("Informations Patient", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1))
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")
    contact_urgence = st.text_input("Contact d'urgence")
    tel_urgence = st.text_input("Téléphone d'urgence")

nom_medecin = st.text_input("Nom du Médecin")
motif = st.text_area("2. Motif")
maladies = st.text_input("3. Antécédents (Maladies)")
allergies = st.text_input("Allergies")
fam = st.text_input("Antécédents familiaux")
habitudes = st.text_area("4. Habitudes de vie")
obs_cliniques = st.text_area("5. Examen clinique")
examens = st.text_area("6. Examens complémentaires")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations")
suivi = st.text_area("10. Suivi médical")

# --- 2. Génération PDF ---
if st.button("Générer le PDF"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)
    
    # Largeur fixe de 180mm. RIEN ne dépassera cette largeur.
    largeur = 180 
    
    # Titre
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(10)
    
    # Données organisées
    sections = [
        ("1. INFORMATIONS PERSONNELLES", f"Patient: {nom} {prenom}\nNé le: {date_nais} | Sexe: {sexe}\nAdresse: {adresse}\nTel: {tel}\nUrgence: {contact_urgence} ({tel_urgence})"),
        ("2. MOTIF", motif),
        ("3. ANTECEDENTS", f"Maladies: {maladies}\nAllergies: {allergies}\nFamiliaux: {fam}"),
        ("4. HABITUDES DE VIE", habitudes),
        ("5. EXAMEN CLINIQUE", obs_cliniques),
        ("6. EXAMENS COMPLEMENTAIRES", examens),
        ("7. DIAGNOSTIC", diagnostic),
        ("8. TRAITEMENT", traitement),
        ("9. RECOMMANDATIONS", recommandations),
        ("10. SUIVI MEDICAL", suivi)
    ]
    
    # Impression des sections
    for titre, contenu in sections:
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur, 8, (contenu if contenu else "Non renseigné").encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        pdf.ln(4)
    
    # Signature dynamique
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(largeur, 8, f"Médecin : {nom_medecin}".encode('latin-1', 'replace').decode('latin-1'), 0, 'R')
    pdf.multi_cell(largeur, 8, "Signature : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")