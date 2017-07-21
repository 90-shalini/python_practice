validate method:
wrapper method that returns validated document

normalizes method:
returns a normalized copy of a document without validating it

Registries:
we can store definitions for schema and rules set
            Use registries:
                    if schema references to themselves i.e schema recursion
                    serialized



-	/1/user/{0}/check-terminate (GET check if can be terminated)
-	/1/user/{0}/terminate (POST terminate)
-	/1/account/members (POST to Create)
-	/1/account/members?include_external_users=1 (GET, this might already be on your list for the old integration)
-	/1/account/members?include_external_users=1&flag=registered (GET, to check if a member is registered or not)
-	/1/languages/ (GET all available languages)


https://api.projectplace.com/1/timereports/<artifact_type:planlets|cards>/<int:artifact_id>
