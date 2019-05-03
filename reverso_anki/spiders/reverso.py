# -*- coding: utf-8 -*-
import os

import scrapy


class ReversoSpider(scrapy.Spider):
    name = 'reverso'
    allowed_domains = ['https://context.reverso.net']
    # start_urls = ['https://context.reverso.net/favourites']
    start_urls = ['https://account.reverso.net/login/context.reverso.net/en']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': os.getenv('USERNAME'), 'password': os.getenv('PASSWORD')},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return
