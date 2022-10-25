# VQC Challenge

In this challenge, you will use [Pennylane](https://github.com/PennyLaneAI/pennylane) and [Amazon Braket](https://github.com/aws/amazon-braket-examples) to implement a variational quantum classifier (VQC) to take on a supervised learning problem based on the work of [Havlíček et al. (2018)](https://arxiv.org/pdf/1804.11326.pdf). Implement each of the four TODOs in [`vqc_challenge.ipynb`](vqc_challenge.ipynb) to construct and train a QML model to solve the binary classification task. You can use the [`gen_binary.py`](gen_binary.py) script to generate a new train/test dataset, and further test your model.

A central feature of Amazon Braket is that its remote simulator can execute multiple circuits in parallel. This capability can be harnessed in PennyLane during circuit training, which requires lots of variations of a circuit to be executed. Hence, the PennyLane-Braket plugin provides a method for scalable optimization of large circuits with many parameters. After validating your implementation and successfully training using a local simulator, enable [qBraid quantum jobs](https://qbraid-qbraid.readthedocs-hosted.com/en/latest/cli/jobs.html) and test your binary classifier on remote quantum hardware using the [Amazon Braket Pennylane plugin](https://github.com/aws/amazon-braket-pennylane-plugin-python). See the resources linked below for more.

### Submissions

- To submit your hack, create a pull request from your team's named branch
- Submission PR title format: `[VQC-CHALLENGE] [team-name] [date]`
- Submissions will be evaluated on a *rolling basis*
- Each team is allowed *one submission per day*

### Leaderboard

A leaderboard will be kept on https://account.qbraid.com/haqs that ranks teams in order of their submitted VQC model accuracy. The leaderboard will be updated every 24 hours with all the submissions from that day. All teams that make a submission, no matter their model's performance, will appear on the leaderboard and therefore be eligable for prizes.

*Important*:  Your final model must be tested with on a remote quantum device using the Amazon Braket Pennylane plugin. Submissions that do not interface with [Amazon Braket supported devices](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html) will not be eligible to be ranked on the leaderboard.

### Resources:

- [PennyLane-Braket Plugin](https://amazon-braket-pennylane-plugin-python.readthedocs.io/en/latest/)
- [Pennylane tutorial: qubit rotation](https://pennylane.ai/qml/demos/tutorial_qubit_rotation.html)
- [Computing gradients in parallel with Amazon Braket](https://pennylane.ai/qml/demos/braket-parallel-gradients.html)
- [Use PennyLane with Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/hybrid.html)
- [Amazon Braket examples: hybrid quantum algorithms](https://github.com/aws/amazon-braket-examples/tree/main/examples/hybrid_quantum_algorithms)
- [qBraid demo notebooks: quantum jobs](https://github.com/qBraid/qbraid-lab-demo/blob/main/qbraid_quantum_jobs.ipynb)
- [qBraid CLI: quantum jobs commands](https://qbraid-qbraid.readthedocs-hosted.com/en/latest/cli/jobs.html)
