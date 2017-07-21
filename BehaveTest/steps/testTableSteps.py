from behave import *

@given(u'Users visited')
def step_impl(context):
    for row in context.table:
        print(row['Name'])
        print(row['Company'])
        name = row['Name']
        company = row['Company']
        print("all the things printed:", name, company)

@when(u'i checked')
def step_impl(context):
    print("I checked visitors.")

    @given(u'created time_report payload for "{artifact_type}"')
    def step_impl(context, artifact_type):
        artifact_dict = {'cards': context.card_ids[0], 'planlets1': context.planlet_ids[0],
                         'planlets2': context.planlet_ids[1], 'planlets3': context.planlet_ids[2]}
        context.time_report_payload = {'artifactId': artifact_dict[artifact_type],
                                       'artifactType': artifact_type.strip('0123456789'),
                                       'projectId': int(context.workspace_id)}

    @given(u'time_report created for "{no_of_weeks}" week')
    def step_impl(context, no_of_weeks):
        create_time_report_status, report_ids_list = context.time_report_ctrl.create(no_week=int(no_of_weeks)
                                                                                     ,
                                                                                     payload_key=context.time_report_payload)
        expected_time_dict = context.time_report_ctrl.get_constructed_time_dict(context.workspace_id, report_ids_list)
        context.list_expected_time_dict.append(expected_time_dict)
        assert create_time_report_status


# @given(u'task created at level PPL+1')
# def step_impl(context):
#     context.phase_desc, context.phase_key, phase_status = context.task_ctrl.create(context.project_key)
#     assert(phase_status)


@given(u'task created at level PPL+2')
def step_impl(context):
    context.activity_desc, context.activity_key, activity_status = context.task_ctrl.create(context.phase_key)
    assert(activity_status)


@given(u'task created at level PPL+3')
def step_impl(context):
    context.task_desc, context.task_key, task_status = context.task_ctrl.create(context.activity_key)
    assert(task_status)


@then(u'verify planlets at level PPL+1')
def step_impl(context):
    context.pp_plnt_id_1, pp_plnt_status_1 = context.pve_verify_ctrl.verify_pp_project_id(context.wbs_dict['1'])
    context.planlet_ids.append(context.pp_plnt_id_1)
    assert pp_plnt_status_1


@then(u'verify planlets at level PPL+2')
def step_impl(context):
    context.pp_plnt_id_11, pp_plnt_status_11 = context.pve_verify_ctrl.verify_pp_project_id(context.wbs_dict['2'])
    context.planlet_ids.append(context.pp_plnt_id_11)
    assert(pp_plnt_status_11)


@then(u'verify planlets at level PPL+3')
def step_impl(context):
    context.pp_plnt_id_111, pp_plnt_status_111 = context.pve_verify_ctrl.verify_pp_project_id(context.wbs_dict['3'])
    context.planlet_ids.append(context.pp_plnt_id_111)
    assert(pp_plnt_status_111)