from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ---------------- MAIN WINDOW ---------------- #
root = Tk()
root.title("Language Translator")
root.geometry("700x500")
root.resizable(False, False)

# ---------------- LANGUAGES ---------------- #
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Urdu": "ur"
}

# ---------------- FUNCTIONS ---------------- #
def translate_text():
    text = input_text.get("1.0", END).strip()

    if not text:
        messagebox.showerror("Error", "Please enter text.")
        return

    try:
        target_lang = languages[target_combo.get()]

        translated = GoogleTranslator(
            source="auto",
            target=target_lang
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)


def copy_text():
    translated = output_text.get("1.0", END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        root.update()
        messagebox.showinfo(
            "Copied",
            "Translated text copied successfully!"
        )


# ---------------- TITLE ---------------- #
title = Label(
    root,
    text="🌍 Language Translator",
    font=("Arial", 22, "bold")
)
title.pack(pady=10)

# ---------------- TARGET LANGUAGE ---------------- #
lang_frame = Frame(root)
lang_frame.pack(pady=5)

Label(
    lang_frame,
    text="Target Language:",
    font=("Arial", 12, "bold")
).pack(side=LEFT, padx=5)

target_combo = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly",
    width=25
)

target_combo.pack(side=LEFT)
target_combo.current(0)

# ---------------- INPUT ---------------- #
Label(
    root,
    text="Enter Text",
    font=("Arial", 12, "bold")
).pack()

input_text = Text(
    root,
    height=8,
    width=80,
    font=("Arial", 11)
)
input_text.pack(pady=5)

# ---------------- BUTTONS ---------------- #
button_frame = Frame(root)
button_frame.pack(pady=10)

translate_btn = Button(
    button_frame,
    text="Translate",
    width=15,
    bg="green",
    fg="white",
    font=("Arial", 10, "bold"),
    command=translate_text
)
translate_btn.grid(row=0, column=0, padx=10)

clear_btn = Button(
    button_frame,
    text="Clear",
    width=15,
    bg="red",
    fg="white",
    font=("Arial", 10, "bold"),
    command=clear_text
)
clear_btn.grid(row=0, column=1, padx=10)

copy_btn = Button(
    button_frame,
    text="Copy",
    width=15,
    bg="blue",
    fg="white",
    font=("Arial", 10, "bold"),
    command=copy_text
)
copy_btn.grid(row=0, column=2, padx=10)

# ---------------- OUTPUT ---------------- #
Label(
    root,
    text="Translated Text",
    font=("Arial", 12, "bold")
).pack()

output_text = Text(
    root,
    height=8,
    width=80,
    font=("Arial", 11)
)
output_text.pack(pady=5)

# ---------------- START APP ---------------- #
root.mainloop()