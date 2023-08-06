# -*- coding: utf-8 -*-

import os
import re
import base64
import random
import hashlib
import secrets

from pathlib import Path
from getpass import getpass
from . import __title__
from . import __version__


# relative path to the package folder (flask_unity)
rel_path = Path(__file__).resolve().parent

_status_codes = {
  # Informational.
  100: ("continue",),
  101: ("switching_protocols",),
  102: ("processing",),
  103: ("checkpoint",),
  122: ("uri_too_long", "request_uri_too_long"),
  200: ("ok", "okay", "all_ok", "all_okay", "all_good", "\\o/", "✓"),
  201: ("created",),
  202: ("accepted",),
  203: ("non_authoritative_info", "non_authoritative_information"),
  204: ("no_content",),
  205: ("reset_content", "reset"),
  206: ("partial_content", "partial"),
  207: ("multi_status", "multiple_status", "multi_stati", "multiple_stati"),
  208: ("already_reported",),
  226: ("im_used",),
  # Redirection.
  300: ("multiple_choices",),
  301: ("moved_permanently", "moved", "\\o-"),
  302: ("found",),
  303: ("see_other", "other"),
  304: ("not_modified",),
  305: ("use_proxy",),
  306: ("switch_proxy",),
  307: ("temporary_redirect", "temporary_moved", "temporary"),
  308: (
      "permanent_redirect",
      "resume_incomplete",
      "resume",
  ),  # "resume" and "resume_incomplete" to be removed in 3.0
  # Client Error.
  400: ("bad_request", "bad"),
  401: ("unauthorized",),
  402: ("payment_required", "payment"),
  403: ("forbidden",),
  404: ("not_found", "-o-"),
  405: ("method_not_allowed", "not_allowed"),
  406: ("not_acceptable",),
  407: ("proxy_authentication_required", "proxy_auth", "proxy_authentication"),
  408: ("request_timeout", "timeout"),
  409: ("conflict",),
  410: ("gone",),
  411: ("length_required",),
  412: ("precondition_failed", "precondition"),
  413: ("request_entity_too_large",),
  414: ("request_uri_too_large",),
  415: ("unsupported_media_type", "unsupported_media", "media_type"),
  416: (
      "requested_range_not_satisfiable",
      "requested_range",
      "range_not_satisfiable",
  ),
  417: ("expectation_failed",),
  418: ("im_a_teapot", "teapot", "i_am_a_teapot"),
  421: ("misdirected_request",),
  422: ("unprocessable_entity", "unprocessable"),
  423: ("locked",),
  424: ("failed_dependency", "dependency"),
  425: ("unordered_collection", "unordered"),
  426: ("upgrade_required", "upgrade"),
  428: ("precondition_required", "precondition"),
  429: ("too_many_requests", "too_many"),
  431: ("header_fields_too_large", "fields_too_large"),
  444: ("no_response", "none"),
  449: ("retry_with", "retry"),
  450: ("blocked_by_windows_parental_controls", "parental_controls"),
  451: ("unavailable_for_legal_reasons", "legal_reasons"),
  499: ("client_closed_request",),
  # Server Error.
  500: ("internal_server_error", "server_error", "/o\\", "✗"),
  501: ("not_implemented",),
  502: ("bad_gateway",),
  503: ("service_unavailable", "unavailable"),
  504: ("gateway_timeout",),
  505: ("http_version_not_supported", "http_version"),
  506: ("variant_also_negotiates",),
  507: ("insufficient_storage",),
  509: ("bandwidth_limit_exceeded", "bandwidth"),
  510: ("not_extended",),
  511: ("network_authentication_required", "network_auth", "network_authentication"),
}


def os_name(lin=False, win=False, name=os.name):
  """detect os name"""
  if lin and name == "posix":
    pass
  elif win and name == "nt":
    pass


def static_dir(app, static_from_pkg=False):
  
  """
    relative path to static files
    
    # :static_from_pkg:
        is the directory name that is in the library package which is `static`
  """
  if static_from_pkg:
    return str(rel_path) + "/static/" + app
  return os.getcwd() + "/static/" + app
  

