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
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1))
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")

motif = st.text_area("2. Motif de la consultation")
# ... (Gardez les autres sections de votre formulaire ici) ...

# --- Génération PDF ---
if st.button("Générer le Dossier Médical"):
    # On crée une instance FPDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    largeur = 180 
    
    # 1. En-tête
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(10)
    
    # 2. Infos Patient (Utilisation des variables définies plus haut)
    pdf.set_font("Arial", '', 12)
    # On utilise .get() ou on vérifie que la variable existe pour éviter les erreurs
    txt_info = f"Date : {date.today()} | Patient : {nom} {prenom}"
    pdf.multi_cell(largeur, 8, txt_info.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)
    
    # 3. Corps du document
    # Important : On accède aux variables directement ici
    sections = [
        ("Motif", motif),
        ("Examen", f"Taille saisie : {date_nais}") # Exemple d'accès aux variables
    ]
    
    for titre, contenu in sections:
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'))
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur, 8, (contenu if contenu else "Non renseigné").encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(5)
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier.pdf", "application/pdf")