import streamlit as st
from fpdf import FPDF
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- Formulaire (identique à ton ancienne version) ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance")
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")
    urgence = st.text_input("Personne à contacter")
    tel_urgence = st.text_input("Téléphone d'urgence")

motif = st.text_area("2. Motif")
maladies = st.text_input("3. Maladies chroniques")
chir = st.text_input("Chirurgies")
allergies = st.text_input("Allergies")
traitements = st.text_input("Traitements")
diabete = st.text_input("Diabète")
ht = st.text_input("Hypertension")
cardio = st.text_input("Cardiaque")
cancer = st.text_input("Cancer")
autres_fam = st.text_input("Autres")
habitudes = st.text_area("4. Habitudes de vie")
obs_clinique = st.text_area("5. Examen clinique")
examens = st.text_area("6. Examens")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations")
suivi = st.text_area("10. Suivi")
nom_medecin = st.text_input("Nom du Médecin")

# --- Génération PDF ---
if st.button("Générer le Dossier"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    largeur = 180 # Largeur totale utile
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(largeur, 10, f"Date : {date.today()} | Patient : {nom} {prenom}", ln=True)
    pdf.ln(5)
    
    sections = [
        ("Motif", motif),
        ("Antécédents", f"Chroniques: {maladies}, Allergies: {allergies}, Familiaux: {diabete}, {ht}, {cardio}, {cancer}, {autres_fam}"),
        ("Habitudes de vie", habitudes),
        ("Examen Clinique", obs_clinique),
        ("Examens complémentaires", examens),
        ("Diagnostic", diagnostic),
        ("Traitement", traitement),
        ("Recommandations", recommandations),
        ("Suivi", suivi)
    ]
    
    for titre, contenu in sections:
        pdf.set_x(15) # FORCE l'alignement à gauche à 15mm
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        
        pdf.set_x(15) # FORCE l'alignement à gauche à 15mm
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur, 8, (contenu if contenu else "").encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        pdf.ln(2)
    
    pdf.ln(10)
    pdf.set_x(15)
    pdf.multi_cell(largeur, 8, f"Médecin : {nom_medecin}".encode('latin-1', 'replace').decode('latin-1'), 0, 'R')
    
    st.download_button("Télécharger", bytes(pdf.output()), "Dossier.pdf", "application/pdf")