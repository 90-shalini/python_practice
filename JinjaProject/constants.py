import os

PAYLOAD_PATH = os.path.abspath((os.path.join(os.path.dirname(__file__), '..\..\pve\\templates')))

##### PVE SOAP WEBSERVICES ####
LOGIN_WSDL = 'https://pve_env/planview/services/LoginService.svc?wsdl'  # Not used from this constant file. Taken care at LoginCertCookie class
PROJECT_WSDL = '$protocol://$pve_env/planview/services/ProjectService.svc'
ATTRIBUTES_WSDL = '$protocol://$pve_env/planview/services/AttributeService.svc'
WORKSTATUS_WSDL = '$protocol://$pve_env/planview/services/WorkStatusService.svc'
EXT_KEY_URI_WSDL = '$protocol://$pve_env/planview/services/ExternalKeyUriMapService.svc'
QUERY_WSDL = '$protocol://$pve_env/planview/services/QueryService.svc'
TASK_WSDL = '$protocol://$pve_env/planview/services/TaskService.svc'
TIME_REPORTED_WSDL = '$protocol://$pve_env/planview/services/TimeReportedService.svc'
AUTHORIZATION_WSDL = '$protocol://$pve_env/planview/services/AuthorizationService.svc'
ALLOCATION_WSDL = '$protocol://$pve_env/planview/services/AllocationService.svc'
RESERVE_WSDL = '$protocol://$pve_env/planview/services/ReserveService.svc'

##### PVE SOAP ACTION HEADER ####
PRJ_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/ProjectService3/2012/08/IProjectService3/'
WRK_STATUS_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/WorkStatusService/2012/11/IWorkStatusService2/'
ATT_SET_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/IAttributeService2/2012/08/IAttributeService2/'
EXT_READBY_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/ExternalKeyUriMap/2012/02/01/IExternalKeyUriMapService/'
QUERY_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/QueryService/2012/12/IQueryService/'
TASK_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08/ITaskService3/'
TIME_REPORTED_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/TimeReportedService/2013/03/ITimeReportedService/'
AUTHORIZATION_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/AuthorizationService/2013/08/IAuthorizationService/'
ALLOCATION_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/Allocation/2012/08/IAllocationService3/'
RESERVE_SOAP_ACTION = 'http://schemas.planview.com/PlanviewEnterprise/Services/Reserve/2012/08/IReserveService2/'

####### DICT CONSTANTS FOR PVE ######

ARTIFACT_MAP = {
    'project': {
        'create': {
            'url': PRJ_SOAP_ACTION + 'Create',
            'payload': PAYLOAD_PATH + '\\projects\\create.xml'
            },
        'delete': {
            'url': PRJ_SOAP_ACTION + 'Delete',
            'payload': PAYLOAD_PATH + '\\projects\\delete.xml'
            },
        'read': {
            'url': PRJ_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\projects\\read.xml'
            },
        'update': {
            'url': PRJ_SOAP_ACTION + 'Update',
            'payload': PAYLOAD_PATH + '\\projects\\update.xml'
            }
        },
    'attributes': {
        'set_multiple_attr': {
            'url': ATT_SET_SOAP_ACTION + 'Set',
            'payload': PAYLOAD_PATH + '\\attributes\set_attributes.xml'
             },
        'set_single_attr': {
            'url': ATT_SET_SOAP_ACTION + 'Set',
            'payload': PAYLOAD_PATH + '\\attributes\set_single_attribute.xml'
        },
        'read': {
            'url': ATT_SET_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\attributes\\read_attributes.xml'
             }
        },
    'workstatus': {
        'update': {
            'url': WRK_STATUS_SOAP_ACTION + 'Update',
            'payload': PAYLOAD_PATH + '\\wrk_status\\wrk_status.xml'
        }
    },
    'task': {
        'create': {
            'url': TASK_SOAP_ACTION + 'Create',
            'payload': PAYLOAD_PATH + '\\tasks\\create.xml'
        },
        'delete': {
            'url': TASK_SOAP_ACTION + 'Delete',
            'payload': PAYLOAD_PATH + '\\tasks\\delete.xml'
            },
        'read': {
            'url': TASK_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\tasks\\read.xml'
            },
        'update': {
            'url': TASK_SOAP_ACTION + 'Update',
            'payload': PAYLOAD_PATH + '\\tasks\\update.xml'
            },
        'update_actual': {
            'url': TASK_SOAP_ACTION + 'Update',
            'payload': PAYLOAD_PATH + '\\tasks\\update_actual.xml'
            },
        'update_start_date': {
            'url': TASK_SOAP_ACTION + 'Update',
            'payload': PAYLOAD_PATH + '\\tasks\\update_start_date.xml'
        },
        'update_schedule': {
            'url': TASK_SOAP_ACTION + 'Update',
            'payload': PAYLOAD_PATH + '\\tasks\\update_schedule.xml'
        }
    },
    'pverallyinfoext': {
        'readallbyinternalkey': {
            'url': EXT_READBY_SOAP_ACTION + 'ReadAllByInternalKey',
            'payload': PAYLOAD_PATH + '\\externalkeys\\internal_key.xml'
        }
    },
    'pverallyinfoquery': {
        'read': {
            'url': QUERY_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\queries\\query.xml'
        }
    },
    'timereported': {
        'upsert': {
            'url': TIME_REPORTED_SOAP_ACTION + 'Upsert',
            'payload': PAYLOAD_PATH + '\\time_reported\\upsert_time_reported.xml'
        },
        'read': {
            'url': TIME_REPORTED_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\time_reported\\read_time_reported.xml'
        }
    },
    'authorization': {
        'create': {
            'url': AUTHORIZATION_SOAP_ACTION + 'Create',
            'payload': PAYLOAD_PATH + '\\authorization\\create.xml'
        },
        'read': {
            'url': AUTHORIZATION_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\authorization\\read.xml'
        }
    },
    'allocation': {
        'create': {
            'url': ALLOCATION_SOAP_ACTION + 'Create',
            'payload': PAYLOAD_PATH + '\\allocation\\create.xml'
        },
        'read': {
            'url': ALLOCATION_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\allocation\\read.xml'
        }
    },
    'reserve': {
        'create': {
            'url': RESERVE_SOAP_ACTION + 'Create',
            'payload': PAYLOAD_PATH + '\\reserve\\create.xml'
        },
        'read': {
            'url': RESERVE_SOAP_ACTION + 'Read',
            'payload': PAYLOAD_PATH + '\\reserve\\read.xml'
        }
    }
}

ATTRIBUTES = {'Rally Sync': 'RallySync',
              'Rally Workspace': 'RalWspace',
              'Rally Project': 'RallyProj',
              'Rally Portfolio Item Type': 'RalPfITyp',
              'Description': 'PW_DESCRIPTION',
              'Work Description': 'PE01',
              'Requested Start Date': 'PW_REQUESTED_START',
              'Requested End Date': 'PW_REQUESTED_FINISH',
              'Rally Report Time': 'RalRepTime',
              'PP Sync': 'PPSync',
              'Shared Assignments': 'PPShAsgn'}
