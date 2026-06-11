import streamlit as st
from fpdf import FPDF
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- Formulaire ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    # Correction date : min_value est en 1900, plus de blocage à 2016
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1), max_value=date.today())
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")
    urgence = st.text_input("Personne à contacter en cas d’urgence")
    tel_urgence = st.text_input("Téléphone d'urgence")

nom_medecin = st.text_input("Nom du Médecin")
motif = st.text_area("2. Motif de la consultation")
maladies = st.text_input("3. Maladies chroniques")
chir = st.text_input("Chirurgies / hospitalisations")
allergies = st.text_input("Allergies")
traitements = st.text_input("Traitements en cours")
diabete = st.text_input("Diabète")
ht = st.text_input("Hypertension")
habitudes = st.text_area("4. Habitudes de vie")
obs_clinique = st.text_area("5. Examen clinique")
examens = st.text_area("6. Examens complémentaires")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations médicales")
suivi = st.text_area("10. Suivi médical")

# --- Génération PDF ---
if st.button("Générer le Dossier Médical"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    largeur_texte = 180 # Largeur fixe pour tout
    
    # Titre
    pdf.set_font("Arial", 'B', 16)
    pdf.set_x(15)
    pdf.cell(largeur_texte, 10, "DOSSIER DE VISITE MEDICALE", ln=True, align='C')
    pdf.ln(10)
    
    # Infos patient
    pdf.set_font("Arial", '', 12)
    pdf.set_x(15)
    pdf.cell(largeur_texte, 8, f"Date : {date.today()} | Patient : {nom} {prenom}", ln=True)
    pdf.ln(5)
    
    # Sections (TITRE + CONTENU)
    sections = [
        ("1. INFOS PERSONNELLES", f"Né(e) le: {date_nais} | Sexe: {sexe}\nAdresse: {adresse}\nTel: {tel}\nUrgence: {urgence} ({tel_urgence})"),
        ("2. MOTIF", motif),
        ("3. ANTECEDENTS", f"Chroniques: {maladies}, Chir: {chir}, Allergies: {allergies}, Traitements: {traitements}, Diabète: {diabete}, Hypertension: {ht}"),
        ("4. HABITUDES DE VIE", habitudes),
        ("5. EXAMEN CLINIQUE", obs_clinique),
        ("6. EXAMENS COMPLEMENTAIRES", examens),
        ("7. DIAGNOSTIC", diagnostic),
        ("8. TRAITEMENT", traitement),
        ("9. RECOMMANDATIONS", recommandations),
        ("10. SUIVI", suivi)
    ]
    
    for titre, contenu in sections:
        pdf.set_x(15) # Force le retour à la marge gauche
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur_texte, 8, titre.encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        
        pdf.set_x(15) # Force le retour à la marge gauche
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur_texte, 7, (contenu if contenu else "").encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        pdf.ln(2)
    
    # Nom médecin
    pdf.ln(10)
    pdf.set_x(15)
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(largeur_texte, 8, f"Médecin : {nom_medecin}".encode('latin-1', 'replace').decode('latin-1'), 0, 'R')
    pdf.set_x(15)
    pdf.multi_cell(largeur_texte, 8, "Signature : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")