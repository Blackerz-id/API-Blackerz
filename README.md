# API-Blackerz
Blackerz API written in Python
<br>
**__Endpoints__**

( GET ) -> https://blackerz-api.herokuapp.com/api/v1/bots/all

( GET ) -> https://blackerz-api.herokuapp.com/api/v1/bots/ <int:id>  (kasih angka setelah "/")

( POST ) -> https://blackerz-api.herokuapp.com/api/v1/bots/submit/ <int:id>    (kasih angka setelah "/")

<br>

**/api/v1/bots/all**
Return semua bot dalam database
<br>
**/api/v1/bots/<int:id>**
Return informasi spesifik bot dalam database
<br>
**/api/v1/bots/submit/ int:id>**
Post bot dengan informasi bot\n
```js
Headers:{
     'Content-Type': 'application/json',
     'apiKey': String  // Contact developer untuk mendapatkan API key
}
```
````js
BODY: {
    name: String,                                        // Nama bot
    owner: { 'id': Number | String, 'name': String },    // Id dan nama akun Discord untuk developer bot
    tag: String,                                         // Tag nama dan diskriminator 
    id: Number | String                                  // Bot id / client id
}
```
<br>

© Copyright 2021 Fastering18/Blackerz-API
