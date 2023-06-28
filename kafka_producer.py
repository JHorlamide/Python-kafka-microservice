from confluent_kafka import KafkaError, KafkaException, Producer

from kafka_settings import KafkaSetting
from kafka_producer_message import ProduceMessage

class KafkaProducer:
  def __init__(self, setting: KafkaSetting) -> None:
    self._producer = Producer(setting.config)
    
  def produce(self, message: ProduceMessage):
    try:
      self._producer.produce(message.topic, key=message.key, value=message.value)
      self._producer.flush()
    except KafkaException as exception:
      if exception.args[0].code == KafkaError.MSG_SIZE_TOO_LARGE:
        pass # handle exception here
      else:
        raise exception
      