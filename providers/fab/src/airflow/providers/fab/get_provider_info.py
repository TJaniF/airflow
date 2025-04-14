# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-fab",
        "name": "Fab",
        "description": "`Flask App Builder <https://flask-appbuilder.readthedocs.io/>`__\n",
        "config": {
            "fab": {
                "description": "This section contains configs specific to FAB provider.",
                "options": {
                    "auth_rate_limited": {
                        "description": "Boolean for enabling rate limiting on authentication endpoints.\n",
                        "version_added": "1.0.2",
                        "type": "boolean",
                        "example": None,
                        "default": "True",
                    },
                    "auth_rate_limit": {
                        "description": "Rate limit for authentication endpoints.\n",
                        "version_added": "1.0.2",
                        "type": "string",
                        "example": None,
                        "default": "5 per 40 second",
                    },
                    "update_fab_perms": {
                        "description": "Update FAB permissions and sync security manager roles\non webserver startup\n",
                        "version_added": "1.0.2",
                        "type": "string",
                        "example": None,
                        "default": "True",
                    },
                    "auth_backends": {
                        "description": "Comma separated list of auth backends to authenticate users of the API.\n",
                        "version_added": "2.0.0",
                        "type": "string",
                        "example": None,
                        "default": "airflow.providers.fab.auth_manager.api.auth.backend.session",
                    },
                    "config_file": {
                        "description": "Path of webserver config file used for configuring the webserver parameters\n",
                        "version_added": "2.0.0",
                        "type": "string",
                        "example": None,
                        "default": "{AIRFLOW_HOME}/webserver_config.py",
                    },
                    "session_backend": {
                        "description": "The type of backend used to store web session data, can be ``database`` or ``securecookie``. For the\n``database`` backend, sessions are store in the database and they can be\nmanaged there (for example when you reset password of the user, all sessions for that user are\ndeleted). For the ``securecookie`` backend, sessions are stored in encrypted cookies on the client\nside. The ``securecookie`` mechanism is 'lighter' than database backend, but sessions are not\ndeleted when you reset password of the user, which means that other than waiting for expiry time,\nthe only way to invalidate all sessions for a user is to change secret_key and restart webserver\n(which also invalidates and logs out all other user's sessions).\n\nWhen you are using ``database`` backend, make sure to keep your database session table small\nby periodically running ``airflow db clean --table session`` command, especially if you have\nautomated API calls that will create a new session for each call rather than reuse the sessions\nstored in browser cookies.\n",
                        "version_added": "2.0.0",
                        "type": "string",
                        "example": "securecookie",
                        "default": "database",
                    },
                    "session_lifetime_minutes": {
                        "description": "The UI cookie lifetime in minutes. User will be logged out from UI after\n``[fab] session_lifetime_minutes`` of non-activity\n",
                        "version_added": "2.0.0",
                        "type": "integer",
                        "example": None,
                        "default": "43200",
                    },
                },
            }
        },
        "auth-managers": ["airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager"],
    }
