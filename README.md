# prepic-density
Pre-pic and plot density profile of a gas jet

To run, `python prepic_density.py`. To generate the corresponding `jupyter notebook`, we use
[`jupytext`](https://github.com/mwouts/jupytext). 

To generate a jupyter notebook from a Python script, do:

```console
jupytext prepic_density.py --to ipynb
```

One then has to delete the original Python script, which will be re-generated by Jupyter.

To install pre-pic: https://prepic.readthedocs.io/en/latest/readme.html

For `LaTeX` font rendering of `matplotlib` figures, under `Ubuntu 20.04`:

```console
$ sudo apt install dvipng texlive-latex-extra texlive-fonts-recommended cm-super
```

![alt text](density.png)
