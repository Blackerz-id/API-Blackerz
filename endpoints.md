### Endpoints  
Our domain always changed everytime, the mostly compatible is [blackerz.herokuapp.com](https://blackerz.herokuapp.com)  

#### GET method endpoints<br>
- [/api/v1/bots/all](https://blackerz.herokuapp.com/api/v1/bots/all)  
Return list all of bots, limit 10 - 100  

- [/api/v1/bots/{BOT_ID}](https://blackerz.herokuapp.com/api/v1/bots/{BOT_ID})  
Return specific information of bot from id parameter  

- [/api/v1/bots/search?q={query}](https://blackerz.herokuapp.com/api/v1/bots/search?q=sc)
Return list information of bot from query parameter  

- [/api/v1/servers/all](https://blackerz.herokuapp.com/api/v1/servers/all)  
Return list all of servers, limit 10 - 100  

- [/api/v1/servers/{SERVER_ID}](https://blackerz.herokuapp.com/api/v1/servers/{SERVER_ID})  
Return specific information of server from id parameter  

#### PUT method endpoints<br>
- [/api/v1/bots/{SERVER_ID}/edit](https://blackerz.herokuapp.com/api/v1/bots/{SERVER_ID}/edit)  
PUT with body and headers structure below:  

**BODY**  
```json  
{  
  "prefix": STRING,  
  "shortDescription": STRING,  
  "longDescription": STRING,  
  "serverCount": NUMBER  
}```  
**prefix**: Prefix of the bot, limited to 5 characters  
**shortDescription**: Short description to display on the web, limited to 120 characters  
**longDescription**: Long description to display on the web, limited to 4000 characters  
**serverCount**: Server count of the bot  
**HEADERS**  
```json  
{  
   "Authorization": STRING  
}```  
**Authorization**: Your authorization key from website, you can get it by visiting your profile  

- https://blackerz.herokuapp.com/api/v1/servers/{SERVER_ID}/edit  
PUT with body and headers structure below:  

**BODY**  
```json  
{  
   "shortDescription": STRING,  
   "longDescription": STRING  
}```  
**shortDescription**: Short description to display on the web, limited to 120 characters  
**longDescription**: Long description to display on the web, limited to 4000 characters  

**HEADERS**  
```json
{
   "Authorization": STRING
}```  
**Authorization**: Your authorization key from website, you can get it by visiting your profile  
