import os
import json
import facebook
import stringer

ENV = None
if os.path.exists('auth.json'):
    ENV_FILE = open('auth.json')
    ENV = json.load(ENV_FILE)
    ENV_FILE.close()
else:
    ENV = {
        "FB_ACC_TOKEN_PAINTMIN":os.environ.get('FB_ACC_TOKEN_PAINTMIN'),
        "PAGE_ID":os.environ.get('PAGE_ID')
    }

stringer_ctrl = stringer.Stringer_Ctrl()

graph = facebook.GraphAPI(access_token=ENV['FB_ACC_TOKEN_PAINTMIN'])
graph.put_object(parent_object='me', connection_name='feed',
                  message=stringer_ctrl.generate())