import csv
from datetime import datetime
import time
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(page_title="Olé Olé, ElFah!", page_icon="⚽")


# =========================================================
# SAVE MESSAGE
# =========================================================


def simpan_pesan(nama, pesan):
  with open("pesan.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
      writer.writerow(["Waktu", "Nama", "Pesan"])

    writer.writerow(
        [datetime.now().strftime("%d-%m-%Y %H:%M"), nama, pesan]
    )


# =========================================================
# SESSION STATE
# =========================================================

if "halaman" not in st.session_state:
  st.session_state.halaman = 1

if "opening_selesai" not in st.session_state:
  st.session_state.opening_selesai = False

if "mau_kabar" not in st.session_state:
  st.session_state.mau_kabar = False

if "kabar_sudah_dikirim" not in st.session_state:
  st.session_state.kabar_sudah_dikirim = False

if "cerita_sudah_dikirim" not in st.session_state:
  st.session_state.cerita_sudah_dikirim = False

if "rencana_sudah_dikirim" not in st.session_state:
  st.session_state.rencana_sudah_dikirim = False

if "tendangan" not in st.session_state:
  st.session_state.tendangan = False

if "game_ready" not in st.session_state:
  st.session_state.game_ready = False


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Cabin+Sketch:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&display=swap');

/* ==============================
   BARÇA PALETTE
   ============================== */

:root {
    --barca-blue: #004D98;
    --barca-red: #A50044;
    --barca-gold: #EDBB00;
    --cream: #FFF9F0;
    --soft-blue: #E8F1FA;
    --dark-blue: #17365D;
    --soft-red: #F8E5ED;
}


/* ==============================
   DEFAULT BACKGROUND
   ============================== */

.stApp {
    background-color: var(--cream);
}


/* ==============================
   GENERAL TEXT & HEADINGS (CRAYON)
   ============================== */

p, li, label, span {
    font-family: 'Cabin Sketch', cursive !important;
    color: var(--dark-blue);
}

h1, h2, h3 {
    font-family: 'Cabin Sketch', cursive !important;
    color: var(--dark-blue) !important;
    font-weight: 700 !important;
}

h1 {
    position: relative;
}


/* ==============================
   BUTTON (FORCE FULL CENTER & EMAS BARÇA)
   ============================== */

div[data-testid="stButton"],
div.stButton {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
    margin: 10px auto !important;
}

div[data-testid="stButton"] > button,
.stButton > button {
    font-family: 'Cabin Sketch', cursive !important;
    font-weight: 700 !important;
    font-size: 1.35rem !important;
    letter-spacing: 1px !important;

    color: #172B45 !important;

    background: linear-gradient(
        135deg,
        #FFD700 0%,
        #EDBB00 50%,
        #D4A000 100%
    ) !important;

    border: 2px solid #FFE066 !important;
    border-radius: 16px !important;
    padding: 0.65rem 2rem !important;

    box-shadow: 
        0 4px 15px rgba(237, 187, 0, 0.35),
        inset 0 1px 0 rgba(255, 255, 255, 0.4) !important;

    transition: all 0.25s ease !important;
    display: block !important;
    margin: 0 auto !important;
}

/* Button hover */
div[data-testid="stButton"] > button:hover,
.stButton > button:hover {
    color: #FFF9F0 !important;

    background: linear-gradient(
        135deg,
        #D8005A 0%,
        #A50044 100%
    ) !important;

    border-color: #FF4D88 !important;
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 20px rgba(165, 0, 68, 0.45) !important;
}


/* ==============================
   INPUT / TEXT AREA (CRAYON STYLE)
   ============================== */

.stTextInput input,
.stTextArea textarea {
    font-family: 'Cabin Sketch', cursive !important;
    font-size: 1.25rem !important;
    font-weight: 700 !important;

    background-color: #FFF9F0 !important;
    border: 2px solid #EDBB00 !important;
    border-radius: 14px !important;
    color: #A50044 !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #FFD700 !important;
    box-shadow: 0 0 0 3px rgba(237, 187, 0, 0.35) !important;
}


/* ==============================
   INFO / BOX & DIVIDER
   ============================== */

div[data-testid="stAlert"] {
    border-radius: 14px !important;
}

hr {
    border: none !important;
    height: 3px !important;
    border-radius: 10px;
    background: linear-gradient(
        90deg,
        var(--barca-blue),
        var(--barca-red),
        var(--barca-gold)
    );
    opacity: 0.8;
}

a {
    color: var(--barca-blue) !important;
    font-weight: 700 !important;
    font-family: 'Cabin Sketch', cursive !important;
}

a:hover {
    color: var(--barca-red) !important;
}

footer, #MainMenu {
    visibility: hidden;
}


