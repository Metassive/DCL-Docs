# DCL-Docs

DCL-Docs is a chatbot designed to answer questions about most matters related to [Decentraland](https://decentraland.org/). This project has been funded by [DecentralandDAO](https://dao.decentraland.org/).

ChatGPT DCL-Docs is published, and ChatGPT Plus users can use it at this link, however, if you want to implement it yourself in an easy and quick way, simply follow step 4 of this guide and you will be able to get it up and running quickly.

In addition to this, the extraction and cleaning scripts that have been used have also been published, being fully available to the community so that the process can be replicated by anyone.

Below is the guide to implementing DCL-Docs, which consists of four steps. The first three steps result in several .txt files that are understandable not only for ChatGPT but also for other large language models (LLM), including open-source ones. Step four details how to implement it in ChatGPT, due to its popularity and ease of use. However, users are free to experiment, replicate, or improve DCL-Docs as they wish.

## Usage Guide

### 1 - Preparing your computer:
1.1 - **Install Python**: Visit [python.org](https://python.org), download, and install Python.

1.2 - **Install pip**: Typically installed with Python. If not, follow the instructions at [pip.pypa.io](https://pip.pypa.io).
<br><br>

### 2 - Extracting information:
2.1 - **Install required libraries**: requests, beautifulsoup4, and selenium.

2.2 - [**Download extraction scripts**](https://github.com/Metassive/DCL-Docs/tree/main/Extraction%20Scripts).

2.3 - **Run extraction scripts**: Execute one by one to obtain .txt files.
<br><br>

### 3 - Processing information:
3.1 - **Install required libraries**: re (usually comes with Python, so this step may not be necessary).

3.2 - [**Download cleaning scripts**](https://github.com/Metassive/DCL-Docs/tree/main/Cleaning%20Scripts).

3.3 - **Run cleaning scripts**: As in step 2.3, execute them one by one to get other .txt files.
<br><br>

### 4 – Implementing in ChatGPT:
4.1 – **Create chat**: Go to ChatGPT and click on “Create a GPT.”

4.2 – **Configure chat**: In the “Configure” tab, select “Upload files” and upload the files you have generated or download them directly from [here](https://github.com/Metassive/DCL-Docs/tree/main/Data) if you want skip steps 1, 2 and 3.

4.3 – **Implement chat**:
Click on “Publish Changes” and then on “Confirm.” The chat is now ready for use.
