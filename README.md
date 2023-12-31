 # Constellatus

Constellatus is an extension of the Eons APIE executable. It provides a RESTful API for storing, retrieving, and optimizing code written within the Eons framework.

**Our goal is to automate the process of translation.**  
By refining our code for us, Constellatus allows us make succinct statements that are easy for others to use.  

We make heavy use of astronomy metaphors.

## Overview
* `Stars` are fully formed `SelfRegistering` classes.
* We measure the mass of code by its behavior. Well structured, well performing, easily repeatable behavior results in higher mass (e.g. one program has a deeper gravity well than another that does the same thing but is slower).
* We model matter as the quantity of code, regardless of its behavior.
* The "density" of a particular bit of code is measured by how well it behaves over how much code it contains.
* The Eons Error Resolution machinery (EER) is our corollary to nuclear fusion: it takes code that is not well behaved but could be (i.e. low mass) and improves its behavior, increasing its gravitational force and thus its mass.

To illustrate what "could be well behaved" means, imagine code which operates perfectly but is missing context, e.g. requires an additional include statement or a package to be installed. These kinds of errors, which are trivial to resolve, provide the fuel for the EER machinery. This is useful as it allows us as programmers to write only what is necessary, and have all dependencies automatically injected. 

## Stars
The minimum requirement for a SelfRegistering class to be a Star is that it possess enough well behaved code such that it requires no interaction with the Eons Error Resolution machinery to be instantiated.
Stars may progress through a normal lifecycle of improvements, whereby they become increasingly dense. This process is similar to how a user might implement Cython: small, well behaved units of the Star are replaced with code from Biology, C++, C, or Assembly. Code that is not well behaved is refined through repeated application of the Eons Error Resolution machinery.
A Star's lifecycle is entirely managed by Constellatus. Stars may be Formed and Destroyed but their updates are entirely automated.
They key to making Constellatus work is the continual rewrite of the code of Stars so that each time it's Observed, it becomes more compact.


## Installation
```
pip install constellatus
```

## Usage
For now, refer to [Apie](https://github.com/eons-dev/apie.exe) for all configuration.

When running as a webserver, the default port is 1137, after the approximation for the [fine structure constant](https://en.wikipedia.org/wiki/Fine-structure_constant): 1/137.