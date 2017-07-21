
import os
from jinja2 import Template, Environment, FileSystemLoader, PackageLoader



class TestJinja:
    def __init__(self):
        PATH = os.path.dirname(os.path.abspath(r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject'))
        # self.template_env = Environment(
        #                                 autoescape=False,
        #                                 loader=FileSystemLoader(r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject\Templates'),
        #                                 trim_blocks=False)


        self.list_of_values = {'ns1:Description': 'My_desc', 'ns1:FatherKey': '12345'}
        # self.env = Environment(
        #             autoescape= True,
        #             loader = FileSystemLoader(r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject\Templates')
        # )
        # template = self.env.get_template('create.xml')
        # print(template.render(list_of_values = self.list_of_values))


    def render_template(self, template_filename, value):
        return self.template_env.get_template(template_filename).render(dict1=value)

    def basicSample(self):
        template = Template('Hello {{name}}!')  # template is new Template object
        print(template.render(
            name='Shalini Arora'))  # arguments in render() method i.e. dict or keywords to expand the template DICT or keywords arguments are CONTEXT of template

        t = Template('My Favorite numbers: {% for n in range(1,10) %}{{n}}' '{% endfor %}')
        print(
            t.render())


    def fileTemplateSample(self):
        fname = "create_jinja.xml"
        dict1 = {'description': 'My_desc',
                'father_key':'My_key'}
        with open(fname, 'w') as f:
            xml =  self.render_template('create.xml',dict1)
            f.write(xml)
            print(f)

        # render values in that template

    def newFileTemplate(self):
        fname = r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject\Templates\create-jinja.xml'
        self.template_env = Environment(
                                        autoescape=False,
                                        loader=FileSystemLoader(r'C:\Users\Shalini\PycharmProjects\Practice\JinjaProject\Templates\create.xml'),
                                        trim_blocks=False)
        template = self.template_env.get_template('').render(list_of_values = self.list_of_values)
        print("template: ", template)
        # with open(fname, 'w') as f:
        #     xmlFile = template.render(list_of_values =self.list_of_values)
        #     print("xml to write: ",xmlFile)
        #     f.write(xmlFile)
        #     # print(f)
        #     f.close()

if __name__ =='__main__':
    test_obj = TestJinja()
    test_obj.newFileTemplate()




