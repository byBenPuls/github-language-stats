const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({"languages": true})
};

async function getColor(language) {
    try {
        const response = await fetch('./src/static/colors.json');
        const data = await response.json();
        const color = data[language]?.color;
        console.log(color);
        return color;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function fetchData() {
    await fetch("/", options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(async data => {
            console.log('POST запрос выполнен успешно:', data);
            const namesFromPost = data.response
            const languages = namesFromPost.map(name => {
                return {
                    name: name
                };
            });


            const langItems = document.querySelector('[data-testid="lang-items"]');
            langItems.setAttribute('font-family', 'Arial');
            langItems.setAttribute('font-size', '16px');
            langItems.setAttribute('fill', 'black');
            for (const lang of languages) {
                const index = languages.indexOf(lang);
                const group = document.createElementNS('http://www.w3.org/2000/svg', 'g');
                group.setAttribute('transform', `translate(0, ${index * 25})`);

                const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                circle.setAttribute('cx', '5');
                circle.setAttribute('cy', '10');
                circle.setAttribute('r', '5');
                circle.setAttribute('fill', await getColor(lang.name));

                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', '15');
                text.setAttribute('y', '15');
                text.setAttribute('class', 'lang-name');
                text.textContent = lang.name;


                group.appendChild(circle);
                group.appendChild(text);
                langItems.appendChild(group);
            }
        })
        .catch(error => {
            console.error('Ошибка при выполнении POST запроса:', error);
        });
}

fetchData()
