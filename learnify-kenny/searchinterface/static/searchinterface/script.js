document.addEventListener('DOMContentLoaded', () => {

    //variables used in code
    const searchBtn = document.getElementById("search-btn");
    const searchBox = document.getElementById("search-box");
    const firstContainer = document.getElementById("container-1");
    const secondContainer = document.getElementById("container-2");
    const secondInput = document.getElementById("search-box-2");
    const secondBtn = document.getElementById("search-btn-2");
    let text;
    let userSearch;

    //Event listener to change the text of main button to search

    searchBox.addEventListener("focus", function () {
        searchBtn.textContent = "Search";
        text = searchBtn.textContent;
        searchBtn.style.paddingRight = "3.5rem";
    });

    searchBtn.addEventListener("focus", function () {
        searchBtn.textContent = "Search";
        searchBtn.style.paddingRight = "3.5rem";
    });

    searchBtn.addEventListener("focusout", function () {
        searchBtn.textContent = "Tap";
        searchBtn.style.paddingRight = "";
    });

    searchBox.addEventListener("focusout", function () {
        searchBtn.textContent = "Tap";
    });

    //Event listener to get value of second input

    secondBtn.addEventListener("click", () => {
        if (secondInput.value) {
            // JEDIDIAH
            userSearch = secondInput.value;
            document.querySelector('.cards').innerHTML = ""
            retrieveOutput(userSearch)
        } 
        secondInput.value = "";
    });

    // event listener to bring out search results and also get the value of the user search from first input

    searchBtn.addEventListener("click", function () {
        if (text === "Search" && searchBox.value) {
            firstContainer.style.display = "none";
            secondContainer.style.display = "flex";
            // JEDIDIAH
            userSearch = searchBox.value;
            document.querySelector('.cards').innerHTML = ""
            retrieveOutput(userSearch)
            document.querySelector('.overLay').style.display = 'flex'

            setInterval( () =>{
                const resultCount = document.querySelector('.cards').childElementCount
                if (resultCount > 0) {
                    document.querySelector('.overLay').style.display = 'none'
                }
            }, 1000)

            setTimeout( ()=> {
                document.querySelector('.overLay_Btn').style.display = 'block'
            }, 20000)

        } 
        else {
            firstContainer.style.display = "flex";
            secondContainer.style.display = "none";
        }
    });

    document.querySelector('.overLay_Btn').addEventListener('click', () => {
        document.querySelector('.overLay').style.display = 'none';
        secondContainer.style.display = "none";
        firstContainer.style.display = "flex";
        searchBox.value = ""
        document.querySelector('.overLay_Btn').style.display = 'none'
    })



    

    //// cards 

    var buttons = document.querySelectorAll("#btn-more");
    buttons.forEach(function (button, index) {
        button.addEventListener("click", function () {
            myFunction(index);
        });
    });

    // Initialize the initial state to "none"
    document.querySelectorAll("#dots").forEach(function (dots) {
        dots.style.display = "none";
    });

    document.querySelectorAll("#more").forEach(function (moreText) {
        moreText.style.display = "none";
    });

    function myFunction(index) {
        var dots = document.querySelectorAll("#dots")[index];
        var moreText = document.querySelectorAll("#more")[index];
        var btnText = document.querySelectorAll("#btn-more")[index];

        if (dots.style.display === "none" || dots.style.display === "") {
            dots.style.display = "inline";
            btnText.innerHTML = "Read less";
            moreText.style.display = "inline";
        } else {
            dots.style.display = "none";
            btnText.innerHTML = "Read more";
            moreText.style.display = "none";
        }
    }




    
    //

    function retrieveOutput(query){
        fetch(`/display_search/${query}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            console.log(`/display_search/${query}`)
            if(data.status){
                alert(data.message)
                document.querySelector('.overLay_Btn').style.display = 'block'
            }
            else{
                const results_data = data
                const result_titles = Object.keys(results_data)
                
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
            }
        })
    }


})