/* =========================================================
   PAGE 1 — HOMEPAGE
   ========================================================= */

.homepage {
    text-align: center;
}

.stApp:has(.homepage) {
    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(0, 77, 152, 0.95),
            transparent 45%
        ),
        radial-gradient(
            circle at 85% 25%,
            rgba(165, 0, 68, 0.95),
            transparent 50%
        ),
        linear-gradient(
            135deg,
            #002B5C 0%,
            #004D98 30%,
            #5B174A 60%,
            #A50044 100%
        ) !important;
}

.stApp:has(.homepage):before {
    content: "";
    position: fixed;
    inset: 0;
    background:
        linear-gradient(
            115deg,
            transparent 0%,
            rgba(237, 187, 0, 0.08) 35%,
            transparent 36%,
            transparent 65%,
            rgba(237, 187, 0, 0.06) 66%,
            transparent 100%
        );
    pointer-events: none;
    z-index: 0;
}

.main .block-container {
    position: relative;
    z-index: 1;
}

/* Seluruh teks di Homepage krem terang anti-tenggelam */
.homepage p,
.homepage label,
.homepage span,
.homepage div {
    color: #FFF9F0 !important;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5) !important;
}


/* ==============================
   DECORATIONS
   ============================== */

.barca-decoration-left {
    position: fixed;
    left: 25px;
    bottom: 45px;
    font-size: 70px;
    opacity: 0.18;
    transform: rotate(-12deg);
    pointer-events: none;
}

.barca-decoration-right {
    position: fixed;
    right: 35px;
    bottom: 55px;
    font-size: 65px;
    opacity: 0.20;
    transform: rotate(10deg);
    pointer-events: none;
}


/* ==============================
   HERO TITLE & SUBTITLE
   ============================== */

.hero-title {
    text-align: center;
    font-family: 'Cabin Sketch', cursive !important;
    font-size: 4.8rem;
    font-weight: 700;
    color: #EDBB00 !important;
    margin-top: 15px;
    margin-bottom: 0;
    letter-spacing: 1.5px;
    text-shadow:
        3px 4px 0px #172B45,
        5px 6px 0px rgba(0, 0, 0, 0.25) !important;
    transform: rotate(-1.5deg);
}

.hero-subtitle {
    text-align: center;
    font-family: 'Cabin Sketch', cursive !important;
    font-size: 1.45rem !important;
    font-weight: 700;
    color: #FFF9F0 !important;
    margin-top: 8px;
    margin-bottom: 25px;
    letter-spacing: 0.8px;
    text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6) !important;
}

.gold-line {
    width: 100px;
    height: 5px;
    margin: 10px auto 20px auto;
    border-radius: 10px;
    background: #EDBB00;
    transform: rotate(-2deg);
}

.football {
    text-align: center;
    font-size: 55px;
    margin-top: 5px;
    margin-bottom: -5px;
    animation: footballFloat 3s ease-in-out infinite;
}

@keyframes footballFloat {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-8px) rotate(8deg); }
}

.barca-slogan {
    text-align: center;
    font-family: 'Cabin Sketch', cursive !important;
    font-size: 1.85rem !important;
    font-weight: 700;
    color: #FFD700 !important;
    margin-top: 35px;
    letter-spacing: 1px;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
}

