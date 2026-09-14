import streamlit as st
import streamlit.components.v1 as components
import time
import csv
from datetime import datetime
st.set_page_config(
    page_title="Olé Olé, ElFah!",
    page_icon="⚽"
)

def simpan_pesan(nama, pesan):
    with open("pesan.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Waktu", "Nama", "Pesan"])

        writer.writerow([
            datetime.now().strftime("%d-%m-%Y %H:%M"),
            nama,
            pesan
        ])

if "halaman" not in st.session_state:
    st.session_state.halaman = 1

if "opening_selesai" not in st.session_state:
    st.session_state.opening_selesai = False

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Fredoka:wght@400;500;600&family=Quicksand:wght@400;500;600;700&display=swap');

.stApp {
    background-color: #FFF9F0;
}

.stApp * {
    font-family: 'Quicksand', sans-serif !important;
}

body {
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 400;
}

.stApp h1 {
    font-family: 'Fredoka', sans-serif !important;
}

h1 {
    color: #7A4636;
    font-size: 2.4rem;
    font-weight: 700;
}

h2, h3 {
    color: #4F83A8;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 500;
}

h1::after {
    content: "";
    display: block;
    width: 60px;
    height: 4px;
    background-color: #F4A261;
    border-radius: 10px;
    margin-top: 10px;
}

p {
    color: #7A4636;
}

.stButton p {
    color: #FFF9F0 !important;
}

.stButton > button {
    background-color: #4F83A8;
    border: none;
    border-radius: 20px;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
}

.stButton > button p {
    color: #FFF9F0 !important;
}

.stButton > button:hover {
    background-color: #3F6F91;
}

.stButton > button:hover p {
    color: #FFF9F0 !important;
}

/* KOTAK INPUT */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background-color: #DCEEF7;
    color: #7A4636;
    border: 2px solid #B8D8E8;
    border-radius: 15px;
    padding: 12px 15px;
}

.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {
    color: #718797;
    opacity: 1;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #4F83A8;
    box-shadow: 0 0 0 2px rgba(79, 131, 168, 0.15);
}

.message-card {
    background-color: #FFFDF8;
    border-left: 5px solid #F4A261;
    padding: 15px 18px;
    border-radius: 12px;
    color: #7A4636;
    margin-top: 15px;
    margin-bottom: 15px;
}

.story-card {
    background-color: #E8F4F9;
    border-left: 5px solid #4F83A8;
    padding: 15px 18px;
    border-radius: 12px;
    color: #7A4636;
    margin-top: 15px;
    margin-bottom: 15px;
}

.plan-card {
    background-color: #FFFDF8;
    border-left: 5px solid #F4A261;
    padding: 15px 18px;
    border-radius: 12px;
    color: #7A4636;
    margin-top: 15px;
    margin-bottom: 15px;
}

.paper-plane {
    font-size: 2rem;
    display: inline-block;
    animation: flyAway 1.5s ease-in-out forwards;
}

@keyframes flyAway {
    0% {
        transform: translate(0, 0) rotate(0deg);
        opacity: 1;
    }

    50% {
        transform: translate(100px, -40px) rotate(-10deg);
        opacity: 1;
    }

    100% {
        transform: translate(250px, -120px) rotate(-15deg);
        opacity: 0;
    }
}

/* ANIMASI PERPINDAHAN HALAMAN */
.page-animation {
    animation: pageIn 0.6s ease-out;
}

