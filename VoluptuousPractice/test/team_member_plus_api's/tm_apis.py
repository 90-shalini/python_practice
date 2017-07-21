from voluptuous import Schema, Datetime


class team_member_plus_api:
    def __init__(self):
        print("Testing Team Member Plus API's...")

        """Languages
        https://api.projectplace.com/1/languages/ (GET all available languages)
        expected output : [
          "danish",
          "dutch",
          "english",
          "french",
          "german",
          "norwegian",
          "swedish",
          "spanish" ]"""

        READ_LANGUAGES = Schema([str], required=True)
        print("Checking Language API: \n", READ_LANGUAGES(([
            "danish",
            "dutch",
            "english",
            "french",
            "german",
            "norwegian",
            "swedish",
            "spanish"])))

        # Account API's for TM+


        # """/1/account/members?include_external_users=1
        # """/1/account/members?include_external_users=1&regis
        # {
        #   "external": [],
        #   "members": [
        #     {
        #       "account_owner": true,
        #       "name": "Shalini Arora",
        #       "id": 1016693,
        #       "account_admin": true,
        #       "avatar": "/ppi/avatars/initial_avatar_SA.png",
        #       "email": "sarora@planview.com"
        #
        #     }
        #   ]
        # }"""

        MEMBERS = Schema({
            'account_owner': bool,
            'name': str,
            'id': int,
            'account_admin': bool,
            'avatar': str,
            'email': str
        }, required=True)

        READ_MEMBERS_EXTERNAL = Schema({'external': [],
                                        'members': [MEMBERS]
                                        }, required=True)

        print("Checking account/members APIs:\n", READ_MEMBERS_EXTERNAL({
            "external": [],
            "members": [
                {
                    "account_owner": True,
                    "name": "Shalini Arora",
                    "id": 1016693,
                    "account_admin": True,
                    "avatar": "/ppi/avatars/initial_avatar_SA.png",
                    "email": "sarora@planview.com"

                }
            ]
        }))

        READ_MEMBERS_EXTERNAL_REGISTERED = Schema({'external': [],
                                                   'members': [MEMBERS.extend({'registered': bool})]
                                                   })

        print('Checking READ_MEMBERS_EXTERNAL_REGISTERED API: \n', READ_MEMBERS_EXTERNAL_REGISTERED(
            {
                "external": [],
                "members": [
                    {
                        "account_owner": True,
                        "name": "Shalini Arora",
                        "id": 1016693,
                        "account_admin": True,
                        "avatar": "/ppi/avatars/initial_avatar_SA.png",
                        "email": "sarora@planview.com",
                        "registered": True

                    }
                ]
            }))

        # Invite members:
        # / 1 / account / members(POST toCreate)
        # {
        #     "invalid_invitees": [
        #         {
        #             "cause": "PART_OF_THIS_ACCOUNT", // Already invited
        #         "id": 947897,
        # "name": "Account Member"
        # },
        # {
        #     "cause": "PART_OF_OTHER_ACCOUNT", // Belongs
        # to
        # another
        # account
        # "id": 947988,
        # "name": "Member of other account"
        # },
        # {
        #     "cause": "UNREGISTERED_MEMBER", // Invited
        # but
        # unregistered
        # "id": 947850,
        # "name": "user3@example.com"
        # }
        # ],
        # "data": [
        #     {
        #         "name": "New Invitee",
        #         "email": "user4@example.com",
        #         "avatar": "/ppi/avatars/initial_avatar_NI.png",
        #         "id": 947897
        #     }
        # ]
        # }




        # 1 / timereports / {0} / {1}?project_id = {2}
        # 1/timereports/planlets/109988?project_id=2314308


        # expectedoutput:
        # [
        #   {
        #     "artifactTitle": "Auto_Task_2017-05-04_10:16:57_238905",
        #     "updatedOn": "2017-05-04 06:47:28",
        #     "projectId": 2314308,
        #     "createdOn": "2017-05-04 06:47:28",
        #     "userId": "757858",
        #     "meta": {
        #       "isParent": false
        #     },
        #     "reportId": 10514,
        #     "reportedDate": "2017-05-02",
        #     "artifactType": "planlets",
        #     "minutes": 60,
        #     "artifactId": 109988
        #   },

        INVALID_INVITEES = Schema({
            'cause': str,
            'id': int,
            'name': str
        })

        VALID_INVITEES = Schema({
            'name': str,
            'email': str,
            'avatar': str,
            'id': int
        })
        CREATE_MEMBERS = Schema({
            'invalid_invitees': [INVALID_INVITEES],
            'data': [VALID_INVITEES]
        }, required=True)

        print('checking CREATE_MEMBERS APIs: \n', CREATE_MEMBERS({
            "data": [
                {
                    "name": "New Invitee",
                    "email": "user4@example.com",
                    "avatar": "/ppi/avatars/initial_avatar_NI.png",
                    "id": 947897
                }

            ],
            "invalid_invitees": [
                {
                    "cause": "UNREGISTERED_MEMBER",
                    "id": 533653,
                    "name": "sarora@planview.com"
                },
                {
                    "cause": "PART_OF_OTHER_ACCOUNT",
                    "id": 947988,
                    "name": "Member of other account"
                }
            ]
        }))



        TIME_REPORTED = Schema([{
            'artifactTitle': str,
            'updatedOn': Datetime(r"%Y-%m-%d %H:%M:%S"),
            'projectId': int,
            'createdOn': Datetime(r"%Y-%m-%d %H:%M:%S"),
            'userId': str,
            'meta': {'isParent': bool},
            'reportId': int,
            'reportedDate': Datetime(r"%Y-%m-%d"),
            'artifactType': str,
            'minutes': int,
            'artifactId': int
        }], required=True)

        print('Checking TIME_REPORTED schema: \n', TIME_REPORTED([
            {
                "artifactTitle": "Auto_Task_2017-05-04_10:16:57_238905",
                "updatedOn": "2017-05-04 06:47:28",
                "projectId": 2314308,
                "createdOn": "2017-05-04 06:47:28",
                "userId": "757858",
                "meta": {
                    "isParent": False
                },
                "reportId": 10514,
                "reportedDate": "2017-05-02",
                "artifactType": "planlets",
                "minutes": 60,
                "artifactId": 109988
            }]))









        # / 1 / user / {0} / check - terminate(GET check if can be terminated)
        # -	/1/user/{0}/terminate (POST terminate)
        #  - / 1 / account / members(POST      to        Create)


instance = team_member_plus_api()
