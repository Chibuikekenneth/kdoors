# Getting Started with Kdoors

## Setup

Make sure you have installed and configured docker in your environment. After that, you can run the below commands and get started with the the project immediately.

Clone the Project
```
$ git clone https://github.com/Chibuikekenneth/kdoors.git
```

Start the services by running 

```powershell
docker-compose up
```

for development You should be able to browse different components of the application by using the below URLs :

```
Web application (UI) :  http://localhost:8080/
Web API :               http://localhost:5000/

PostgreSql database:    port 5432
Redis Cache: Port       port 6379
```

**Note, for development purposes, PostgreSql DB password is stored in docker compose environment configuration**

### Basic Scenerio

The Web application on ```http://localhost:8080/```

![image](https://user-images.githubusercontent.com/38410485/127044491-a9434b94-c1fd-45a7-acdd-0983bf06afa0.png)


**Web API**

[GET] fetch list of doors

``` http://localhost:5000/api/v1/doors/ ```

[GET] fetch doors by Id

``` http://localhost:5000/api/v1/doors/{id}```

[GET] fetch users with permissions to a particular door

``` http://localhost:5000/api/v1/permissions/{door_id}```
