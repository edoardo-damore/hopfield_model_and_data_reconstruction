# Hopfield model and data reconstruction

## Authors
- [Bezzi Filippo](https://github.com/filippobezzi), filippo.bezzi@studenti.unipd.it
- [Conte William](https://github.com/WilliamConte), william.conte@studenti.unipd.it
- [D'Amore Edoardo](https://github.com/edoardo-damore), edoardo.damore@studenti.unipd.it
- [Gasparotto Giacomo](https://github.com/GiacomoGasparotto), giacomo.gasparotto@studenti.unipd.it

## Supervisor
- Professor Baiesi Marco, marco.baiesi@unipd.it


## Abstract

In this work we studied the Hopfield model and tested its ability in the task of data reconstruction.

In particular we divided our work in four sections:
1. **Hopfield Model definition and deterministic method for pattern reconstruction**: we define the Hopfield model as it was first introduced and apply the deterministic update rule to retrieve learned patterns from corrupted versions of them.
2. **Pattern reconstruction using Monte Carlo methods and Metropolis algorithm**: we tackle the retrieval task by minimizing the energy value of the network via stochastic methods.
3. **Modern Hopfield Network**: we define a more recent implementation of the classical Hopfield network and test its ability in the reconstruction task.
4. **Applying the Hopfield Network to the MNIST dataset**: we apply and compare both the classical and the modern implementations of the model in the reconstruction of learned digits taken from the MNIST dataset.