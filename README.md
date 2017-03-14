#razor

## Introduction

The razor project is a POC of using pytest, vagrant, and rpyc to deploy a VM for endpoint testing.  This project was developed and tested on OS X using VMware Fusion.  In theory it should work on other platforms and other virtualization solutions.

This simple POC will create a Linux Ubunutu 12.04 VM using vagrant and then verify the install by checking that it is Linux Ubuntu 12.04.  Communication to the VM is done via rpyc.

## Installation

### Install from github using pip

Download and install razor (its recommended to use a virtualenv):

    pip install git+https://github.com/jebegin/razor.git

## Usage

The test_endpoint.py test can be found in your python site-packages under razor/tests.

Example command:

    pytest -vsx test_endpoint.py --box=hashicorp/precise64 --hostname=endpoint --vagrant_template=endpoint_template
