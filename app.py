import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(
    page_title="For Veduuu 🎞️",
    page_icon="🤎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# PHOTOS
# -----------------------------
PHOTOS = [
    "photo1.jpg.jpeg",
    "photo2.jpg.jpeg",
    "photo3.jpg.jpeg",
    "photo4.jpg.jpeg",
    "photo5.jpg.jpeg",
    "photo6.jpg.jpeg",
    "photo7.jpg.jpeg",
    "photo8.jpg.jpeg",
    "photo9.jpg.jpeg",
    "photo10.jpg.jpeg",
]

CAPTIONS = [
    "somehow, you became my favourite frame.",
    "this one feels like a scene i'd replay.",
    "no script. just us.",
    "one of those moments i wanna keep.",
    "the kind of memory that stays.",
    "yeah... this frame.",
    "still one of my favourites.",
    "a little piece of us.",
    "if life had a favourite scene, maybe this.",
    "and i'd still choose this frame."
]

YOUTUBE_ID = "xQ6TZGc-IHU"

# Check photos
missing = [p for p in PHOTOS if not os.path.exists(p)]

if missing:
    st.error("Missing photos: " + ", ".join(missing))
    st.stop()

# -----------------------------
# SESSION STATE
# -----------------------------
if "entered" not in st.session_state:
    st.session_state.entered = False


# =========================================================
# OPENING SCREEN
# =========================================================

if not st.session_state.entered:

    st.markdown(
        """
        <style>
        html, body, [data-testid="stAppViewContainer"] {
            background: #21130e !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }

        .opening {
            min-height: 82vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .opening:before {
            content: "";
            position: absolute;
            width: 500px;
            height: 500px;
            background: radial-gradient(
                circle,
                rgba(190,130,75,.20),
                transparent 70%
            );
            animation: glow 5s infinite alternate ease-in-out;
        }

        .tiny {
            color: #b99b87;
            letter-spacing: 5px;
            font-size: 11px;
            margin-bottom: 25px;
            animation: fade 2s ease;
        }

        .title {
            color: #eee0d4;
            font-size: clamp(40px, 7vw, 82px);
            font-weight: 300;
            letter-spacing: 5px;
            margin: 0;
            animation: titleIn 1.7s ease;
        }

        .subtitle {
            color: #a98c79;
            font-size: 14px;
            letter-spacing: 3px;
            margin-top: 20px;
            animation: fade 2.5s ease;
        }

        @keyframes glow {
            from { transform: scale(.8); opacity: .5; }
            to { transform: scale(1.3); opacity: 1; }
        }

        @keyframes titleIn {
            from {
                opacity: 0;
                transform: translateY(30px);
                letter-spacing: 20px;
            }
            to {
                opacity: 1;
                transform: translateY(0);
                letter-spacing: 5px;
            }
        }

        @keyframes fade {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Streamlit button styling */
        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: -80px;
            position: relative;
            z-index: 20;
        }

        div.stButton > button {
            background: transparent !important;
            color: #ead9cc !important;
            border: 1px solid rgba(220,190,165,.55) !important;
            border-radius: 50px !important;
            padding: 14px 42px !important;
            letter-spacing: 4px !important;
            font-size: 12px !important;
            transition: all .35s ease !important;
        }

        div.stButton > button:hover {
            background: rgba(220,190,165,.12) !important;
            border-color: #ead9cc !important;
            transform: scale(1.06);
        }

        @media(max-width:600px) {
            .title {
                font-size: 42px;
            }

            .subtitle {
                font-size: 11px;
            }
        }
        </style>

        <div class="opening">
            <div class="tiny">A LITTLE FILM ABOUT US</div>
            <div class="title">FOR VE DUUU</div>
            <div class="subtitle">10 frames · one story</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("ENTER FILM", use_container_width=False):
        st.session_state.entered = True
        st.rerun()

    st.stop()


# =========================================================
# MOVIE SCREEN
# =========================================================

photo_data = []

for photo in PHOTOS:
    with open(photo, "rb") as f:
        import base64
        encoded = base64.b64encode(f.read()).decode()

    ext = photo.lower().split(".")[-1]

    mime = "image/jpeg"
    if ext == "png":
        mime = "image/png"
    elif ext == "webp":
        mime = "image/webp"

    photo_data.append(f"data:{mime};base64,{encoded}")


photos_json = json.dumps(photo_data)
captions_json = json.dumps(CAPTIONS)
youtube_json = json.dumps(YOUTUBE_ID)

HTML = r"""
<!DOCTYPE html>
<html>
<head>

<meta name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

<style>

* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #160b07;
    font-family: Arial, sans-serif;
}

body {
    position: relative;
}

/* CINEMATIC BACKGROUND */

.scene {
    position: fixed;
    inset: 0;
    overflow: hidden;
    background:
        radial-gradient(
            circle at 50% 45%,
            #513223 0%,
            #2a170f 42%,
            #120806 100%
        );
}

/* MOVING LIGHTS */

.light {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: .28;
}

.l1 {
    width: 350px;
    height: 350px;
    background: #a36c42;
    top: -120px;
    left: -100px;
    animation: move1 9s infinite alternate ease-in-out;
}

.l2 {
    width: 300px;
    height: 300px;
    background: #75472d;
    right: -100px;
    bottom: -80px;
    animation: move2 11s infinite alternate ease-in-out;
}

@keyframes move1 {
    to {
        transform: translate(180px, 180px) scale(1.3);
    }
}

@keyframes move2 {
    to {
        transform: translate(-150px, -150px) scale(1.2);
    }
}

/* FILM GRAIN */

.grain {
    position: absolute;
    inset: -50%;
    opacity: .08;
    background-image:
        repeating-radial-gradient(
            circle,
            #fff 0 1px,
            transparent 1px 3px
        );
    animation: grain .15s steps(2) infinite;
}

@keyframes grain {
    0% { transform: translate(0,0); }
    25% { transform: translate(2%, -2%); }
    50% { transform: translate(-2%, 2%); }
    75% { transform: translate(1%, 2%); }
    100% { transform: translate(-1%, -1%); }
}

/* DUST */

.dust {
    position: absolute;
    width: 3px;
    height: 3px;
    background: rgba(255,220,190,.5);
    border-radius: 50%;
    animation: float 7s infinite linear;
}

@keyframes float {
    from {
        transform: translateY(100vh);
        opacity: 0;
    }

    30% {
        opacity: .7;
    }

    to {
        transform: translateY(-10vh);
        opacity: 0;
    }
}

/* FILM STRIPS */

.strip {
    position: fixed;
    left: 0;
    width: 100%;
    height: 32px;
    background: #090403;
    z-index: 10;
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.strip.top {
    top: 0;
}

.strip.bottom {
    bottom: 0;
}

.hole {
    width: 17px;
    height: 9px;
    border-radius: 2px;
    background: #342018;
}

/* TOP INFO */

.info {
    position: fixed;
    top: 48px;
    left: 28px;
    right: 28px;
    z-index: 15;
    display: flex;
    justify-content: space-between;
    color: rgba(240,220,205,.65);
    font-size: 10px;
    letter-spacing: 3px;
}

.rec {
    display: flex;
    gap: 7px;
    align-items: center;
}

.dot {
    width: 7px;
    height: 7px;
    background: #c77b58;
    border-radius: 50%;
    animation: blink 1s infinite;
}

@keyframes blink {
    50% { opacity: .2; }
}

/* PHOTO */

.stage {
    position: absolute;
    inset: 70px 25px 75px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.photo-frame {
    position: relative;
    max-width: 90vw;
    max-height: 70vh;
    width: auto;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    transition:
        width .65s cubic-bezier(.2,.8,.2,1),
        height .65s cubic-bezier(.2,.8,.2,1),
        transform .65s ease;
}

.photo-frame img {
    display: block;
    max-width: 90vw;
    max-height: 70vh;
    width: auto;
    height: auto;
    object-fit: contain;
    box-shadow:
        0 30px 70px rgba(0,0,0,.55);
    animation: photoIn .8s ease;
}

@keyframes photoIn {
    from {
        opacity: 0;
        transform: scale(.94);
        filter: brightness(.4);
    }

    to {
        opacity: 1;
        transform: scale(1);
        filter: brightness(1);
    }
}

/* SHINE */

.shine {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background:
        linear-gradient(
            110deg,
            transparent 35%,
            rgba(255,255,255,.16) 50%,
            transparent 65%
        );
    transform: translateX(-120%);
}

.shine.play {
    animation: shine 1.1s ease;
}

@keyframes shine {
    to {
        transform: translateX(120%);
    }
}

/* CAPTION */

.caption {
    position: fixed;
    left: 20px;
    right: 20px;
    bottom: 115px;
    text-align: center;
    color: #eadbd0;
    font-size: 14px;
    letter-spacing: 2px;
    z-index: 15;
    transition: opacity .35s ease, transform .35s ease;
}

.caption.hide {
    opacity: 0;
    transform: translateY(8px);
}

/* CONTROLS */

.controls {
    position: fixed;
    bottom: 48px;
    left: 0;
    right: 0;
    z-index: 20;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 18px;
}

button {
    cursor: pointer;
    color: #eadbd0;
    background: rgba(30,15,10,.65);
    border: 1px solid rgba(230,205,185,.35);
    border-radius: 50px;
    padding: 9px 20px;
    letter-spacing: 2px;
    font-size: 10px;
    transition: .3s;
}

button:hover {
    background: rgba(230,205,185,.13);
    transform: scale(1.05);
}

.counter {
    color: rgba(240,220,205,.6);
    font-size: 10px;
    letter-spacing: 3px;
}

/* FINAL */

.final {
    position: fixed;
    inset: 0;
    z-index: 30;
    background:
        radial-gradient(
            circle,
            #4c2d20,
            #160b07 70%
        );
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 1s ease;
    text-align: center;
}

.final.show {
    opacity: 1;
    pointer-events: auto;
}

.final h1 {
    color: #eee0d4;
    font-size: clamp(38px, 7vw, 75px);
    font-weight: 300;
    letter-spacing: 7px;
    margin: 0 0 20px;
}

.final p {
    color: #bda493;
    letter-spacing: 3px;
    font-size: 12px;
}

/* MOBILE */

@media(max-width:600px) {

    .info {
        top: 42px;
        left: 16px;
        right: 16px;
        font-size: 8px;
    }

    .stage {
        inset: 65px 10px 100px;
    }

    .photo-frame img {
        max-width: 94vw;
        max-height: 64vh;
    }

    .caption {
        bottom: 105px;
        font-size: 12px;
        line-height: 1.6;
    }

    .controls {
        bottom: 45px;
        gap: 10px;
    }

    button {
        padding: 8px 14px;
    }

}

</style>

</head>

<body>

<div class="scene">

<div class="light l1"></div>
<div class="light l2"></div>

<div class="grain"></div>

<!-- dust -->
<div class="dust" style="left:8%;animation-delay:1s"></div>
<div class="dust" style="left:18%;animation-delay:4s"></div>
<div class="dust" style="left:31%;animation-delay:2s"></div>
<div class="dust" style="left:47%;animation-delay:5s"></div>
<div class="dust" style="left:63%;animation-delay:1.5s"></div>
<div class="dust" style="left:78%;animation-delay:3s"></div>
<div class="dust" style="left:91%;animation-delay:6s"></div>

<div class="strip top">
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
</div>

<div class="strip bottom">
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
    <div class="hole"></div>
</div>

<div class="info">
    <div>BOYFRIEND'S DAY • 2026</div>

    <div class="rec">
        <span class="dot"></span>
        REC
    </div>
</div>

<div class="stage">

    <div class="photo-frame" id="frame">
        <img id="photo" src="">
        <div class="shine" id="shine"></div>
    </div>

</div>

<div class="caption" id="caption"></div>

<div class="controls">

    <button onclick="previousPhoto()">←</button>

    <div class="counter" id="counter">01 / 10</div>

    <button onclick="nextPhoto()">→</button>

</div>

<div class="final" id="final">

    <h1>THE END.</h1>

    <p>
        same us. different frames.
    </p>

    <button onclick="restart()">
        REPLAY
    </button>

</div>

</div>

<!-- MUSIC GETS CREATED BY JAVASCRIPT -->
<div id="music"></div>

<script>

const photos = __PHOTOS__;
const captions = __CAPTIONS__;
const youtubeID = __YOUTUBE__;

let current = 0;

const photo = document.getElementById("photo");
const caption = document.getElementById("caption");
const counter = document.getElementById("counter");
const shine = document.getElementById("shine");
const finalScreen = document.getElementById("final");


/* MUSIC */

function startMusic() {

    const music = document.getElementById("music");

    music.innerHTML = `
        <iframe
            width="1"
            height="1"
            src="https://www.youtube.com/embed/${youtubeID}?autoplay=1&loop=1&playlist=${youtubeID}"
            allow="autoplay; encrypted-media"
            style="position:absolute;left:-9999px;border:0;">
        </iframe>
    `;
}


/* PHOTO */

function showPhoto(index) {

    current = index;

    caption.classList.add("hide");

    setTimeout(() => {

        photo.src = photos[current];

        photo.onload = () => {

            /*
            Browser reads the REAL image dimensions.
            Nothing is cropped.
            */

            const ratio =
                photo.naturalWidth /
                photo.naturalHeight;

            const maxWidth =
                Math.min(window.innerWidth * .90, 1100);

            const maxHeight =
                window.innerHeight * .68;

            let width = maxWidth;
            let height = width / ratio;

            if (height > maxHeight) {
                height = maxHeight;
                width = height * ratio;
            }

            document.getElementById("frame").style.width =
                width + "px";

            document.getElementById("frame").style.height =
                height + "px";
        };

        caption.textContent = captions[current];

        counter.textContent =
            String(current + 1).padStart(2,"0")
            + " / "
            + photos.length;

        caption.classList.remove("hide");

        shine.classList.remove("play");

        void shine.offsetWidth;

        shine.classList.add("play");

    }, 220);
}


/* NEXT */

function nextPhoto() {

    if (current >= photos.length - 1) {
        finalScreen.classList.add("show");
        return;
    }

    showPhoto(current + 1);
}


/* PREVIOUS */

function previousPhoto() {

    if (current <= 0) return;

    showPhoto(current - 1);
}


/* REPLAY */

function restart() {

    finalScreen.classList.remove("show");

    showPhoto(0);
}


/* KEYBOARD */

document.addEventListener("keydown", function(e) {

    if (e.key === "ArrowRight") {
        nextPhoto();
    }

    if (e.key === "ArrowLeft") {
        previousPhoto();
    }

});


/* SWIPE */

let touchStartX = 0;

document.addEventListener("touchstart", function(e) {

    touchStartX = e.changedTouches[0].screenX;

});

document.addEventListener("touchend", function(e) {

    const touchEndX =
        e.changedTouches[0].screenX;

    const difference =
        touchEndX - touchStartX;

    if (Math.abs(difference) < 50) return;

    if (difference < 0) {
        nextPhoto();
    } else {
        previousPhoto();
    }

});


/*
IMPORTANT:
Music starts as soon as the movie page loads.
*/

window.addEventListener("load", function() {

    showPhoto(0);

    setTimeout(() => {
        startMusic();
    }, 150);

});

</script>

</body>
</html>
"""

# Safe replacement — NO f-string, so no curly-brace SyntaxError
HTML = HTML.replace("__PHOTOS__", photos_json)
HTML = HTML.replace("__CAPTIONS__", captions_json)
HTML = HTML.replace("__YOUTUBE__", youtube_json)

components.html(
    HTML,
    height=900,
    scrolling=False
)