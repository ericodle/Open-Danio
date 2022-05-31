<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/ericodle/Open-Danio/blob/main/opendanio_logo.jpeg" alt="Logo" width="400" height="400">
  </a>

<h3 align="center">Open Danio</h3>

  <p align="center">
    Our lab's license for the Smart2.0 Zebrafish tracking software suite produced by the company PANLAB had long expired and I got tired of scheduling time with the senior students to use the one cracked version we had running off a USB.
    This is my first coding project, and is little more than a collection of Python scripts I wrote during my biology M.Sc. thesis at National Taiwan Normal University. It's not sophisticated, but the sentimental value is through the roof!
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About this Project

Danio rerio, also known as the zebrafish, is a common model organism for its clear larval stage, high fecundity, and rich library of available mutants. While working with zebrafish for my master's project, I found conventional behavioral analysis tools lacking. To address this issue, I began writing simple scripts that interpret raw XY-coordinate output from excellent, open-source animal tracking projects such as [IdTrackerAI](https://gitlab.com/polavieja_lab/idtrackerai) and [DeepLabCut](https://github.com/DeepLabCut/DeepLabCut). As my labmates and I learned more about Python programming, our modules became more ambitious. Though still in its infancy, we hope OpenDanio inspires you to contribute to our project, incorporate our tools, and take full control of your own data processing workflow! 

It's your data. You should decide what the computer does with it.

<p align="right">(<a href="#top">back to top</a>)</p>


### Prerequisites

Open Danio gives researchers a way to interpret the framewise XY corrdinates generated from animal tracking tools. Therefore, users have to provide their own animals, video files, and tracking output data. As previously stated, we recommend using either DeepLabCut or IdTrackerAI, depending on your available hardware and research requirements. For example, DeepLabCut is excellent at pose estimation, but in our experience, requires a strong GPU and a lot of time to train. Moreover, DeepLabCut has been better for our single-animal tracking experiments, whereas IdTrackerAI is great for simultaneous multi-animal tracking in the same region of interest. This is because IdTrackerAI was specifically designed to keep track of animal identitiy in a group, which becomes a non-trivial challenge when you film multiple crossing zebrafish from a top-down angle.

## Getting Started

Download this repository by going up to the green "Code" button at the top right and clicking "Download ZIP". 

Alternatively, you can also clone the repo directly using the following commands.

  ```sh
  # Replace "your_folderpath_here" with the actual folder where you want the project to go.
  cd /your_folderpath_here
  git clone git@github.com:ericodle/Open-Danio.git
  ```

> __For this example, the working directory is the repository root directory.__ 

### 2D_trajectory.py

Open-source tracking solutions didn't have readily-available trajectory image generators when I was doing my masters, so I made my own. Whatever tracking solution you use should spit out a video frame-wise XY coordinate table, which 2D_trajectory.py converts into a linear path the object (zebrafish) moved (swam). The input file assumes only two columns, with the first column representing X position and the second column representing Y position (often in pixel units). It's rudimentary, and perhaps my colleague Connor and I will fancy it up later. For now, I hope this script gives you ideas for writing your own trajectory mappper.

### novel_tank_dive.py

The Novel Tank Dive (NTD) is a standard zebrafish anxiety experiment. Ideally, the zebrafish spends more time at the bottom of a tank when first introduced and then gradually builds up the courage to poke around at the top as it begins to feel safe. Fish experiencing higher therefore spend more time on the bottom and venture upwards at a slower rate than "normal" fish. The novel_tank_dive.py script takes an XY output from a single-fish NTD video recorded side-on such that the Y value reflects fish depth in the tank. My thesis experiements considered a 5-minutes test duration, so I chopped up each video into five 1-minute segments based on the recording frame rate used at the time of filming. Feel free to adapt the base script to your own needs.

### shoal_analysis.py

I also worked a lot with zebrafish larvae. 5 days after fertilization, zebrafish have hatched from their egg and are capable of twitchy swim bursts when agitated. 5-day-old zebrafish also display shoaling --- the tendency to swim in close proximity to one another. The shoal_analysis.py script takes a 2-column table of paired data containing the X pixel position in the first column and Y pixel position in the second column. This data is obtained from static images of petri dishes housing larval zebrafish. The images were processed using ImageJ to make an XY coordinate list of each fish. While the image processing step is time-consuming and could be automated, I chose to do it the slow but reliable way. Still, this script saves time by automating the calculation of inter-fish distance for each individual with respect to every other individual present. Then, the arithmetic mean of all the unique inter-fish euclidean distances is calculated to generate a single "shoal cohesion" value. 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions make the open source community great. Everyone has a unique combination of skills and experience. Your input is **highly valued**.
If you have ideas for improvement, please fork the repo and create a pull request. 
If this is your first pull request, just follow the steps below:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU Lesser General Public License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
