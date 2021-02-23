# Gitcoin Analysis

This cadCAD model and notebook series is a collaboration between Gitcoin, BlockScience, Longtail Financial, and the Token Engineering Academy. Check it out 🦊

## How to use

1. Create and Activate you Python Virtual Environment
2. Install all requirements: `pip install -r requirements.txt`
3. Change the parameters on `env_config.py` so that it fits your use case.
4. See the simulation help documentation for advice on running: `python run_simulation.py --help`
5. The data results will be pickled `model/data/simulation_result.pkl.gz`.
    * Alternatively, you can just unzip the `model/data/simulation_result.tar.xz` file.
6. Perform any analytics on the generated data or use one of the available notebooks.

Additionally, there are several options on the `run_simulation.py` script 
that encapsulates the features on `env_config.py` without needing to modify it.

## Repository Structure

### Root of the Repository:

* Notebook: [dynamic_network.ipynb](dynamic_network.ipynb)  
  This notebook showcases the cadCAD networked model using raw CSV data

* Notebook: [graph_communities.ipynb](graph_communities.ipynb)  
  This notebook contains visualizations of communites on Gitcoin

### Optimality Gap Folder

Python functions for the optimality gap research on Gitcoin grants. More info can be found on this [hackmd](https://hackmd.io/QCCJWZE0Ru27X_GRk6UKjQ).

### Model Folder

cadCAD configuration scripts for the model and the data to be used on the analysis.

## Medium Articles

* [Towards Computer-Aided Governance of Gitcoin Grants](https://medium.com/block-science/towards-computer-aided-governance-of-gitcoin-grants-730de7bcdbef)
* [Colluding Communities or New Markets?](https://medium.com/block-science/colluding-communities-or-new-markets-f64194a1b754)

### Quadratic Funding

Quadratic Voting captured the hearts of the web3 space after being re-introduced by the [Radical xChange movement](https://www.radicalxchange.org/). Gitcoin builds on the same principle by leveraging a powerful algorithmic policy called [Quadratic Funding (QF)](https://wtfisqf.com/?grant=&grant=&grant=&grant=&match=1000) to allocate sponsor funds via matching community donations to grants submitted through the Gitcoin Grants program. The purpose of this form of grant matching is to allocate sponsor funding via a community preference signal by capturing not just the depth of donations ($ amount donated), but also the breadth of the donation base (# people who donated). The outcome is that grants that are supported by many people with small donations would receive relatively larger matching than grants supported by few donations of larger amounts. In effect, **Quadratic Funding aims to boost the influence of people over plutocracy.**

### Development

Currently, this repository references a custom branch of networkx that implements the sub-graph solver. The branch is here: https://github.com/danlessa/networkx/tree/rewiring-optimizers

To use the above and get tests running, I did the following inside of this repository:
```
mkdir scratch/
git clone git@github.com:danlessa/networkx.git
mv networkx scratch/networkx/
cp -r scratch/networkx/networkx/ ./
```
and then I run tests as
```
pytest --ignore scratch/ --ignore networkx/
```
