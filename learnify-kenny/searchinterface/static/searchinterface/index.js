document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#search-btn').addEventListener("click", function () {
        retrieveOutput()
    });

    function retrieveOutput(){
        fetch('/display_search/rope')
        .then(response => response.json())
        .then(data => {
            const results_data = data.search_result
            const result_titles = Object.keys(results_data)
            // 
            result_titles.forEach( (result_title)=> {
                const cards_item = document.createElement('li')
                cards_item.classList.add('cards_item')
                // 
                    const card = document.createElement('div')
                    card.classList.add('card')
                    // 
                        const card_image = document.createElement('div')
                        card_image.classList.add('card_image')
                        // 
                            const card_image_img = document.createElement('img')
                            card_image.append(card_image_img)
                        // 
                        const card_content = document.createElement('div')
                        card_content.classList.add('card_content')
                        // 
                            const card_title = document.createElement('h2')
                            card_title.classList.add('card_title')
                            card_title.innerHTML = result_title
                            // 
                            const  card_text = document.createElement('p')
                            card_text.classList.add('card_text')
                            card_text.innerHTML = results_data[result_title]
                            // 
                            const btn = document.createElement('button')
                            btn.classList.add('btn')
                            btn.classList.add('card_btn')
                            btn.id = 'btn-more'
                            btn.innerHTML = 'Read More'
                            // 
                        card_content.append(card_title)
                        card_content.append(card_text)
                        card_content.append(btn)
                        // 
                    card.append(card_image)
                    card.append(card_content)
                    // 
                cards_item.append(card)
                document.querySelector('.cards').append(cards_item)
                // 
            })
        })
    }

})