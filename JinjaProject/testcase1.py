import sys
import constants
import os
from jinja2 import Environment, FileSystemLoader, Template



class testcase1:

    def __init__(self):
        self.operation = None
        self.artifact = None

        # PATH = os.path.dirname(os.path.abspath(r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject'))
        # self.template_env = Environment(
        #     autoescape=False,
        #     loader=FileSystemLoader(r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject\Templates'),
        #     trim_blocks=False)

    def create_step(self):
        self.project_key= '123456'
        self.task_desc, self.task_key, task_status = self.create(self.project_key)


    # Controller's create
    def create(self, father_key, name='Task', encoding='utf-8'):
        description = "My_desc"    #self.helper.get_name(name)
        self.list_create_task_values = [{'Description': description, 'FatherKey': father_key}]

        self.modelCreate(self.list_create_task_values, encoding)
    #     task_key = self.verify_created_key
    #
    #     status = self.verify_create(encoding)
    #
    # return description, task_key, status
    # model's create

    def modelCreate(self, list_of_dict, encoding='utf-8'):
        soap_create_action, soap_payload = self.get_soap_details('task', 'create', list_of_dict)
        print("soap_create_action", soap_create_action)
        print("soap_payload kin Model create", soap_payload)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_create_action)
        # response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)
        #
        # self.verify_created_key = self.parse_wrapper.get_values(response.text)[0]
        # self.verify_description = list_of_dict[0]['ns1:Description']
        # self.verify_father_key = list_of_dict[0]['ns1:FatherKey']

    #Payload generator
    def get_soap_details(self, artifact, operation, list_dict_values):
            soap_action = self.get_action(artifact, operation)
            soap_payload = self.get_payload(list_dict_values)
            return soap_action, soap_payload

    def get_action(self, artifact, operation):
        self.artifact = artifact
        self.operation = operation
        return constants.ARTIFACT_MAP[artifact][operation]['url']

    def get_payload(self, values):
        print("Lits of dict values: ", values)
        template = self.template_env.get_template('create.xml').render(values = values)
        print("template: ", template)
        return template



    def get_template(self):
        payload_path = constants.ARTIFACT_MAP[self.artifact][self.operation]['payload']
        return self.template_env.get_template('create.xml')

    def update_step(self):
        pass

    def verify_step(self):
        pass

    def run(self):
        self.create_step()

        self.verify_step()
        self.update_step()

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 8:
        pve_env = args[1]
        pve_dsn = args[2]
        pve_db = args[3]
        rally_env = args[4]
        rally_user = args[5]
        integ_env = args[6]
        run_id = args[7]
        test_obj = testcase1(pve_env, pve_dsn, pve_db, rally_env, rally_user, integ_env)
        test_obj.run(run_id)
    else:
        sys.exit(-1)