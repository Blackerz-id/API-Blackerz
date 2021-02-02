# API-Blackerz
Blackerz API for Discord, written in Python.
<br><br>

## Endpoints

( GET ) -> https://blackerz.herokuapp.com/api/v1/bots/all

( GET ) -> https://blackerz.herokuapp.com/api/v1/bots/{BOT_ID}

( POST ) -> https://blackerz.herokuapp.com/api/v1/bots/submit/{BOT_ID} 

( POST ) -> https://blackerz.herokuapp.com/api/v1/bots/{BOT_ID}/edit 

( GET ) -> https://blackerz.herokuapp.com/api/v1/discord/me

( GET ) -> https://blackerz.herokuapp.com/api/v1/discord/check

( GET ) -> https://blackerz.herokuapp.com/api/v1/servers/all

( GET ) -> https://blackerz.herokuapp.com/api/v1/servers/{SERVER_ID}

( POST ) -> https://blackerz.herokuapp.com/api/v1/servers/submit/{SERVER_ID}
<br>
<br>

**/api/v1/bots/all**
Return semua bot dalam database

<br>

**/api/v1/bots/{BOT_ID}**

Return informasi spesifik bot dalam database

<br>

**/api/v1/bots/submit/{BOT_ID}**

Post bot dengan informasi bot

<br>

**/api/v1/bots/{BOT_ID}/edit**

Edit data bot spesifik bot (Post / Put)

<br>

**/api/v1/servers/all**

Return semua servers dalam database

<br>

**/api/v1/servers/{SERVER_ID}**

Return informasi spesifik server dalam database

<br>

**/api/v1/servers/submit/{SERVER_ID}**

Post data spesifik server ke database

<br>
<br>

### Struktur Headers & Body untuk Upload bot;

```js
Headers:{
     'Content-Type': 'application/json',
     'apiKey': String  // Contact developer untuk mendapatkan API key
}
```

```js
BODY: {
    name: String,                                        // Nama bot
    owner: { 'id': Number | String, 'name': String },    // Id dan nama akun Discord untuk developer bot
    tag: String,                                         // Tag nama dan diskriminator 
    id: Number | String,                                 // Bot id / client id
    avatar?: String,                                     // Avatar bot icon id pada cdn.discordapp.com
    inviteLink?: String                                  // Kode untuk link untuk add bot, harus sesuai dari Discord Developer Portal
}
```

<br>
<br>

### Struktur Headers & Body untuk Upload server;

```js
Headers:{
     'Content-Type': 'application/json',
     'apiKey': String  // Contact developer untuk mendapatkan API key
}
```

```js
BODY: {
    name: String,                                        // Nama bot
    owner: { 'id': Number | String, 'name': String },    // Id dan nama akun Discord untuk developer bot
    memberCount: Number,                                 // Jumlah member terbaru
    id: Number | String,                                 // Server id / Guild id
    joinLink: String,                                    // Kode untuk link masuk server, tidak memerlukan "https://discord.gg/"
    avatar?: String                                      // Avatar server icon id pada cdn.discordapp.com
}
```

<br>

## Kode error<br>
**500** Terdapat error dalam server, sering terjadi saat server sedang maintenance, <br>
**429** Jumlah request melebihi batas, API membatasi jumlah reuquest dari client agar tidak terjadi penyalahgunaan, <br>
**404** Resource tidak ditemukan dalam api, termasuk bot & server yang tidak terdapat dalam database, <br>
**403** Operasi dilarang dengan alasan tertentu, dapat diketahui dengan membaca JSON response dari server, <br>
**401** Tidak terverifikasi, server menolak permintaan dari client karena kredensial yang invalid, <br>
**400** Body JSON dari client yang invalid, harus memiliki spesifikasi dari struktur data diatas. <br>

<br>

## Info lainnya<br>
**"{BOT_ID}"** Adalah bot / client id yang dapat didapatkan dengan mengklik kanan icon server,<br>
**"{SERVER_ID}"** Adalah server / guid id yang dapat didapatkan dengan mengklik kanan icon server,<br>
**"?"** Menandakan bahwa parameter tersebut bersifat opsional, server akan mengganti dengan alternatif atau menghilangkannya.<br><br>

© Copyright 2021 Fastering18/Blackerz-API
