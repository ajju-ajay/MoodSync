document.addEventListener("DOMContentLoaded", function () {

    const emotion = document.querySelector(
        'select[name="emotion"]'
    );

    const button = document.querySelector("button");

    emotion.addEventListener("change", function () {

        const emojis = {
            Happy: "😊",
            Sad: "😢",
            Angry: "😠",
            Relaxed: "😌",
            Motivated: "🔥"
        };

        button.textContent =
            "Find My Music " + (emojis[emotion.value] || "🎧");

    });

});