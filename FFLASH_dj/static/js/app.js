// Request an intention creation from your marketplace APIs and confirm the payment using the client_secret.
fetch("http://localhost:8000/secret/").then(function (response) {
        return response.json();
    }).then(function (json) {
        // client_secret is your customer reference for the created intention, and it's used for one time only.
        Paymob("pk_test_FBd6waQYzXWYW71B9Z5RI3kzKEGZdgxL").checkoutButton(json.client_secret).mount("#paymob-checkout");
    }).catch(function (err) {
        console.error(err);
    });
