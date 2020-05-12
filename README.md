<div align="center">
<a href="https://www.pland.com.br" target="_blank">
    <img src="https://pland.com.br/img/PlanD_Logo_Posit_RGB.png" height="100px" alt="PlanD"/>
</a>

<h3>Backend Developer Challenge</h3>

<a href="https://www.python.org" target="_blank">
  <img src="https://img.shields.io/badge/devel-Python-brightgreen" alt="Python"/>
</a>

<a href="https://travis-ci.com" target="_blank">
  <img src="https://img.shields.io/badge/ci-Travis-brightgreen" alt="Travis CI"/>
</a>

<a href="https://www.django-rest-framework.org" target="_blank">
  <img src="https://img.shields.io/badge/api-DRF-brightgreen" alt="Django Rest Framework"/>
</a>

<a href="https://www.djangoproject.com" target="_blank">
  <img src="https://img.shields.io/badge/main--framework-Django-brightgreen" alt="Django"/>
</a>

<a href="https://www.docker.com" target="_blank">
  <img src="https://img.shields.io/badge/deploy-Docker|Heroku-brightgreen" alt="Docker"/>
</a>

<a href="https://docs.conda.io/en/latest/miniconda.html" target="_blank">
  <img src="https://img.shields.io/badge/venv-Conda-brightgreen" alt="Conda"/>
</a>

<a href="https://docs.pytest.org/en/latest" target="_blank">
  <img src="https://img.shields.io/badge/coverage-PyTest-brightgreen" alt="PyTest"/>
</a>

<a href="https://opensource.org/licenses/MIT" target="_blank">
  <img src="https://img.shields.io/badge/license-MIT-brightgreen" alt="MIT"/>
</a>

</div>

## TL;DR
##### Front End Application: https://pdchallenge.herokuapp.com/
##### API Postman Documentation: https://cutt.ly/pdtest-postman
##### Continuous Integration Tests: https://cutt.ly/pdtest-travis
##### Github Repository: https://cutt.ly/pdtest-github
##### Docker Repository: https://cutt.ly/pdtest-docker

## Local execution

### 1 - Run using Docker
<pre>
$ docker run -p 8030:8030 -d --name pdtest-web souluanf/pdchallenge:1.0
</pre>
Point your browser to localhost:8030

### 2 -  Without using the docker
#### Getting the code

```
$ git clone https://github.com/souluanf/pland-challenge.git
```
#### Database configuration:

Install PostgreSQL on Linux:
<pre>
<code> $ sudo apt-get update </code>
<code> $ sudo apt-get install postgresql postgresql-contrib</code></pre>

Now we go create a user and database:
<pre>
<code> $ sudo -i -u postgres psql</code>
<code> $ CREATE ROLE pdtest WITH LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;</code>
<code> $ ALTER ROLE pdtest ENCRYPTED PASSWORD 'pdtest1234';</code>
<code> $ CREATE DATABASE pdtest;</code>
<code> $ GRANT ALL ON DATABASE pdtest TO pdtest;</code>
</pre>

Create a virtual environment with your favorite management system (conda, pyenv, virtualenv, etc);

Activate the created environment and install the requirements:
<pre><code> $ pip install -r requirements.txt </code></pre>

Run the server with the following command:

<pre><code> $ python manager.py runserver </code></pre>
Now is ready!

Then point your browser to localhost:8000

###  Default Credentials

<table>
    <thead>
        <tr class="table100-head">
            <th class="column1">USER</th>
            <th class="column2">PASSWORD</th>
        </tr>
    </thead>
    <tbody>
            <tr>
                <td class="column1">test</td>
                <td class="column2">pdtest1234</td>
            </tr>
    </tbody>
</table>


###  Challenge Description
This is a simple challenge to test your skills on building APIs.
It has to be done using Python and the Django Framework

### What to do

Create a simple API to manage places (CRUD). This API should allow to:

- Create a place
- Edit a place
- Get a specific place
- List places and filter them by name

A place must have the following fields:

- name
- slug
- city
- state
- created at
- updated at

#### Requirements
- All API responses must be JSON
- Provide a README.md file with usage instructions (how to run, endpoints etc)
- Provide a testing environment (heroku, docker, etc)

#### Recommendations
- Tests
- SOLID / DRY
- Code and commits in english (methods, classes, variables, etc)

#### Evaluation
- Project structure, architecturing and organization
- Programming good practices
- VCS practices

### Description of the proposed solution
The application is being developed in python / django, on the back-end (API REST) ​​and on the front-end, containing 1 apps (place). The API can only be used after obtaining the token, with the exception of the customer's registration..

### Front-end
All resources will be made available on the backend through the REST API. A frontend was developed just for this documentation.


### Coverage
Due to the short time, it was only possible to perform a few tests in order to demonstrate the technique. The package used for the tests was pytest.

### Development Environment


<table>
    <thead>
        <tr class="table100-head">
            <th class="column1">Resource</th>
            <th class="column2">Description</th>
            <th class="column3">Version</th>
        </tr>
    </thead>
    <tbody>
            <tr>
                <td class="column1">Laptop</td>
                <td class="column2">16 GB Memory</td>
                <td class="column3">I7 G7</td>
            </tr>
            <tr>
                <td class="column1">Operating System</td>
                <td class="column2">Ubuntu LTS</td>
                <td class="column3">18.04.2</td>
            </tr>
            <tr>
                <td class="column1">Editor/IDE</td>
                <td class="column2">Pycharm Professional</td>
                <td class="column3">2019.3</td>
            </tr>
            <tr>
                <td class="column1">Virtual Env</td>
                <td class="column2">Conda (Miniconda) </td>
                <td class="column3">4.8.3</td>
            </tr>
            <tr>
                <td class="column1">Graphics Card</td>
                <td class="column2">nVidia GM107 </td>
                <td class="column3">GeForce 940MX</td>
            </tr>
            <tr>
                <td class="column1">Devel</td>
                <td class="column2">Python</td>
                <td class="column3">3.8.2</td>
            </tr>
    </tbody>
</table>
