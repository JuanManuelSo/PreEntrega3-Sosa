
// const closeModalBtn = document.querySelector(".close-modal-btn");
const overlay = document.querySelector(".overlay");
const bioLinksList = document.querySelectorAll(".bio-link");
const playersContainer = document.querySelector(".players-container");
const overlaysList = playersContainer.querySelectorAll(".overlay");

// closeModalBtn.addEventListener("click", () => {
//     loginModal.classList.remove("active");
//     overlay.classList.remove("d-block");
// });

overlay.addEventListener("click", e => {
    if (e.target === overlay) {
        loginModal.classList.remove("active");
        overlay.classList.remove("d-block");
    }
});

bioLinksList.forEach(link => {

    link.addEventListener("click", e => {
        e.preventDefault()
        const idJugador = e.target.id.split('-')[1];
        console.log(idJugador)
        const overlay = document.querySelector(`#overlay-${idJugador}`);
        const jugadorModal = overlay.firstElementChild;
        jugadorModal.classList.add("active");
        overlay.classList.add("d-block");
    });

});

overlaysList.forEach(ol => {

    const jugadorModal = ol.firstElementChild;
    const closeBtn = jugadorModal.querySelector(".close-modal-btn");

    closeBtn.addEventListener("click", () => {
        jugadorModal.classList.remove("active");
        ol.classList.remove("d-block");
    });

    ol.addEventListener("click", e => {
        if (e.target === ol) {
            jugadorModal.classList.remove("active");
            ol.classList.remove("d-block");
        }
    });

});