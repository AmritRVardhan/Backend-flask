# Backend-flask
## Instructions to run
On a machine having docker run the following command. This is a public repository so it should work fine.
> docker pull amritrv/dockerhub:backend-flask

I used postman to send/receive GET/POST requests to test the same. I have used flask to create the backend. 
After pulling the docker image use the below command to run the server.
> docker run amritrv/dockerhub:backend-flask


Post the above, use GET and POST from Postman to be able to send JSON details commands to get the details. 
JSON example :

``
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
``
EACH UUID generated is unique, so when it is generated copy it in and then paste in the GET URL
