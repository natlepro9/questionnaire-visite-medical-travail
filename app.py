import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale")

# --- 1. Formulaire ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom du patient")
    prenom = st.text_input("Prénom du patient")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1))
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")
    contact_urgence = st.text_input("Personne à contacter en cas d’urgence")
    tel_urgence = st.text_input("Téléphone d'urgence")

nom_medecin = st.text_input("Nom du Médecin") # Champ ajouté

motif = st.text_area("2. Motif de la consultation")

with st.expander("3. Antécédents médicaux"):
    maladies = st.text_input("Maladies chroniques")
    chir = st.text_input("Chirurgies / Hospitalisations")
    allergies = st.text_input("Allergies")
    traitements_cours = st.text_input("Traitements en cours")
    vaccins = st.checkbox("Vaccinations à jour")
    diabete = st.text_input("Diabète")
    ht = st.text_input("Hypertension")
    cardio = st.text_input("Maladies cardiaques")
    cancer = st.text_input("Cancer")
    autres_fam = st.text_input("Autres antécédents familiaux")

habitudes = st.text_area("4. Habitudes de vie (Tabac, Alcool, etc.)")

with st.expander("5. Examen clinique"):
    taille = st.number_input("Taille (cm)")
    poids = st.number_input("Poids (kg)")
    tension = st.text_input("Tension artérielle")
    freq_card = st.text_input("Fréquence cardiaque")
    temp = st.text_input("Température")
    obs_cliniques = st.text_area("Observations médicales")

examens = st.text_area("6. Examens complémentaires")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations médicales")
suivi = st.text_area("10. Suivi médical")

# --- 2. Génération PDF ---
if st.button("Générer le Dossier Médical PDF"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)
    largeur = 180 
    
    # En-tête
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)
    
    pdf.ln(25)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(5)
    
    pdf.set_font("Arial", '', 12)
    info = f"Date : {date.today()} | Patient : {nom} {prenom}"
    pdf.multi_cell(largeur, 8, info.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)
    
    # Liste des données
    data = [
        ("1. INFORMATIONS PERSONNELLES", f"Date naissance: {date_nais} | Sexe: {sexe}\nAdresse: {adresse}\nTel: {tel}\nUrgence: {contact_urgence} ({tel_urgence})"),
        ("2. MOTIF", motif),
        ("3. ANTECEDENTS", f"Maladies: {maladies}, Chir: {chir}, Allergies: {allergies}, Traitements: {traitements_cours}\nFamiliaux: Diabète: {diabete}, HT: {ht}, Cardio: {cardio}, Cancer: {cancer}, Autres: {autres_fam}"),
        ("4. HABITUDES DE VIE", habitudes),
        ("5. EXAMEN CLINIQUE", f"Taille: {taille}cm, Poids: {poids}kg, Tension: {tension}, Fréq: {freq_card}, Temp: {temp}\nObs: {obs_cliniques}"),
        ("6. EXAMENS COMPLEMENTAIRES", examens),
        ("7. DIAGNOSTIC", diagnostic),
        ("8. TRAITEMENT", traitement),
        ("9. RECOMMANDATIONS", recommandations),
        ("10. SUIVI MEDICAL", suivi)
    ]
    
    # Génération des blocs
    for titre, contenu in data:
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur, 8, (contenu if contenu else "Non renseigné").encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.ln(2)
    
    # Section médecin dynamique
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(largeur, 8, f"Médecin traitant : {nom_medecin}".encode('latin-1', 'replace').decode('latin-1'), 0, 'R')
    pdf.multi_cell(largeur, 8, "Signature : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")