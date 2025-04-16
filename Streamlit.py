import streamlit as st
st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6 {
            color: #c2185b !important;
        }

        label, p, span, .stTextInput, .stSelectbox, .stRadio {
            color: #d63384 !important;
        }

        .css-1cpxqw2, .css-10trblm, .css-1v0mbdj {
            color: #d63384 !important;
        }

        .stButton>button {
            background-color: #f06292;
            color: white;
            font-weight: bold;
            border-radius: 12px;
        }

        .stButton>button:hover {
            background-color: #e91e63;
        }

        .stTextInput>div>input {
            color: #000000 !important;
        }

        .stSelectbox>div>div>div {
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- Fonction principale ---
def chatbot():
    st.title("Bienvenue chez Beyond The Sim ! 🏁✨")
    st.markdown("#### GUI avec toi ! Ta question concerne quoi ?")

    options = {
        "🛒 Choisir un abonnement": choisir_abonnement,
        "💬 Questions sur mon abonnement": questions_abonnement,
        "🔧 Support technique": support_technique,
        "📦 Suivi de commande": suivi_commande,
        "🎟️ Pass Propriétaire": pass_proprietaire,
    }

    choix = st.selectbox("Sélectionne une option :", list(options.keys()) + ["❌ Quitter"])

    if choix == "❌ Quitter":
        st.success("Merci de ta visite ! 🚗💨")
    else:
        if options[choix]():
            st.info("Tu peux choisir une autre option ci-dessus.")

# --- Fonctions secondaires ---
def choisir_abonnement():
    st.subheader("Quel est ton niveau de sim racing ?")
    niveau = st.radio("", ["Débutant", "Intermédiaire", "Perfectionnement"])

    if niveau == "Débutant":
        st.markdown("**Offre Débutant** :\n- 60€/mois sans engagement\n- 55€/mois pour 6 mois\n- 50€/mois pour 12 mois")
    elif niveau == "Intermédiaire":
        st.markdown("**Offre Intermédiaire** :\n- 110€/mois sans engagement\n- 100€/mois pour 6 mois\n- 90€/mois pour 12 mois")
    elif niveau == "Perfectionnement":
        st.markdown("**Offre Perfectionnement** :\n- 160€/mois sans engagement\n- 145€/mois pour 6 mois\n- 130€/mois pour 12 mois")

    return continuer()

def questions_abonnement():
    st.subheader("Quelle est ta question ?")
    question = st.selectbox("", [
        "Changer d'abonnement",
        "Résilier mon abonnement",
        "Paiement et facturation",
        "Date de renouvellement"
    ])

    if question == "Changer d'abonnement":
        st.write("👉 Tu peux changer ton abonnement dans ton espace utilisateur.")
    elif question == "Résilier mon abonnement":
        st.write("📞 Contacte le service client au 00.00.00.00.00.")
    elif question == "Paiement et facturation":
        st.write("🧾 Les infos de paiement sont sur ton compte.")
    elif question == "Date de renouvellement":
        st.write("🔁 Ton abonnement se renouvelle automatiquement chaque mois.")

    return continuer()

def support_technique():
    st.subheader("Quel type de support recherches-tu ?")
    choix = st.radio("", ["Problèmes de livraison", "Mode d'emploi des périphériques"])

    if choix == "Problèmes de livraison":
        st.write("📦 Contacte notre service de livraison au 00.00.00.00.00")
    elif choix == "Mode d'emploi des périphériques":
        st.write("🛠️ Modes d'emploi : [BeyondTheSim - Guides]( https://beyond-the-sim-website.vercel.app/#features  )")

    return continuer()

def suivi_commande():
    st.subheader("Saisis ton numéro de commande 📦")
    numero = st.text_input("Numéro de commande :")
    if numero:
        st.success(f"Ta commande `{numero}` est en cours de traitement.")
    return continuer()

def pass_proprietaire():
    st.subheader("Pass Propriétaire - Achète ton matériel 🎮")
    st.write("Tu as loué du matériel et tu veux l'acheter ? Voici nos offres :")
    niveau = st.selectbox("Sélectionne ton niveau :", ["Débutant", "Intermédiaire", "Perfectionnement"])

    if niveau == "Débutant":
        st.markdown("Réduction de 20% à 35% selon l'état du matériel.")
    elif niveau == "Intermédiaire":
        st.markdown("Réduction de 20% à 30% selon l'état du matériel.")
    elif niveau == "Perfectionnement":
        st.markdown("Réduction de 20% à 30% selon l'état du matériel.")

    st.write("📝 Nous te proposerons un examen du matériel pour établir le prix final.")
    return continuer()

def continuer():
    return st.radio("Souhaites-tu continuer ?", ["oui", "non"]) == "oui"

# --- Lancement ---
if __name__ == "__main__":
    chatbot()