def template_dir(temp_from_pkg=False):

  """
    relative path to html page

    # :temp_from_pkg:
        is the directory name that is in the library package which is `templates`
  """
  if temp_from_pkg:
    return str(rel_path) + "/templates/" + temp_from_pkg
  return os.getcwd() + "/templates"
  

def stylePage(name, _is, version=False):
  """function for styling project/app description default pages"""

  if version:
    # it will style the description in the footer
    desc = "@ " + name + " software - v" + version
    desc_center = desc.center(len(desc) + 2)
    border = "=" * len(desc_center)
    return [desc_center, border]

  # it will style the description of default app pages
  desc = "Your " + name + " " + _is + " default pages"
  desc_center = desc.center(len(desc) + 6)
  border = "=" * len(desc_center)
  return [desc_center, border]
  
  
footer_style = stylePage(__title__, "do_nothing", version=__version__)


class AuthCredentials:
  def __init__(self, username=None, email=None, password=None):
    self.username = username
    self.email = email
    self.password = password

    while self.username == None or self.username == "" or len(self.username) < 5:
      if self.username == None:
        self.username = input("Enter username: ")
        print()
      elif self.username == "":
        print("username can't be empty")
        self.username = input("Enter username: ")
        print()
      elif len((self.username)) < 5:
        print("username must be not less than 5 character")
        self.username = input("Enter username: ")
        print()
        
    while self.email == None or self.email == "":
      if self.email == None:
        self.email = input("Enter email: ")
        print()
      elif self.email == "":
        print("email can't be empty")
        self.email = input("Enter email: ")
        print()
        
    while self.password == None or self.password == "" or len(self.password) < 8:
      if self.password == None:
        self.password = getpass("Enter password: ")
        print()
      elif self.password == "":
        print("password can't be empty")
        self.password = getpass("Enter password: ")
        print()
      elif len((self.password)) < 8:
        print("password must be not less than 8 character")
        self.password = getpass("Enter password: ")
        print()
        
  @property
  def validate_username(self):
    return self.username

  @property
  def validate_email(self):
    pattern = re.compile(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")
    if re.match(pattern, self.email):
      return self.email
    while not re.match(pattern, self.email):
      print("Put a valid email: ")
      self.email = input("Enter email: ")
      print()
    return self.email

  @property
  def validate_password(self):
    return self.password

  @property
  def result(self):
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
    self.token_generate = "".join(token_generate)
    

  @property
  def passcode_salt(self):
    """
    salting our passcode with this class method
    
    By using the random sample method, where we make:
      population = self.token_generate
      k = random.randint(32, 64)
    """

    salt = "".join(random.sample(self.token_generate, random.randint(32, 64)))
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
    b64_encode = base64.b64encode(key).decode("ascii").strip()

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
    return f"Passcode security class"
    
    
def security(_passwd, r_min=260000, r_max=400000, r_step=7) -> list:
  """
    this function collect a raw password, and then hash it using random generated salt,
    and random generated iteration number generated by a class method of `Security`
    ( passcode_salt, passcode_iteration, and get_hash )
    
    # :password ( _passwd ) it is the raw password that you pass as an argument into this function,
      which will later be hashed, also it will generate your password hash with a randomly
      generated iteration number and salt combine with your raw password.
    # :min ( r_min ) of 260000,
    # :max ( r_max ) of 400000, and
    # :stepping ( r_step ) of 7

    you can change the `r_min`, `r_max`, and `r_step` values to your desired ones,
    when calling the function, but make sure to pass the value of the password sting
  """

  # passwd_data = security(_passwd="password")
  # passwd_data = security(_passwd="password", r_min=100, r_max=300, r_step=7)
  # hashed_password = passwd_data[2]
  
  pwd = Security() # base class of password hashing
  pwd_salt = pwd.passcode_salt # salting method
  pwd_itter = pwd.passcode_iteration(r_min=r_min, r_max=r_max, r_step=r_step) # passwd iteration

  # passwod hash (a list of hashed_pwd and password ingredients)
  pwd_hash = pwd.get_hash(pwd_salt, pwd_itter, _passwd)

  #      [salt,     iteration, hashed_pwd,  ingredients]
  return [pwd_salt, pwd_itter, pwd_hash[0], pwd_hash[1]]
