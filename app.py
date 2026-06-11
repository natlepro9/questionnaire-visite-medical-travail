import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# ... (Gardez votre formulaire tel quel) ...

if st.button("Générer le Dossier Médical"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    # Largeur de page et marge
    largeur = 170
    x_pos = 20 # Marge gauche fixe
    
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=20, y=15, w=30)

    pdf.set_font("Arial", 'B', 16)
    pdf.set_xy(x_pos, 50)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    
    pdf.set_font("Arial", '', 12)
    y = 65
    infos = f"Date : {date.today()} | Patient : {nom} {prenom}"
    pdf.set_xy(x_pos, y)
    pdf.multi_cell(largeur, 8, infos.encode('latin-1', 'replace').decode('latin-1'))
    
    y += 15
    sections = [
        ("Motif", motif), 
        ("Antécédents", f"Chroniques: {maladies}, Allergies: {allergies}, Familiaux: {diabete}, {ht}, {cardio}, {cancer}, {autres_fam}"),
        ("Examen Clinique", f"Taille: {taille}cm, Poids: {poids}kg, Tension: {tension}, Obs: {obs_clinique}"), 
        ("Diagnostic", diagnostic),
        ("Traitement", traitement), 
        ("Suivi", suivi)
    ]
    
    for titre, contenu in sections:
        # Titre
        pdf.set_font("Arial", 'B', 12)
        pdf.set_xy(x_pos, y)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'))
        y += 8
        
        # Contenu
        pdf.set_font("Arial", '', 11)
        pdf.set_xy(x_pos, y)
        pdf.multi_cell(largeur, 8, contenu.encode('latin-1', 'replace').decode('latin-1'))
        
        # Calcul automatique de la hauteur prise par le texte pour déplacer le 'y' suivant
        # On ajoute un espace de 10mm après chaque section
        y += pdf.get_string_width(contenu) / 10 + 15 
        
        # Si on arrive en bas de page, on saute de page
        if y > 250:
            pdf.add_page()
            y = 20
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")