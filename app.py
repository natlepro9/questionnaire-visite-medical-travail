# --- Génération PDF corrigée ---
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
    
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(largeur, 8, f"Date : {date.today()} | Patient : {nom} {prenom}".encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)
    
    # --- LA CORRECTION EST ICI ---
    # On crée une liste de textes complets (Titre + contenu ensemble)
    sections = [
        f"MOTIF :\n{motif}",
        f"ANTECEDENTS :\nChroniques: {maladies}, Allergies: {allergies}, Familiaux: {diabete}, {ht}, {cardio}, {cancer}, {autres_fam}",
        f"EXAMEN CLINIQUE :\nTaille: {taille}cm, Poids: {poids}kg, Tension: {tension}, Obs: {obs_clinique}",
        f"DIAGNOSTIC :\n{diagnostic}",
        f"TRAITEMENT :\n{traitement}",
        f"SUIVI :\n{suivi}"
    ]
    
    for bloc in sections:
        pdf.set_font("Arial", 'B', 12)
        # On écrit tout le bloc d'un coup dans le même multi_cell
        pdf.multi_cell(largeur, 8, bloc.encode('latin-1', 'replace').decode('latin-1'), 1)
        pdf.ln(2)
    
    pdf.ln(10)
    pdf.multi_cell(largeur, 8, "Signature du medecin : ____________________", 0, 'R')
    
    st.download_button("Télécharger le Dossier", bytes(pdf.output()), "Dossier_Medical.pdf", "application/pdf")