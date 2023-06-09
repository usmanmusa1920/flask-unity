# -*- coding: utf-8 -*-

import os
import re
import base64
import random
import hashlib
import secrets

from pathlib import Path
from getpass import getpass
from sakyum import __title__
from sakyum import __version__


# relative path to the package folder (sakyum)
REL_PATH = Path(__file__).resolve().parent
OS_SEP = os.path.sep # platform-specific path separator (for linux `/`, for windows `\\`)


def static_dir(app, static_from_pkg=False, os_name: 'nt or posix'=os.name):
  """
  relative path to static files
  if `static_from_pkg` is not false, it will use the directory name that is in the library package which is `static`, else it will use for project `static` directory
  """

  if static_from_pkg:
      return str(REL_PATH) + OS_SEP + 'static' + OS_SEP + app
  return os.getcwd() + OS_SEP + 'static' + OS_SEP + app
  

def template_dir(temp_from_pkg=False, os_name=os.name):
  """
  relative path to html page
  if `temp_from_pkg` is not false, it will use the directory name that is in the library package which is `templates`, else it will use for project `templates` directory
  """

  if temp_from_pkg:
    return str(REL_PATH) + OS_SEP + 'templates' + OS_SEP + temp_from_pkg
  return os.getcwd() + OS_SEP + 'templates'
  

def stylePage(name, version=False):
  """function for styling project/app description default pages"""
  if version:
    # it will style the description in the footer
    desc = '@ ' + name + ' software - v' + version
    desc_center = desc.center(len(desc) + 2)
    border = '=' * len(desc_center)
    return [desc_center, border]

  # it will style the description of default app pages
  desc = 'Your ' + name + ' application default pages'
  desc_center = desc.center(len(desc) + 6)
  border = '=' * len(desc_center)
  return [desc_center, border]
  
  
# Style for sakyum default pages:
    # ============================
    #  @ sakyum software - v0.0.8 
    # ============================
footer_style = stylePage(__title__, version=__version__)


def rem_blueprint(lst_blue=None, rem_blue=None):
  # these are blueprint that we don't want to show on the
  # default page so we are removing them from the list
  # reason is they are not route
  for blue in rem_blue:
    if blue in lst_blue:
      # finding the index of the `blue` item blueprint in the list
      err_index = lst_blue.index(blue)
      # removing it `blue` item from the list using it index number
      lst_blue.pop(err_index)
  blueprints_list = lst_blue
  return blueprints_list


class AuthCredentials:
  """Authenticate new user credentials"""
  def __init__(self, username=None, email=None, password=None, u_args=True, e_args=True, p_args=True):
    self.username = username
    self.email = email
    self.password = password
    self.u_args = u_args
    self.e_args = e_args
    self.p_args = p_args

    if self.u_args:
      while self.username == None or self.username == '' or len(self.username) < 3:
        if self.username == None:
          self.username = input('Enter username: ')
          print()
        elif self.username == '':
          print('username can\'t be empty')
          self.username = input('Enter username: ')
          print()
        elif len((self.username)) < 3:
          print('username must be not less than 3 character')
          self.username = input('Enter username: ')
          print()

    if self.e_args:
      while self.email == None or self.email == '':
        if self.email == None:
          self.email = input('Enter email: ')
          print()
        elif self.email == '':
          print('email can\'t be empty')
          self.email = input('Enter email: ')
          print()

    if self.p_args:
      while self.password == None or self.password == '' or len(self.password) < 6:
        if self.password == None:
          self.password = getpass('Enter password: ')
          print()
        elif self.password == '':
          print('password can\'t be empty')
          self.password = getpass('Enter password: ')
          print()
        elif len((self.password)) < 6:
          print('password must be not less than 6 character')
          self.password = getpass('Enter password: ')
          print()
        
  @property
  def validate_username(self):
    """validate username"""
    # the below while is included to check data validation
    # when user uses flags `-u` or `--username`
    while len(self.username) < 3:
      print('username must be not less than 3 character')
      self.username = input('Enter username: ')
      print()
    return self.username

  @property
  def validate_email(self):
    """email validator"""
    pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
    if re.match(pattern, self.email):
      return self.email
    while not re.match(pattern, self.email):
      print('Put a valid email: ')
      self.email = input('Enter email: ')
      print()
    return self.email

  @property
  def validate_password(self):
    """validate password"""
    # the below while is included to chech data validation
    # when user uses flags `-p` or `--password`
    while len(self.password) < 6:
      print('password must be not less than 6 character')
      self.password = getpass('Enter password: ')
      print()
    return self.password

  @property
  def result(self):
    """user credentials in a list"""
    auth_list = [self.validate_username, self.validate_email, self.validate_password]
    return auth_list
    

