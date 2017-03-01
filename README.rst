======
Scrapy
======

.. image:: https://img.shields.io/pypi/v/Scrapy.svg
   :target: https://pypi.python.org/pypi/Scrapy
   :alt: PyPI Version

.. image:: https://img.shields.io/travis/scrapy/scrapy/master.svg
   :target: http://travis-ci.org/scrapy/scrapy
   :alt: Build Status

.. image:: https://img.shields.io/badge/wheel-yes-brightgreen.svg
   :target: https://pypi.python.org/pypi/Scrapy
   :alt: Wheel Status

.. image:: https://img.shields.io/codecov/c/github/scrapy/scrapy/master.svg
   :target: http://codecov.io/github/scrapy/scrapy?branch=master
   :alt: Coverage report

.. image:: https://anaconda.org/conda-forge/scrapy/badges/version.svg
   :target: https://anaconda.org/conda-forge/scrapy
   :alt: Conda Version


Overview
========

======
Instagram Followers crawler
======
.. image::https://img.shields.io/badge/Python-3.5-blue.svg

Introduction
======
There are two codes here which help you to crawl all of your followers and their followings. The main library which I used here is Selenium (you should install it before running the codes).
You can directly download these python files and use them through command line or any Python IDE. 

Here, I used “Phantomjs” as my default browser for Selenium which you can download it from [this link](http://phantomjs.org/download.html). Then you have to make sure to place “phantomjs.exe” file in your path and in “\Anaconda3\Lib\site-packages\selenium\webdriver\phantomjs” or “\Python34\Lib\site-packages\selenium\webdriver\phantomjs”.

### First code: My_Followers.py

This code will import all of your followers which you are following them as well. If you want to have access to your follower’s followers or follower’s followings you have to follow them. The output would be a “.CSV” file which contains list of your followers (not all of your followers just whom you are following)

You have to input your username, password, and your Instagram ID which is usually the same as your username. The exported file will be saved in your user directory which usually you have the privilege to save data into it. At the end of the code the path of saved file will be printed out.
