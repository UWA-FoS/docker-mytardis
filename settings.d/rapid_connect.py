from os import getenv

RAPID_CONNECT_ENABLED = False
RAPID_CONNECT_CONFIG = {
  'secret': getenv("RAPID_CONNECT_SECRET","Generate Secret: LC_CTYPE=C tr -dc '[[:alnum:][:punct:]]' < /dev/urandom | head -c32 ;echo"),
  'authnrequest_url': getenv("RAPID_CONNECT_AUTHNREQUEST_URL",'AAF registration: https://rapid.aaf.edu.au/registration'),
  'iss': getenv("RAPID_CONNECT_ISS",'https://rapid.aaf.edu.au'),
  'aud': getenv("RAPID_CONNECT_AUD",'https://<your.mytardis.service>/rc'),
}
