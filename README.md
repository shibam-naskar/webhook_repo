# Dev Assessment - Webhook Receiver

Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* create a .env file in the root directory
* .env file content for local db

```bash
MONGO_URI=mongodb://localhost:27017/ACTIONS
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint for webhook is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

* The endpoint for getdata is at:

```bash
GET http://127.0.0.1:5000/getrecents/recent
```

* The endpoint for Frontend is at:

```bash
GET http://127.0.0.1:5000/getrecents/dashboard
```


*******************
