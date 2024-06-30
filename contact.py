import qrcode
from PIL import Image
import tkinter as tk
from tkinter import messagebox, filedialog

def generate_vcard_qr_code(
    name: str,
    phone: str,
    email: str,
    address: str = "",
    company: str = "",
    job_title: str = "",
    website: str = "",
    note: str = "",
    logo_path: str = None
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
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction to accommodate logo
        box_size=10,
        border=4,
    )
    qr.add_data(vcard.strip())
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white').convert('RGB')

    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Calculate the position and size for the logo
            logo_size = min(img.size[0], img.size[1]) // 4
            logo = logo.resize((logo_size, logo_size))
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo, pos, logo)
        except Exception as e:
            messagebox.showerror("Fehler", f"Das Logo konnte nicht geladen werden: {e}")

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
    logo_path = entry_logo_path.get()
    
    if not name or not phone or not email:
        messagebox.showerror("Fehler", "Name, Telefon und E-Mail sind Pflichtfelder.")
        return

    generate_vcard_qr_code(name, phone, email, address, company, job_title, website, note, logo_path)

def browse_logo():
    logo_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    entry_logo_path.delete(0, tk.END)
    entry_logo_path.insert(0, logo_path)

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

tk.Label(root, text="Logo (optional)").grid(row=8, column=0, padx=10, pady=5)
entry_logo_path = tk.Entry(root)
entry_logo_path.grid(row=8, column=1, padx=10, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_logo)
browse_button.grid(row=8, column=2, padx=10, pady=5)

submit_button = tk.Button(root, text="QR-Code erstellen", command=submit)
submit_button.grid(row=9, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
