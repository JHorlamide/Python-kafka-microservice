import json

class ProduceMessage:
  def __init__(self, topic: str, value, key=None) -> None:
    self.topic = f"{topic}"
    self.value = value
    self.key = key
    
  @classmethod
  def convert_value_to_byte(cls, value):
    if isinstance(value, dict):
      return cls.from_json(value)
    
    if isinstance(value, str):
      return cls.from_string(value)
    
    if isinstance(value, bytes):
      return cls.from_bytes(value)
    
  @classmethod
  def from_json(cls, value):
    return json.dump(value, indent=None, sort_keys=True, default=str, ensure_ascii=False)
  
  @classmethod
  def from_string(cls, value):
    return value.encode("utf-8")
  
  @classmethod
  def from_bytes(cls, value):
    return value