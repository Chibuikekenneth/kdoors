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
Web application :       http://localhost:3000/
Web API :               hhttp://localhost:5000/

PostgreSql database:    port 5432
Redis Cache: Port       port 6379
```

**Note, for development purposes, PostgreSql DB password is stored in docker compose environment configuration**