.message-card {
    max-width: 720px;
    margin: 25px auto;
    padding: 20px;
    background: rgba(255, 249, 240, 0.95);
    border-radius: 20px;
    color: #A50044 !important;
    font-family: 'Cabin Sketch', cursive !important;
    font-size: 1.45rem;
    font-weight: 700;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.paper-plane {
    text-align: center;
    font-size: 45px;
    color: #EDBB00;
    animation: flyPlane 1.5s ease-out forwards;
}

@keyframes flyPlane {
    0% { transform: translateX(-100px) rotate(-10deg); opacity: 0; }
    30% { opacity: 1; }
    100% { transform: translateX(100px) rotate(-10deg); opacity: 0; }
}


/* =========================================
   PAGE 2 — CERITA HARI INI
   ========================================= */

.stApp:has(.story-page) p,
.stApp:has(.story-page) label,
.stApp:has(.story-page) textarea {
    font-family: 'Cabin Sketch', cursive !important;
}

.stApp:has(.story-page) p,
.stApp:has(.story-page) label {
    color: #A50044 !important;
    font-size: 1.35rem !important;
}


/* =========================================
   PAGE 3 — RENCANA ELFAH
   ========================================= */

.stApp:has(.plan-page) p,
.stApp:has(.plan-page) label,
.stApp:has(.plan-page) textarea {
    font-family: 'Cabin Sketch', cursive !important;
}

.stApp:has(.plan-page) p,
.stApp:has(.plan-page) label {
    color: #004D98 !important;
    font-size: 1.35rem !important;
}


/* =========================================================
   PAGE 4 — BARÇA FOOTBALL
   ========================================================= */

.stApp:has(.stadium-page-marker) {
    background:
        radial-gradient(circle at 15% 10%, rgba(0, 77, 152, 0.95), transparent 35%),
        radial-gradient(circle at 85% 20%, rgba(165, 0, 68, 0.95), transparent 40%),
        linear-gradient(135deg, #002B5C 0%, #004D98 35%, #5B174A 65%, #A50044 100%) !important;
}

.stadium-page-marker {
    display: none;
}

@media (max-width: 768px) {
    .hero-title { font-size: 3.2rem; }
    .hero-subtitle { font-size: 1.15rem; }
    .barca-decoration-left, .barca-decoration-right { font-size: 45px; }
}

</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# OPENING ANIMATION
# =========================================================

if not st.session_state.opening_selesai:

  components.html(
      """
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background: transparent;
            }
            .opening {
                width: 100%;
                height: 120px;
                position: relative;
                overflow: hidden;
            }
            .ball {
                position: absolute;
                font-size: 42px;
                left: -60px;
                bottom: 10px;
                animation: kickBall 2.2s ease-out forwards;
            }
            @keyframes kickBall {
                0% {
                    left: -60px;
                    bottom: 10px;
                    transform: rotate(0deg);
                    opacity: 0;
                }
                10% { opacity: 1; }
                35% {
                    left: 30%;
                    bottom: 75px;
                    transform: rotate(180deg);
                }
                60% {
                    left: 55%;
                    bottom: 25px;
                    transform: rotate(360deg);
                }
                80% {
                    left: 75%;
                    bottom: 55px;
                    transform: rotate(540deg);
                }
                100% {
                    left: 105%;
                    bottom: 15px;
                    transform: rotate(720deg);
                    opacity: 0;
                }
            }
        </style>
        <div class="opening">
            <div class="ball">⚽</div>
        </div>
        """,
      height=120,
  )

  time.sleep(2.2)
  st.session_state.opening_selesai = True
  st.rerun()


# =========================================================
# PAGE 1
# =========================================================

if st.session_state.halaman == 1:

  st.markdown('<div class="homepage">', unsafe_allow_html=True)

  # ==============================
  # DECORATIONS
  # ==============================
  st.markdown(
      '<div class="barca-decoration-left">⚽</div>', unsafe_allow_html=True
  )
  st.markdown(
      '<div class="barca-decoration-right">⚽</div>', unsafe_allow_html=True
  )

  # ==============================
  # HERO
  # ==============================
  st.markdown('<div class="football">⚽</div>', unsafe_allow_html=True)
  st.markdown(
      '<div class="hero-title">Olé Olé, ElFah!</div>', unsafe_allow_html=True
  )
  st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)
  st.markdown(
      '<div class="hero-subtitle">'
      'Hi, Elman & Fahman! Ini Uni Najwa dan Uni Ega 👋'
      '</div>',
      unsafe_allow_html=True,
  )

  # ==============================
  # INTERACTION (TOMBOL CENTER VIA 3 COLUMNS)
  # ==============================
  if not st.session_state.mau_kabar:

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("💌 Kabarin Uni Dong!", use_container_width=True):
        st.session_state.mau_kabar = True
        st.rerun()

  else:

    st.write("Ceritain ke Uni dongg tentang hari ini!!!")

    jawaban = st.text_input(
        "Tulis kabar kalian di sini:",
        placeholder="Ketik kabar kalian di sini...",
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("💌 Kirim Kabar ke Uni", use_container_width=True):

        if jawaban:
          simpan_pesan("Kabar", jawaban)

          st.markdown(
              '<div class="paper-plane">➤</div>', unsafe_allow_html=True
          )

          time.sleep(1.5)
          st.session_state.kabar_sudah_dikirim = True
          st.rerun()

        else:
          st.write("Kabarin Uni dulu yaa, Elfah. 🥺")

  # ==============================
  # AFTER MESSAGE
  # ==============================
  if st.session_state.kabar_sudah_dikirim:

    st.markdown(
        '<div class="message-card">'
        'Aaa Uni seneng banget bisa denger kabar kalian ❤️'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("⚽ Cerita apaa ya hari ini?", use_container_width=True):
        st.session_state.halaman = 2
        st.rerun()

  # ==============================
  # SLOGAN
  # ==============================
  st.markdown(
      '<div class="barca-slogan">Més que un club, una família 💙❤️</div>',
      unsafe_allow_html=True,
  )

  st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PAGE 2
# =========================================================

if st.session_state.halaman == 2:

  st.markdown('<div class="story-page"></div>', unsafe_allow_html=True)

  components.html(
      """
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background: transparent;
            }
            .ball {
                font-size: 32px;
                position: absolute;
                left: -50px;
                top: 5px;
                animation: kick 1.5s linear forwards;
            }
            @keyframes kick {
                0% {
                    left: -50px;
                    transform: rotate(0deg);
                    opacity: 0;
                }
                15% { opacity: 1; }
                85% { opacity: 1; }
                100% {
                    left: 90%;
                    transform: rotate(720deg);
                    opacity: 0;
                }
            }
        </style>
        <div class="ball">⚽</div>
        """,
      height=50,
  )

  st.header("🌤️ Cerita Hari Ini")
  st.write("Jadiii, Un, hari ini tuh... El, Fah....")

  cerita = st.text_area("Cerita kalian:")

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("Dengerin Cerita Elman Fahman, yaa, Un!", use_container_width=True):

      if cerita:
        simpan_pesan("Cerita", cerita)

        st.markdown(
            '<div class="message-card">'
            "Wahh, uni baca dulu ya cerita kalian. ❤️"
            "</div>",
            unsafe_allow_html=True,
        )

        st.session_state.cerita_sudah_dikirim = True

      else:
        st.write("Tulis ceritanya dulu yaa, Elfah. 🥺")

  if st.session_state.cerita_sudah_dikirim:

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("Mau cerita lagi sama Uni?", use_container_width=True):
        st.session_state.halaman = 3
        st.rerun()


# =========================================================
# PAGE 3 — RENCANA ELFAH
# =========================================================

if st.session_state.halaman == 3:

  # Gunakan container khusus agar semua elemen halaman 3 terisolasi
  page3_container = st.container()

  with page3_container:
    st.markdown('<div class="plan-page"></div>', unsafe_allow_html=True)
    st.header("📅 Rencana Elman & Fahman")

    st.write(
        "Kira-kira apa rencana Elman dan Fahman selama "
        "beberapa minggu ke depan sampai nanti bisa pulang lagi?🧐"
    )

    rencana = st.text_area("Rencana kalian:", key="input_rencana")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("Jadi gitu, Un, rencananya...", use_container_width=True):
        if rencana:
          simpan_pesan("Rencana", rencana)
          st.session_state.rencana_sudah_dikirim = True

          # Kosongkan wadah halaman 3 seketika
          page3_container.empty()

          # Alihkan ke halaman loading terisolasi (3.5)
          st.session_state.game_ready = False
          st.session_state.tendangan = False
          st.session_state.halaman = 3.5
          st.rerun()
        else:
          st.write("Tulis rencananya dulu yaa, Elfah. 🥺")


# =========================================================
# PAGE 3.5 — TRANSISI LOADING KHUSUS (BERSIH DARI FORM APAPUN)
# =========================================================

if st.session_state.halaman == 3.5:

  st.markdown(
      '<div class="stadium-page-marker"></div>', unsafe_allow_html=True
  )

  st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)

  # Komponen animasi loading berdiri sendiri tanpa ada form di belakangnya
  components.html(
      """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Cabin+Sketch:wght@700&display=swap');

            body {
                margin: 0;
                padding: 0;
                background: transparent;
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
            }

            .loading-container {
                text-align: center;
                font-family: 'Cabin Sketch', cursive;
                color: white;
            }

            .loading-title {
                font-size: 2.2rem;
                font-weight: 700;
                color: #FFF9F0;
                letter-spacing: 1px;
                margin-bottom: 20px;
                text-shadow: 0 4px 10px rgba(0, 0, 0, 0.45);
                animation: pulseText 1.5s ease-in-out infinite;
            }

            @keyframes pulseText {
                0%, 100% { transform: scale(1); opacity: 0.9; }
                50% { transform: scale(1.04); opacity: 1; }
            }

            .loading-balls {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 16px;
            }

            .loading-ball {
                font-size: 38px;
                display: inline-block;
                animation: bounceAndSpin 1.1s cubic-bezier(0.28, 0.84, 0.42, 1) infinite;
            }

            .loading-ball:nth-child(2) { animation-delay: 0.18s; }
            .loading-ball:nth-child(3) { animation-delay: 0.36s; }

            @keyframes bounceAndSpin {
                0%, 100% { transform: translateY(0) rotate(0deg); }
                50%      { transform: translateY(-26px) rotate(180deg); }
            }
        </style>

        <div class="loading-container">
            <div class="loading-title">Sebelum Uni lanjutin.......</div>
            <div class="loading-balls">
                <div class="loading-ball">⚽</div>
                <div class="loading-ball">⚽</div>
                <div class="loading-ball">⚽</div>
            </div>
        </div>
        """,
      height=200,
  )

  time.sleep(3)
  st.session_state.game_ready = True
  st.session_state.halaman = 4
  st.rerun()


# =========================================================
# PAGE 4 — FOOTBALL GAME (MURNI GAWANG BOLA)
# =========================================================

if st.session_state.halaman == 4:

  st.markdown(
      '<div class="stadium-page-marker"></div>', unsafe_allow_html=True
  )

  # -----------------------------------------------------
  # FASE STANDBY MENUNGGU TENDANGAN
  # -----------------------------------------------------
  if not st.session_state.tendangan:

    components.html(
        """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Cabin+Sketch:wght@700&display=swap');

                body {
                    margin: 0;
                    padding: 0;
                    background: transparent;
                }

                .football-intro {
                    text-align: center;
                    font-family: 'Cabin Sketch', cursive;
                    color: white;
                }

                .kick-intro {
                    font-size: 1.8rem;
                    font-weight: 700;
                    margin-top: 10px;
                    margin-bottom: 10px;
                    color: #FFD700;
                    letter-spacing: 1px;
                    text-shadow: 0 3px 6px rgba(0,0,0,0.4);
                }

                .game-area {
                    width: 100%;
                    height: 200px;
                    position: relative;
                    overflow: hidden;
                }

                .goal {
                    position: absolute;
                    right: 25px;
                    top: 25px;
                    font-size: 90px;
                    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.35));
                }

                .game-football {
                    position: absolute;
                    left: 25px;
                    top: 110px;
                    font-size: 58px;
                    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
                }
            </style>

            <div class="football-intro">
                <div class="kick-intro">Ayo coba masukin ke gawang~</div>
                <div class="game-area">
                    <div class="goal">🥅</div>
                    <div class="game-football">⚽</div>
                </div>
            </div>
            """,
        height=240,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("⚽ TENDANG!", use_container_width=True):
        st.session_state.tendangan = True
        st.rerun()

  # -----------------------------------------------------
  # FASE TENDANGAN + KOMENTAR LIVE + GOL + CONFETTI BRUTAL
  # -----------------------------------------------------
  else:

    components.html(
        """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Cabin+Sketch:wght@700&family=Baloo+2:wght@800&display=swap');

                * { box-sizing: border-box; }
                body { margin: 0; padding: 0; overflow: hidden; background: transparent; }

                .stage-container {
                    position: relative;
                    width: 100%;
                    height: 340px;
                    overflow: hidden;
                }

                #confetti-canvas {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    z-index: 20;
                }

                .game-area {
                    width: 100%;
                    height: 175px;
                    position: relative;
                }

                .goal {
                    position: absolute;
                    right: 25px;
                    top: 25px;
                    font-size: 85px;
                    z-index: 1;
                    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
                }

                .game-football {
                    position: absolute;
                    left: 20px;
                    top: 105px;
                    font-size: 48px;
                    z-index: 5;
                    animation: kickToGoal 1.8s cubic-bezier(0.25, 0.8, 0.35, 1) forwards;
                }

                @keyframes kickToGoal {
                    0%   { left: 20px; top: 105px; transform: rotate(0deg) scale(1); }
                    30%  { left: 32%;  top: 35px;  transform: rotate(450deg) scale(1.12); }
                    58%  { left: 58%;  top: 15px;  transform: rotate(950deg) scale(1.02); }
                    80%  { left: 74%;  top: 45px;  transform: rotate(1400deg) scale(0.92); }
                    100% { left: 84%;  top: 55px;  transform: rotate(1800deg) scale(0.82); }
                }

                .barca-loading-commentary {
                    position: absolute;
                    top: 195px;
                    left: 0;
                    right: 0;
                    text-align: center;
                    font-family: 'Cabin Sketch', cursive;
                    font-size: 1.65rem;
                    font-weight: 700;
                    letter-spacing: 1.5px;
                    height: 40px;
                    pointer-events: none;
                    z-index: 15;
                }

                .comment-line {
                    position: absolute;
                    width: 100%;
                    left: 0;
                    opacity: 0;
                    transform: translateY(8px);
                }

                .c-line-1 {
                    color: #FFD700;
                    text-shadow: 0 2px 5px rgba(0,0,0,0.5);
                    animation: showComment 0.7s ease-in-out forwards 0.05s;
                }

                .c-line-2 {
                    color: #FFF9F0;
                    text-shadow: 0 2px 5px rgba(0,0,0,0.5);
                    animation: showComment 0.7s ease-in-out forwards 0.75s;
                }

                .c-line-3 {
                    color: #FF3366;
                    font-size: 1.8rem;
                    text-shadow: 0 2px 6px rgba(0,0,0,0.6);
                    animation: showComment 0.5s ease-in-out forwards 1.45s;
                }

                @keyframes showComment {
                    0%   { opacity: 0; transform: translateY(10px) scale(0.95); }
                    25%  { opacity: 1; transform: translateY(0) scale(1); }
                    80%  { opacity: 1; transform: translateY(0) scale(1); }
                    100% { opacity: 0; transform: translateY(-8px) scale(1.05); }
                }

                .goal-text {
                    text-align: center;
                    margin-top: 5px;
                    font-family: 'Baloo 2', cursive;
                    font-size: 3.3rem;
                    font-weight: 800;
                    letter-spacing: 2px;
                    color: #FFF9F0;
                    -webkit-text-stroke: 2px #004D98;
                    text-shadow: 0 5px 0 #002B5C, 0 10px 20px rgba(0,0,0,0.4);
                    white-space: nowrap;
                    position: relative;
                    z-index: 10;
                }

                .goal-letter {
                    display: inline-block;
                    opacity: 0;
                    transform: translateY(40px) scale(0.3);
                    animation: letterPop 0.6s cubic-bezier(.17,.89,.32,1.49) forwards,
                               bubbleWobble 1.1s ease-in-out infinite;
                }

                .goal-letter:nth-child(1) { animation-delay: 1.80s, 2.40s; }
                .goal-letter:nth-child(2) { animation-delay: 1.90s, 2.50s; }
                .goal-letter:nth-child(3) { animation-delay: 2.00s, 2.60s; }
                .goal-letter:nth-child(4) { animation-delay: 2.10s, 2.70s; }
                .goal-letter:nth-child(5) { animation-delay: 2.20s, 2.80s; }
                .goal-letter:nth-child(6) { animation-delay: 2.30s, 2.90s; }
                .goal-letter:nth-child(7) { animation-delay: 2.40s, 3.00s; }
                .goal-letter:nth-child(8) { animation-delay: 2.50s, 3.10s; }

                @keyframes letterPop {
                    0%   { opacity: 0; transform: translateY(40px) scale(0.3); }
                    60%  { opacity: 1; transform: translateY(-12px) scale(1.22); }
                    100% { opacity: 1; transform: translateY(0) scale(1); }
                }

                @keyframes bubbleWobble {
                    0%, 100% { transform: translateY(0) scale(1) rotate(0deg); }
                    50%      { transform: translateY(-7px) scale(1.05) rotate(-2deg); }
                }

                .goal-subtext {
                    text-align: center;
                    color: #FFD700;
                    margin-top: 4px;
                    font-family: 'Cabin Sketch', cursive;
                    font-size: 1.55rem;
                    font-weight: 700;
                    opacity: 0;
                    animation: fadeInSub 0.5s ease forwards;
                    animation-delay: 2.2s;
                    text-shadow: 1px 2px 4px rgba(0,0,0,0.5);
                    position: relative;
                    z-index: 10;
                }

                @keyframes fadeInSub {
                    from { opacity: 0; transform: translateY(10px); }
                    to   { opacity: 1; transform: translateY(0); }
                }
            </style>

            <div class="stage-container">
                <canvas id="confetti-canvas"></canvas>

                <div class="game-area">
                    <div class="goal">🥅</div>
                    <div class="game-football">⚽</div>
                </div>

                <div class="barca-loading-commentary">
                    <div class="comment-line c-line-1">Yapp...Tiki-taka dimulai...</div>
                    <div class="comment-line c-line-2">Mencari celah... AURA JUARA!</div>
                    <div class="comment-line c-line-3">VISCA EL BARÇA! SIAP-SIAP...</div>
                </div>

                <div class="goal-text">
                    <span class="goal-letter">G</span>
                    <span class="goal-letter">O</span>
                    <span class="goal-letter">O</span>
                    <span class="goal-letter">O</span>
                    <span class="goal-letter">L</span>
                    <span class="goal-letter">L</span>
                    <span class="goal-letter">L</span>
                    <span class="goal-letter">!</span>
                </div>

                <div class="goal-subtext">
                    VISCA EL BARÇA I VISCA ELFAH!!!
                </div>
            </div>

            <script>
                const canvas = document.getElementById('confetti-canvas');
                const ctx = canvas.getContext('2d');

                function resizeCanvas() {
                    canvas.width = window.innerWidth;
                    canvas.height = window.innerHeight;
                }
                resizeCanvas();
                window.addEventListener('resize', resizeCanvas);

                const colors = [
                    '#EDBB00', '#FFD700',
                    '#A50044', '#D8005A',
                    '#004D98', '#0070DF',
                    '#00E676', '#FF1744', '#E040FB', '#00E5FF', '#FFFFFF'
                ];

                class Particle {
                    constructor(x, y, angle, speed, sizeMultiplier = 1) {
                        this.x = x;
                        this.y = y;
                        this.vx = Math.cos(angle) * speed;
                        this.vy = Math.sin(angle) * speed;
                        this.color = colors[Math.floor(Math.random() * colors.length)];
                        this.w = (Math.random() * 8 + 6) * sizeMultiplier;
                        this.h = (Math.random() * 12 + 8) * sizeMultiplier;
                        this.rot = Math.random() * Math.PI * 2;
                        this.rotSpeed = (Math.random() - 0.5) * 0.28;
                        this.rotY = Math.random() * Math.PI * 2;
                        this.rotYSpeed = (Math.random() - 0.5) * 0.35;
                        this.opacity = 1;
                        this.decay = Math.random() * 0.005 + 0.003;
                        this.gravity = 0.22;
                        this.drag = 0.985;
                        this.isCircle = Math.random() < 0.25;
                    }

                    update() {
                        this.vx *= this.drag;
                        this.vy *= this.drag;
                        this.vy += this.gravity;
                        this.x += this.vx;
                        this.y += this.vy;
                        this.rot += this.rotSpeed;
                        this.rotY += this.rotYSpeed;
                        this.opacity -= this.decay;
                    }

                    draw(ctx) {
                        if (this.opacity <= 0) return;
                        ctx.save();
                        ctx.translate(this.x, this.y);
                        ctx.rotate(this.rot);
                        ctx.scale(Math.cos(this.rotY), 1);
                        ctx.globalAlpha = Math.max(0, this.opacity);
                        ctx.fillStyle = this.color;

                        if (this.isCircle) {
                            ctx.beginPath();
                            ctx.arc(0, 0, this.w / 2, 0, Math.PI * 2);
                            ctx.fill();
                        } else {
                            ctx.fillRect(-this.w / 2, -this.h / 2, this.w, this.h);
                        }

                        ctx.restore();
                    }
                }

                let particles = [];

                function shootCannon(originX, originY, count, minAngle, maxAngle, minSpeed, maxSpeed) {
                    for (let i = 0; i < count; i++) {
                        const angle = minAngle + Math.random() * (maxAngle - minAngle);
                        const speed = minSpeed + Math.random() * (maxSpeed - minSpeed);
                        particles.push(new Particle(originX, originY, angle, speed, Math.random() * 0.4 + 0.9));
                    }
                }

                function triggerBrutalExplosion() {
                    const goalX = canvas.width - 70;
                    const goalY = 85;

                    shootCannon(goalX, goalY, 220, Math.PI * 0.65, Math.PI * 1.35, 12, 28);

                    setTimeout(() => {
                        shootCannon(40, canvas.height - 10, 130, -Math.PI * 0.45, -Math.PI * 0.15, 14, 26);
                        shootCannon(canvas.width - 40, canvas.height - 10, 130, -Math.PI * 0.85, -Math.PI * 0.55, 14, 26);
                    }, 220);

                    setTimeout(() => {
                        shootCannon(goalX, goalY, 140, Math.PI * 0.7, Math.PI * 1.3, 10, 24);
                    }, 480);
                }

                setTimeout(() => {
                    triggerBrutalExplosion();
                }, 1800);

                function loop() {
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    for (let i = particles.length - 1; i >= 0; i--) {
                        particles[i].update();
                        particles[i].draw(ctx);
                        if (particles[i].opacity <= 0 || particles[i].y > canvas.height + 50) {
                            particles.splice(i, 1);
                        }
                    }
                    requestAnimationFrame(loop);
                }
                loop();
            </script>
            """,
        height=340,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      if st.button("💌 Buka pesan dari Uni", use_container_width=True):
        st.session_state.halaman = 5
        st.rerun()
# =========================================================
# PAGE 5
# =========================================================

if st.session_state.halaman == 5:

  components.html(
      """
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background: transparent;
            }
            .ball {
                font-size: 32px;
                position: absolute;
                left: -50px;
                top: 5px;
                animation: kick 1.5s linear forwards;
            }
            @keyframes kick {
                0% {
                    left: -50px;
                    transform: rotate(0deg);
                    opacity: 0;
                }
                15% { opacity: 1; }
                85% { opacity: 1; }
                100% {
                    left: 90%;
                    transform: rotate(720deg);
                    opacity: 0;
                }
            }
        </style>
        <div class="ball">⚽</div>
        """,
      height=50,
  )

  st.header("Elman, Fahman, yang selalu uni sayang...")

  st.write(
      "Mungkin Uni nggak selalu tahu apa yang kalian lakukan setiap hari, tapi"
      " Uni selalu senang kalau bisa dengar cerita kalian. ❤️"
  )

  st.write(
      "Selama beberapa minggu ke depan, jalanin hari-harinya dengan baik yaa."
      " Kalau capek, istirahat. Kalau senang, dinikmati. Kalau ada cerita,"
      " jangan disimpan sendiri."
  )

  st.write(
      "Gak cuma Uni Najwa sama Uni Ega, tapi Papa, Mama, selalu doain kalian,"
      " sampai nanti waktunya pulang lagi. ❤️"
  )

  st.write(
      "Jaga diri baik-baik ya, El, Fah. Sukses untuk segala doa dan harapan"
      " cita-cita kalian, Uni sayang bangetttt sm adek! 🫶🏻"
  )