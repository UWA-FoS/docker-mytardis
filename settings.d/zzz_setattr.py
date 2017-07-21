# Get all Environment variables with a MYTARDIS_ prefix; remove prefix
#print { k: v for k, v in os.environ.iteritems() if k.startswith('MYTARDIS_') }
_mytardis_environ = { k[9:]: v for k, v in os.environ.iteritems() if k.startswith('MYTARDIS_') }
for key in _mytardis_environ:
    try:
        setattr(this_module, key, literal_eval(_mytardis_environ[key]))
    except:
        setattr(this_module, key, _mytardis_environ[key])
        #print "ValueError for %s: %s (%s)" % (key,_django_environ[key],str(e))

