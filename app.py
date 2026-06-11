import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Certificat de Compatibilité à la Garde à Vue")

# --- Formulaire ---
with st.form("certificat_garde_a_vue"):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1))
    lieu = st.text_input("Lieu (Commissariat / Gendarmerie)")
    obs_details = st.text_area("Observations médicales")
    traitements = st.text_area("Traitements")
    conclusion = st.selectbox("Conclusion", ["Compatible", "Compatible sous réserve", "Incompatible"])
    submit = st.form_submit_button("Générer le PDF")

if submit:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    # Marges généreuses pour éviter que le texte ne sorte
    pdf.set_margins(20, 20, 20)
    largeur = 170 # Largeur utile pour A4 (210 - 20 - 20)

    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=20, y=20, w=30)

    pdf.ln(30)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "CERTIFICAT MEDICAL DE COMPATIBILITE", 0, 'C')
    pdf.ln(10)
    
    pdf.set_font("Arial", '', 12)
    texte = f"Je soussigné(e), médecin urgentiste, atteste avoir procédé à l'examen de {nom} {prenom}, né(e) le {date_nais}."
    pdf.multi_cell(largeur, 8, texte.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)

    # Structure verticale : Titre puis texte en dessous, jamais côte à côte
    sections = [("Observations :", obs_details), ("Traitements :", traitements), ("Conclusion :", conclusion)]
    
    for titre, contenu in sections:
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'))
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(largeur, 8, contenu.encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(5)

    pdf.ln(10)
    pdf.multi_cell(largeur, 8, f"Fait à {lieu}, le {date.today()}".encode('latin-1', 'replace').decode('latin-1'), 0, 'R')
    
    st.download_button("Télécharger", bytes(pdf.output()), "Certificat.pdf", "application/pdf")