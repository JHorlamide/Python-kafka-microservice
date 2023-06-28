from dotenv import load_dotenv

from kafka_settings import KafkaSetting
from kafka_producer import KafkaProducer
from kafka_producer_message import ProduceMessage

def main():
  setting = KafkaSetting()
  producer = KafkaProducer(setting)
  message = ProduceMessage(
    topic="MyFirstKafkaTopic",
    value={"value": "MyFirstKafkaValue"},
    key=None
  )
  
if __name__ == "__main__":
  load_dotenv()
  main()