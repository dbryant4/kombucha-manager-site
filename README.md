# Kombucha Manager

Currently, this repo is a Django site with an app which will help keep
track of Kombucha brews and bottling. The app will eventually be 
broken out of this repo and placed in to its own repo.

This repo is currently a Django site which is designed to be pushed to
Heroku. This is why the files `runtime.txt`, `Procfile`, and
`.buildpacks` exist. This README will not cover how to deploy to
Heroku but rather will focus on running the Kombucha Manager app
locally.

## Description

The Kombucha Manager app allows a user to keep track of their kombucha
brews from the beginning of fermentation to bottling. The user can keep track of the types of teas used, length of fermentation, length of secondary fermentation, and flavors used.

## Requirements

- Vagrant
- Virtualbox
- Ansible

## Getting Started

The easiest way to get started is to use Vagrant. To spin up the app in
a Vagrant VM, ensure you have [Vagrant](https://www.vagrantup.com/),
[Virtualbox](https://www.virtualbox.org/wiki/Downloads) (or some [other
provider](https://docs.vagrantup.com/v2/providers/index.html)), and
[Ansible](http://www.ansible.com/home) >= 1.6.10 installed.

1. Download Vagrant and Virtualbox from their websites.
2. Install ansible using pip: `sudo pip install ansible`
3. Then bring up the Vagrant VM by running `vagrant up`
4. Once the VM has been provisioned, you can visit
   [http://127.0.0.1:8080](http://127.0.0.1:8000/) and login with the username and password "admin"
5. To destroy the Vagrant environment, run `vagrant destroy -f`. Be sure
   to destory the environment since VMs consume CPU and therefore
   battery.

### More Information

Vagrant uses the Ansible playbook located at `provision/main.yml` to
provision a base CentOS 7 box to run the Kombucha Manager Django app.
This playbook should be used as documentation for how to install this
app. It can also be used to provision the environment within another
provider such as AWS. The provision playbook assumes the database will
reside on the same instance. This funcationality may need to be pulled
out of the main provisioner playbook and in to its own playbook.

## Tests

There are a few tests for the `kombucha_manager` app located in
`kombucha_manager/tests/`. This is a work in progress but the ones which
exist can be executed by running `/tmp/run_tests.sh` from within the
Vagrant VM. This little script handles setting the `DATABASE_URL`
environment variable to the correct value, making running tests a lot
easier.

The Django tests are automatically ran after Vagrant provisioning.

## Generate Model Graphs

Ensure [Graphviz](http://graphviz.org) is installed.

```
python manage.py graph_models -a -g -o kombucha_manager_visualized.png

```
