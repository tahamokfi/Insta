======
Instagram Followers crawler
======

.. image:: https://img.shields.io/badge/Python-3.4%20and%203.5%20and%203.6-blue.svg
   :alt: Python Version 3
.. image:: https://img.shields.io/badge/Issuses-0%20open-green.svg
   :alt: 0 Issues are open
[![Build Status](https://travis-ci.org/ex0dus-0x/brut3k1t.svg?branch=master)](https://travis-ci.org/ex0dus-0x/brut3k1t)
[![GitHub forks](https://img.shields.io/github/forks/ex0dus-0x/brut3k1t.svg)](https://github.com/ex0dus-0x/brut3k1t/network)
[![GitHub issues](https://img.shields.io/github/issues/ex0dus-0x/brut3k1t.svg)](https://github.com/ex0dus-0x/brut3k1t/issues)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/ex0dus-0x/brut3k1t/master/LICENSE)
Overview
========
There are two codes here which help you to crawl all of your followers and their followings. The main library which I used here is Selenium (you should install it before running the codes).
You can directly download these python files and use them through command line or any Python IDE. 

Here, I used “Phantomjs” as my default browser for Selenium which you can download it from [this link](http://phantomjs.org/download.html). Then you have to make sure to place “phantomjs.exe” file in your path and in “\Anaconda3\Lib\site-packages\selenium\webdriver\phantomjs” or “\Python34\Lib\site-packages\selenium\webdriver\phantomjs”.

### First code: My_Followers.py

This code will import all of your followers which you are following them as well. If you want to have access to your follower’s followers or follower’s followings you have to follow them. The output would be a “.CSV” file which contains list of your followers (not all of your followers just whom you are following)

You have to input your username, password, and your Instagram ID which is usually the same as your username. The exported file will be saved in your user directory which usually you have the privilege to save data into it. At the end of the code the path of saved file will be printed out.
