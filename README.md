# WifiDisabler

---

<a title="Python version"><img src="https://img.shields.io/badge/python-3.9-green.svg"></a>

```
  __---__  ##   ##
 / __-__ \  ## ##
  / ___ \    ###
   /   \    ## ##
     @     ##   ##
```

About
---
WifiDisabler is a tool for DoS'ing a wifi you are connected to with incredible force
With the right settings you can take down almost any wifi

How it works
---
WifiDisabler works by flooding tcp pings to an external server (it can be any external server)
The router then gets so stressed from the pings, that it stops forwarding other requests

Installation
---

```
# clone the repository
git clone https://github.com/GilbertEnevoldsen/WifiDisabler

# navigate to folder
cd WifiDisabler

# launch disabler
python3 disabler.py [OPTIONS]
```