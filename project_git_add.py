# -*- coding: utf-8 -*-
import re
import time
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ProjectGitAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.0.18/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_project_git_add(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("user")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("bitnami")
        driver.find_element_by_name("login").click()
        driver.find_element_by_css_selector("#top-menu > div > ul > li:nth-child(5) > a").click()
        driver.find_element_by_css_selector("#admin-menu > ul > li > a.projects").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(project)
        driver.find_element_by_css_selector("fieldset > input.small").click()
        driver.find_element_by_link_text(project).click()
        driver.find_element_by_id("tab-repositories").click()
        driver.find_element_by_link_text(u"新建版本库").click()
        Select(driver.find_element_by_id("repository_scm")).select_by_visible_text("Git")
        driver.find_element_by_id("repository_identifier").clear()
        # driver.find_element_by_id("repository_identifier").send_keys("server")
        sleep(0.5)
        driver.find_element_by_css_selector("#repository_identifier").send_keys("server")
        driver.find_element_by_id("repository_url").clear()
        driver.find_element_by_id("repository_url").send_keys(server_path)
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"新建版本库").click()
        Select(driver.find_element_by_id("repository_scm")).select_by_visible_text("Git")
        driver.find_element_by_id("repository_identifier").clear()
        # driver.find_element_by_id("repository_identifier").send_keys("web")
        sleep(0.5)
        driver.find_element_by_css_selector("#repository_identifier").send_keys("web")
        driver.find_element_by_id("repository_url").clear()
        driver.find_element_by_id("repository_url").send_keys(web_path)
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"新建版本库").click()
        Select(driver.find_element_by_id("repository_scm")).select_by_visible_text("Git")
        driver.find_element_by_id("repository_identifier").clear()
        # driver.find_element_by_id("repository_identifier").send_keys("android")
        sleep(0.5)
        driver.find_element_by_css_selector("#repository_identifier").send_keys("android")
        driver.find_element_by_id("repository_url").clear()
        driver.find_element_by_id("repository_url").send_keys(android_path)
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"新建版本库").click()
        Select(driver.find_element_by_id("repository_scm")).select_by_visible_text("Git")
        driver.find_element_by_id("repository_identifier").clear()
        # driver.find_element_by_id("repository_identifier").send_keys("ios")
        sleep(0.5)
        driver.find_element_by_css_selector("#repository_identifier").send_keys("ios")
        driver.find_element_by_id("repository_url").clear()
        driver.find_element_by_id("repository_url").send_keys(ios_path)
        driver.find_element_by_name("commit").click()
        driver.find_element_by_id("tab-wiki").click()
        driver.find_element_by_link_text("Wiki").click()
        driver.find_element_by_id("content_text").clear()
        driver.find_element_by_id("content_text").send_keys("")
        driver.find_element_by_id("content_text").clear()
        driver.find_element_by_id("content_text").send_keys(wiki_text)
        driver.find_element_by_name("commit").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    project = raw_input('输入项目标志名称：')
    project_name = project.lower()
    server_path = '/opt/bitnami/projects/{}/{}.server/'.format(project_name, project_name)
    web_path = '/opt/bitnami/projects/{}/{}.web/'.format(project_name, project_name)
    android_path = '/opt/bitnami/projects/{}/{}.android/'.format(project_name, project_name)
    ios_path = '/opt/bitnami/projects/{}/{}.ios/'.format(project_name, project_name)

    wiki_text = "http://git.redmine_viziner.com/{}/{}.server\nhttp://git.redmine_viziner.com/{}" \
                "/{}.web\nhttp://git.redmine_viziner.com/{}/{}.android\nhttp://git.redmine_viziner.com" \
                "/{}/{}.ios ".format(project_name, project_name, project_name, project_name,
                                     project_name, project_name, project_name, project_name,)
    unittest.main()
