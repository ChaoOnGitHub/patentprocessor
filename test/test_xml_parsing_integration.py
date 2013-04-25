#!/usr/bin/env python

import os
import re
import sys
import unittest
from xml_driver import XMLElement, XMLHandler, Patent
from xml.sax import make_parser, handler

sys.path.append('../lib')
from patXML import *

# Directory of test files
basedir = os.curdir
testdir = os.path.join(basedir, 'fixtures/xml/')
xml_files = [x for x in os.listdir(testdir)
             if re.match(r"20\d\d_\d+.xml", x) != None] # Match fixtures

parsed_xml_old = []
parsed_xml_new = []
for xf in xml_files:
    old = XMLPatentBase(open(testdir+xf).read())
    new = Patent(open(testdir+xf))
    parsed_xml_old.append(old)
    parsed_xml_new.append(new)

xml_files = [x for x in os.listdir(testdir)
            if re.match(r'ipg120327.one.xml', x) != None]
for xf in xml_files:
    old = XMLPatentBase(open(testdir+xf).read())
    new = Patent(open(testdir+xf))
    parsed_xml_old.append(old)
    parsed_xml_new.append(new)

class Test_Compatibility(unittest.TestCase):
    def setUp(self):
        # sanity check
        self.assertTrue(xml_files)

    def test_country(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.country == new.country, "{0}\nshould be\n{1}".format(new.country,old.country))

    def test_patent(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.patent == new.patent, "{0}\nshould be\n{1}".format(new.patent,old.patent))

    def test_kind(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.kind == new.kind, "{0}\nshould be\n{1}".format(new.kind,old.kind))

    def test_date_grant(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.date_grant == new.date_grant, "{0}\nshould be\n{1}".format(new.date_grant,old.date_grant))

    def test_pat_type(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.pat_type == new.pat_type, "{0}\nshould be\n{1}".format(new.pat_type,old.pat_type))

    def test_date_app(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.date_app == new.date_app, "{0}\nshould be\n{1}".format(new.date_app,old.date_app))
        
    def test_country_app(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.country_app == new.country_app, "{0}\nshould be\n{1}".format(new.country_app,old.country_app))

    def test_patent_app(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.patent_app == new.patent_app, "{0}\nshould be\n{1}".format(new.patent_app,old.patent_app))

    def test_classes(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.classes == new.classes, "{0}\nshould be\n{1}".format(new.classes,old.classes))

    def test_code_app(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.code_app == new.code_app , "{0}\nshould be\n{1}".format(new.code_app,old.code_app))

    def test_clm_num(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.clm_num == new.clm_num , "{0}\nshould be\n{1}".format(new.clm_num,old.clm_num))

    def test_abstract(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.abstract == new.abstract , "{0}\nshould be\n{1}".format(new.abstract,old.abstract))

    def test_invention_title(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.invention_title == new.invention_title, "{0}\nshould be\n{1}".format(new.invention_title,old.invention_title))

    def test_asg_list(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.asg_list == new.asg_list, "{0}\nshould be\n{1}".format(new.asg_list,old.asg_list))

    def test_cit_list(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.cit_list == new.cit_list, "{0}\nshould be\n{1}".format(new.cit_list,old.cit_list))

    def test_rel_list(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.rel_list == new.rel_list, "{0}\nshould be\n{1}".format(new.rel_list,old.rel_list))

    def test_inv_list(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.inv_list == new.inv_list, "{0}\nshould be\n{1}".format(new.inv_list,old.inv_list))

    def test_law_list(self):
        for old,new in zip(parsed_xml_old, parsed_xml_new):
            self.assertTrue( old.law_list == new.law_list, "{0}\nshould be\n{1}".format(new.law_list,old.law_list))

    def tearDown(self):
        #anything needed to be torn down  should be  added here, pass for now
        pass

#unittest.main()
