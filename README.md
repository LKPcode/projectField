## The Field Project
*A short Description for every root folder:*

 - **django_project_ktima:**  is the main folder of the django application. It contains mostly settings and a bit of routing logic.
 - **main_app:**  is where the API logic is being formed and database models are being created.
 - **serve_web_app:** is the logic that will serve our lovely VueJS application to the client.
 - **ktima_vue:** is the folder where the Vue application is being developed.
 - **testing:** is a folder to test whatever we want.  More like a basket.

>The Voyage to the destination is why we started in the first place

## **API Documentation**

**Root:**  /api

 URL | Request | Authorization| Description|
|--|--|--|--|
| **/user** | GET | YES|  user's info| 
| **/user**|POST| NO| create account|
| **/user/field** |GET |YES|Get user's fields
|**/field**|GET|NO|Get All Fields
|**/field/:id**|GET|NO|Get field with id
|**/field**| POST| YES |Create new Field
|**/field/:id**|PUT|YES|Update field info
|**/field/:id**|DELETE|YES|Delete Field
| **/xy/:id**|GET|NO|Get coordinates of field with id
|**/xy/:id**|POST|YES|Create coordinates for field with id


>This Table is not complete. More stuff should be added in the future
