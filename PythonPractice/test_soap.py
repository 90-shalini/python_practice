import requests
import pprint
import xml.etree.cElementTree as ET1
from lxml import etree as ET




class SampleClass:

    def __init__(self):
        # client = SoapClient(wsdl="http://192.168.1.7:8080/Testmart/ProductCatalogService?WSDL", trace=False)
        # response = client.getProducts("books")
        # result = response['books']
        # print(response)
        url = "http://192.168.1.7:8080/Testmart/ProductCatalogService?WSDL"
        # headers = {'content-type': 'application/soap+xml'}
        # headers = {'content-type': 'text/xml'}
        # body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap="http://soap.trainings.cisco.org/">
        #             <soapenv:Header/>
        #              <soapenv:Body>
        #                 <soap:getProducts>
        #                  <!--Optional:-->
        #                     <arg0>books</arg0>
        #                 </soap:getProducts>
        #             </soapenv:Body>
        #         </soapenv:Envelope>"""
        #
        # response = requests.post(url, data=body, headers=headers)
        # print(response.content)
        self.getBody()

    def getBody(self):
        envelope = ET.Element("Envelope")
        header = ET.SubElement(envelope, "Header")
        body = ET.SubElement(envelope, "Body")
        products = ET.SubElement(body, "getProducts")


        ET.SubElement(products, "args", name="blah").text = "some value1"

        self.tree = ET.ElementTree(envelope)
        print(ET.tostring(self.tree, pretty_print=True))




