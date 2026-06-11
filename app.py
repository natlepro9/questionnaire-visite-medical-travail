import streamlit as st
from fpdf import FPDF
import os
import datetime
from datetime import date

st.title("Dossier de Visite Médicale Complet")

# --- Formulaire ---
with st.expander("1. Informations personnelles", expanded=True):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_nais = st.date_input("Date de naissance", min_value=datetime.date(1900, 1, 1))
    sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
    adresse = st.text_area("Adresse")
    tel = st.text_input("Téléphone")
    contact_urgence = st.text_input("Personne à contacter en cas d’urgence")
    tel_urgence = st.text_input("Téléphone d’urgence")

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
    autres_fam = st.text_input("Antécédents familiaux autres")

habitudes = st.text_area("4. Habitudes de vie (Tabac, Alcool, Activité, Sommeil, etc.)")

with st.expander("5. Examen clinique"):
    taille = st.number_input("Taille (cm)")
    poids = st.number_input("Poids (kg)")
    tension = st.text_input("Tension artérielle")
    freq_card = st.text_input("Fréquence cardiaque")
    temp = st.text_input("Température")
    obs_cliniques = st.text_area("Observations médicales")

examens = st.text_area("6. Examens complémentaires (Sang, Radio, etc.)")
diagnostic = st.text_area("7. Diagnostic")
traitement = st.text_area("8. Traitement")
recommandations = st.text_area("9. Recommandations médicales")
suivi = st.text_area("10. Suivi médical (Prochain RDV, Examens à prévoir)")

# --- Génération PDF ---
if st.button("Générer le Dossier Médical PDF"):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 15, 15)
    
    largeur = 180 
    
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)
    
    pdf.ln(25)
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(largeur, 10, "DOSSIER DE VISITE MEDICALE", 0, 'C')
    pdf.ln(5)
    
    # Construction de la liste des données
    data = [
        ("1. INFORMATIONS PERSONNELLES", f"Nom: {nom} | Prénom: {prenom} | Date nais: {date_nais} | Sexe: {sexe}\nAdresse: {adresse}\nTel: {tel}\nUrgence: {contact_urgence} ({tel_urgence})"),
        ("2. MOTIF", motif),
        ("3. ANTECEDENTS", f"Maladies: {maladies}, Chir: {chir}, Allergies: {allergies}, Traitements: {traitements_cours}\nFamiliaux: Diabète: {diabete}, HT: {ht}, Cardio: {cardio}, Cancer: {cancer}, Autres: {autres_fam}"),
        ("4. HABITUDES DE VIE", habitudes),
        ("5. EXAMEN CLINIQUE", f"Taille: {taille}cm, Poids: {poids}kg, Tension: {tension}, Fréq. Cardiaque: {freq_card}, Temp: {temp}\nObservations: {obs_cliniques}"),
        ("6. EXAMENS COMPLEMENTAIRES", examens),
        ("7. DIAGNOSTIC", diagnostic),
        ("8. TRAITEMENT", traitement),
        ("9. RECOMMANDATIONS", recommandations),
        ("10. SUIVI MEDICAL", suivi)
    ]
    
    for titre, contenu in data:
        pdf.set_font("Arial", 'B', 12)
        pdf.multi_cell(largeur, 8, titre.encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(largeur, 8, (contenu if contenu else "Non renseigné").encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.ln(2)
    
    pdf.ln(10)
    pdf.multi_cell(largeur, 8, "Signature du medecin : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")