@keyframes pageIn {
    from {
        opacity: 0;
        transform: translateX(35px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.transition-page {
    animation: pageSlideIn 2.0s ease-out;
}

@keyframes pageSlideIn {
    from {
        opacity: 0;
        transform: translateX(80px);
    }

    60% {
        opacity: 0.7;
        transform: translateX(20px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}

</style>
""", unsafe_allow_html=True)

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

                10% {
                    opacity: 1;
                }

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
        height=120
    )

    time.sleep(2.2)

    st.session_state.opening_selesai = True
    st.rerun()

if st.session_state.halaman == 1:
    st.markdown('<div class="page-animation">', unsafe_allow_html=True)

    st.title("⚽ Olé Olé, ElFah!")

    st.write("Hi, Elman & Fahman! Ini Uni Najwa dan Uni Ega 👋")

    if "mau_kabar" not in st.session_state:
        st.session_state.mau_kabar = False

    if not st.session_state.mau_kabar:
        if st.button("Kabarin uni dong!!"):
            st.session_state.mau_kabar = True
            st.rerun()

    else:
        st.write("Ceritain ke Uni dongg tentang hari ini!!!")

        jawaban = st.text_input("Tulis kabar kalian di sini:")

        if st.button("Kirim Kabar ke Uni"):
            if jawaban:

                simpan_pesan("Kabar", jawaban)

                st.markdown(
                    '<div class="paper-plane">➤</div>',
                    unsafe_allow_html=True
                )

                time.sleep(1.5)

                st.session_state.kabar_sudah_dikirim = True
                st.rerun()

            else:
                st.write("Kabarin Uni dulu yaa, Elfah. 🥺")

        if st.session_state.get("kabar_sudah_dikirim", False):
            st.markdown(
                '<div class="message-card">Aaa Uni seneng banget bisa denger kabar kalian ❤️</div>',
                unsafe_allow_html=True
            )

            if st.button("Cerita apaa ya hari ini?"):
                st.session_state.halaman = 2
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.halaman == 2:
    components.html(
        """
        <style>
            body {
                margin: 0;
                overflow: hidden;
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

                15% {
                    opacity: 1;
                }

                85% {
                    opacity: 1;
                }

                100% {
                    left: 90%;
                    transform: rotate(720deg);
                    opacity: 0;
                }
            }
        </style>

        <div class="ball">⚽</div>
        """,
        height=50
    )

    st.markdown('<div class="transition-page">', unsafe_allow_html=True)

    st.header("🌤️ Cerita Hari Ini")

    st.write("Jadiii, Un, hari ini tuh... El, Fah....")
  

    cerita = st.text_area("Cerita kalian:")

    if st.button("Dengerin Cerita Elman Fahman, yaa, Un!"):
        if cerita:

            simpan_pesan("Cerita", cerita)

            st.markdown(
                '<div class="message-card">Wahh, uni baca dulu ya cerita kalian. ❤️</div>',
                unsafe_allow_html=True
            )

            st.session_state.cerita_sudah_dikirim = True

        else:
            st.write("Tulis ceritanya dulu yaa, Elfah. 🥺")

    if st.session_state.get("cerita_sudah_dikirim", False):

        if st.button("Mau cerita lagi sama Uni?"):
            st.session_state.halaman = 3
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.halaman == 3:

    st.markdown(
        '<div class="transition-page">',
        unsafe_allow_html=True
    )

    st.header("📅 Rencana Elman & Fahman")

    st.write(
        "Kira-kira apa rencana Elman dan Fahman selama beberapa minggu ke depan sampai nanti bisa pulang lagi?🧐"
    )

    st.write(
        "Cerita ajaa, Uni pengen tahu kalian mau ngapain aja selama di sana."
    )

    rencana = st.text_area("Rencana kalian:")

    if st.button("Jadi gitu, Un, rencananya..."):

        if rencana:

            simpan_pesan("Rencana", rencana)

            st.markdown(
                '<div class="plan-card">Okee, siappp, goodluck, dekk!</div>',
                unsafe_allow_html=True
            )

            st.session_state.rencana_sudah_dikirim = True

        else:

            st.write(
                "Tulis rencananya dulu yaa, Elfah. 🥺"
            )

    if st.session_state.get("rencana_sudah_dikirim", False):

        st.markdown(
            '<div class="message-card">⚽ Sebelum lanjut...<br><br>Masukin bola ke gawang dulu dong! 😆🥅</div>',
            unsafe_allow_html=True
        )

        if "tendangan" not in st.session_state:
            st.session_state.tendangan = False

        if not st.session_state.tendangan:

            components.html(
                """
                <style>

                    .game-area {
                        width: 100%;
                        height: 180px;
                        position: relative;
                        overflow: hidden;
                    }

                    .goal {
                        position: absolute;
                        right: 30px;
                        top: 45px;
                        font-size: 65px;
                    }

                    .football {
                        position: absolute;
                        left: 20px;
                        top: 115px;
                        font-size: 42px;
                    }

                </style>

                <div class="game-area">

                    <div class="goal">🥅</div>

                    <div class="football">⚽</div>

                </div>
                """,
                height=180
            )

            if st.button(
                "⚽ TENDANG!",
                use_container_width=True
            ):

                st.session_state.tendangan = True
                st.rerun()

        else:

            components.html(
                """
                <style>

                    .game-area {
                        width: 100%;
                        height: 180px;
                        position: relative;
                        overflow: hidden;
                    }

                    .goal {
                        position: absolute;
                        right: 30px;
                        top: 45px;
                        font-size: 65px;
                    }

                    .football {
                        position: absolute;
                        left: 20px;
                        top: 115px;
                        font-size: 42px;
                        animation: kickToGoal 1.8s ease-out forwards;
                    }

                    @keyframes kickToGoal {

                        0% {
                            left: 20px;
                            top: 115px;
                            transform: rotate(0deg);
                        }

                        20% {
                            left: 25%;
                            top: 70px;
                            transform: rotate(360deg);
                        }

                        40% {
                            left: 45%;
                            top: 25px;
                            transform: rotate(720deg);
                        }

                        60% {
                            left: 62%;
                            top: 15px;
                            transform: rotate(1080deg);
                        }

                        78% {
                            left: 76%;
                            top: 55px;
                            transform: rotate(1440deg);
                        }

                        100% {
                            left: 88%;
                            top: 65px;
                            transform: rotate(1800deg);
                        }

                    }

                    .goal-text {
                        text-align: center;
                        margin-top: 10px;
                        font-family: 'Fredoka', sans-serif;
                        font-size: 1.8rem;
                        color: #4F83A8;
                        opacity: 0;
                        animation: showGoal 0.5s ease forwards;
                        animation-delay: 1.8s;
                    }

                    .goal-subtext {
                        text-align: center;
                        color: #7A4636;
                        margin-top: 5px;
                        opacity: 0;
                        animation: showGoal 0.5s ease forwards;
                        animation-delay: 2.1s;
                    }

                    @keyframes showGoal {

                        from {
                            opacity: 0;
                            transform: translateY(10px);
                        }

                        to {
                            opacity: 1;
                            transform: translateY(0);
                        }

                    }

                </style>

                <div class="game-area">

                    <div class="goal">🥅</div>

                    <div class="football">⚽</div>

                </div>

                <div class="goal-text">
                    GOOOOOLLLL!!! 🎉⚽🥅
                </div>

                <div class="goal-subtext">
                    Vamos!!! Elman Fahman selalu best!!!😆
                </div>

                """,
                height=250
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(
                "💌 Buka pesan dari Uni",
                use_container_width=True
            ):

                st.session_state.halaman = 4
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.halaman == 4:
    components.html(
        """
        <style>
            body {
                margin: 0;
                overflow: hidden;
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

                15% {
                    opacity: 1;
                }

                85% {
                    opacity: 1;
                }

                100% {
                    left: 90%;
                    transform: rotate(720deg);
                    opacity: 0;
                }
            }
        </style>

        <div class="ball">⚽</div>
        """,
        height=50
    )

    st.markdown(
        '<div class="transition-page">',
        unsafe_allow_html=True
    )

    st.header("Elman, Fahman, yang selalu uni sayang...")

    st.write("Mungkin Uni nggak selalu tahu apa yang kalian lakukan setiap hari, tapi Uni selalu senang kalau bisa dengar cerita kalian. ❤️")

    st.write("Selama beberapa minggu ke depan, jalanin hari-harinya dengan baik yaa. Kalau capek, istirahat. Kalau senang, dinikmati. Kalau ada cerita, jangan disimpan sendiri.")

    st.write("Gak cuma Uni Najwa sama Uni Ega, tapi Papa, Mama, selalu doain kalian, sampai nanti waktunya pulang lagi. ❤️")

    st.write("Jaga diri baik-baik ya, El, Fah. Sukses untuk segala doa dan harapan cita-cita kalian, Uni sayang bangetttt sm adek! 🫶🏻")

    st.markdown('</div>')