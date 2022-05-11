<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/ericodle/Open-Danio/blob/main/opendanio_logo.jpeg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Open Danio</h3>

  <p align="center">
    My colleagues and I aim to provide a transparent set of free-to-use tools for zebrafish behavior analysis. Similar commercially available software suites are restrictive, secretive, outdated, and unreasonably priced for the features offered. 
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

<!-- USAGE EXAMPLES -->
## Walkthrough

Walkthrough video coming soon!

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Content

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
- [ ] Nested Feature

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
