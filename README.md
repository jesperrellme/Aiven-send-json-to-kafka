# Aiven-send-json-to-kafka
 Sends a json formatted message to a Kafka topic


**Usage:**


Download your certificate files either from the console or through Aiven CLI:
(Replace *TOKEN, SERVICE_NAME and PROJECT_NAME*):


> *avn --auth-token $TOKEN service user-creds-download $SERVICE_NAME  --project $PROJECT_NAME --username avnadmin -d ./certs* 

Place the files in a folder accessible to the program, e.g. "/certs"

**Set your variables:**

 
> *bootstrap_servers = 'your-aiven-instance:port'* 

> *topic = 'your_topic'*

> *cert_folder = 'folder-with-your-cert-files'*

**Run the program:**

> *python main.py*
