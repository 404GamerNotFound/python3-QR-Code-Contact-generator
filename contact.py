import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_vcard_qr_code(
    name: str, 
    phone: str, 
    email: str, 
    address: str = "", 
    company: str = "", 
    job_title: str = "", 
    website: str = "", 
    note: str = ""
):
    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{address}
ORG:{company}
TITLE:{job_title}
URL:{website}
NOTE:{note}
END:VCARD
"""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard.strip())
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('contact_qr_code.png')
    messagebox.showinfo("Erfolg", "Der QR-Code wurde erfolgreich erstellt und als contact_qr_code.png gespeichert.")

def submit():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    company = entry_company.get()
    job_title = entry_job_title.get()
    website = entry_website.get()
    note = entry_note.get()
    
    if not name or not phone or not email:
        messagebox.showerror("Fehler", "Name, Telefon und E-Mail sind Pflichtfelder.")
        return

    generate_vcard_qr_code(name, phone, email, address, company, job_title, website, note)

# GUI erstellen
root = tk.Tk()
root.title("Kontakt QR-Code Generator")

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Telefon").grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="E-Mail").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Adresse").grid(row=3, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Firma").grid(row=4, column=0, padx=10, pady=5)
entry_company = tk.Entry(root)
entry_company.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Job Titel").grid(row=5, column=0, padx=10, pady=5)
entry_job_title = tk.Entry(root)
entry_job_title.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Website").grid(row=6, column=0, padx=10, pady=5)
entry_website = tk.Entry(root)
entry_website.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Notiz").grid(row=7, column=0, padx=10, pady=5)
entry_note = tk.Entry(root)
entry_note.grid(row=7, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="QR-Code erstellen", command=submit)
submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

root.mainloop()

