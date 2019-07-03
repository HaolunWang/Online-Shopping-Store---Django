# Online-Shopping-Store---Django

Description:

This project is based on campus project, and it can represent the products information and it can also show the registration, login layouts and users can place the orders and view the orders that they purchased as well. All in all, this project is a course - based demo, it has the bootstrap to render, it looks simple but it is actually a skeleton website of real online shopping store like Amazon, e-bay.
I hope it will help you (especially for students group) a lot.

Features:

The features are the basic required features and some optional features.

The main page have a login link. Either users and superusers can be access to this site. 

Users should register the username and password before login. If the user using wrong username or password is will show an 

invalid info.

Once registered，users are able to view the products list and users' orders while adding order with place order function.

When viewing the admin page, users are able to see the products category, stock, and products details.

There is a validation range from 0 to 1000 in place order products.

After login , user can also logout clicking the logout botton. The page will show a  Hello Guest instead of user name.

This website using Bootstrap to style the pages. 

For bootstrap installed:

If you meet some issues with installing the bootstrap on PyCharm, you should do the following steps:

The first step: install the "Django-bootstrap3" package from the PyCharm IDE;

The second step: put "bootstrap3" in INSTALLEDAPP in setting.py

The last step: put three lines "{% load bootstrap3 %}", "{% load bootstrap3_css %}", "{% load bootstrap3_javascript %}" in the html files that needed

If you also meet some issues such as Python version while installing the bootstrap on PyCharm, I highly recommend you to look 

at these links:

https://wsvincent.com/install-python3-mac/

https://www.youtube.com/watch?v=5y9Z_BhEr5Q

These resources are really helpful.

