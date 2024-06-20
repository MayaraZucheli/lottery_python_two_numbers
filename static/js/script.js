document.getElementById("gerarNumeros").addEventListener("click", function() {
    fetch("/api/gerar_numeros_loteria1")
        .then(response => response.json())
        .then(data => {
            document.getElementById("numerosGerados").innerText = "Lottery Numbers 1:\n" + data.join(", ");
        })
        .catch(error => console.error('Erro ao gerar números:', error));
});

document.getElementById("gerarNumeros2").addEventListener("click", function() {
    fetch("/api/gerar_numeros_loteria2")
        .then(response => response.json())
        .then(data => {
            document.getElementById("numerosGerados2").innerText = "Lottery Numbers 2:\n" + data.join(", ");
        })
        .catch(error => console.error('Erro ao gerar números:', error));
});