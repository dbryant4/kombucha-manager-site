# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "centos-7-minimal"
  config.vm.box_url = "https://atlas.hashicorp.com/relativkreativ/boxes/centos-7-minimal/versions/1.0.3/providers/virtualbox.box"

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/main.yml"
    ENV['ANSIBLE_ROLES_PATH'] = '..'
    ansible.verbose = "v"
  end
  config.vm.provision "shell", inline: "/tmp/run_tests.sh"
end
