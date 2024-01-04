<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/ericodle/Open-Danio/blob/main/imgs/danio_logo.png" alt="Logo" width="400" height="400">
  </a>
</div>

Zebrafish (*Danio rerio*) are a common model organism for their transparent larval stage, high fecundity, and large library of mutants.



## About this project
 
While working on my master's thesis in Taiwan, I began playing around with Python.

Now I use this repository to demonstrate basic Github management skills and store bioinformatics lessons.

## Prerequisite

Install [Python3](https://www.python.org/downloads/) on your computer.

Enter this into your computer's command line interface (terminal, control panel, etc.) to check the version:

  ```sh
  python --version
  ```

If the first number is not a 3, update to Python3.

## Setup

Here is an easy way to use this GitHub repository.

### Step 1: Clone the repository

Open the command line interface and run:
  ```sh
  git clone git@github.com:ericodle/Open-Danio.git
  ```

You have now downloaded the entire project, including all its sub-directories and files.
(We will avoid using Git commands.)

### Step 2: Navigate to the project directory
Find where your computer saved the project. On Linux, it will go to the Home directory (folder) by default.
When you figure out the project path, run this command.

  ```sh
  cd /path/to/project/directory
  ```

For example, the path was /home/ericodle/Open-Danio on my computer.
Therefore, I entered the command:

  ```sh
  cd /home/ericodle/Open-Danio
  ```
If performed correctly, your command line interface should change from:

```
user@user:~$
```

to:

```
user@user:~/Open-Danio$
```

Good, we're in. (⌐■_■)


### Step 3: Create a virtual environment:
Differences between software versions can break your programs and waste your time. 
Therefore, we use a **virtual environment** to ensure software versions on our computer match the versions used by developers when making an open-source project like Open-Danio.


```sh
python3 -m venv environment-name
```

Your "environment-name" can be anything you want. 
For simplicity, let's call it opendanio (one word, all lowercase).

```sh
python3 -m venv opendanio
```

The virtual environment has been created. 
We enter the environment to do our work by using the following command:

```sh
source opendanio/bin/activate
```

Enter your preferred name in place of "opendanio", if desired.

When performed correctly, your command line interface prompt should change from something resembling 

```
user@user:~/Open-Danio$
```

to 

```
(opendanio) user@user:~/Open-Danio$
```

Now we're really in. (⌐■_■)


### Step 3: Install requirements.txt

Run the following command to install specific software versions to your virtual environment.

  ```sh
pip install -r requirements.txt
  ```

### Step 4: Use Open-Danio

This is a simple project containing only three main modules: 2D_trajectory_analysis.py, 3D_trajectory_analysis.py, and novel_tank_dive.py.
These modules are organized in the "src" (source) sub-directory.
There are other directories as well, such as "imgs" (images), "tests", and "notebooks".
Later sections provide a detailed explanation of how to use these elements.


### Step 5: Deactivate the virtual environment

When finished working, it is best to deactivate the virtual environment and change directory (cd) out of the project directory. Enter the following command:

  ```sh
deactivate
cd
  ```

...or you can just close the command line interface window.

## src

### 2D_trajectory_analysis.py

This script does xyz.

  ```sh
how to start it up
  ```

Then this will happen.

  ```sh
what to do next.
  ```

And this is the output.

### 3D_trajectory_analysis.py

This script does xyz.

  ```sh
how to start it up
  ```

Then this will happen.

  ```sh
what to do next.
  ```

And this is the output.

### novel_tank_dive.py

This script does xyz.

  ```sh
how to start it up
  ```

Then this will happen.

  ```sh
what to do next.
  ```

And this is the output.


## tests

Testing was performed on Intel and AMD systems running Linux kernel versions 5.14 and 5.15. 

explain the synthetic data scripts, and toss up the output images.



## notebooks

### notebook 1


## Citing this project


As of January 2024, users can access the full paper by following this link: [Evaluation of the therapeutic effects of dimethyl sulfoxide on FMR1 mutant zebrafish using open-source deep learning software](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwii7qGgzMKDAxVNmK8BHXF2D7sQFnoECAsQAQ&url=http%3A%2F%2Frportal.lib.ntnu.edu.tw%2Fbitstreams%2F2534e275-1fa0-44c6-883a-7024325cdcb1%2Fdownload&usg=AOvVaw0MRYBsjjBFlv8bwUM1aeuR&opi=89978449).

If my amateur masters thesis is somehow beneficial to your work, kindly use the following citation:

```
@masterthesis{odleFMR1,
    title        = {Evaluation of the therapeutic effects of dimethyl sulfoxide on FMR1 mutant zebrafish using open-source deep learning software},
    author       = {Eric Odle},
    year         = 2021,
    month        = {June},
    address      = {Taipei, Taiwan},
    school       = {National Taiwan Normal University},
    type         = {Master's thesis}
}
```

<!-- LICENSE -->
## License

Distributed under the GNU Lesser General Public License. See `LICENSE.txt` for more information.
