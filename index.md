## Introduction into our API

Blackerz Discord bot list API is a RESTful API to interact with our database.

To get started, please read our documentation about endpoints.

### Endpoints

#### GET method endpoints<br>
https://blackerz-api.herokuapp.com/api/v1/bots/all<br>
Return list all of bots, limit 10 - 100

https://blackerz-api.herokuapp.com/api/v1/bots/ (Bot id)<br>
Return specific information of bot id parameter

#### POST method endpoints<br>
https://blackerz-api.herokuapp.com/api/v1/bots/submit/ (bot id)<br>
Upload/edit bot to our database, NOTE: this endpoint require apiKey to access<br>
To post bot data, you will need to input these data:<br>
##### Headers<br>
```js
{
   'Content-Type': 'application/json',
   'apiKey': String                   // You can get API key by contacting our API developer
}
```
##### Body (JSON)
```js
{
   name: String,                                // bot username
   owner: { 'id': String, 'name': String },     // owner id and tag
   tag: String,                                 // Tag (name and discriminator) of bot
   id: String / Number                          // Id of the bot / client id
}
```


Having trouble with API? Check out our Discord server [server link](https://discord.gg/BjnD867JAT) or [visit github](https://github.com/Blackerz-id/API-Blackerz) and we’ll help you sort it out.
