<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/ericodle/Open-Danio/blob/main/misc/opendanio_logo.jpeg" alt="Logo" width="400" height="400">
  </a>

<h3 align="center">Open Danio</h3>

  <p align="center">
    My first computer programming project.
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

Danio rerio, also known as the zebrafish, is a common model organism for its clear larval stage, high fecundity, and rich library of available mutants. While working with zebrafish for my master's project, I began writing simple scripts that interpret raw XY-coordinate output from [IdTrackerAI](https://gitlab.com/polavieja_lab/idtrackerai).

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

Here is my recommended way to use this GitHub repository.

Step 1: Clone the repository

  ```sh
  # Replace "your_folderpath_here" with the actual folder where you want the project to go.
  cd /your_folderpath_here
  git clone git@github.com:ericodle/Open-Danio.git
  ```

Step 2:

Step 3:

Step 4:

Step 5:

> __For this example, the working directory is the repository root directory.__ 

## Using the Open-Danio tools

### 2D_trajectory.py

This script does xyz.

  ```sh
# Usage example
import 2D_trajectory as tj
file_path = 'path_data.csv'
data = tj.load_csv(file_path)
tj.trace_and_plot_path(data)
length = tj.calculate_path_length(data)
print("Cumulative length of the path:", length)

# save the trajectory image
plt.savefig(file_path+'XY_trajectory.tif')
  ```


### 3D_trajectory.py

This script does xyz.

  ```sh
# Usage example
import 2D_trajectory as tj
file_path = 'path_data.csv'
data = tj.load_csv(file_path)
tj.trace_and_plot_path(data)
length = tj.calculate_path_length(data)
print("Cumulative length of the path:", length)

# save the trajectory image
plt.savefig(file_path+'XY_trajectory.tif')
  ```

### novel_tank_dive.py

This script does xyz.

  ```sh
# Usage example
import 2D_trajectory as tj
file_path = 'path_data.csv'
data = tj.load_csv(file_path)
tj.trace_and_plot_path(data)
length = tj.calculate_path_length(data)
print("Cumulative length of the path:", length)

# save the trajectory image
plt.savefig(file_path+'XY_trajectory.tif')

### shoal_analysis.py

I also worked a lot with zebrafish larvae. 5 days after fertilization, zebrafish have hatched from their egg and are capable of twitchy swim bursts when agitated. 5-day-old zebrafish also display shoaling --- the tendency to swim in close proximity to one another. The shoal_analysis.py script takes a 2-column table of paired data containing the X pixel position in the first column and Y pixel position in the second column. This data is obtained from static images of petri dishes housing larval zebrafish. The images were processed using ImageJ to make an XY coordinate list of each fish. While the image processing step is time-consuming and could be automated, I chose to do it the slow but reliable way. Still, this script saves time by automating the calculation of inter-fish distance for each individual with respect to every other individual present. Then, the arithmetic mean of all the unique inter-fish euclidean distances is calculated to generate a single "shoal cohesion" value. 


  ```sh
import shoal_analysis as sa
dot_positions = sa.detect_dots('image.jpg')
distances = sa.calculate_pairwise_distances(dot_positions)
average_distance = sa.calculate_average_pairwise_distance(distances)
print("Average Pairwise Distance:", average_distance)
sa.main()
  ```
## Citing this project


As of January 2024, users can access the full paper by following this link: [Evaluation of the therapeutic effects of dimethyl sulfoxide on FMR1 mutant zebrafish using open-source deep learning software](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwii7qGgzMKDAxVNmK8BHXF2D7sQFnoECAsQAQ&url=http%3A%2F%2Frportal.lib.ntnu.edu.tw%2Fbitstreams%2F2534e275-1fa0-44c6-883a-7024325cdcb1%2Fdownload&usg=AOvVaw0MRYBsjjBFlv8bwUM1aeuR&opi=89978449).

If my amateur masters thesis is somehow beneficial to your work, kindly use the following citation:


> @masterthesis{odleFMR1,
>> title        = {Evaluation of the therapeutic effects of dimethyl sulfoxide on FMR1 mutant zebrafish using open-source deep learning software},
>> author       = {Eric Odle},
>> year         = 2021,
>> month        = {June},
>> address      = {Taipei, Taiwan},
>> school       = {National Taiwan Normal University},
>> type         = {Master's thesis}
>}


<!-- LICENSE -->
## License

Distributed under the GNU Lesser General Public License. See `LICENSE.txt` for more information.
