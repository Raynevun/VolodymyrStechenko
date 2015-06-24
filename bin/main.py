
import xml.etree.ElementTree as ET

import requests



class Request():
    httpcode = None
    url = "https://beacon.nist.gov/rest/record/0"

    def makeRequest(self):

        # request here
        self.r = requests.get(self.url)
        self.httpcode = str(self.r)
        self.document = self.r.text

        return self.document

    def makeTimeRequest(self, time):
        info = {'nocache': str(time)}
        self.request = requests.get(self.url, data=info)
        self.timedoc = self.request.text

        return self.timedoc

    # getting desired tagname content here
    def tagContent(self, tagname):


        self.tree = ET.fromstringlist(self.makeRequest(self))

        for elt in self.tree.iter():
            if elt.tag == str(tagname):
                self.tagvalue = elt.text.strip()

        return self.tagvalue

    def tagTimeContent(self, tagname, time):
        self.tree = ET.fromstringlist(self.makeTimeRequest(self, time))

        for elt in self.tree.iter():
            if elt.tag == str(tagname):
                self.tagvalue = elt.text.strip()

        return self.tagvalue

    def giveStats(self, tagname):

        try:
            # calling this get tagname text
            self.statsinfo = self.tagContent(self, tagname)

            # set for all unique chars
            self.statsset = set(list(self.statsinfo))

            # counting how much each unique char occurs in response tagname field
            for ch in self.statsset:
                print(ch, ',', self.statsinfo.count(ch))

        except AttributeError:
            print('no attribute for ', tagname, 'check if spelling is correct')



if __name__ == "__main__":
    Request.giveStats(Request, 'outputValue')




