# Saritasa-Python-Test-Eng-Version-1

<!-- PROJECT LOGO -->

<div align="center">
    <p align="center">
    <a href="https://saritasa-memory.onrender.com/">View Demo</a>
    </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#">Run locally</a>
      
    </li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Saritasa Memory is a website for storing memories about places that you have visited.

Features:
- [x] Upload images.
- [x] Mark places on map.
- [ ] Login With
    - [x] Signup Account
    - [ ] Facebook



### Built With

* Django
* geocoder & folium
* Firebase Object Storage
* Render
* Bootstrap



<!-- GETTING STARTED -->
## Run locally

### Prerequisites

_Install docker and login docker via terminal._

Then
1. Pull docker image
   ```sh
   docker pull thien0611/saritasa-memory:v1
   ```
2. Build container
   ```sh
   docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8000:8765 thien0611/saritasa-memory:v1
   ```
3. Access the contianer via [http://localhost:8000/](http://localhost:8000/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

