# HAQS-2022

<a href="https://qbraid.com/">
    <img src="https://qbraid-static.s3.amazonaws.com/logos/qbraid.png"
         alt="qbraid logo"
         width="250px"
         align="right">
</a>

[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/qBraid/HAQS-2022.git)

Repository containing challenges for the qBraid HAQS 2022 quantum computing hackathon.

For non-registered individuals:
https://qbraid.com/haqs

For participants:
https://account.qbraid.com/haqs

Oct 21st - Nov 5th 2022

## Challenges

- [**QML Classifier Challenge**](qml-classifier-challenge/README.md)

- [**qBraid Open Challenge**](qbraid-open-challenge/README.md)

## Getting started

1. Fork this repository into your account, and copy its git clone url e.g. `https://github.com/<user>/HAQS-2022.git`
2. At the top of this `README` in the forked repo, click the **Launch on qBraid** button to clone this repository and launch qBraid Lab.
3. Open terminal (first icon in the **Other** column in Launcher) and `cd` into the HAQS repo. Set the repo's remote origin using the git clone url you copied in Step 1, and then create a new branch for your team:
```bash
cd HAQS-2022
git remote set-url origin <url>
git branch <team_name>
git checkout <team_name>
```
4. Use the environment manager (**ENVS** tab in the right sidebar) to [install environment](https://qbraid-qbraid.readthedocs-hosted.com/en/latest/lab/environments.html#install-environment) "HAQS 2022". The installation should take ~2 min.
3. Once the installation is complete, click **Activate** to [add a new ipykernel](https://qbraid-qbraid.readthedocs-hosted.com/en/latest/lab/kernels.html#add-remove-kernels) for "HAQS 2022".
5. From the **FILES** tab in the left sidebar, double-click on the `HAQS-2022` directory.
6. Open and follow instructions in [`verify_setup.ipynb`](verify_setup.ipynb) to verify your "HAQS 2022" environment setup.
7. You are now ready to begin hacking! Work with your team to complete either of the challenges listed above.

To submit your hack, create a pull request from your team's named branch (created during Step 4 above) following challenge submission instructions.

For help with these instructions, follow along with the HAQS getting started video demo: https://youtu.be/uYGV9w2DUcg

For other questions or additional help using qBraid, see [Lab User Guide](https://qbraid-qbraid.readthedocs-hosted.com/en/latest/lab/overview.html), or reach out on [Discord](https://discord.gg/gwBebaBZZX).
