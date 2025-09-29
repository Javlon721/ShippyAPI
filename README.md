# How to run this project

## Initiate DB

- To run project correctly you need to run db via docker-compose
- First run docker
    
    ```
     docker compose run
    ```
    
- Then connect to container via hash/name
    
    ```
    docker exec -it shippyapi-mongodb-1 bash
    ```
    
- Inside of container we need to import database that related to project and it exists in **jsons/backup.archive.gz** that binded into docker container **/tmp/jsons/backup.archive.gz**
    
    ```
    mongorestore --gzip --archive=./tmp/jsons/backup.archive.gz --username=user --password=pass
    ```
    

## Install requirements (you can use uv though)

- First, create **venv** folder for packages
    
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    
- Then run
    
    ```
    pip install -r requirements.txt
    ```
    
    if some modules are not installed, just install manually like pip install pymongo etc
    

## Run FastAPI project

```
uvicorn main:app --reload
```

## Quick notes

- To see capabilities of this simple api you can use docs [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Main endpoints to play are
    - **GET**: [http://127.0.0.1:8000/ship/](http://127.0.0.1:8000/ship/) - to see all available ships for battle
    - **POST**: [http://127.0.0.1:8000/ship/battle/](http://127.0.0.1:8000/ship/battle/) - to start battle.
        Here is the sample body data that you should send:
        ```json
        {
            "ship1": {
                "ship_id": "bismarck",
                "coords": {
                    "x": -15,
                    "y": 6,
                    "azimuth": 90
                }
            },
            "ship2": {
                "ship_id": "Hood",
                "coords": {
                    "y": -5,
                    "azimuth": 90
                }
            }
        }
        ```
        
- For create new ships with available options there is html in templates folder
    - Run in terminal
    
    ```
    python3 -m http.server 5001 -d templates/create
    ```
    

* I use MacOS so make sure all command matches your system