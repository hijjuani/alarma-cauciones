import tkinter as tk
import winsound

def beep():
    winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

def create_ui():
    root = tk.Tk()
    root.title("Monitor de Cauciones")
    root.geometry("460x420")
    root.configure(bg="#111")

    tk.Label(
        root, text="Cauciones",
        font=("Arial", 20, "bold"),
        fg="white", bg="#111"
    ).pack(pady=10)

    # -------- Frame 1D --------
    frame_1d = tk.Frame(root, bg="#1b1b1b", bd=2, relief="ridge")
    frame_1d.pack(padx=15, pady=8, fill="x")

    tk.Label(frame_1d, text="1 DÍA", font=("Arial", 14, "bold"),
             fg="white", bg="#1b1b1b").pack(pady=5)

    label_ars_1 = tk.Label(frame_1d, text="ARS: -- %", font=("Arial", 18),
                           fg="cyan", bg="#1b1b1b")
    label_usd_1 = tk.Label(frame_1d, text="USD: -- %", font=("Arial", 18),
                           fg="orange", bg="#1b1b1b")
    label_ars_1.pack()
    label_usd_1.pack()

    status_1d = tk.Label(frame_1d, text="Estado: OK",
                         font=("Arial", 12), fg="lightgreen", bg="#1b1b1b")
    status_1d.pack(pady=5)

    # -------- Frame 7D --------
    frame_7d = tk.Frame(root, bg="#1b1b1b", bd=2, relief="ridge")
    frame_7d.pack(padx=15, pady=8, fill="x")

    tk.Label(frame_7d, text="7 DÍAS", font=("Arial", 14, "bold"),
             fg="white", bg="#1b1b1b").pack(pady=5)

    label_ars_7 = tk.Label(frame_7d, text="ARS: -- %", font=("Arial", 18),
                           fg="cyan", bg="#1b1b1b")
    label_usd_7 = tk.Label(frame_7d, text="USD: -- %", font=("Arial", 18),
                           fg="orange", bg="#1b1b1b")
    label_ars_7.pack()
    label_usd_7.pack()

    status_7d = tk.Label(frame_7d, text="Estado: OK",
                         font=("Arial", 12), fg="lightgreen", bg="#1b1b1b")
    status_7d.pack(pady=5)

    # -------- Estado general --------
    label_status = tk.Label(
        root, text="Esperando datos...",
        font=("Arial", 14),
        fg="lightgray", bg="#111"
    )
    label_status.pack(pady=10)

    return {
        "root": root,
        "label_status": label_status,

        "label_ars_1": label_ars_1,
        "label_usd_1": label_usd_1,
        "label_ars_7": label_ars_7,
        "label_usd_7": label_usd_7,

        "status_1d": status_1d,
        "status_7d": status_7d,

        "frame_1d": frame_1d,
        "frame_7d": frame_7d,
    }


def update_ui(w, data, prev, targets):
    def arrow(curr, prev):
        if prev is None:
            return ""
        if curr > prev:
            return " ↑"
        if curr < prev:
            return " ↓"
        return ""

    ars_1 = data["ars_1"]
    usd_1 = data["usd_1"]
    ars_7 = data["ars_7"]
    usd_7 = data["usd_7"]

    # -------- Labels --------
    w["label_ars_1"].config(text=f"ARS: {ars_1:.2f}" + arrow(ars_1, prev["ars_1"]))
    w["label_usd_1"].config(text=f"USD: {usd_1:.2f}" + arrow(usd_1, prev["usd_1"]))
    w["label_ars_7"].config(text=f"ARS: {ars_7:.2f}" + arrow(ars_7, prev["ars_7"]))
    w["label_usd_7"].config(text=f"USD: {usd_7:.2f}" + arrow(usd_7, prev["usd_7"]))

    stress_1d = ars_1 >= targets["ars"] or usd_1 >= targets["usd"]
    stress_7d = ars_7 >= targets["ars"] or usd_7 >= targets["usd"]

    # -------- 1D --------
    if stress_1d:
        w["status_1d"].config(text="⚠️ Estrés de liquidez", fg="red")
        w["frame_1d"].config(bg="#2b0000")
        if not prev["stress_1d"]:
            beep()
    else:
        w["status_1d"].config(text="Estado: OK", fg="lightgreen")
        w["frame_1d"].config(bg="#1b1b1b")

    # -------- 7D --------
    if stress_7d:
        w["status_7d"].config(text="⚠️ Estrés", fg="red")
        w["frame_7d"].config(bg="#2b0000")
        if not prev["stress_7d"]:
            beep()
    else:
        w["status_7d"].config(text="Estado: OK", fg="lightgreen")
        w["frame_7d"].config(bg="#1b1b1b")

    # -------- General --------
    if stress_1d or stress_7d:
        w["root"].config(bg="#220000")
        w["label_status"].config(text="Mercado estresado", fg="red")
    else:
        w["root"].config(bg="#111")
        w["label_status"].config(text="Mercado normal", fg="lightgreen")

    prev.update({
        "ars_1": ars_1, "usd_1": usd_1,
        "ars_7": ars_7, "usd_7": usd_7,
        "stress_1d": stress_1d,
        "stress_7d": stress_7d
    })