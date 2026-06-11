import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- Formulaire simplifié pour l'exemple ---
# (Garde ton formulaire actuel, c'est la partie PDF qui nous intéresse)

if st.button("Générer le Dossier Médical"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Largeur de texte totale (180mm)
    largeur = 180 
    
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)
    
    pdf.ln(25)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(10)
    
    # Fonction pour créer un bloc propre : Titre en gras, Contenu en dessous
    def ajouter_section(pdf, titre, contenu):
        pdf.set_font("Arial", 'B', 12)
        # Le titre prend toute la largeur
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        pdf.set_font("Arial", '', 11)
        # Le contenu prend toute la largeur en dessous, avec une légère marge
        pdf.multi_cell(largeur, 7, (contenu if contenu else "Non renseigné").encode('latin-1', 'replace').decode('latin-1'), 0, 'L')
        pdf.ln(3) # Espace entre les sections

    # Ajout des 10 sections proprement
    ajouter_section(pdf, "1. INFORMATIONS PERSONNELLES", f"Patient: {nom} {prenom} | Né(e) le: {date_nais} | Tel: {tel}\nUrgence: {contact_urgence} ({tel_urgence})")
    ajouter_section(pdf, "2. MOTIF", motif)
    ajouter_section(pdf, "3. ANTECEDENTS", f"Maladies: {maladies}, Chir: {chir}, Allergies: {allergies}, Traitements: {traitements_cours}\nFamiliaux: {diabete}, {ht}, {cardio}, {cancer}")
    ajouter_section(pdf, "4. HABITUDES DE VIE", habitudes)
    ajouter_section(pdf, "5. EXAMEN CLINIQUE", f"Taille: {taille}cm, Poids: {poids}kg, Tension: {tension}, Fréq: {freq_card}\nObs: {obs_cliniques}")
    ajouter_section(pdf, "6. EXAMENS COMPLEMENTAIRES", examens)
    ajouter_section(pdf, "7. DIAGNOSTIC", diagnostic)
    ajouter_section(pdf, "8. TRAITEMENT", traitement)
    ajouter_section(pdf, "9. RECOMMANDATIONS", recommandations)
    ajouter_section(pdf, "10. SUIVI MEDICAL", suivi)

    # Nom du médecin en bas
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(largeur, 8, f"Médecin : {nom_medecin}".encode('latin-1', 'replace').decode('latin-1'), 0, 'R')
    pdf.multi_cell(largeur, 8, "Signature : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")