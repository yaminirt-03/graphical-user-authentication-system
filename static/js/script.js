let selected = [];

function selectEmoji(emoji) {
    if (selected.length < 3) {
        selected.push(emoji);
        document.getElementById("emoji_sequence").value = selected.join(",");
    }
}

/* Theme Toggle */
function toggleTheme() {
    document.body.classList.toggle("light-mode");
}
/* Smooth Page Switch Fade Out */
document.addEventListener("DOMContentLoaded", function () {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 0.5s ease-in-out";
    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 100);
});

document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", function (e) {
        const href = this.getAttribute("href");
        if (href && !href.startsWith("#")) {
            e.preventDefault();
            document.body.style.opacity = "0";
            setTimeout(() => {
                window.location.href = href;
            }, 400);
        }
    });
});
/* Trigger Shake on Login Error */
function triggerShake() {
    const card = document.getElementById("loginCard");
    if (card) {
        card.classList.add("shake");
        setTimeout(() => {
            card.classList.remove("shake");
        }, 500);
    }
}
/* Typing Sound Effect */
document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll("input");
    const sound = document.getElementById("typingSound");

    inputs.forEach(input => {
        input.addEventListener("keydown", () => {
            if (sound) {
                sound.currentTime = 0;
                sound.play();
            }
        });
    });
});
let selectedEmojis = [];

function selectEmoji(element) {

    if (element.classList.contains("selected")) {
        element.classList.remove("selected");
        selectedEmojis = selectedEmojis.filter(e => e !== element.innerText);
    } else {
        if (selectedEmojis.length < 3) {
            element.classList.add("selected");
            selectedEmojis.push(element.innerText);
        } else {
            alert("Select only 3 emojis");
        }
    }

    document.getElementById("emoji_sequence").value = selectedEmojis.join(",");
}