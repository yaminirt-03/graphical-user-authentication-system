for (let i = 0; i < 40; i++) {
    let particle = document.createElement("div");
    particle.style.position = "absolute";
    particle.style.width = "5px";
    particle.style.height = "5px";
    particle.style.background = "#00f2fe";
    particle.style.borderRadius = "50%";
    particle.style.top = Math.random() * 100 + "vh";
    particle.style.left = Math.random() * 100 + "vw";
    particle.style.opacity = "0.5";
    particle.style.animation = "float 5s infinite ease-in-out";
    document.body.appendChild(particle);
}