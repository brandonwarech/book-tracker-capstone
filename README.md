# Getting Started with Book Tracker Orchestartion App

### Live Application: http://book-tracker-orch1-brave-elephant.mybluemix.net/api/
#### Token: 'test_token'

The following instructions are for deploying the application as a Cloud Foundry application. To deploy as a container to **IBM Cloud Kubernetes Service** instead, [see README-kubernetes.md](README-kubernetes.md)

## Prerequisites

You'll need the following:
* [IBM Cloud account](https://console.ng.bluemix.net/registration/)
* [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads)
* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)
* Python Packages found in Requirements.txt (`pip install -r requirements.txt`)

## 1. Clone the app from Github

Now you're ready to start working with the app. Clone the repo and change to the directory where the sample app is located.
  ```
git clone https://github.com/brandonwarech/book-tracker-capstone
cd book-tracker-capstone
  ```
  Peruse the files in the *book-tracker-capstone* directory to familiarize yourself with the contents.

## 2. Run the app locally

Install the dependencies listed in the [requirements.txt](https://pip.readthedocs.io/en/stable/user_guide/#requirements-files) file to be able to run the app locally.

You can optionally use a [virtual environment](https://packaging.python.org/installing/#creating-and-using-virtual-environments) to avoid having these dependencies clash with those of other Python projects or your operating system.

  ```
pip install -r requirements.txt
  ```

Run the app.
  ```
python hello.py
  ```

 View your app at: http://localhost:5000/api
 Note: Token based authentication is active. Token is currently `test_token`. 

## 3. Prepare the app for deployment

The manifest.yml includes basic information about our app, such as the name, how much memory to allocate for each instance and the route. In this manifest.yml **random-route: true** generates a random route for your app to prevent your route from colliding with others.  You can replace **random-route: true** with **host: myChosenHostName**, supplying a host name of your choice. [Learn more...](https://console.bluemix.net/docs/manageapps/depapps.html#appmanifest)
 ```
 applications:
 - name: book-tracker-orchestration
   random-route: true
   memory: 128M
 ```

## 4. Deploy the app

You can use the IBM Cloud / Cloud Foundry CLI to deploy apps.

Login to your IBM Cloud account

  ```
ibmcloud login
  ```

From within the *get-started-python* directory push your app to IBM Cloud
  ```
ibmcloud cf push
  ```

This can take a minute. If there is an error in the deployment process you can use the command `ibmcloud cf logs <App-Name> --recent` to troubleshoot.

When deployment completes you should see a message indicating that your app is running.  View your app at the URL listed in the output of the push command.  You can also issue the
  ```
ibmcloud cf apps
  ```
  command to view your apps status and see the URL.



