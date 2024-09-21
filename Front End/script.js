// Setze den Füllstand der Füllstandsanzeige für jeden Button (vertikal)
function setFillLevel(buttonId, percentage) {
    const button = document.getElementById(buttonId);
    const fillBar = button.querySelector('.fill');
    fillBar.style.height = percentage + '%'; // Setze den Füllstand in Prozent (vertikal)
}

// Beispiel: Füllstände für die Buttons festlegen
setFillLevel('button1', 10); // 75% für Button 1
setFillLevel('button2', 40); // 40% für Button 2
setFillLevel('button3', 60); // 60% für Button 3
setFillLevel('button4', 90); // 90% für Button 4
setFillLevel('button5', 20); // 20% für Button 5
setFillLevel('button6', 50); // 50% für Button 6
setFillLevel('button7', 85); // 85% für Button 7
setFillLevel('button8', 10); // 10% für Button 8

// Vorhandene Klickfunktion für Buttons
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        alert(button.textContent + ' wurde geklickt!');
    });
});
