# Helm 101

## What is Helm?

If you have used a Linux environment (and it's safe to assume you have), then you are already acquainted with package managers (apt, yum). Helm basically the same thing, but for Kubernetes. Imagine you want to add MongoDB to your existing Kubernetes implementation, and this resource comes with services, deployments, secrets, stateful sets, etc... Taking the Yaml files of each of these resources and deploying them one by one into your Kubernetes cluster would be both cumbersome and time-consuming. Additionally, this task would also be repetitive since various developers around the world may gather these exact same Yaml files to set up MongoDB over and over again. This is where **Helm Charts** come in.

## What are Helm charts? 

A Helm chart is, simply put, a collection of Yaml files. Imagine someone takes all the necessary Yaml files to set up MongoDB and then bundles them into a package. Similar to how normal package managers work, it would then be a simple matter to upload this package into a common repository. Once that's done, any other developer looking to set up MongoDB would only have to download this package instead of doing the legwork themselves by simply writing:

```
helm install <chart>
```

## What is a Helm repository?

This is a place where Helm charts are storedm and where you can download them.  [Artifact Hub](https://artifacthub.io) is a centralised repository for Helm packages and is extensively used by Kubernetes developers in their daily work. 

## What is a Helm release?

This is once single instance of a chart. Even within a single Kubernetes cluster, the same chart can be installed multiple times. In order to facilitiate this, each installation is considered to be a release. So if you want 2 instances of MongoDb running in your cluster, it is just a matter of installing the chart twice.

## Helm as a templating engine 

If you have used Kubernetes for even a simple project, you would have noticed that the Yaml files you create for various resources tend to get repetitive. For instance, deployment files may be identical to each other apart from the image they use. This means you would end up creating a deployment file for each image even though they have only minor differences. Helm can step into the rescue here as well, by introducing templating to Yaml's. Now, you could get rid of all the duplicates and replace them with a single Yaml file. But what about the parts that are different? Well, Helm allows you to dynamically set those values. So instead of hardcoding the image name like this:

```
...
spec:
    containers:
    - name: nginx
      image: nginx
...
```

You could convert it into a template:

```
...
spec:
    containers:
    - name: {{ .Values.name }}
      image: {{ .Values.container.image }}
...
```

Then set the name and image dynamically.

Now that we have a broad understanding of how Helm works, let's first install a helm chart and see what this is all about, before taking a deep-dive into the specifics, starting with a deeper introduction to Helm charts.

## Installing a chart

The easiest way to get into the subject is to do it hands-on. So let's go ahead and install a Helm chart.

Firstly, you must have an active Kubernetes cluster. The easiest way to get this up and running is using [Minikube](https://minikube.sigs.k8s.io/docs/start/).

If you have a Kubernetes cluster up and running, then it's time to install Helm. The installation is fairly straightforward, and the full installation steps can be found [here](https://helm.sh/docs/intro/install/). **Make sure you install Helm 3**. There are some [significant changes](https://helm.sh/docs/faq/changes_since_helm2/) between Helm 2 and Helm 3, which means that the below tutorial will not work if you use Helm 2 instead.

Once this is done, you can add a chart repository. Note that this isn't the actual chart. Rather, it is the repository where various packages are stored. The [Artifact Hub](https://artifacthub.io/packages/search?kind=0) has a comprehensive list of chart repositories. We will install the bitnami chart repository:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```

Once this command has run, you can explore this repo which will show you all the available charts within this repository.

```bash
helm search repo bitnami
```

Next, let's install an example chart. Before we do that, we have to ensure we get the latest list of charts. Do that using:

```bash
helm repo update 
```

The chart we will install is the MySql chart. Install that using:

```bash
helm install bitnami/mysql --generate-name
```

Note that ```--generate-name``` will generate a name for the release. You can also set your own name like so:

```bash
helm install my-custom-name bitnami/mysql
```

The chart you just installed is considered a **release**. This means that each time you install a chart. a new release is created. Thanks to this, you can go ahead and install a chart multiple times into the same cluster.

Let us now explore the MySQL chart we just installed. Run:

```bash
helm show chart bitnami/mysql
```

This will output the details (metadata) about the chart. For example, you get details on the repository, version, and keywords this chart will match for when you search on Artifact Hub. Basically, anything that makes this specific chart stand out. You can get now get a list of available helm charts by running ```helm list```. You should be able to see the unique name of this helm chart from here (something like mysql-xxxxx). This name can be used to get the status of the helm chart:

```bash
helm status mysql-1652869723
```

Uninstalling the chart is as easy as calling ```helm uninstall``` with the chart name. You could also use the flag ```--keep-history``` if you want to get rid of the chart but keep the release history.

Now that we have the basics out of the way, let's do a deep dive into Helm charts.
