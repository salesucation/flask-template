window.addEventListener('load', function () {
    var $ = Dom7;

    const app = new Framework7({
        el: '#app',
        theme: 'md',
        darkMode: "auto",
        clicks: {
            externalLinks: 'a:not(.panel-open)',
        }

    })

    // create searchbar
    app.searchbar.create({
        el: '.searchbar',
        searchContainer: '.list-email',
        searchIn: '.item-title',
        on: {
            search(sb, query, previousQuery) {
                console.log(query, previousQuery);
            }
        }
    });
    //
    if(!this.localStorage.getItem("cookies_accepted")){
        this.localStorage.setItem("cookies_accepted", new Date().toLocaleString());
        const cookieMessage = app.sheet.create(
            {
                el: '.cookie-message'
            });
        $(".cookie-message .sheet-close").on("click", ()=>{
            cookieMessage.close();
        })
        cookieMessage.open();
    }

});