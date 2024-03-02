#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value = ""):
    self.value = value

  @property
  def value(self):
    return self._value 
  
  @value.setter
  def value(self, val):
    if isinstance(val, str):
      self._value = val
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if self._value.endswith('.') else False
  
  def is_question(self):
    return True if self._value.endswith('?') else False
  
  def is_exclamation(self):
    return True if self._value.endswith('!') else False
  
  def count_sentences(self):
    
    #sentences = self.split(" ")
    #return len(sentences)
    sentences = re.split(r'[!?.]', self.value)
    sentences = [sentence for sentence in sentences if sentence]
    return len(sentences)

  
  
    
    
