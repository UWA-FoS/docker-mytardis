RAPID_CONNECT_ENABLED = False
RAPID_CONNECT_CONFIG = {}
RAPID_CONNECT_CONFIG['secret'] = os.getenv(RAPID_CONNECT_SECRET,'***Secret***')
RAPID_CONNECT_CONFIG['authnrequest_url'] = os.getenv(RAPID_CONNECT_AUTHNREQUEST_URL,'***UniqueURL***')
RAPID_CONNECT_CONFIG['iss'] = os.getenv(RAPID_CONNECT_ISS,'https://rapid.test.aaf.edu.au')
RAPID_CONNECT_CONFIG['aud'] = os.getenv(RAPID_CONNECT_AUD,'http://************/rc')
