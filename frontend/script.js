setInterval(async () => {
    try {
        const res = await fetch("/status");
        const data = await res.json();

        const signals = document.querySelectorAll(".signal");

        signals.forEach((s, i) => {
            s.className = "signal";

            if (i === data.current_lane) {
                if (data.state === "GREEN") s.classList.add("green");
                else s.classList.add("yellow");
            } else {
                s.classList.add("red");
            }
        });

    } catch {
        console.log("Backend not connected");
    }
}, 1000);