class Security:
  """
  Passcode class for suggesting user passcode iteration,
  generating salt, and creating secure passcode for every user
  
  A reqular expression that matches any character that
  should never appear in base 64 encodings would be:
    [^A-Za-z0-9+/=]
  we follow the base64 pattern of [^A-Za-z0-9+/=] that should never appear in base64, (in reqex)
  """
  
  token_sm_alpha = 'abcdefghijklmnopqrstuvwxyz'
  token_cap_alpha = token_sm_alpha.upper()
  token_num = '0123456789'
  token_char = '/+='
  token_sum = token_sm_alpha + token_cap_alpha + token_num
  
  """
  We times the above variable (token_sum) by 2 (total length is 124),
  so that we will randomly select from it without any restriction,
  since we make the minimum length of the salt to be 32 and the maximum to be 64,
  and also it will randomly select from that range of (32 - 64)
  """

  token_times = token_sum * 2
  token_list = list(token_times)
  random.shuffle(token_list) # shuffling the above list
  token_generate = ''.join(token_list)
  
  def __init__(self, token_generate = token_generate):
    self.token_generate = ''.join(token_generate)
    
  @property
  def passcode_salt(self):
    """
    salting our passcode with this class method
    
    By using the random sample method, where we make:
      population = self.token_generate
      k = random.randint(20, 50)
    """

    salt = ''.join(random.sample(self.token_generate, random.randint(20, 50)))
    return salt # return type is string
    
  def passcode_iteration(self, r_min, r_max, r_step):
    """
    Generating a random iteration. The iterations is not static,
    it is dynamic (every user's iteration is randomly choosen),
    by using the random method of randrange
    """

    itter = random.randrange(r_min, r_max, r_step)
    return itter # return type is integer
    
  def get_hash(self, salt: str, itter: int, passwd: str) -> str:
    """
    generating our key using this class method, and also
    the return type of the key is bytes
    """
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        passwd.encode('utf-8'), # Convert the password to bytes
        salt.encode('utf-8'), # Convert the salt to bytes
        itter, # iteration type is integer
        dklen=128 # Get a 128 byte key
    )
    
    """
    Base64 encoding convert the binary data (sequence of byte) into text format,
    to avoid data corruption when transfer via only text channel.
    It is Privacy enhanced Electronic Mail (PEM).
    
    We use ascii to encode the (key)
    """
    
    # encodeing the key, type is string
    b64_encode = base64.b64encode(key).decode('ascii').strip()

    # hashing our b64_encode (the second hash), type is string
    hash_result = hashlib.sha256(str.encode(str(b64_encode))).hexdigest()

    # salt + iteration + hash_result, type is string
    secure_ingredient = '%s%d%s' % (salt, itter, hash_result)
    
    # return types of the list is string all, access it by print(self.get_hash.__annotations__)
    return [hash_result, secure_ingredient]

  def secret(self):
    r = random.randint(32, 52)
    secret = secrets.token_hex(r)
    return secret
    
  def __str__(self):
    return f'Passcode security class'
