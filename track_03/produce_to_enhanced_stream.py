import oci
from base64 import b64encode  
import json
from json import dumps

STREAM_NAME='enhanced_stream' #in your compartment
STREAM_OCID='<STREAM_OCID>'
MESSAGE_ENDPOINT='<STREAM_END_POINT>'
  
def produce_messages(json_str, client, stream_ocid):
  message_list = []
  encoded_value =b64encode(json_str.encode()).decode()
  message_list.append(oci.streaming.models.PutMessagesDetailsEntry(value = encoded_value))  
  messages = oci.streaming.models.PutMessagesDetails(messages=message_list)
  put_message_result = client.put_messages(stream_ocid, messages)
  
  return put_message_result

with open('../enhanced_livelabs.json', 'r') as file:
    livelabs = json.load(file)

print("Total Data Size:", len(livelabs))

config = oci.config.from_file()
stream_client = oci.streaming.StreamClient(config, service_endpoint=MESSAGE_ENDPOINT)

for livelab in livelabs:
   result = produce_messages(json.dumps(livelab), stream_client, STREAM_OCID)
   print(result)

print("Task(Sedning MSG to The enhanced_stream) completed....")
