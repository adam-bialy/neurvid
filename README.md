# Neurvid

A neural network app for identifying birds from <i>Corvidae</i> family.

### Description

The network was built using TensorFlow library for Python.
It consists of three convolutional + max-pooling layer pairs, with 96 filters in each.
It was trained on ca. 1500 photos of 6 species of <i>Corvidae</i> scraped from Google Images.

The web application was created in Flask framework.

(c) Adam Grzelak 2022

### Deployment

#### Local

Set up:

```
docker build -t neurvid .
docker run --name neurvid -d -p 8000:8000 neurvid
```

Clean up:

```
docker stop neurvid && docker rm neurvid
docker image rm neurvid
```

Notes:
The application in its current form may not work on MacOS with ARM
architecture (M1 / M2 chip).
